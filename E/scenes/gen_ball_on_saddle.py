"""
Generate scenes/ball_on_saddle.xml — overlapping tile grid on z = A*(x² − y²) + Z0.
"""
import os

A = 2.5
Z0 = 0.062
HALF = 0.16
N = 32
OVERLAP = 0.58
HALF_H = 0.0018
BALL_R = 0.022
Y0 = 0.006
DURATION = 1.0
INIT_QVEL = "0,0.02,0,0,0,0"

script_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(script_dir, "ball_on_saddle.xml")


def saddle_z(x, y):
    return A * (x * x - y * y) + Z0


def max_tile_top_under(bx, by, r=BALL_R):
    """Highest tile top under a sphere at (bx, by)."""
    best = -1e9
    half_tile = step * OVERLAP
    for i in range(N):
        for j in range(N):
            x = -HALF + i * step
            y = -HALF + j * step
            if abs(x - bx) <= half_tile + r and abs(y - by) <= half_tile + r:
                best = max(best, saddle_z(x, y) + 2 * HALF_H)
    return best


step = (2 * HALF) / (N - 1)
tile = step * OVERLAP
geoms = []
for i in range(N):
    for j in range(N):
        x = -HALF + i * step
        y = -HALF + j * step
        z_top = saddle_z(x, y)
        geoms.append(
            f'    <geom type="box" pos="{x:.4f} {y:.4f} {z_top + HALF_H:.5f}" '
            f'size="{tile:.5f} {tile:.5f} {HALF_H:.4f}" material="saddle_mat"/>'
        )

geoms_xml = "\n".join(geoms)
z_ball = max_tile_top_under(0, Y0) + BALL_R

xml = f"""<mujoco model="ball_on_saddle">
  <!-- Saddle z = {A}*(x² − y²) + {Z0}; ball rolls along +y (unstable axis).
       Render {DURATION} s with --init-qvel "{INIT_QVEL}" -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.0005" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="5" cone="elliptic"/>

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
    <material name="saddle_mat" rgba="0.78 0.65 0.40 1" specular="0.12" shininess="0.15"/>
    <material name="ball_blue" rgba="0.30 0.50 0.78 1" specular="0.55" shininess="0.65"/>
  </asset>

  <default>
    <geom friction="0.07 0.003 0.0001" solref="0.003 1" solimp="0.96 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"
          contype="0" conaffinity="0"/>

{geoms_xml}

    <body name="ball" pos="0 {Y0:.4f} {z_ball:.5f}">
      <joint name="ball_free" type="free"/>
      <geom name="ball_geom" type="sphere" size="{BALL_R}" mass="0.040"
            material="ball_blue"/>
    </body>

    <!-- Elevated oblique view: standing beside (+x, −y) and above the saddle -->
    <camera name="cam" pos="0.30 -0.20 0.26" fovy="36"
            xyaxes="0.640 0.768 0.000  -0.310 0.258 0.915"/>
  </worldbody>
</mujoco>
"""

with open(xml_path, "w") as f:
    f.write(xml)

print(f"Wrote {xml_path} ({N}x{N} overlapping tiles)")
print(f'Render {DURATION}s --init-qvel "{INIT_QVEL}"')
