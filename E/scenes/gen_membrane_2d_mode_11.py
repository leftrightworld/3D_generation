"""
Procedurally generate scenes/membrane_2d_mode_11.xml: 10×10 mass-spring membrane
with pure (1,1) normal mode.  Interior nodes slide on +z; edges are fixed.
Nearest-neighbor spatial tendons couple the lattice (no diagonals).
Initial z_ij = A·sin(πi/9)·sin(πj/9),  A = 0.02 m.
"""
import math
import os

import numpy as np

N = 10
A = 0.02
ORIGIN = -0.10
SPACING = 0.022
Z0 = 0.20
R = 0.005
M = 0.005

K_LINK = 30.0
D_LINK = 0.012
K_MEM = 0.0
D_MEM = 0.008

# Frame the full 0.20×0.20 m lattice centered in a 16:9 shot.
MEM_CX = ORIGIN + 0.5 * (N - 1) * SPACING
MEM_CY = MEM_CX
MEM_CZ = Z0
# Look slightly below the membrane plane so the lattice sits centered in 16:9.
CAM_TARGET = (MEM_CX, MEM_CY, Z0 - 0.06)
_CAM_DIR = np.array([0.58, -0.58, 0.52], dtype=float)
_CAM_DIR /= np.linalg.norm(_CAM_DIR)
CAM_DIST = 0.40
CAM_POS = tuple(np.array(CAM_TARGET) + CAM_DIST * _CAM_DIR)
CAM_FOVY = 44.0


def camera_xyaxes(pos, target):
    """MuJoCo camera: local -Z looks toward target; xyaxes gives X and Y axes."""
    forward = np.asarray(target, dtype=float) - np.asarray(pos, dtype=float)
    forward /= np.linalg.norm(forward)
    z_cam = -forward
    world_up = np.array([0.0, 0.0, 1.0])
    x_cam = np.cross(world_up, z_cam)
    n = np.linalg.norm(x_cam)
    if n < 1e-8:
        x_cam = np.array([1.0, 0.0, 0.0])
    else:
        x_cam /= n
    y_cam = np.cross(z_cam, x_cam)
    y_cam /= np.linalg.norm(y_cam)
    return (
        f"{x_cam[0]:.4f} {x_cam[1]:.4f} {x_cam[2]:.4f}   "
        f"{y_cam[0]:.4f} {y_cam[1]:.4f} {y_cam[2]:.4f}"
    )


bodies = []
sites = []
tendons = []
qpos_parts = []

for i in range(N):
    for j in range(N):
        x = ORIGIN + i * SPACING
        y = ORIGIN + j * SPACING
        z_mode = A * math.sin(math.pi * i / 9.0) * math.sin(math.pi * j / 9.0)
        name = f"n{i}_{j}"
        edge = i == 0 or i == N - 1 or j == 0 or j == N - 1
        mat = "membrane_edge" if edge else "membrane_interior"

        if edge:
            bodies.append(
                f'    <geom name="{name}" type="sphere" '
                f'pos="{x:.4f} {y:.4f} {Z0 + z_mode:.4f}" '
                f'size="{R}" mass="{M}" material="{mat}" '
                f'contype="0" conaffinity="0"/>'
            )
            sites.append(
                f'    <site name="s{i}_{j}" '
                f'pos="{x:.4f} {y:.4f} {Z0 + z_mode:.4f}" size="0.001"/>'
            )
        else:
            bodies.append(
                f'    <body name="{name}" pos="{x:.4f} {y:.4f} {Z0:.4f}">\n'
                f'      <joint name="z{i}_{j}" type="slide" axis="0 0 1"\n'
                f'             stiffness="{K_MEM}" damping="{D_MEM}" '
                f'range="-0.05 0.05"/>\n'
                f'      <geom type="sphere" size="{R}" mass="{M}" '
                f'material="{mat}" contype="0" conaffinity="0"/>\n'
                f'      <site name="s{i}_{j}" pos="0 0 0" size="0.001"/>\n'
                f'    </body>'
            )
            qpos_parts.append(f"{z_mode:.6f}")

bodies_xml = "\n".join(bodies)
sites_xml = "\n".join(sites)

