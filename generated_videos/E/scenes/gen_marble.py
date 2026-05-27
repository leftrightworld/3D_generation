"""
Procedurally generate scenes/marble.xml: a curved quarter-pipe ramp
approximated by N short box segments, with a marble that rolls down it.

The ramp is the inside of a circular arc of radius R, going from horizontal
at the top (marble sits here) down to horizontal at the bottom.
"""
import math
import os

# ---- geometry parameters ---------------------------------------------------
R = 0.55              # radius of the curve
NSEG = 18             # number of box segments along the arc
ARC_START_DEG = 0     # start angle (top of ramp, surface horizontal)
ARC_END_DEG = 90      # end angle (bottom of ramp, surface horizontal)
RAMP_WIDTH = 0.18     # width of the channel (y extent)
RAMP_THICKNESS = 0.015
WALL_HEIGHT = 0.04    # side walls so marble doesn't roll off sideways

# Where the *top* edge of the ramp sits in world coords.
# Center of curvature is directly above the bottom of the ramp.
CENTER_X = 0.0
CENTER_Z = R          # so the bottom of the ramp is at z=0

# ---- marble ---------------------------------------------------------------
MARBLE_R = 0.035
# Start the marble at the top, just inside the upper lip
START_ANGLE_DEG = ARC_START_DEG - 2  # tiny push past horizontal
sa = math.radians(START_ANGLE_DEG)
MARBLE_X = R * math.sin(sa) + R * math.sin(math.radians(ARC_START_DEG))  # just past the lip
MARBLE_X = 0.40
MARBLE_Z = R + MARBLE_R + 0.005   # rest on top platform

# ---- top platform (where marble starts) ----------------------------------
PLATFORM_X = 0.45
PLATFORM_Z = R           # same height as the top of the ramp
PLATFORM_HALFX = 0.07
PLATFORM_HALFY = 0.10
PLATFORM_HALFZ = 0.01

# ---- build XML strings ----------------------------------------------------

def seg_xml(i):
    """One box segment of the curved ramp at angle index i (0..NSEG-1)."""
    # We discretize the arc from ARC_START_DEG to ARC_END_DEG.
    # angle increases as you go DOWN the ramp.
    a0_deg = ARC_START_DEG + i / NSEG * (ARC_END_DEG - ARC_START_DEG)
    a1_deg = ARC_START_DEG + (i + 1) / NSEG * (ARC_END_DEG - ARC_START_DEG)
    a_mid_deg = 0.5 * (a0_deg + a1_deg)
    a_mid = math.radians(a_mid_deg)

    # Position on the arc (center is on -X side... no wait).
    # We want the marble to roll on the INSIDE of the curve, with the
    # center of curvature to the +X side (above-right of the bottom).
    # Surface point at angle a: (CENTER_X + R*sin(a), 0, CENTER_Z - R*cos(a))
    # At a=0: (CENTER_X, 0, CENTER_Z - R) = (0, 0, 0). That's the BOTTOM.
    # At a=90°: (CENTER_X + R, 0, CENTER_Z) = (R, 0, R). That's the TOP-RIGHT.
    # So increasing a goes from bottom to top.
    # Marble rolls from large a (top) toward small a (bottom). Good.
    x = CENTER_X + R * math.sin(a_mid)
    z = CENTER_Z - R * math.cos(a_mid)

    # Each segment is a thin box whose +X axis is tangent to the arc
    # (pointing in the direction of increasing a), and whose +Z axis
    # points outward (away from center of curvature).
    # Tangent at angle a: (cos(a), 0, sin(a))
    # Outward radial at angle a: (sin(a), 0, -cos(a))
    # Default box axes: X=(1,0,0), Y=(0,1,0), Z=(0,0,1).
    # We need rotation R such that:
    #   R*(1,0,0) = (cos(a), 0, sin(a))    [tangent → ramp length]
    #   R*(0,0,1) = (sin(a), 0, -cos(a))   [outward radial → ramp thickness]
    # Wait: marble is on the INSIDE of the curve, so the ramp surface
    # FACING the marble is the surface toward the center of curvature,
    # which is the -outward, i.e. inward radial = (-sin(a), 0, cos(a)).
    # So we want the box's "+Z face" to face inward (toward center).
    #   R*(0,0,1) = (-sin(a), 0, cos(a))
    #
    # This is a rotation about Y by angle -a (right-hand rule, thumb +Y):
    #   R_y(theta): X→cos(theta)X + sin(theta)Z,  Z→-sin(theta)X + cos(theta)Z
    # Check with theta = -a:
    #   R*(1,0,0) = (cos(-a), 0, sin(-a)) = (cos(a), 0, -sin(a))  ✗
    # Try theta = +a:
    #   R*(1,0,0) = (cos(a), 0, sin(a))  ✓
    #   R*(0,0,1) = (-sin(a), 0, cos(a))  ✓
    # So euler-Y rotation angle = +a.
    euler_y_rad = a_mid

    # Segment dimensions:
    # length along arc ≈ R * dθ (chord), make it slightly longer to overlap
    dtheta = math.radians(a1_deg - a0_deg)
    L = R * dtheta * 1.10  # 10% overlap
    half_len = L * 0.5

    # Material alternates so we can tell segments apart
    mat = "ramp_wood" if i % 2 == 0 else "ramp_wood_dark"

    return f'''    <geom type="box" pos="{x:.4f} 0 {z:.4f}" euler="0 {euler_y_rad:.4f} 0"
          size="{half_len:.4f} {RAMP_WIDTH*0.5:.4f} {RAMP_THICKNESS*0.5:.4f}"
          material="{mat}"/>'''

