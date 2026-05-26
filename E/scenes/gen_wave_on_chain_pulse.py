"""
Procedurally generate scenes/wave_on_chain_pulse.xml.

Physics:
  - N=15 identical masses on a horizontal line (x-axis), equilibrium z = Z_EQ.
  - Each mass has one vertical slide joint (transverse displacement only).
  - Adjacent masses are coupled by stiff spatial tendons (spring-like links).
  - A localized pulse is applied only to m0 via --init-qpos (see render command).
  - The disturbance propagates rightward along the chain as a transverse wave.

Visual:
  - m0 red, m1..m14 blue; gray tendons; faint equilibrium reference line.
  - Side view from -y; standard project skybox / cream floor (masses do not touch floor).
"""
import math
import os

N = 15
DX = 0.055
Z_EQ = 0.25
R = 0.014
M = 0.020

K_LINK = 220.0
D_LINK = 1.0
D_SLIDE = 0.10

PULSE_Z = 0.045

CAM_POS = (0.38, -1.0, 0.28)
CAM_TARGET = (0.38, 0.0, Z_EQ)
CAM_FOVY = 34.0

CHAIN_X0 = 0.0
CHAIN_X1 = (N - 1) * DX


def _cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def _norm(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)


def camera_xyaxes(pos, target):
    """MuJoCo camera xyaxes from world position and look-at point."""
    forward = tuple(target[k] - pos[k] for k in range(3))
    f_len = _norm(forward)
    forward = tuple(c / f_len for c in forward)
    z_cam = tuple(-c for c in forward)
    world_up = (0.0, 0.0, 1.0)
    x_cam = _cross(world_up, z_cam)
    n = _norm(x_cam)
    if n < 1e-8:
        x_cam = (1.0, 0.0, 0.0)
    else:
        x_cam = tuple(c / n for c in x_cam)
    y_cam = _cross(z_cam, x_cam)
    y_len = _norm(y_cam)
    y_cam = tuple(c / y_len for c in y_cam)
    return (
        f"{x_cam[0]:.4f} {x_cam[1]:.4f} {x_cam[2]:.4f}   "
        f"{y_cam[0]:.4f} {y_cam[1]:.4f} {y_cam[2]:.4f}"
    )


bodies = []
tendons = []
qpos_parts = []

for i in range(N):
    x = CHAIN_X0 + i * DX
    mat = "bob_red" if i == 0 else "bob_blue"
    bodies.append(
        f'    <body name="m{i}" pos="{x:.4f} 0 {Z_EQ:.4f}">\n'
        f'      <joint name="z{i}" type="slide" axis="0 0 1"\n'
        f'             stiffness="0" damping="{D_SLIDE}" range="-0.10 0.10"/>\n'
        f'      <geom type="sphere" size="{R}" mass="{M}" material="{mat}"\n'
        f'            contype="0" conaffinity="0"/>\n'
        f'      <site name="s{i}" pos="0 0 0" size="0.001"/>\n'
        f'    </body>'
    )
    qpos_parts.append(f"{PULSE_Z if i == 0 else 0:.4f}")

for i in range(N - 1):
    tendons.append(
        f'    <spatial name="link{i}" stiffness="{K_LINK}" damping="{D_LINK}"\n'
        f'             springlength="{DX:.5f}" width="0.006"\n'
        f'             rgba="0.35 0.32 0.30 0.90" limited="false">\n'
        f'      <site site="s{i}"/>\n'
        f'      <site site="s{i + 1}"/>\n'
        f'    </spatial>'
    )

bodies_xml = "\n".join(bodies)
tendons_xml = "\n".join(tendons)
init_qpos = ",".join(qpos_parts)
cam_axes = camera_xyaxes(CAM_POS, CAM_TARGET)
ref_half = 0.5 * (CHAIN_X1 + 0.04)

xml = f"""<mujoco model="wave_on_chain_pulse">
  <!-- {N}-mass transverse chain; pulse on m0 via --init-qpos. -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 0" integrator="implicitfast"/>

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
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="bob_red" rgba="0.86 0.34 0.30 1" specular="0.35" shininess="0.4"/>
    <material name="bob_blue" rgba="0.30 0.50 0.78 1" specular="0.35" shininess="0.4"/>
    <material name="ref_line" rgba="0.55 0.52 0.50 0.45" specular="0" shininess="0"/>
  </asset>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"
          contype="0" conaffinity="0"/>

    <!-- Equilibrium height z = {Z_EQ} (visual only). -->
    <geom name="eq_line" type="box" size="{ref_half:.4f} 0.001 0.001"
          pos="{0.5 * CHAIN_X1:.4f} 0 {Z_EQ:.4f}" material="ref_line"
          contype="0" conaffinity="0"/>

{bodies_xml}

    <camera name="cam" pos="{CAM_POS[0]:.2f} {CAM_POS[1]:.2f} {CAM_POS[2]:.2f}"
            fovy="{CAM_FOVY:.0f}" xyaxes="{cam_axes}"/>
  </worldbody>

  <tendon>
{tendons_xml}
  </tendon>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "wave_on_chain_pulse.xml")
with open(out_path, "w") as f:
    f.write(xml)

print(f"Wrote {out_path}  (N={N}, Z_EQ={Z_EQ}, pulse dz={PULSE_Z} on m0)")
print(f'Suggested --init-qpos: "{init_qpos}"')
print("Render 3.0 s:")
print(f'  python3 render.py --scene scenes/wave_on_chain_pulse.xml '
      f'--out out/new_scenes/wave_on_chain_pulse.mp4 --duration 3.0 '
      f'--init-qpos "{init_qpos}"')