neighbor_dirs = ((1, 0), (0, 1))
stiffness_for = {
    (1, 0): (K_LINK, D_LINK),
    (0, 1): (K_LINK, D_LINK),
}
# Optional diagonal shear stiffening (disabled — tends to bleed (1,1) mode energy).
# neighbor_dirs = ((1, 0), (0, 1), (1, 1), (1, -1))

for i in range(N):
    for j in range(N):
        for di, dj in neighbor_dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            x0 = ORIGIN + i * SPACING
            y0 = ORIGIN + j * SPACING
            x1 = ORIGIN + ni * SPACING
            y1 = ORIGIN + nj * SPACING
            rest = math.hypot(x1 - x0, y1 - y0)
            k_stiff, k_damp = stiffness_for[(di, dj)]
            tendons.append(
                f'    <spatial name="k_{i}_{j}_{ni}_{nj}" '
                f'stiffness="{k_stiff}" damping="{k_damp}" '
                f'springlength="{rest:.5f}" width="0.0012" '
                f'rgba="0.45 0.42 0.40 0.50" limited="false">\n'
                f'      <site site="s{i}_{j}"/>\n'
                f'      <site site="s{ni}_{nj}"/>\n'
                f'    </spatial>'
            )

tendons_xml = "\n".join(tendons)
init_qpos = ",".join(qpos_parts)
cam_axes = camera_xyaxes(CAM_POS, CAM_TARGET)

xml = f"""<mujoco model="membrane_2d_mode_11">
  <!-- 10×10 square membrane; pure (1,1) mode, +z vertical oscillation. -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 0" integrator="implicitfast"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="{CAM_FOVY:.0f}"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="6" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="frame_wood" rgba="0.78 0.65 0.40 1" specular="0.12" shininess="0.15"/>
    <material name="membrane_edge" rgba="0.22 0.32 0.52 1" specular="0.35" shininess="0.45"/>
    <material name="membrane_interior" rgba="0.92 0.55 0.28 1" specular="0.45" shininess="0.55"/>
    <material name="ref_plane" rgba="0.88 0.86 0.84 0.18" specular="0" shininess="0"/>
  </asset>

  <default>
    <geom contype="0" conaffinity="0"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <!-- Rest plane at equilibrium height z = {Z0}. -->
    <geom name="ref_plane" type="box" size="0.105 0.105 0.0005"
          pos="0 0 {Z0:.4f}" material="ref_plane"/>

    <!-- Square frame marking fixed boundary. -->
    <geom type="box" size="0.004 0.11 0.004" pos="0 {-0.10:.4f} {Z0 - 0.012:.4f}" material="frame_wood"/>
    <geom type="box" size="0.004 0.11 0.004" pos="0 {0.098:.4f} {Z0 - 0.012:.4f}" material="frame_wood"/>
    <geom type="box" size="0.11 0.004 0.004" pos="{-0.10:.4f} 0 {Z0 - 0.012:.4f}" material="frame_wood"/>
    <geom type="box" size="0.11 0.004 0.004" pos="{0.098:.4f} 0 {Z0 - 0.012:.4f}" material="frame_wood"/>

{sites_xml}

{bodies_xml}

    <camera name="cam" pos="{CAM_POS[0]:.3f} {CAM_POS[1]:.3f} {CAM_POS[2]:.3f}" fovy="{CAM_FOVY:.0f}"
            xyaxes="{cam_axes}"/>
  </worldbody>

  <tendon>
{tendons_xml}
  </tendon>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "membrane_2d_mode_11.xml")
with open(out_path, "w") as f:
    f.write(xml)

n_interior = len(qpos_parts)
DURATION = 3.5
print(f"Wrote {out_path}  ({N}×{N} nodes, {n_interior} slide DOFs, "
      f"{len(tendons)} tendons)")
print(f'Suggested --init-qpos: "{init_qpos}"')
print(f"Render {DURATION} s:")
print(
    f'  python3 render.py --scene scenes/membrane_2d_mode_11.xml '
    f'--out out/new_scenes/membrane_2d_mode_11.mp4 --duration {DURATION} '
    f'--init-qpos "{init_qpos}"'
)
print("Grid 8-frame preview:")
print(
    f'  python3 make_grid.py --scene scenes/membrane_2d_mode_11.xml '
    f'--out out/membrane_2d_mode_11_grid.png --duration {DURATION} '
    f'--cols 4 --rows 2 --init-qpos "{init_qpos}"'
)
