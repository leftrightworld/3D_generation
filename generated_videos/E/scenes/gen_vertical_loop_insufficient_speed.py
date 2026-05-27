"""
Generate scenes/vertical_loop_insufficient_speed.xml — vertical loop in the x-z plane.

Concave inner-wall box rail (gen_loop geometry): inner face at R = 0.25 m blocks
outward motion; ball centre path r = 0.222 m stays inside the rail.

    v_required_bottom = sqrt(5 * g * R) ≈ 3.50 m/s
    v0 = 3.00 m/s  (below completion speed; strong inward detach)

2.65 m/s detaches gently; 3.00 m/s carries further through the loop centre
(r_min ≈ 0.04 m) for a clearer loss-of-contact feel.

Render:
    python3 render.py --scene scenes/vertical_loop_insufficient_speed.xml \\
        --out out/new_scenes/vertical_loop_insufficient_speed.mp4 --duration 1.5 \\
        --init-qvel "3.0,0,0,0,0,0"
"""
import math
import os

R_RAIL = 0.25
CENTER_Z = 0.35
N_LOOP = 96
DELTA = 2 * math.pi / N_LOOP
TRACK_W = 0.014
TRACK_T = 0.006
CHORD_OVERLAP = 1.05

BALL_R = 0.025
BALL_M = 0.05
BALL_MARGIN = 0.003
R_BALL_PATH = R_RAIL - BALL_R - BALL_MARGIN
BALL_Z = CENTER_Z - R_BALL_PATH

RAIL_Y = 0.035
V0 = 3.0
G = 9.81
V_BOTTOM_REQ = math.sqrt(5 * G * R_RAIL)


def loop_segment(i):
    """Box segment; inner face on circle R_RAIL (concave inner guide)."""
    alpha = i * DELTA
    r_seg = R_RAIL + TRACK_T * 0.5
    x = r_seg * math.sin(alpha)
    z = CENTER_Z - r_seg * math.cos(alpha)
    chord = CHORD_OVERLAP * 2 * R_RAIL * math.sin(DELTA * 0.5)
    return (
        f'    <geom name="rail_{i:03d}" type="box" '
        f'pos="{x:.5f} 0 {z:.5f}" euler="0 {-alpha:.5f} 0" '
        f'size="{chord * 0.5:.5f} {TRACK_W * 0.5:.5f} {TRACK_T * 0.5:.5f}" '
        f'material="track_blue" friction="0.008 0.0008 0.0001"/>'
    )


def side_guide(i, y_side):
    """Visual y-guides only; do not affect x-z motion."""
    am = (i + 0.5) * DELTA
    r = R_BALL_PATH
    x = r * math.sin(am)
    z = CENTER_Z - r * math.cos(am)
    half_len = r * DELTA * CHORD_OVERLAP * 0.5
    tag = "p" if y_side > 0 else "m"
    return (
        f'    <geom name="guide_{i:03d}_{tag}" type="box" '
        f'pos="{x:.5f} {y_side:.5f} {z:.5f}" euler="0 {-am:.5f} 0" '
        f'size="{half_len:.5f} 0.0020 {TRACK_T:.4f}" '
        f'material="rail_glass" contype="0" conaffinity="0"/>'
    )


rail_xml = "\n".join(loop_segment(i) for i in range(N_LOOP))
guide_xml = "\n".join(side_guide(i, y) for i in range(N_LOOP) for y in (-RAIL_Y, RAIL_Y))

xml = f"""<mujoco model="vertical_loop_insufficient_speed">
  <!-- Ball path r={R_BALL_PATH:.3f} m inside rail R={R_RAIL} m.
       v_required ≈ {V_BOTTOM_REQ:.2f} m/s;  v0 = {V0} m/s. -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"
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
    <material name="track_blue" rgba="0.34 0.52 0.80 1" specular="0.20" shininess="0.25"/>
    <material name="rail_glass" rgba="0.85 0.82 0.78 0.28" specular="0.25" shininess="0.35"/>
    <material name="bob_red"  rgba="0.86 0.34 0.30 1" specular="0.40" shininess="0.40"/>
  </asset>

  <default>
    <geom solref="0.004 1" solimp="0.95 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <!-- {N_LOOP} inner-wall segments, R={R_RAIL} m, centre z={CENTER_Z} m -->
{rail_xml}

{guide_xml}

    <body name="ball" pos="0 0 {BALL_Z:.5f}">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="{BALL_R}" mass="{BALL_M}"
            material="bob_red" friction="0.008 0.0008 0.0001"/>
    </body>

    <camera name="cam" pos="0 -1.4 0.35" fovy="42"
            xyaxes="1 0 0  0 0 1"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "vertical_loop_insufficient_speed.xml")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(xml)
print(f"Wrote {out_path}")
print(f"  r_ball={R_BALL_PATH:.3f}  ball_z={BALL_Z:.3f}  v0={V0}  v_req={V_BOTTOM_REQ:.2f}")
