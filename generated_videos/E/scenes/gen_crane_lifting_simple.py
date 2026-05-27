#!/usr/bin/env python3
"""Generate scenes/crane_lifting_simple.xml — single rigid crane tipping forward.

One body (base + pole + arm + cable + load) hinged at the front-bottom edge.
Physics-driven smooth tip when load_torque > stability_torque.

Render (simulation — no --kinematic):
  python3 render.py --scene scenes/crane_lifting_simple.xml \\
      --out out/new_scenes/crane_lifting_simple.mp4 --duration 3
  python3 make_grid.py --scene scenes/crane_lifting_simple.xml \\
      --out out/crane_lifting_simple_grid.png --duration 3 --cols 4 --rows 2
"""
import math
import os

G = 9.81

# Geometry (metres) — arm extends +x, pivot at front edge x=0, z=0
BASE_HALF_X = 0.26          # base extends backward to x = -BASE_HALF_X
BASE_HALF_Y = 0.14
BASE_HALF_Z = 0.055
BASE_M = 0.13

POLE_X = -0.20
POLE_HALF_Z = 0.52
POLE_THICK = 0.045

ARM_X0 = POLE_X
ARM_X1 = 0.92                 # arm tip x
ARM_Z = BASE_HALF_Z * 2 + POLE_HALF_Z * 2
ARM_THICK = 0.038

CABLE_TOP = (ARM_X1, 0.0, ARM_Z)
LOAD_HALF = 0.11
CABLE_LEN = 0.42
LOAD_Z = ARM_Z - CABLE_LEN - LOAD_HALF
LOAD_X = ARM_X1
LOAD_M = 1.00

ARM_EXT = LOAD_X - 0.0          # horizontal distance pivot → load
LOAD_TORQUE = LOAD_M * G * ARM_EXT
STAB_TORQUE = BASE_M * G * BASE_HALF_X

# Side camera on -Y looking +Y (x horizontal, z vertical on screen)
CAM_POS = (0.45, -4.0, 0.88)
CAM_XYAXES = "1 0 0   0 0 1"
CAM_FOVY = 32

# Hinge: rotation about +Y tips load side (+x) downward
HINGE_DAMPING = 22.0
HINGE_ARMATURE = 12.0
# Stop when load bottom corner (+x face) touches z=0
LOAD_BOTTOM_Z = LOAD_Z - LOAD_HALF
CONTACT_X = LOAD_X + LOAD_HALF
TIP_LIMIT = math.atan(LOAD_BOTTOM_Z / CONTACT_X) * 0.998


def torque_arc_geoms(radius, z0, n=9):
  parts = []
  for i in range(n):
    a0 = i * math.radians(6.5)
    a1 = (i + 1) * math.radians(6.5)
    x0 = radius * math.sin(a0)
    z0p = z0 + radius * (1.0 - math.cos(a0))
    x1 = radius * math.sin(a1)
    z1p = z0 + radius * (1.0 - math.cos(a1))
    parts.append(
      f'      <geom name="tq_{i}" type="capsule" '
      f'fromto="{x0:.4f} 0.0000 {z0p:.4f} {x1:.4f} 0.0000 {z1p:.4f}" '
      f'size="0.009" rgba="0.88 0.28 0.24 0.88" contype="0" conaffinity="0"/>'
    )
  a_tip = n * math.radians(6.5)
  parts.append(
    f'      <geom name="tq_head" type="sphere" '
    f'pos="{radius * math.sin(a_tip):.4f} 0.0000 {z0 + radius * (1 - math.cos(a_tip)):.4f}" '
    f'size="0.018" rgba="0.88 0.28 0.24 0.88" contype="0" conaffinity="0"/>'
  )
  return "\n".join(parts)


arm_cx = (ARM_X0 + ARM_X1) / 2.0
arm_hx = (ARM_X1 - ARM_X0) / 2.0
pole_cz = BASE_HALF_Z * 2 + POLE_HALF_Z

torque_xml = torque_arc_geoms(0.18, BASE_HALF_Z * 2 + 0.02)

