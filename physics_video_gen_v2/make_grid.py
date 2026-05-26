"""
Render a scene at K evenly-spaced timesteps and stitch the frames into a grid PNG.

Usage:
  python3 make_grid.py --scene scenes/foo.xml --out out/foo_grid.png \
      --duration 5 --cols 4 --rows 2 --init-qpos "0.6,0,0,0,0"
"""
import argparse
import os

import mujoco
import numpy as np
import imageio.v2 as imageio
from PIL import Image


def render_grid(xml_path, out_path,
                duration=5.0, cols=4, rows=2,
                width=1920, height=1080,
                tile_w=640, tile_h=360,
                init_qpos=None, init_qvel=None, camera="cam"):
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)

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

    mocap_pull_speed = 0.11 if model.nmocap > 0 else 0.0
    mocap_x0 = float(data.mocap_pos[0, 0]) if model.nmocap > 0 else None

    string_L = 0.52
    r_start, r_end = 0.44, 0.16
    reel_scene = "mass_through_hole" in xml_path.replace("\\", "/")
    adr_r = adr_z = None
    if reel_scene:
        j_r = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "r")
        j_z = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "z_hang")
        adr_r = model.jnt_qposadr[j_r]
        adr_z = model.jnt_qposadr[j_z]
    reel_rate = 0.038 if reel_scene else 0.0

    K = cols * rows
    # Snapshot times include t=0 and t=duration.
    times = np.linspace(0.0, duration, K)

    frames = []
    t_now = 0.0
    for t_target in times:
        n_steps = max(0, int(round((t_target - t_now) / sim_dt)))
        if reel_scene:
            r_tgt = max(r_end, r_start - reel_rate * t_target)
            data.qpos[adr_r] = r_tgt
            data.qpos[adr_z] = string_L - r_tgt
            mujoco.mj_forward(model, data)
        if mocap_x0 is not None:
            data.mocap_pos[0, 0] = mocap_x0 + mocap_pull_speed * t_target
        for _ in range(n_steps):
            if reel_scene:
                r_tgt = max(r_end, r_start - reel_rate * t_target)
                data.qpos[adr_r] = r_tgt
                data.qpos[adr_z] = string_L - r_tgt
                mujoco.mj_forward(model, data)
            elif model.nu > 0:
                data.ctrl[:] = model.actuator_ctrlrange[:, 1]
            mujoco.mj_step(model, data)
            t_now += sim_dt
        renderer.update_scene(data, camera=camera)
        img = renderer.render()
        # Downscale for grid
        pil = Image.fromarray(img).resize((tile_w, tile_h), Image.LANCZOS)
        frames.append(np.asarray(pil))

    # Stitch into grid
    grid = np.zeros((rows * tile_h, cols * tile_w, 3), dtype=np.uint8)
    for i, f in enumerate(frames):
        r, c = i // cols, i % cols
        grid[r * tile_h:(r + 1) * tile_h, c * tile_w:(c + 1) * tile_w] = f

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    imageio.imwrite(out_path, grid)
    print(f"Wrote {out_path}  ({rows}x{cols} grid, times: "
          f"{', '.join(f'{t:.2f}s' for t in times)})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--duration", type=float, default=5.0)
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--rows", type=int, default=2)
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--tile-w", type=int, default=640)
    ap.add_argument("--tile-h", type=int, default=360)
    ap.add_argument("--init-qpos", type=str, default=None)
    ap.add_argument("--init-qvel", type=str, default=None)
    ap.add_argument("--camera", type=str, default="cam")
    args = ap.parse_args()

    init_qpos = [float(x) for x in args.init_qpos.split(",")] if args.init_qpos else None
    init_qvel = [float(x) for x in args.init_qvel.split(",")] if args.init_qvel else None

    render_grid(args.scene, args.out,
                duration=args.duration, cols=args.cols, rows=args.rows,
                width=args.width, height=args.height,
                tile_w=args.tile_w, tile_h=args.tile_h,
                init_qpos=init_qpos, init_qvel=init_qvel, camera=args.camera)


if __name__ == "__main__":
    main()
