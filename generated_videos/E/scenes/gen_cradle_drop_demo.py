#!/usr/bin/env python3
"""Generate scenes/cradle_drop_demo.xml (pendulum hits block on low launch ramp).

Render (kinematic — analytic pendulum + ramp-tangent launch + projectile):
  python3 render.py --scene scenes/cradle_drop_demo.xml \\
      --out out/new_scenes/cradle_drop_demo.mp4 --duration 3 --kinematic \\
      --init-qpos "-0.785"
  python3 make_grid.py --scene scenes/cradle_drop_demo.xml \\
      --out out/cradle_drop_demo_grid.png --duration 3 --cols 4 --rows 2 --kinematic \\
      --init-qpos "-0.785"
"""
import math
import os

# --- physics constants (must match kinematic.py) ----------------------------
G = 9.81
HINGE = (0.0, -0.75, 1.165)
L = 1.0
BOB_R = 0.115
BLOCK_HALF = 0.025
BLOCK_HALF_W = 0.035
THETA0 = -0.785          # release from the left; bottom crossing moves +x
OMEGA = math.sqrt(G / L)

# Ramp ahead of block in +x (bob swings left→right through bottom and hits)
RAMP_X0 = -0.110
RAMP_X1 = 0.060
RAMP_H = 0.042
BLOCK_X = -0.028


def ramp_height(x):
    if x <= RAMP_X0:
        return 0.0
    if x >= RAMP_X1:
        return RAMP_H
    u = (x - RAMP_X0) / (RAMP_X1 - RAMP_X0)
    return RAMP_H * 0.5 * (1.0 - math.cos(math.pi * u))


def ramp_slope(x):
    if x <= RAMP_X0 or x >= RAMP_X1:
        return 0.0
    u = (x - RAMP_X0) / (RAMP_X1 - RAMP_X0)
    span = RAMP_X1 - RAMP_X0
    return RAMP_H * 0.5 * math.pi / span * math.sin(math.pi * u)


def block_rest_pos():
    z = ramp_height(BLOCK_X) + BLOCK_HALF
    return (BLOCK_X, -0.75, z)


def contact_theta():
    """Bob right edge meets block left edge while swinging in from the left."""
    s = (BLOCK_X - BLOCK_HALF_W - BOB_R) / L
    return math.asin(max(-1.0, min(1.0, s)))


def bob_vx(theta, theta_dot):
    """Horizontal speed of bob (d/dt of L sin theta)."""
    return theta_dot * L * math.cos(theta)


def hit_time(theta0=THETA0):
    th = contact_theta()
    return math.acos(th / theta0) / OMEGA


def launch_velocity(theta0=THETA0, transfer=1.75, vz_boost=2.05):
    th = contact_theta()
    td = -theta0 * OMEGA * math.sin(OMEGA * hit_time(theta0))
    v_bob_x = bob_vx(th, td)
    slope = ramp_slope(BLOCK_X)
    alpha = math.atan(slope)
    speed = transfer * abs(v_bob_x)
    # Camera 3/4 view maps world +x to screen-left; flip so block flies with the swing
    vx = -speed * math.cos(alpha) * (1.0 if v_bob_x >= 0 else -1.0)
    vz = speed * math.sin(alpha) * vz_boost
    return vx, vz


BLOCK_POS = block_rest_pos()
T_HIT = hit_time()
LAUNCH_VX, LAUNCH_VZ = launch_velocity()


def bob_world(theta):
    return (
        HINGE[0] + L * math.sin(theta),
        HINGE[1],
        HINGE[2] - L * math.cos(theta),
    )


# --- stand: post top meets arm bottom (like pendulum.xml, scaled to hinge) --
ARM_Z = HINGE[2]
ARM_HALF_Z = 0.045
POST_TOP_Z = ARM_Z - ARM_HALF_Z
POST_HALF_Z = POST_TOP_Z / 2.0
POST_CENTER_Z = POST_HALF_Z

# --- ramp geometry (visual only) --------------------------------------------
ramp_geoms = []
n_ramp = 9
for i in range(n_ramp):
    x = RAMP_X0 + i * (RAMP_X1 - RAMP_X0) / (n_ramp - 1)
    z = ramp_height(x)
    hz = max(0.003, z * 0.5 + 0.002)
    ramp_geoms.append(
        f'    <geom name="ramp_{i}" type="box" pos="{x:.4f} -0.75 {hz:.4f}" '
        f'size="0.011 0.030 {hz:.4f}" material="ramp_mat" contype="0" conaffinity="0"/>'
    )
ramp_xml = "\n".join(ramp_geoms)

arc_geoms = []
n_arc = 14
for i in range(n_arc + 1):
    th = THETA0 + (2 * abs(THETA0)) * i / n_arc
    x, y, z = bob_world(th)
    arc_geoms.append(
        f'    <geom name="arc_{i}" type="sphere" pos="{x:.4f} {y:.4f} {z:.4f}" '
        f'size="0.008" rgba="0.96 0.83 0.36 0.22" contype="0" conaffinity="0"/>'
    )