xml = f"""<mujoco model="crane_lifting_simple">
  <!-- Single rigid crane: base+pole+arm+cable+load on one body, hinged at
       front-bottom edge (x=0,z=0). Tips forward (+x load side) when
       loadWeight*armExtension > baseWeight*baseHalfWidth.
       Render WITHOUT --kinematic (see gen_crane_lifting_simple.py). -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"
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
    <material name="wood" rgba="0.93 0.72 0.48 1" specular="0.12" shininess="0.12"/>
    <material name="wood_dark" rgba="0.82 0.55 0.32 1" specular="0.12" shininess="0.12"/>
    <material name="cable_mat" rgba="0.28 0.25 0.22 1" specular="0" shininess="0"/>
    <material name="load_mat" rgba="0.78 0.22 0.20 1" specular="0.35" shininess="0.4"/>
  </asset>

  <default>
    <geom friction="0.6 0.04 0.005" solref="0.003 1" solimp="0.97 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 10" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 6" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <!-- Fixed support-region marker (base half-width behind pivot) -->
    <geom name="support_marker" type="box" pos="{-BASE_HALF_X / 2:.4f} 0 0.003"
          size="{BASE_HALF_X / 2:.4f} 0.16 0.003"
          rgba="0.35 0.68 0.78 0.55" contype="0" conaffinity="0"/>
    <geom name="support_tick" type="box" pos="{-BASE_HALF_X:.4f} 0 0.006"
          size="0.012 0.12 0.006" rgba="0.30 0.62 0.72 0.85"
          contype="0" conaffinity="0"/>

    <!-- Pivot at front-bottom edge: x=0, z=0 -->
    <body name="crane" pos="0 0 0">
      <joint name="tip" type="hinge" axis="0 1 0"
             damping="{HINGE_DAMPING}" armature="{HINGE_ARMATURE}"
             limited="true" range="0 {TIP_LIMIT:.6f}"/>

      <geom name="base" type="box"
            size="{BASE_HALF_X:.4f} {BASE_HALF_Y:.4f} {BASE_HALF_Z:.4f}"
            pos="{-BASE_HALF_X:.4f} 0 {BASE_HALF_Z:.4f}"
            material="wood_dark" mass="{BASE_M:.4f}"
            contype="0" conaffinity="0"/>

      <geom name="pole" type="box"
            size="{POLE_THICK:.4f} {POLE_THICK:.4f} {POLE_HALF_Z:.4f}"
            pos="{POLE_X:.4f} 0 {pole_cz:.4f}"
            material="wood" mass="0.10"
            contype="0" conaffinity="0"/>

      <geom name="arm" type="box"
            size="{arm_hx:.4f} {ARM_THICK:.4f} {ARM_THICK:.4f}"
            pos="{arm_cx:.4f} 0 {ARM_Z:.4f}"
            material="wood" mass="0.08"
            contype="0" conaffinity="0"/>

      <geom name="cable" type="capsule"
            fromto="{CABLE_TOP[0]:.4f} 0 {CABLE_TOP[2]:.4f} {LOAD_X:.4f} 0 {LOAD_Z + LOAD_HALF:.4f}"
            size="0.006" material="cable_mat"
            contype="0" conaffinity="0"/>

      <geom name="load" type="box"
            size="{LOAD_HALF:.4f} {LOAD_HALF:.4f} {LOAD_HALF:.4f}"
            pos="{LOAD_X:.4f} 0 {LOAD_Z:.4f}"
            material="load_mat" mass="{LOAD_M:.4f}"
            friction="0.9 0.05 0.005" solref="0.003 1" solimp="0.97 0.99 0.001"/>

{torque_xml}

    </body>

    <camera name="cam" pos="{CAM_POS[0]:.2f} {CAM_POS[1]:.1f} {CAM_POS[2]:.2f}"
            fovy="{CAM_FOVY}" xyaxes="{CAM_XYAXES}"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "crane_lifting_simple.xml")
with open(out_path, "w", encoding="utf-8") as f:
  f.write(xml)

print(f"Wrote {out_path}")
print(f"  loadTorque     = {LOAD_TORQUE:.2f} N·m")
print(f"  stabilityTorque = {STAB_TORQUE:.2f} N·m  (tips: {LOAD_TORQUE > STAB_TORQUE})")
print(f"  tip limit at load contact = {math.degrees(TIP_LIMIT):.1f} deg")
print("Suggested render: --duration 3  (simulation, no --kinematic)")
