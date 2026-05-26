"""
Generate scenes/marble_in_funnel.xml — smooth inverted cone funnel + spiraling marble.

Geometry (z-up, throat at z=0, wide rim at z=H):
  - Visual: outer frustum + opaque top rim annulus (no white skybox peek / tip fan).
  - Collision: invisible slope-aligned boxes on inner surface; throat sized for jam.
  - Marble ends wedged in the throat (hole diameter < ball diameter).

Run:
  python3 scenes/gen_funnel.py
  python3 render.py --scene scenes/marble_in_funnel.xml \\
      --out out/new_scenes/marble_in_funnel.mp4 --duration 4.0 --settle 0.06 \\
      --init-qvel "$(cat scenes/marble_in_funnel_qvel.txt)"
"""
import math
import os

# ---- funnel dimensions -------------------------------------------------------
R_TOP = 0.15
# Throat radius < marble radius so the ball jams by diameter at the bottom.
R_BOT = 0.0030
H = 0.20
SHELL_T = 0.003
Z_MIN = 0.012          # mesh/collision start above tip (avoids white degenerate apex)

N_THETA = 128
N_RINGS = 32

N_COLL_THETA = 64
N_COLL_RINGS = 24
COLL_WALL_T = 0.003
OVERLAP = 1.10

# ---- marble ------------------------------------------------------------------
MARBLE_R = 0.008
MARBLE_M = 0.005
START_THETA = 0.0
START_Z = 0.18
VT = 0.42
V_PRESS = 0.11
# Center offset: marble radius + half collision patch thickness (touch box, not air gap).
MARBLE_SURFACE_GAP = COLL_WALL_T * 0.5

FRICTION = "0.14 0.005 0.001"
FRICTION_THROAT = "0.28 0.005 0.001"
SETTLE_S = 0.08

CAM_POS = (0.25, -0.25, 0.30)
CAM_LOOKAT = (0.0, 0.0, 0.10)
CAM_FOVY = 38
DURATION = 4.0

DR_DZ = (R_TOP - R_BOT) / H
CONE_SLOPE = math.atan2(R_TOP - R_BOT, H)


def r_at_z(z: float) -> float:
    return R_BOT + (R_TOP - R_BOT) * (z / H)


def normalize(v):
    n = math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
    if n < 1e-12:
        return (0.0, 0.0, 1.0)
    return (v[0] / n, v[1] / n, v[2] / n)


def quat_from_axes(local_x, local_y, local_z):
    r00, r01, r02 = local_x[0], local_y[0], local_z[0]
    r10, r11, r12 = local_x[1], local_y[1], local_z[1]
    r20, r21, r22 = local_x[2], local_y[2], local_z[2]
    trace = r00 + r11 + r22
    if trace > 0.0:
        s = math.sqrt(trace + 1.0) * 2.0
        w, x, y, z = 0.25 * s, (r21 - r12) / s, (r02 - r20) / s, (r10 - r01) / s
    elif r00 > r11 and r00 > r22:
        s = math.sqrt(1.0 + r00 - r11 - r22) * 2.0
        w, x, y, z = (r21 - r12) / s, 0.25 * s, (r01 + r10) / s, (r02 + r20) / s
    elif r11 > r22:
        s = math.sqrt(1.0 + r11 - r00 - r22) * 2.0
        w, x, y, z = (r02 - r20) / s, (r01 + r10) / s, 0.25 * s, (r12 + r21) / s
    else:
        s = math.sqrt(1.0 + r22 - r00 - r11) * 2.0
        w, x, y, z = (r10 - r01) / s, (r02 + r20) / s, (r12 + r21) / s, 0.25 * s
    return (w, x, y, z)


def surface_frame(theta: float, z: float):
    ct, st = math.cos(theta), math.sin(theta)
    inward = normalize((-ct, -st, DR_DZ))
    t_theta = (-st, ct, 0.0)
    t_down = normalize((-DR_DZ * ct, -DR_DZ * st, -1.0))
    return t_down, inward, t_theta


def inner_point(theta: float, z: float):
    r = r_at_z(z)
    return (r * math.cos(theta), r * math.sin(theta), z)


def coll_ring_z(k: int) -> float:
    u = k / (N_COLL_RINGS - 1) if N_COLL_RINGS > 1 else 0.0
    z_lin = Z_MIN + u * (H - Z_MIN)
    z_bias = H * (1.0 - (1.0 - u) ** 1.35)
    return 0.35 * z_lin + 0.65 * z_bias


