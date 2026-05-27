"""
Procedurally generate scenes/brachistochrone.xml: two tracks side by side,
same start point and same end point, with two balls racing down.
   - Track A (red ball): a straight inclined ramp
   - Track B (blue ball): a cycloid (the brachistochrone curve)
Counter-intuitively the cycloid ball arrives FIRST even though its path is
longer.

Cycloid equations (parameter theta from 0 to pi):
    x(theta) = r * (theta - sin theta)
    z(theta) = -r * (1 - cos theta)
For end at (L, -H): r = L / pi, H = 2r = 2L / pi.

Times (analytical, frictionless, rolling neglected for the linear case):
    t_cycloid = pi * sqrt(r / g)
    t_straight = sqrt(2 * sqrt(L^2 + H^2) / (g * sin(angle)))

For L=1.0 m: r = 0.3183, H = 0.6366
    t_cycloid  = 0.566 s
    t_straight = 0.671 s
Cycloid beats straight by ~16%.

NOTE: the cycloid has a CUSP at theta=0 (vertical tangent).  We skip the
first tiny segment (theta in [0, epsilon]) and place the ball at theta=eps;
otherwise the simulation has trouble settling the ball on a vertical
surface at the very start.
"""
import math
import os

# ---- parameters ------------------------------------------------------------
L          = 1.0       # horizontal span (start to end x)
g          = 9.81

R_CYCLOID  = L / math.pi               # cycloid radius
H          = 2 * R_CYCLOID             # vertical drop
ANGLE      = math.atan(H / L)          # straight ramp angle

N_CYCLOID  = 40        # cycloid segments
EPS_START  = 0.06      # parameter epsilon: skip [0, EPS] to avoid the cusp
THETA_END  = math.pi   # end of cycloid

TRACK_W    = 0.12      # width in y (lane width)
TRACK_T    = 0.012     # thickness (radial)
CHORD_OVERLAP = 1.10

BALL_R     = 0.030
BALL_MASS  = 0.040

# Lane y positions (two parallel tracks, separated in y).
Y_STRAIGHT = -0.18
Y_CYCLOID  =  0.18

print(f"L={L:.3f}  H={H:.3f}  r_cyc={R_CYCLOID:.4f}  ramp_angle={math.degrees(ANGLE):.2f} deg")


# ---- cycloid segments ------------------------------------------------------
def cycloid_segment(i):
    """Box segment of the cycloid track at angle index i.
    Surface normal (body +z) points UPWARD-INWARD (the side the ball touches).
    """
    th0 = EPS_START + (THETA_END - EPS_START) * i / N_CYCLOID
    th1 = EPS_START + (THETA_END - EPS_START) * (i + 1) / N_CYCLOID
    thm = 0.5 * (th0 + th1)
    # Midpoint position
    xm = R_CYCLOID * (thm - math.sin(thm))
    zm = -R_CYCLOID * (1 - math.cos(thm))
    # Endpoints (for chord length)
    x0 = R_CYCLOID * (th0 - math.sin(th0))
    z0 = -R_CYCLOID * (1 - math.cos(th0))
    x1 = R_CYCLOID * (th1 - math.sin(th1))
    z1 = -R_CYCLOID * (1 - math.cos(th1))
    chord = math.hypot(x1 - x0, z1 - z0) * CHORD_OVERLAP
    # Tangent direction (toward increasing theta).
    tx = math.cos(thm) - 1  # = -(1 - cos thm) ... wait
    # dx/dtheta = r * (1 - cos theta);  dz/dtheta = -r * sin theta
    tx_raw = (1 - math.cos(thm))
    tz_raw = -math.sin(thm)
    tnorm = math.hypot(tx_raw, tz_raw)
    tx, tz = tx_raw / tnorm, tz_raw / tnorm
    # Inward (concave) normal: rotate tangent +90 deg.  Tangent points DOWN
    # along the slope, so rotating +90 CCW gives (tz, -tx) ... we want the
    # upward (toward the +z side of the curve) normal. The cycloid curves
    # upward to the +z side (the "cup" shape).  Try normal = (-tz, tx).
    nx, nz = -tz, tx
    # Box body +z direction should be normal (nx, 0, nz); body +x direction
    # is tangent (tx, 0, tz).  Need rotation about y-axis by angle alpha s.t.
    # body +x -> world (tx, 0, tz):
    #   R_y(alpha) * (1,0,0) = (cos alpha, 0, -sin alpha)
    #   => cos alpha = tx, -sin alpha = tz  =>  alpha = -atan2(tz, tx)
    alpha = -math.atan2(tz, tx)
    return (
        f'    <geom type="box" pos="{xm:.4f} {Y_CYCLOID} {zm:.4f}" '
        f'euler="0 {alpha:.5f} 0" '
        f'size="{chord * 0.5:.4f} {TRACK_W * 0.5} {TRACK_T * 0.5}" '
        f'material="track_cyc"/>'
    )


