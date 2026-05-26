"""
Procedurally generate scenes/rotating_fluid.xml: a cylindrical bucket spinning
about its vertical axis, filled with ~150 small balls acting as "fluid
particles".  Centrifugal effect pushes the balls outward; the free surface
should form a paraboloid:
        z(r) = z_0 + Ω² r² / (2g)
with depression depth  Δh = Ω² R² / (2g).

Why "balls as fluid": MuJoCo has no native fluid/MPM/SPH.  Granular packing of
many rigid spheres is the closest cheap approximation — surface shape is
qualitatively correct, individual particles are visible (which makes the demo
read better than a continuous surface anyway).

Design parameters
-----------------
   R_bucket   = 0.10  bucket inner radius
   H_bucket   = 0.12  bucket height
   R_ball     = 0.010
   N_balls    ≈ 150   (5 rings × 6 angles × 5 layers, hand-placed grid)
   Ω          = 5.0 rad/s
   → Δh       = Ω²·R²/(2g) = 25·0.01/19.62 ≈ 0.0127 m  visible parabola depth
   → h_avg from 150 balls in a R=0.10 bucket ≈ 0.020 m
   → depth/avg ≈ 0.64 — parabola is visible without the center dipping below
     the floor (no dry annulus).

The bucket spins freely about z (no actuator).  To keep Ω roughly constant
over the clip despite ball friction, the bucket bottom has a high mass
(~12 kg) so its moment of inertia dominates: any back-torque from the balls
barely slows it.
"""
import math
import os

# ---- bucket -----------------------------------------------------------------
R_BUCKET   = 0.10
H_BUCKET   = 0.12
WALL_T     = 0.004
N_WALLS    = 32        # wall segments around the ring
BOTTOM_T   = 0.012     # thickness of bucket bottom disc

# ---- balls ------------------------------------------------------------------
R_BALL     = 0.013
M_BALL     = 0.010     # kg (a bit heavier than water for numerical stability)

# Hand-placed grid: rings × angles × layers — 160 balls explodes contact count
# and renders ~10 minutes; 72 is the sweet spot (visible parabola, ~30 s render)
RING_RADII = [0.020, 0.050, 0.078]            # 3 rings, gap 0.028 > ball d=0.026
N_THETA    = 8                                # 8 balls per ring per layer
Z_LAYERS   = [0.080, 0.108, 0.136]            # 3 vertical layers (world frame)
# Total: 3 * 8 * 3 = 72 balls

# ---- dynamics ---------------------------------------------------------------
OMEGA      = 7.0                              # bucket angular velocity (rad/s)
                                              # Ω=5 gave Δh≈13mm ≈ 1 ball
                                              # diameter — too subtle.  Ω=7
                                              # gives ~25mm ≈ 2 diameters,
                                              # which reads as a real bowl
                                              # rather than just packing noise.
BUCKET_MASS = 12.0                            # heavy bottom keeps Ω stable

# Derived
g          = 9.81
DELTA_H    = OMEGA**2 * R_BUCKET**2 / (2 * g)
print(f"Δh (predicted parabola depression) = {DELTA_H*1000:.1f} mm")
print(f"#balls = {len(RING_RADII) * N_THETA * len(Z_LAYERS)}")


# ---- bucket wall segments ---------------------------------------------------
def wall_segment(i):
    th = 2 * math.pi * i / N_WALLS
    cx = R_BUCKET * math.cos(th)
    cy = R_BUCKET * math.sin(th)
    # box's local +x = tangent (perpendicular to radial); orient by rotating
    # about z by (th + π/2)
    yaw = th + math.pi / 2
    # half-chord along tangent (slight overlap to avoid gaps)
    half_chord = R_BUCKET * math.sin(math.pi / N_WALLS) * 1.05
    sx = half_chord
    sy = WALL_T / 2
    sz = H_BUCKET / 2
    return (f'      <geom name="wall{i}" type="box" '
            f'pos="{cx:.4f} {cy:.4f} {H_BUCKET/2:.4f}" '
            f'euler="0 0 {yaw:.5f}" '
            f'size="{sx:.4f} {sy:.4f} {sz:.4f}" '
            f'material="bucket"/>')


walls_xml = "\n".join(wall_segment(i) for i in range(N_WALLS))


# ---- balls and their initial linear velocities ------------------------------
ball_bodies = []
init_qpos_parts = []   # for placeholder, balls use free joints w/ default qpos
init_qvel_parts = []   # bucket first (single hinge), then 6 dofs per ball

