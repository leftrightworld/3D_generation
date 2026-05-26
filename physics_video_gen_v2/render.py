import argparse
import os
import sys

import mujoco
import numpy as np
import imageio.v2 as imageio


def _reset_rattleback(model, data, z0=0.015):
    """Flat on table, identity orientation."""
    data.qpos[:] = 0
    data.qpos[2] = z0
    data.qpos[3] = 1
    data.qvel[:] = 0
    mujoco.mj_forward(model, data)


def _fade_frames(frames, n_fade, to_black=True):
    """Cross-fade last/first frames to black over ``n_fade`` frames."""
    if not frames or n_fade <= 0:
        return
    arr = np.asarray(frames[-1 if to_black else 0], dtype=np.float32)
    for i in range(1, n_fade + 1):
        u = i / n_fade
        if to_black:
            out = ((1.0 - u) * arr).astype(np.uint8)
        else:
            out = (u * arr).astype(np.uint8)
        frames.append(out)


def render_rattleback_compare(model, data, renderer, output_path,
                              fps=60, width=1920, height=1080, camera="cam"):
    """Preferred spin then wrong-way: bob, slow down, reverse."""
    sim_dt = model.opt.timestep
    frame_dt = 1.0 / fps
    steps_per_frame = max(1, int(round(frame_dt / sim_dt)))
    bid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "rattle")
    z0 = float(model.body_pos[bid][2])
    fade_frames = max(4, int(round(0.12 * fps)))

    segments = [
        (2.5, -7.0),   # preferred: steady spin, masts vertical
        (5.0, 7.5),    # wrong: glide → bob/slow → reverse (~3.4s), then preferred spin
    ]

    frames = []
    for seg_i, (seg_dur, wz) in enumerate(segments):
        if seg_i > 0:
            _fade_frames(frames, fade_frames, to_black=True)
        _reset_rattleback(model, data, z0)
        data.qvel[5] = wz
        mujoco.mj_forward(model, data)
        n_frames = int(round(seg_dur * fps))
        for fi in range(n_frames):
            for _ in range(steps_per_frame):
                mujoco.mj_step(model, data)
            renderer.update_scene(data, camera=camera)
            frame = renderer.render()
            if seg_i > 0 and fi < fade_frames:
                u = (fi + 1) / fade_frames
                frame = (u * frame.astype(np.float32)).astype(np.uint8)
            frames.append(frame)
        if seg_i == 0:
            pause_frames = int(round(0.25 * fps))
            if pause_frames > 0:
                frames.extend([frames[-1]] * pause_frames)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    imageio.mimsave(output_path, frames, fps=fps, quality=8, macro_block_size=1)
    print(f"Wrote {output_path}  ({len(frames)} frames @ {fps} fps, "
          f"preferred 2.5s + wrong 5s + fade, {width}x{height})")


def _solve_catenary_a(half_span, sag):
    """Solve a for z(±half)=z0, z(0)=z0-sag with z = z0 + a*(cosh(x/a)-cosh(h/a))."""
    if sag <= 1e-6:
        return 1e6

    def f(a):
        return a * (np.cosh(half_span / a) - 1.0)

    lo, hi = 1e-4, 80.0
    for _ in range(64):
        mid = 0.5 * (lo + hi)
        if f(mid) < sag:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def _solve_catenary_a_from_length(half_span, arc_length):
    """Solve a for symmetric catenary with arc length 2*a*sinh(h/a) = arc_length."""
    chord = 2.0 * half_span
    if arc_length <= chord + 1e-9:
        return 1e6
    lo, hi = half_span / 100.0, 1e6
    for _ in range(64):
        mid = 0.5 * (lo + hi)
        if 2.0 * mid * np.sinh(half_span / mid) > arc_length:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _catenary_points_by_arclength(n_seg, x0, x1, z0, arc_length):
    """Sample n_seg+1 points on a catenary pinned at both ends, spaced by arc length."""
    half = 0.5 * (x1 - x0)
    a = _solve_catenary_a_from_length(half, arc_length)
    ch_ref = np.cosh(half / a)
    sinh_x0 = np.sinh(x0 / a)

    def s_at(x):
        return a * (np.sinh(x / a) - sinh_x0)

    xs = np.empty(n_seg + 1)
    for i in range(n_seg + 1):
        target = arc_length * i / n_seg
        lo, hi = x0, x1
        for _ in range(48):
            mid = 0.5 * (lo + hi)
            if s_at(mid) < target:
                lo = mid
            else:
                hi = mid
        xs[i] = 0.5 * (lo + hi)
    zs = z0 + a * (np.cosh(xs / a) - ch_ref)
    return xs, zs


