"""
Procedurally generate scenes/dominoes.xml: a chain of N upright domino tiles
laid out along a straight line.  First domino is pre-tilted just past the
balance angle so it falls forward and starts the cascade.
"""
import math
import os

# ---- geometry parameters ---------------------------------------------------
N = 22                  # number of dominoes
HX, HY, HZ = 0.006, 0.018, 0.045   # half-sizes (toppling dir, depth, height)
SPACING = 0.04          # base-to-base spacing along +x (must be < HZ + HX)
START_X = -0.45         # base position of first domino
COLOR_CYCLE = [
    "dom_cream",
    "dom_peach",
    "dom_blue",
    "dom_dark",
]

# ---- first-domino tilt (so it starts the cascade) -------------------------
# Tip angle past the balance point. Balance angle = atan(HX/HZ) ≈ 7.6°.
# Use 10 deg so it definitely falls forward.
TILT_DEG = 10.0
tilt = math.radians(TILT_DEG)
# Quaternion for rotation about +y so the body tips with its TOP moving in +x
# (toward the next domino).  +y rotation by alpha sends body +z -> +x direction.
qw = math.cos(tilt * 0.5)
qy = math.sin(tilt * 0.5)


def domino_body(i):
    x = START_X + i * SPACING
    mat = COLOR_CYCLE[i % len(COLOR_CYCLE)]
    if i == 0:
        # Pre-tilted: pivot around the leading bottom edge (at x_base + HX, z=0)
        # so it falls onto the next domino instead of slipping back.
        # Place body origin at the pivot, then geom offset accordingly.
        # Simpler: keep body at upright base position, tilt via quat.  When
        # the quat tilts the body, the bottom face lifts off the ground on
        # one side, but with the small angle gravity will tip it forward.
        return (
            f'    <body name="d{i}" pos="{x:.4f} 0 {HZ:.4f}" '
            f'quat="{qw:.5f} 0 {qy:.5f} 0">\n'
            f'      <joint type="free"/>\n'
            f'      <geom type="box" size="{HX} {HY} {HZ}" mass="0.025" '
            f'material="{mat}"/>\n'
            f'    </body>'
        )
    return (
        f'    <body name="d{i}" pos="{x:.4f} 0 {HZ:.4f}">\n'
        f'      <joint type="free"/>\n'
        f'      <geom type="box" size="{HX} {HY} {HZ}" mass="0.025" '
        f'material="{mat}"/>\n'
        f'    </body>'
    )


bodies = "\n".join(domino_body(i) for i in range(N))
chain_end_x = START_X + (N - 1) * SPACING

xml = f"""<mujoco model="dominoes">
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="3" cone="elliptic"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="36"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="6" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="dom_cream" rgba="0.96 0.92 0.85 1" specular="0.15" shininess="0.2"/>
    <material name="dom_peach" rgba="0.95 0.78 0.62 1" specular="0.15" shininess="0.2"/>
    <material name="dom_blue"  rgba="0.36 0.58 0.82 1" specular="0.25" shininess="0.3"/>
    <material name="dom_dark"  rgba="0.32 0.30 0.32 1" specular="0.25" shininess="0.3"/>
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

{bodies}

    <!-- Camera: a low 3/4 view along the line of dominoes -->
    <camera name="cam" pos="-0.95 -0.85 0.30" fovy="42"
            xyaxes="0.65 -0.76 0   0.16 0.14 0.978"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "dominoes.xml")
with open(out_path, "w") as f:
    f.write(xml)
print(f"Wrote {out_path}  ({N} dominoes, chain {START_X:.2f}..{chain_end_x:.2f} m)")