# Bucket's hinge has 1 DOF; we'll provide its qvel at the very start.
init_qvel_parts.append(f"{OMEGA}")

for iz, z in enumerate(Z_LAYERS):
    for ir, r in enumerate(RING_RADII):
        # Stagger angles between layers so balls don't stack in vertical columns
        phase = (math.pi / N_THETA) * (iz * 0.4 + ir * 0.7)
        for it in range(N_THETA):
            theta = 2 * math.pi * it / N_THETA + phase
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            name = f"b_{iz}_{ir}_{it}"
            ball_bodies.append(
                f'    <body name="{name}" pos="{x:.4f} {y:.4f} {z:.4f}">\n'
                f'      <freejoint/>\n'
                f'      <geom type="sphere" size="{R_BALL}" mass="{M_BALL}" '
                f'material="water" friction="0.10 0.005 0.0001"/>\n'
                f'    </body>'
            )
            # Initial velocity in sync with bucket rotation:
            # linear v = Ω × r = (-Ω y, Ω x, 0)
            vx = -OMEGA * y
            vy = OMEGA * x
            init_qvel_parts.append(f"{vx:.4f},{vy:.4f},0,0,0,{OMEGA}")

balls_xml = "\n".join(ball_bodies)
init_qvel_str = ",".join(init_qvel_parts)


xml = f"""<mujoco model="rotating_fluid">
  <!-- Granular approximation to a rotating fluid: 160 balls inside a heavy
       spinning bucket.  Centrifugal effect should pile balls outward and
       form a parabolic free surface, depth Δh = Ω²R²/(2g) ≈ {DELTA_H*1000:.1f} mm. -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.0008" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="3" cone="elliptic"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="42"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="6" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="wood_dark" rgba="0.78 0.65 0.40 1" specular="0.1" shininess="0.1"/>
    <material name="bucket"    rgba="0.93 0.82 0.58 1" specular="0.2" shininess="0.3"/>
    <material name="water"     rgba="0.34 0.56 0.86 1" specular="0.6" shininess="0.7"/>
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

    <!-- A short pedestal so the bucket sits at a viewable height. -->
    <geom type="cylinder" pos="0 0 0.025" size="0.13 0.025" material="wood_dark"/>

    <!-- Bucket: parent body with one hinge joint about z, ring of walls + a
         heavy bottom disc.  All bucket parts rotate together about z.
         The bottom is heavy ({BUCKET_MASS} kg) so the bucket's moment of inertia
         dominates over ball-friction back-torque → spin stays ~constant. -->
    <body name="bucket" pos="0 0 0.05">
      <joint name="bucket_spin" type="hinge" axis="0 0 1"/>
      <!-- Heavy bottom disc -->
      <geom name="bottom" type="cylinder"
            pos="0 0 {BOTTOM_T/2:.4f}" size="{R_BUCKET} {BOTTOM_T/2:.4f}"
            material="bucket" mass="{BUCKET_MASS}"/>
      <!-- Ring of {N_WALLS} wall segments -->
{walls_xml}
    </body>

    <!-- {len(ball_bodies)} "fluid" balls (granular) -->
{balls_xml}

    <!-- Pure top-down (looking straight down -z) so the ring-of-balls
         distribution reads cleanly as an annulus around the central
         depression.  Granular balls won't form a smooth parabolic surface
         from a side view; the 2D centrifugal pile-up is the clearest
         visualization of the effect. -->
    <camera name="cam" pos="0 0 0.50" fovy="32"
            xyaxes="1 0 0   0 1 0"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "rotating_fluid.xml")
with open(out_path, "w") as f:
    f.write(xml)
print(f"Wrote {out_path}")
print(f"init-qvel length: {len(init_qvel_parts)} terms "
      f"(1 bucket hinge + 6×{len(ball_bodies)} ball freejoints)")
print()
print("Run with:")
print(f'  python3 render.py --scene scenes/rotating_fluid.xml '
      f'--out out/new_scenes/rotating_fluid.mp4 --duration 4.0 \\')
print(f'    --init-qvel "{init_qvel_str}"')

# Also save the init-qvel string to a file so the render command is reusable
qvel_path = os.path.join(os.path.dirname(__file__), "rotating_fluid_qvel.txt")
with open(qvel_path, "w") as f:
    f.write(init_qvel_str)
print(f"\nQvel string saved to {qvel_path} for shell convenience.")