bx, by, bz = BLOCK_POS
parab_geoms = []
for i in range(1, 16):
    dt = 0.06 * i
    px = bx + LAUNCH_VX * dt
    pz = bz + LAUNCH_VZ * dt - 0.5 * G * dt * dt
    if pz < 0.005 or px > 4.5 or px < -4.5:
        break
    parab_geoms.append(
        f'    <geom name="parab_{i}" type="sphere" pos="{px:.4f} {by:.4f} {pz:.4f}" '
        f'size="0.007" rgba="0.34 0.52 0.80 0.28" contype="0" conaffinity="0"/>'
    )

impact_geoms = (
    f'    <geom name="impact_glow" type="sphere" pos="{bx:.4f} {by:.4f} {bz:.4f}" '
    f'size="0.045" rgba="0.98 0.90 0.55 0.14" contype="0" conaffinity="0"/>'
)

arc_xml = "\n".join(arc_geoms)
parab_xml = "\n".join(parab_geoms)

xml = f"""<mujoco model="cradle_drop_demo">
  <!-- Pendulum released from the left; block on a low ramp at the swing bottom.
       Bob strikes while moving +x; block leaves along ramp tangent (+vx, +vz).
       Render with --kinematic (see gen_cradle_drop_demo.py). -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="3" cone="elliptic"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-15" offwidth="1920" offheight="1080" fovy="40"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="5" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="wood" rgba="0.93 0.82 0.58 1" specular="0.1" shininess="0.1"/>
    <material name="ramp_mat" rgba="0.88 0.84 0.76 1" specular="0.05" shininess="0.05"/>
    <material name="bob_yellow" rgba="0.96 0.83 0.36 1" specular="0.35" shininess="0.4"/>
    <material name="block_blue" rgba="0.34 0.52 0.80 1" specular="0.35" shininess="0.4"/>
    <material name="string_mat" rgba="0.28 0.25 0.22 1" specular="0" shininess="0"/>
  </asset>

  <default>
    <geom friction="0.7 0.04 0.001" solref="0.002 1" solimp="0.97 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 10" dir="-0.35 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 6" dir="0.45 -0.3 -1" directional="true" castshadow="false"
           diffuse="0.30 0.30 0.36" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <!-- L-stand: vertical post meets horizontal arm (no gap) -->
    <geom type="box" size="0.045 0.045 {POST_HALF_Z:.4f}"
          pos="0 0.55 {POST_CENTER_Z:.4f}" material="wood"/>
    <geom type="box" size="0.045 0.65 0.045"
          pos="0 -0.10 {ARM_Z:.4f}" material="wood"/>
    <!-- corner block where post top meets arm -->
    <geom type="box" size="0.045 0.045 0.045"
          pos="0 0.55 {POST_TOP_Z - 0.045:.4f}" material="wood"/>

{ramp_xml}

{arc_xml}
{parab_xml}
{impact_geoms}

    <body name="pendulum" pos="{HINGE[0]} {HINGE[1]} {HINGE[2]}">
      <joint name="hinge" type="hinge" axis="0 1 0" damping="0.012"/>
      <geom name="string" type="capsule"
            fromto="0 0 0  0 0 -{L}" size="0.005"
            material="string_mat" contype="0" conaffinity="0"/>
      <geom name="bob" type="sphere" pos="0 0 -{L}" size="{BOB_R}"
            material="bob_yellow" mass="0.50"/>
    </body>

    <body name="top_block" pos="{BLOCK_POS[0]:.4f} {BLOCK_POS[1]:.4f} {BLOCK_POS[2]:.4f}">
      <freejoint name="block_free"/>
      <geom name="block" type="box" size="0.035 0.035 {BLOCK_HALF}"
            material="block_blue" mass="0.05"/>
    </body>

    <camera name="cam" pos="2.6 -2.9 1.05"
            xyaxes="0.74 0.67 0   -0.12 0.13 0.98"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "cradle_drop_demo.xml")
with open(out_path, "w") as f:
    f.write(xml)

alpha_deg = math.degrees(math.atan(ramp_slope(BLOCK_X)))
print(f"Wrote {out_path}")
print(f"  post top / arm bottom = {POST_TOP_Z:.3f} / {ARM_Z - ARM_HALF_Z:.3f}")
print(f"  block on ramp at ({BLOCK_POS[0]:.3f}, {BLOCK_POS[2]:.3f}), angle ~{alpha_deg:.1f}°")
print(f"  hit t~{T_HIT:.2f}s  launch vx={LAUNCH_VX:.2f} vz={LAUNCH_VZ:.2f} m/s")
print(f'Suggested render: --kinematic --init-qpos "{THETA0}" --duration 3')
