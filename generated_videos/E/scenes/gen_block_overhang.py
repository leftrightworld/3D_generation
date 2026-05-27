"""
Procedurally generate scenes/block_overhang.xml: the classic "book stacking"
problem.  N identical bricks stacked so that each brick shifts to the +x
side of the one below it.  The theoretical max-overhang formula is:

    overhang_past_table_edge = (L/2) * H_N           (H_N = 1 + 1/2 + ... + 1/N)

construction: brick at position k from the top is offset by L/(2k) toward +x
from the brick below it (where k counts top-down, 1 for the top).  For our
brick 0 = bottom indexing, the offset from brick j-1 to brick j is
L / (2 * (N - j)).

We use SAFETY < 1.0 so the stack's CoM is comfortably inside the table edge;
exact-maximum stacks are unstable to any numerical perturbation in MuJoCo.
"""
import math
import os

# ---- parameters ------------------------------------------------------------
N      = 12
L      = 0.40      # brick length along x
W      = 0.10      # brick width  along y
H      = 0.04      # brick height along z
M      = 0.06      # brick mass
SAFETY = 0.85      # fraction of theoretical maximum offset (1.0 == on the brink)

# Cumulative x of each brick center.  Bottom brick (j=0) sits with its
# RIGHT edge at x=0 (the table edge), so x_0 = -L/2.
def brick_x(j):
    x = -L / 2
    for k in range(1, j + 1):
        x += SAFETY * L / (2 * (N - k))
    return x

bricks_xml = []
for j in range(N):
    xj = brick_x(j)
    zj = j * H + H / 2 + 0.001 * j  # tiny extra gap so contacts settle cleanly
    color = "brick_warm" if j % 2 == 0 else "brick_cool"
    bricks_xml.append(f'''    <body name="brick{j}" pos="{xj:.5f} 0 {zj:.5f}">
      <freejoint/>
      <geom type="box" size="{L * 0.5} {W * 0.5} {H * 0.5}" mass="{M}"
            material="{color}"/>
    </body>''')

bricks_block = "\n".join(bricks_xml)

# Stack CoM (for camera framing reference).
stack_com = sum(brick_x(j) for j in range(N)) / N
top_right = brick_x(N - 1) + L / 2
print(f"Stack CoM x = {stack_com:.4f}  (must be <= 0 for stability)")
print(f"Top brick right edge x = {top_right:.4f}  (overhang past table edge)")


xml = f"""<mujoco model="block_overhang">
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="3" cone="elliptic"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="34"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="6" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <material name="floor_mat"  rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="table_wood" rgba="0.55 0.42 0.28 1" specular="0.15" shininess="0.2"/>
    <material name="brick_warm" rgba="0.92 0.78 0.46 1" specular="0.1" shininess="0.12"/>
    <material name="brick_cool" rgba="0.78 0.66 0.36 1" specular="0.1" shininess="0.12"/>
  </asset>

  <default>
    <!-- High friction so bricks don't slip; stiff contacts so the stack
         doesn't sag visibly under its own weight. -->
    <geom friction="0.8 0.04 0.005" solref="0.003 1" solimp="0.97 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <!-- Table.  Top face at z=0; right edge at x=0; brick 0 sits with its
         right edge aligned to the table edge. -->
    <geom name="table" type="box" pos="-0.80 0 -0.06"
          size="0.80 0.40 0.06" material="table_wood"/>
    <!-- Table legs for visual context. -->
    <geom type="box" size="0.025 0.025 0.50"
          pos="-1.55 -0.30 -0.62" material="table_wood"/>
    <geom type="box" size="0.025 0.025 0.50"
          pos="-1.55  0.30 -0.62" material="table_wood"/>
    <geom type="box" size="0.025 0.025 0.50"
          pos="-0.10 -0.30 -0.62" material="table_wood"/>
    <geom type="box" size="0.025 0.025 0.50"
          pos="-0.10  0.30 -0.62" material="table_wood"/>

    <!-- {N} bricks stacked with overhang = SAFETY * theoretical max. -->
{bricks_block}

    <!-- Camera: pure profile from -y direction, horizontal look — the
         cantilever silhouette is the point of the demo. -->
    <camera name="cam" pos="0.18 -2.20 0.26" fovy="36"
            xyaxes="1 0 0   0 0 1"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "block_overhang.xml")
with open(out_path, "w") as f:
    f.write(xml)
print(f"Wrote {out_path}  (N={N}, max overhang past table = {top_right:.3f} m)")