def marble_center_on_wall(theta: float, z: float):
    """Place sphere center so it rests on collision patches, not floating off the mesh."""
    px, py, pz = inner_point(theta, z)
    _, n_in, _ = surface_frame(theta, z)
    d = MARBLE_R + MARBLE_SURFACE_GAP
    return (px + d * n_in[0], py + d * n_in[1], pz + d * n_in[2])


def marble_init_velocity(theta: float, z: float):
    _, n_in, t_theta = surface_frame(theta, z)
    tt = normalize(t_theta)
    return (
        VT * tt[0] + V_PRESS * n_in[0],
        VT * tt[1] + V_PRESS * n_in[1],
        VT * tt[2] + V_PRESS * n_in[2],
    )


def jam_height_estimate():
    """Height where inner radius ≈ marble diameter (tangent jam)."""
    target_r = 2.0 * MARBLE_R * 0.98
    if target_r <= R_BOT:
        return Z_MIN
    return H * (target_r - R_BOT) / (R_TOP - R_BOT)


# =============================================================================
# Visual mesh: frustum side (z in [Z_MIN, H]) + top rim annulus (no tip fan)
# =============================================================================
def build_funnel_visual_mesh():
    verts = []
    faces = []

    def add_vertex(x, y, z):
        verts.extend((x, y, z))
        return len(verts) // 3 - 1

    # --- side surface (outer) ---
    grid = []
    for k in range(N_RINGS):
        z = Z_MIN + k * (H - Z_MIN) / (N_RINGS - 1) if N_RINGS > 1 else Z_MIN
        r_out = r_at_z(z) + SHELL_T
        row = []
        for j in range(N_THETA):
            th = j * 2.0 * math.pi / N_THETA
            row.append(add_vertex(r_out * math.cos(th), r_out * math.sin(th), z))
        grid.append(row)

    for k in range(N_RINGS - 1):
        for j in range(N_THETA):
            j1 = (j + 1) % N_THETA
            a, b, c, d = grid[k][j], grid[k + 1][j], grid[k + 1][j1], grid[k][j1]
            faces.extend([a, b, c, a, c, d])

    # --- top rim annulus at z=H (same material; blocks white skybox sliver) ---
    r_in, r_out = R_TOP, R_TOP + SHELL_T
    inner_top, outer_top = [], []
    for j in range(N_THETA):
        th = j * 2.0 * math.pi / N_THETA
        ct, st = math.cos(th), math.sin(th)
        inner_top.append(add_vertex(r_in * ct, r_in * st, H))
        outer_top.append(add_vertex(r_out * ct, r_out * st, H))
    for j in range(N_THETA):
        j1 = (j + 1) % N_THETA
        i0, i1, o0, o1 = inner_top[j], inner_top[j1], outer_top[j], outer_top[j1]
        faces.extend([i0, o0, o1, i0, o1, i1])

    vert_str = " ".join(f"{v:.6f}" for v in verts)
    face_str = " ".join(str(f) for f in faces)
    return vert_str, face_str


# =============================================================================
# Collision patches on inner surface
# =============================================================================
def build_collision_geoms_xml():
    geoms = []
    dth = 2.0 * math.pi / N_COLL_THETA
    z_jam = jam_height_estimate()

    for k in range(N_COLL_RINGS):
        z = coll_ring_z(k)
        z_next = coll_ring_z(min(k + 1, N_COLL_RINGS - 1))
        dz_local = max(abs(z_next - z), (H - Z_MIN) / (N_COLL_RINGS - 1) * 0.5)
        half_g = 0.5 * math.hypot(dz_local, dz_local * DR_DZ) * OVERLAP
        r = r_at_z(z)
        half_chord = max(r * math.sin(math.pi / N_COLL_THETA) * OVERLAP, 0.0008)
        fric = FRICTION_THROAT if z < z_jam + 0.025 else FRICTION
        for j in range(N_COLL_THETA):
            th = (j + 0.5) * dth
            cx, cy, cz = inner_point(th, z)
            lx, ly, lz = surface_frame(th, z)
            qw, qx, qy, qz = quat_from_axes(lx, ly, lz)
            geoms.append(
                f'      <geom name="coll_{k}_{j}" type="box" '
                f'pos="{cx:.5f} {cy:.5f} {cz:.5f}" '
                f'quat="{qw:.6f} {qx:.6f} {qy:.6f} {qz:.6f}" '
                f'size="{half_g:.5f} {COLL_WALL_T * 0.5:.5f} {half_chord:.5f}" '
                f'rgba="0 0 0 0" contype="1" conaffinity="1" group="3" '
                f'density="0" friction="{fric}"/>'
            )
    return "\n".join(geoms)


