"""
Generate scenes/monkey_and_hunter.xml — three side-by-side monkey-and-hunter demos
with slow / medium / fast dart speeds (different |qvel|, different collision times).

Run:
  python3 scenes/gen_monkey_and_hunter.py
  python3 render.py --scene scenes/monkey_and_hunter.xml \\
      --out out/new_scenes/monkey_and_hunter.mp4 --duration 3.5 \\
      --init-qvel "$(cat scenes/monkey_and_hunter_qvel.txt)"
  python3 make_grid.py --scene scenes/monkey_and_hunter.xml \\
      --out out/monkey_and_hunter_grid.png --duration 1.0 --cols 4 --rows 2 \\
      --init-qvel "$(cat scenes/monkey_and_hunter_qvel.txt)"
"""
import math
import os

# ---- per-demo geometry (local coords, z up) ---------------------------------
MUZZLE = (0.12, 0.0, 0.12)
MONKEY = (1.00, 0.0, 0.80)
DART_R = 0.032
MONKEY_R = 0.040

# Side-by-side spacing (m); each dart aims at its own local monkey.
X_OFFSETS = [0.0, 2.0, 4.0]

# Slow / medium / fast (m/s). 2.2 m/s is below the in-air range for this geometry
# (|r|/v would exceed free-fall time from z=0.8 m); 2.85 is the slowest that still
# collides clearly above the floor in simulation.
DART_SPEEDS = [2.85, 3.50, 5.20]
SCENE_LABELS = ["A slow", "B medium", "C fast"]
DART_MATERIALS = ["dart_slow", "dart_med", "dart_fast"]

# ---- cannon visuals ---------------------------------------------------------
BASE_POS = (-0.06, 0.0, 0.025)
BASE_SIZE = (0.06, 0.05, 0.025)
BARREL_LEN = 0.10
BARREL_SIZE = (0.10, 0.035, 0.035)

AIM_LINE_RADIUS = 0.004
MARKER_R = 0.012

DURATION_MP4 = 3.5
DURATION_GRID = 1.0   # collisions occur ~0.20–0.37 s; grid must sample that window
CAM_FOVY = 38


def local_aim_unit():
    dx = MONKEY[0] - MUZZLE[0]
    dz = MONKEY[2] - MUZZLE[2]
    length = math.hypot(dx, dz)
    return dx / length, dz / length, length


def barrel_euler_y(ux: float, uz: float) -> float:
    return math.atan2(uz, ux)


def dart_qvel(speed: float, ux: float, uz: float) -> tuple[float, float, float]:
    return speed * ux, 0.0, speed * uz


def scene_block(idx: int, x0: float, speed: float, label: str, dart_mat: str) -> str:
    ux, uz, _ = local_aim_unit()
    pitch = barrel_euler_y(ux, uz)
    mx, my, mz = MONKEY[0] + x0, MONKEY[1], MONKEY[2]
    dx, dy, dz = MUZZLE[0] + x0, MUZZLE[1], MUZZLE[2]
    vx, vy, vz = dart_qvel(speed, ux, uz)
    barrel_cx = dx - ux * BARREL_LEN * 0.45
    barrel_cz = dz - uz * BARREL_LEN * 0.45

    return f"""
    <!-- Scene {chr(65 + idx)} ({label}): speed={speed:.2f} m/s
         dart qvel linear=({vx:.4f}, {vy:.4f}, {vz:.4f}) |q|={speed:.2f}
         aim: local monkey ({MONKEY[0]:.2f},{MONKEY[2]:.2f}) from local muzzle ({MUZZLE[0]:.2f},{MUZZLE[2]:.2f}) -->
    <geom name="cannon_base_{idx}" type="box"
          pos="{x0 + BASE_POS[0]:.4f} {BASE_POS[1]:.4f} {BASE_POS[2]:.4f}"
          size="{BASE_SIZE[0]} {BASE_SIZE[1]} {BASE_SIZE[2]}"
          material="wood_dark" contype="0" conaffinity="0"/>
    <geom name="cannon_barrel_{idx}" type="box"
          pos="{barrel_cx:.4f} {dy:.4f} {barrel_cz:.4f}"
          euler="0 {pitch:.6f} 0"
          size="{BARREL_SIZE[0]} {BARREL_SIZE[1]} {BARREL_SIZE[2]}"
          material="wood" contype="0" conaffinity="0"/>
    <geom name="aim_line_{idx}" type="capsule"
          fromto="{dx:.4f} {dy:.4f} {dz:.4f} {mx:.4f} {my:.4f} {mz:.4f}"
          size="{AIM_LINE_RADIUS}" rgba="0.55 0.72 0.55 0.35"
          contype="0" conaffinity="0"/>
    <geom name="release_marker_{idx}" type="sphere"
          pos="{mx:.4f} {my:.4f} {mz:.4f}" size="{MARKER_R}"
          material="marker_mat" contype="0" conaffinity="0"/>

    <body name="dart_{idx}" pos="{dx:.4f} {dy:.4f} {dz:.4f}">
      <joint name="dart_free_{idx}" type="free"/>
      <geom name="dart_geom_{idx}" type="sphere" size="{DART_R}"
            mass="0.08" material="{dart_mat}"/>
    </body>

    <body name="monkey_{idx}" pos="{mx:.4f} {my:.4f} {mz:.4f}">
      <joint name="monkey_free_{idx}" type="free"/>
      <geom name="monkey_geom_{idx}" type="sphere" size="{MONKEY_R}"
            mass="0.10" material="bob_red"/>
    </body>
"""