cycloid_xml = "\n".join(cycloid_segment(i) for i in range(N_CYCLOID))


# ---- straight ramp ---------------------------------------------------------
# Center of the straight ramp box: midpoint between start (0,Y_STRAIGHT,0) and
# end (L, Y_STRAIGHT, -H).
mid_x = L * 0.5
mid_z = -H * 0.5
ramp_length = math.hypot(L, H)
# Rotate the box about +y by ANGLE so its long axis aligns with the slope.
# Body +x in world should be (cos(-ANGLE), 0, sin(-ANGLE)) = (cos A, 0, -sin A).
# That requires R_y(ANGLE) which sends body +x to (cos A, 0, -sin A). ✓
straight_xml = (
    f'    <geom type="box" pos="{mid_x} {Y_STRAIGHT} {mid_z:.4f}" '
    f'euler="0 {ANGLE:.5f} 0" '
    f'size="{ramp_length * 0.5:.4f} {TRACK_W * 0.5} {TRACK_T * 0.5}" '
    f'material="track_str"/>'
)


# ---- starting positions for the balls --------------------------------------
# Place each ball on top of its track at the START point (the curve at
# x=0 + slight offset for the cycloid, and at x=0 for the straight ramp).
# Ball center = track surface + BALL_R along the surface normal.

# Cycloid start (at theta = EPS_START):
th_s = EPS_START
xs = R_CYCLOID * (th_s - math.sin(th_s))
zs = -R_CYCLOID * (1 - math.cos(th_s))
tx_raw = 1 - math.cos(th_s);  tz_raw = -math.sin(th_s)
tnorm = math.hypot(tx_raw, tz_raw)
tx, tz = tx_raw / tnorm, tz_raw / tnorm
nx, nz = -tz, tx
ball_cyc_x = xs + BALL_R * nx
ball_cyc_z = zs + BALL_R * nz

# Straight start at (0, Y_STRAIGHT, 0) on the ramp.  Surface normal is
# perpendicular to the slope (-sin A, 0, cos A) (in world): pointing up-left.
nx_s = -math.sin(ANGLE)
nz_s = math.cos(ANGLE)
ball_str_x = 0 + BALL_R * nx_s
ball_str_z = 0 + BALL_R * nz_s

print(f"Cycloid ball start: ({ball_cyc_x:.4f}, {Y_CYCLOID}, {ball_cyc_z:.4f})")
print(f"Straight ball start: ({ball_str_x:.4f}, {Y_STRAIGHT}, {ball_str_z:.4f})")


# ---- floor ground level ----------------------------------------------------
FLOOR_Z = -H - 0.08  # below the lowest point of either track


xml = f"""<mujoco model="brachistochrone">
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.0005" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="3" cone="elliptic"/>

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
    <material name="floor_mat"  rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="track_str"  rgba="0.93 0.82 0.58 1" specular="0.15" shininess="0.2"/>
    <material name="track_cyc"  rgba="0.78 0.65 0.40 1" specular="0.15" shininess="0.2"/>
    <material name="ball_red"   rgba="0.86 0.32 0.30 1" specular="0.55" shininess="0.7"/>
    <material name="ball_blue"  rgba="0.30 0.50 0.78 1" specular="0.55" shininess="0.7"/>
  </asset>

  <default>
    <!-- Low rolling friction so both balls approach the analytic
         (point-particle, frictionless) prediction. -->
    <geom friction="0.05 0.005 0.0001" solref="0.003 1" solimp="0.97 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" pos="0 0 {FLOOR_Z:.3f}" size="40 40 0.1"
          material="floor_mat"/>

    <!-- Straight ramp (lane y={Y_STRAIGHT}). -->
{straight_xml}

    <!-- Cycloid track (lane y={Y_CYCLOID}), {N_CYCLOID} segments. -->
{cycloid_xml}

    <!-- Red ball on the straight ramp. -->
    <body name="ball_straight" pos="{ball_str_x:.4f} {Y_STRAIGHT} {ball_str_z:.4f}">
      <freejoint/>
      <geom type="sphere" size="{BALL_R}" mass="{BALL_MASS}"
            material="ball_red"/>
    </body>

    <!-- Blue ball on the cycloid track. -->
    <body name="ball_cycloid" pos="{ball_cyc_x:.4f} {Y_CYCLOID} {ball_cyc_z:.4f}">
      <freejoint/>
      <geom type="sphere" size="{BALL_R}" mass="{BALL_MASS}"
            material="ball_blue"/>
    </body>

    <!-- Camera: 3/4 view from front-left so both lanes are visible distinctly. -->
    <camera name="cam" pos="-0.55 -1.25 0.10" fovy="40"
            xyaxes="0.917 -0.399 0   0.105 0.241 0.965"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "brachistochrone.xml")
with open(out_path, "w") as f:
    f.write(xml)
print(f"Wrote {out_path}")