def side_wall_xml(i, side_y):
    """Side wall on one edge of the ramp at angle index i."""
    a0_deg = ARC_START_DEG + i / NSEG * (ARC_END_DEG - ARC_START_DEG)
    a1_deg = ARC_START_DEG + (i + 1) / NSEG * (ARC_END_DEG - ARC_START_DEG)
    a_mid = math.radians(0.5 * (a0_deg + a1_deg))
    x = CENTER_X + R * math.sin(a_mid)
    z = CENTER_Z - R * math.cos(a_mid) + WALL_HEIGHT * 0.5  # wall sits on top of ramp surface
    dtheta = math.radians(a1_deg - a0_deg)
    L = R * dtheta * 1.10
    half_len = L * 0.5
    return f'''    <geom type="box" pos="{x:.4f} {side_y:.4f} {z:.4f}" euler="0 {a_mid:.4f} 0"
          size="{half_len:.4f} 0.008 {WALL_HEIGHT*0.5:.4f}"
          material="ramp_wood"/>'''

# Assemble XML
segments_xml = "\n".join(seg_xml(i) for i in range(NSEG))
left_walls = "\n".join(side_wall_xml(i, -RAMP_WIDTH*0.5 - 0.008) for i in range(NSEG))
right_walls = "\n".join(side_wall_xml(i,  RAMP_WIDTH*0.5 + 0.008) for i in range(NSEG))

xml = f"""<mujoco model="marble_ramp">
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="3" cone="elliptic"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="35"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="6" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="ramp_wood" rgba="0.93 0.78 0.50 1" specular="0.15" shininess="0.15"/>
    <material name="ramp_wood_dark" rgba="0.86 0.71 0.42 1" specular="0.15" shininess="0.15"/>
    <material name="platform_wood" rgba="0.88 0.84 0.86 1" specular="0.1" shininess="0.1"/>
    <material name="marble_blue" rgba="0.36 0.62 0.85 1" specular="0.5" shininess="0.6"/>
  </asset>

  <default>
    <geom friction="0.4 0.02 0.0005" solref="0.002 1" solimp="0.95 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <!-- Top platform (white-ish block) where the marble starts -->
    <geom type="box" pos="{PLATFORM_X:.3f} 0 {PLATFORM_Z+PLATFORM_HALFZ:.3f}"
          size="{PLATFORM_HALFX:.3f} {PLATFORM_HALFY:.3f} {PLATFORM_HALFZ:.3f}"
          material="platform_wood"/>
    <!-- A small "wall" so marble doesn't roll backward off the platform -->
    <geom type="box" pos="{PLATFORM_X+PLATFORM_HALFX-0.005:.3f} 0 {PLATFORM_Z+PLATFORM_HALFZ*2+0.025:.3f}"
          size="0.005 {PLATFORM_HALFY:.3f} 0.025" material="platform_wood"/>

    <!-- Curved ramp (made of {NSEG} short segments) -->
{segments_xml}

    <!-- Side walls so marble stays in the channel -->
{left_walls}
{right_walls}

    <!-- Marble: blue sphere, sits on the platform, rolls down when released -->
    <body name="marble" pos="{MARBLE_X:.3f} 0 {MARBLE_Z:.3f}">
      <joint type="free"/>
      <geom type="sphere" size="{MARBLE_R}" mass="0.05" material="marble_blue"/>
    </body>

    <!-- Camera: front-left 3/4 view, framing the whole ramp -->
    <camera name="cam" pos="-1.7 -1.4 0.85" fovy="36"
            xyaxes="0.63 -0.77 0   0.18 0.15 0.97"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "marble.xml")
with open(out_path, "w") as f:
    f.write(xml)
print(f"Wrote {out_path}  ({NSEG} ramp segments)")
