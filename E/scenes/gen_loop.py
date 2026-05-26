"""
Procedurally generate scenes/loop_the_loop.xml: a closed vertical circular
track ("loop").  A ball starts at the bottom with horizontal velocity, climbs
the inside of the loop, and orbits (energy conservation + centripetal force).

Why a closed loop and not the iconic ramp+loop+runway?  Making a smooth
ramp-to-loop tangent junction in MuJoCo segmented geometry is fragile (the
ball tends to slip through the seam).  A closed loop with a single
prescribed launch velocity is rock-solid and shows the same physics: at the
top of the loop the ball needs v^2 >= g R, energy conservation predicts
v_bottom^2 = v_top^2 + 4 g R.

Segments are placed at radius R_loop + T/2 from the center so the segment
TOP FACE (where the ball contacts) sits on the ideal circle of radius R_loop.
This makes the inside-of-loop surface a perfect circle.
"""
import math
import os

# --- geometry ---------------------------------------------------------------
R_LOOP = 0.30
N_LOOP = 28                # number of segments around the loop
DELTA  = 2 * math.pi / N_LOOP
TRACK_W = 0.12             # full width in y
TRACK_T = 0.008            # full thickness (radial)
CHORD_OVERLAP = 1.08

BALL_R = 0.040
BALL_MASS = 0.040


def loop_segment(i):
    """Box segment at alpha = i * DELTA.  Body center is offset radially outward
    by T/2 so the top face (body +z, which is the inward normal) lies on the
    ideal loop circle of radius R_LOOP centered at (0, 0, R_LOOP)."""
    alpha = i * DELTA
    R_seg = R_LOOP + TRACK_T * 0.5
    x = R_seg * math.sin(alpha)
    z = R_LOOP - R_seg * math.cos(alpha)
    L = CHORD_OVERLAP * 2 * R_LOOP * math.sin(DELTA * 0.5)
    return (
        f'    <geom type="box" pos="{x:.4f} 0 {z:.4f}" '
        f'euler="0 {-alpha:.5f} 0" '
        f'size="{L * 0.5:.4f} {TRACK_W * 0.5} {TRACK_T * 0.5}" '
        f'material="track_warm"/>'
    )


segments_xml = "\n".join(loop_segment(i) for i in range(N_LOOP))

# Side glass walls in +-y so the ball cannot drift sideways out of the loop.
WALL_Y = TRACK_W * 0.5 + 0.004
WALL_HALF = R_LOOP + 0.05  # covers full loop extent
walls_xml = (
    f'    <geom type="box" pos="0 {-WALL_Y:.4f} {R_LOOP:.4f}" '
    f'size="{WALL_HALF} 0.003 {WALL_HALF}" material="wall_glass" contype="0" conaffinity="0"/>\n'
    f'    <geom type="box" pos="0 { WALL_Y:.4f} {R_LOOP:.4f}" '
    f'size="{WALL_HALF} 0.003 {WALL_HALF}" material="wall_glass" contype="0" conaffinity="0"/>'
)


xml = f"""<mujoco model="loop_the_loop">
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.0005" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="5" cone="elliptic"/>

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
    <material name="track_warm" rgba="0.93 0.82 0.58 1" specular="0.15" shininess="0.2"/>
    <material name="wall_glass" rgba="0.85 0.82 0.78 0.18" specular="0.4" shininess="0.5"/>
    <material name="ball_blue"  rgba="0.30 0.50 0.78 1" specular="0.55" shininess="0.65"/>
  </asset>

  <default>
    <!-- Very low friction so the ball can keep orbiting; ball-on-track is
         primarily a normal-force interaction here, not a frictional one. -->
    <geom friction="0.06 0.003 0.0001" solref="0.002 1" solimp="0.97 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <!-- Loop: {N_LOOP} segments, closed.  Bottom of inside-surface at z=0. -->
{segments_xml}

{walls_xml}

    <!-- Ball: starts on the loop bottom, gets a horizontal launch via CLI
         init-qvel.  Center z = BALL_R so it sits just inside the loop. -->
    <body name="ball" pos="0 0 {BALL_R + 0.001:.4f}">
      <joint name="ball_free" type="free"/>
      <geom name="ball_geom" type="sphere" size="{BALL_R}" mass="{BALL_MASS}"
            material="ball_blue"/>
    </body>

    <!-- Camera: nearly pure side view (-y), slight tilt so the loop reads as
         a true circle. -->
    <camera name="cam" pos="0.40 -2.50 0.35" fovy="36"
            xyaxes="0.987 0.158 0   -0.003 0.019 1.000"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "loop_the_loop.xml")
with open(out_path, "w") as f:
    f.write(xml)
print(f"Wrote {out_path}  (closed loop, R={R_LOOP} m, {N_LOOP} segments)")