def _fabrik_xz(x0, z0, x1, z1, n_seg, seg_len, xs_hint, zs_hint, iterations=24):
    """2D FABRIK with fixed endpoints and uniform segment length."""
    pts = np.column_stack([xs_hint[: n_seg + 1], zs_hint[: n_seg + 1]]).copy()
    anchor_a = np.array([x0, z0])
    anchor_b = np.array([x1, z1])
    for _ in range(iterations):
        pts[-1] = anchor_b
        for i in range(n_seg - 1, -1, -1):
            d = pts[i] - pts[i + 1]
            dist = np.linalg.norm(d)
            if dist > 1e-12:
                pts[i] = pts[i + 1] + d / dist * seg_len
        pts[0] = anchor_a
        for i in range(n_seg):
            d = pts[i + 1] - pts[i]
            dist = np.linalg.norm(d)
            if dist > 1e-12:
                pts[i + 1] = pts[i] + d / dist * seg_len
    return pts[:, 0], pts[:, 1]


def _apply_catenary_chain(model, data, blend, x0=-0.45, x1=0.45, z0=1.0):
    """Set hinge qpos so the chain hangs between both posts.

    ``blend`` in [0, 1]: 0 = straight span, 1 = equilibrium catenary for the
    model's total link length (arc-length parameterization keeps both ends pinned).
    """
    n_hinge = sum(
        1 for i in range(model.njnt)
        if model.jnt_type[i] == mujoco.mjtJoint.mjJNT_HINGE
    )
    span = x1 - x0
    seg_len = span / max(n_hinge - 1, 1)
    arc_length = seg_len * n_hinge

    xs_line = np.linspace(x0, x1, n_hinge + 1)
    zs_line = np.full(n_hinge + 1, z0)

    blend = float(np.clip(blend, 0.0, 1.0))
    if blend <= 1e-6:
        xs, zs = xs_line, zs_line
    elif blend >= 1.0 - 1e-6:
        xs, zs = _catenary_points_by_arclength(n_hinge, x0, x1, z0, arc_length)
    else:
        xs_cat, zs_cat = _catenary_points_by_arclength(
            n_hinge, x0, x1, z0, arc_length
        )
        xs = (1.0 - blend) * xs_line + blend * xs_cat
        zs = (1.0 - blend) * zs_line + blend * zs_cat
        xs[0], zs[0] = x0, z0
        xs[-1], zs[-1] = x1, z0

    xs, zs = _fabrik_xz(x0, z0, x1, z0, n_hinge, seg_len, xs, zs)

    thetas = np.arctan2(np.diff(zs), np.diff(xs))
    q = np.zeros(n_hinge)
    q[0] = thetas[0]
    for i in range(1, n_hinge):
        q[i] = thetas[i] - thetas[i - 1]
    j = 0
    for i in range(model.njnt):
        if model.jnt_type[i] != mujoco.mjtJoint.mjJNT_HINGE:
            continue
        adr = model.jnt_qposadr[i]
        data.qpos[adr] = -q[j]
        j += 1
    data.qvel[:] = 0