ux, uz, aim_len = local_aim_unit()
x_max = max(X_OFFSETS) + MONKEY[0]
cam_cx = 0.5 * (min(X_OFFSETS) + x_max)
cam_cz = 0.5 * (MUZZLE[2] + MONKEY[2])
cam_dist_y = max(3.2, (x_max - min(X_OFFSETS)) * 0.90)

scenes_xml = "".join(
    scene_block(i, x0, sp, lab, mat)
    for i, (x0, sp, lab, mat) in enumerate(
        zip(X_OFFSETS, DART_SPEEDS, SCENE_LABELS, DART_MATERIALS)
    )
)

# init-qvel order in XML: dart_0, monkey_0, dart_1, monkey_1, dart_2, monkey_2
qvel_lines = []
qvel_parts = []
for i, speed in enumerate(DART_SPEEDS):
    vx, vy, vz = dart_qvel(speed, ux, uz)
    qvel_lines.append(
        f"# Scene {chr(65+i)} speed={speed:.2f} m/s  "
        f"dart_qvel=({vx:.6f}, {vy:.6f}, {vz:.6f}, 0, 0, 0)"
    )
    qvel_parts.extend([vx, vy, vz, 0.0, 0.0, 0.0])
    qvel_parts.extend([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
qvel_str = ", ".join(f"{v:.6f}" for v in qvel_parts)

speed_comment = "\n".join(
    f"  <!-- Scene {chr(65+i)} speed = {s:.2f} m/s -->"
    for i, s in enumerate(DART_SPEEDS)
)

xml = f"""<mujoco model="monkey_and_hunter">
  <!-- Three parallel monkey-and-hunter demos: different dart speeds, same local geometry.
       Regenerate: python3 scenes/gen_monkey_and_hunter.py
       Render init-qvel: scenes/monkey_and_hunter_qvel.txt -->
{speed_comment}
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="3" cone="elliptic"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="{CAM_FOVY}"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="6" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="wood" rgba="0.93 0.82 0.58 1" specular="0.1" shininess="0.1"/>
    <material name="wood_dark" rgba="0.78 0.65 0.40 1" specular="0.1" shininess="0.1"/>
    <material name="dart_slow" rgba="0.55 0.72 0.92 1" specular="0.35" shininess="0.4"/>
    <material name="dart_med" rgba="0.30 0.50 0.78 1" specular="0.35" shininess="0.4"/>
    <material name="dart_fast" rgba="0.12 0.28 0.55 1" specular="0.35" shininess="0.4"/>
    <material name="bob_red" rgba="0.86 0.34 0.30 1" specular="0.35" shininess="0.4"/>
    <material name="marker_mat" rgba="0.28 0.27 0.26 1" specular="0.1" shininess="0.1"/>
  </asset>

  <default>
    <geom friction="0.7 0.04 0.001" solref="0.005 1" solimp="0.95 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>
{scenes_xml}
    <camera name="cam" pos="{cam_cx:.4f} {-cam_dist_y:.4f} {cam_cz:.4f}" fovy="{CAM_FOVY}"
            xyaxes="1.000 0.000 0.000   0.000 0.000 1.000"/>
  </worldbody>
</mujoco>
"""

here = os.path.dirname(__file__)
xml_path = os.path.join(here, "monkey_and_hunter.xml")
qvel_path = os.path.join(here, "monkey_and_hunter_qvel.txt")


def verify_collisions():
    try:
        import mujoco
        import numpy as np
    except ImportError:
        return

    m = mujoco.MjModel.from_xml_path(xml_path)
    d = mujoco.MjData(m)
    qvel = [float(x) for x in qvel_str.split(",")]
    for i, v in enumerate(qvel):
        d.qvel[i] = v

    names = [f"dart_{i}" for i in range(3)] + [f"monkey_{i}" for i in range(3)]
    body_ids = [mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, n) for n in names]

    contact_r = DART_R + MONKEY_R
    hits = [None] * 3
    print("\n--- collision debug ---")
    for step in range(3000):
        mujoco.mj_step(m, d)
        t = step * m.opt.timestep
        for pi in range(3):
            if hits[pi] is not None:
                continue
            pa = d.xpos[body_ids[pi]]
            pb = d.xpos[body_ids[pi + 3]]
            dist = float(np.linalg.norm(pa - pb))
            if dist < contact_r and float(pa[2]) > 0.05:
                hits[pi] = (t, float(pa[2]), dist)
    for pi, sp in enumerate(DART_SPEEDS):
        h = hits[pi]
        if h:
            print(
                f"Scene {chr(65+pi)} speed={sp:.2f} m/s  "
                f"t_hit≈{h[0]:.3f}s  z_hit≈{h[1]:.3f}m  min_dist={h[2]:.4f}m"
            )
        else:
            print(f"Scene {chr(65+pi)} speed={sp:.2f} m/s  NO mid-air hit")


with open(xml_path, "w") as f:
    f.write(xml)
with open(qvel_path, "w") as f:
    f.write(qvel_str + "\n")

print(f"Wrote {xml_path}")
print(f"Wrote {qvel_path}")
print(f"Local aim distance={aim_len:.3f} m, unit=({ux:.4f}, {uz:.4f})")
for line in qvel_lines:
    print(line)

verify_collisions()