def camera_axes(pos, target):
    up = (0.0, 0.0, 1.0)
    z_ax = tuple(target[i] - pos[i] for i in range(3))
    zn = math.sqrt(sum(v * v for v in z_ax))
    z_ax = tuple(-v / zn for v in z_ax)
    x_ax = (
        up[1] * z_ax[2] - up[2] * z_ax[1],
        up[2] * z_ax[0] - up[0] * z_ax[2],
        up[0] * z_ax[1] - up[1] * z_ax[0],
    )
    xn = math.sqrt(sum(v * v for v in x_ax))
    x_ax = tuple(v / xn for v in x_ax)
    y_ax = (
        z_ax[1] * x_ax[2] - z_ax[2] * x_ax[1],
        z_ax[2] * x_ax[0] - z_ax[0] * x_ax[2],
        z_ax[0] * x_ax[1] - z_ax[1] * x_ax[0],
    )
    return x_ax, y_ax


mesh_v, mesh_f = build_funnel_visual_mesh()
coll_xml = build_collision_geoms_xml()
cam_x, cam_y = camera_axes(CAM_POS, CAM_LOOKAT)

mx, my, mz = marble_center_on_wall(START_THETA, START_Z)
vx, vy, vz = marble_init_velocity(START_THETA, START_Z)
init_qvel = f"{vx:.4f},{vy:.4f},{vz:.4f},0,0,0"
z_jam = jam_height_estimate()
xml = f"""<mujoco model="marble_in_funnel">
  <!-- Funnel R_top={R_TOP}, R_bot={R_BOT} (jam), H={H}. Est. jam z≈{z_jam:.3f} m -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="5" cone="elliptic" iterations="80"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="38"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="6" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <mesh name="funnel_shell" vertex="{mesh_v}" face="{mesh_f}"/>
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="funnel" rgba="0.88 0.80 0.66 0.93" specular="0.10" shininess="0.25"/>
    <material name="marble_red" rgba="0.95 0.12 0.10 1" specular="0.60" shininess="0.80"/>
  </asset>

  <default>
    <geom solref="0.012 1" solimp="0.98 0.995 0.0005" margin="0.0005"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.32 0.32 0.38" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <body name="funnel" pos="0 0 0">
      <geom name="funnel_vis" type="mesh" mesh="funnel_shell" material="funnel"
            contype="0" conaffinity="0" group="1"/>
{coll_xml}
      <!-- Keep the ball on the sloping wall (block fall-through on the axis). -->
      <geom name="throat_pin" type="cylinder" pos="0 0 {0.5 * z_jam:.4f}"
            size="{MARBLE_R * 0.45:.4f} {0.5 * z_jam:.4f}"
            rgba="0 0 0 0" contype="1" conaffinity="1" group="3"
            density="0" friction="{FRICTION_THROAT}"/>
    </body>

    <body name="marble" pos="{mx:.4f} {my:.4f} {mz:.4f}">
      <freejoint/>
      <geom name="marble_geom" type="sphere" size="{MARBLE_R}" mass="{MARBLE_M}"
            material="marble_red" friction="{FRICTION}" group="2"/>
    </body>

    <camera name="cam" pos="{CAM_POS[0]:.2f} {CAM_POS[1]:.2f} {CAM_POS[2]:.2f}"
            fovy="{CAM_FOVY}"
            xyaxes="{cam_x[0]:.5f} {cam_x[1]:.5f} {cam_x[2]:.5f} {cam_y[0]:.5f} {cam_y[1]:.5f} {cam_y[2]:.5f}"/>
  </worldbody>
</mujoco>
"""

scene_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(scene_dir, "marble_in_funnel.xml")
qvel_path = os.path.join(scene_dir, "marble_in_funnel_qvel.txt")

with open(out_path, "w") as f:
    f.write(xml)
with open(qvel_path, "w") as f:
    f.write(init_qvel)

print(f"Wrote {out_path}")
print(f"  Throat R_bot={R_BOT} m (ball D={2*MARBLE_R} m), est. jam z≈{z_jam:.4f} m")
print(f"  Marble: ({mx:.4f}, {my:.4f}, {mz:.4f}), qvel=({init_qvel})")
print(f'  render.py ... --duration {DURATION} --settle {SETTLE_S} --init-qvel "{init_qvel}"')