def render_scene(xml_path, output_path,
                 duration=5.0, fps=30,
                 width=1920, height=1080,
                 init_qpos=None, init_qvel=None, camera="cam"):
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)
    path_norm = xml_path.replace("\\", "/")

    if "rattleback" in path_norm:
        renderer = mujoco.Renderer(model, height=height, width=width)
        render_rattleback_compare(model, data, renderer, output_path,
                                  fps=fps, width=width, height=height,
                                  camera=camera)
        return

    if init_qpos is not None:
        for i, v in enumerate(init_qpos):
            if i < model.nq:
                data.qpos[i] = v

    if init_qvel is not None:
        for i, v in enumerate(init_qvel):
            if i < model.nv:
                data.qvel[i] = v

    mujoco.mj_forward(model, data)

    renderer = mujoco.Renderer(model, height=height, width=width)

    sim_dt = model.opt.timestep
    frame_dt = 1.0 / fps
    steps_per_frame = max(1, int(round(frame_dt / sim_dt)))
    n_frames = int(round(duration * fps))

    # Mocap pull hand: ramp x along +x (m/s).  Used by spool_with_string.
    mocap_pull_speed = 0.0
    mocap_x0 = None
    if model.nmocap > 0:
        mocap_pull_speed = 0.11
        mocap_x0 = float(data.mocap_pos[0, 0])

    # mass_through_hole: kinematic reel-in (r+z from equality); phi from dynamics.
    string_L = 0.52
    r_start, r_end = 0.44, 0.16
    reel_scene = "mass_through_hole" in xml_path.replace("\\", "/")
    adr_r = adr_z = dof_r = dof_z = None
    if reel_scene:
        j_r = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "r")
        j_z = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "z_hang")
        adr_r = model.jnt_qposadr[j_r]
        adr_z = model.jnt_qposadr[j_z]
        dof_r = model.jnt_dofadr[j_r]
        dof_z = model.jnt_dofadr[j_z]
    reel_rate = 0.038 if reel_scene else 0.0
    catenary_scene = "hanging_chain_catenary" in path_norm
    sag_start, sag_end = 0.0, 1.0
    settle_t = 4.0
    pyramid_scene = "pyramid_keystone_removal" in path_norm
    pyramid_kick_t = 0.55
    pyramid_kick_vy = 2.6
    pyramid_kicked = False
    if pyramid_scene:
        ks_bid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "keystone")
        ks_jnt = model.body_jntadr[ks_bid]
        ks_dof = model.jnt_dofadr[ks_jnt]

    frames = []
    for i in range(n_frames):
        t_frame = i * frame_dt
        if catenary_scene:
            u = min(1.0, t_frame / settle_t)
            u = u * u * (3.0 - 2.0 * u)
            sag = sag_start + (sag_end - sag_start) * u
            _apply_catenary_chain(model, data, sag)
            mujoco.mj_forward(model, data)
        elif model.nu > 0:
            data.ctrl[:] = model.actuator_ctrlrange[:, 1]
        for j in range(steps_per_frame):
            if catenary_scene:
                break
            t = t_frame + j * sim_dt
            if reel_scene:
                r_tgt = max(r_end, r_start - reel_rate * t)
                data.qpos[adr_r] = r_tgt
                data.qpos[adr_z] = string_L - r_tgt
                data.qvel[dof_r] = -reel_rate
                data.qvel[dof_z] = reel_rate
                mujoco.mj_forward(model, data)
            if mocap_x0 is not None:
                data.mocap_pos[0, 0] = mocap_x0 + mocap_pull_speed * t
            if pyramid_scene and t >= pyramid_kick_t and not pyramid_kicked:
                data.qvel[ks_dof + 1] = pyramid_kick_vy
                pyramid_kicked = True
            mujoco.mj_step(model, data)
        renderer.update_scene(data, camera=camera)
        frame = renderer.render()
        frames.append(frame)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    imageio.mimsave(output_path, frames, fps=fps, quality=8,
                    macro_block_size=1)
    print(f"Wrote {output_path}  ({len(frames)} frames @ {fps} fps, {width}x{height})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True, help="MuJoCo XML path")
    ap.add_argument("--out", required=True, help="Output MP4 path")
    ap.add_argument("--duration", type=float, default=5.0)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--init-qpos", type=str, default=None,
                    help="Comma-separated initial joint positions")
    ap.add_argument("--init-qvel", type=str, default=None,
                    help="Comma-separated initial joint velocities")
    ap.add_argument("--camera", type=str, default="cam")
    args = ap.parse_args()

    init_qpos = None
    if args.init_qpos:
        init_qpos = [float(x) for x in args.init_qpos.split(",")]
    init_qvel = None
    if args.init_qvel:
        init_qvel = [float(x) for x in args.init_qvel.split(",")]

    render_scene(args.scene, args.out,
                 duration=args.duration, fps=args.fps,
                 width=args.width, height=args.height,
                 init_qpos=init_qpos, init_qvel=init_qvel,
                 camera=args.camera)


if __name__ == "__main__":
    main()
