"""
Generate scenes/truss_collapse.xml — planar 4-bar linkage with
a critical diagonal C-B that is removed at t ≈ 0.8 s during render (see
kinematic.TrussMemberRemoval).

Before removal the diagonal triangulates the frame and it carries the top load.
After removal the frame becomes a shear mechanism and collapses.
"""
import math
import os

# Node positions in the x-z plane (y = 0).
A = (-0.50, 0.05)
B = (0.50, 0.05)
C = (-0.35, 0.55)
D = (0.35, 0.55)

AC = (C[0] - A[0], C[1] - A[1])
CD = (D[0] - C[0], D[1] - C[1])
DB = (B[0] - D[0], B[1] - D[1])
CB = (B[0] - C[0], B[1] - C[1])
CB_LEN = math.hypot(*CB)

M_BAR = 0.06
M_LOAD = 1.05
R_BAR = 0.013
R_PIN = 0.016
D_HINGE = 0.35
PED_H = 0.04

# Slight load offset: stable with diagonal, drives shear after removal.
LOAD_OFFSET_X = 0.08

K_DIAG = 6500.0
D_DIAG = 2.5


def vec3(v):
    return f"{v[0]:.4f} 0 {v[1]:.4f}"


def fromto_vec(v):
    return f'fromto="0 0 0  {v[0]:.4f} 0 {v[1]:.4f}"'


linkage_xml = f"""    <!-- Open chain A-C-D-B with hinges at A, C, D -->
    <body name="leg_AC" pos="{vec3(A)}">
      <joint name="h_A" type="hinge" axis="0 1 0" damping="{D_HINGE}"/>
      <geom name="bar_AC" type="capsule" {fromto_vec(AC)} size="{R_BAR}"
            mass="{M_BAR}" material="bar_mat"/>
      <geom type="sphere" size="{R_PIN}" material="joint_pin" mass="0.008"
            contype="0" conaffinity="0"/>

      <body name="coupler" pos="{vec3(AC)}">
        <joint name="h_C" type="hinge" axis="0 1 0" damping="{D_HINGE}"/>
        <geom name="bar_CD" type="capsule" {fromto_vec(CD)} size="{R_BAR}"
              mass="{M_BAR * 0.7:.3f}" material="bar_mat"/>
        <geom type="sphere" size="{R_PIN}" material="joint_pin" mass="0.008"
              contype="0" conaffinity="0"/>
        <site name="s_C" pos="0 0 0" size="0.001"/>
        <geom name="bar_CB" type="capsule" {fromto_vec(CB)} size="{R_BAR}"
              mass="0.001" material="bar_mat" contype="0" conaffinity="0"/>
        <geom name="load" type="box"
              pos="{CD[0] * 0.5 + LOAD_OFFSET_X:.4f} 0 {CD[1] * 0.5 + 0.07:.4f}"
              size="0.065 0.035 0.065" mass="{M_LOAD}" material="payload"
              contype="1" conaffinity="1"
              solref="0.003 1" solimp="0.95 0.99 0.001"/>

        <body name="leg_DB" pos="{vec3(CD)}">
          <joint name="h_D" type="hinge" axis="0 1 0" damping="{D_HINGE}"/>
          <geom name="bar_BD" type="capsule" {fromto_vec(DB)} size="{R_BAR}"
                mass="{M_BAR}" material="bar_mat"/>
          <geom type="sphere" size="{R_PIN}" material="joint_pin" mass="0.008"
                contype="0" conaffinity="0"/>
          <geom type="sphere" pos="{vec3(DB)}" size="{R_PIN}" material="joint_pin"
                mass="0.008" contype="0" conaffinity="0"/>
        </body>
      </body>
    </body>

    <!-- Fixed pin at support B (closure point for the open chain) -->
    <body name="anchor_B" pos="{vec3(B)}">
      <geom type="sphere" size="{R_PIN}" material="joint_pin" mass="0.001"
            contype="0" conaffinity="0"/>
      <site name="s_B" pos="0 0 0" size="0.001"/>
    </body>"""

cam_pos = "0.00 -1.55 0.28"

xml = f"""<mujoco model="truss_collapse">
  <!-- 4-bar trapezoid + diagonal C-B (removed at t≈0.8 s in render). -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"
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
    <material name="floor_mat" rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="support_mat" rgba="0.30 0.27 0.24 1" specular="0.1" shininess="0.1"/>
    <material name="bar_mat" rgba="0.42 0.44 0.46 1" specular="0.15" shininess="0.15"/>
    <material name="joint_pin" rgba="0.22 0.20 0.22 1" specular="0.25" shininess="0.25"/>
    <material name="payload" rgba="0.86 0.34 0.30 1" specular="0.35" shininess="0.4"/>
  </asset>

  <default>
    <geom contype="0" conaffinity="0" friction="0.6 0.04 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"
          contype="1" conaffinity="1"/>

    <geom type="box" size="0.05 0.06 {PED_H:.4f}" pos="{A[0]:.4f} 0 {PED_H:.4f}"
          material="support_mat"/>
    <geom type="box" size="0.05 0.06 {PED_H:.4f}" pos="{B[0]:.4f} 0 {PED_H:.4f}"
          material="support_mat"/>

    <geom name="bar_AB" type="capsule"
          fromto="{A[0]:.4f} 0 {A[1]:.4f}  {B[0]:.4f} 0 {B[1]:.4f}"
          size="{R_BAR}" material="bar_mat"/>

{linkage_xml}

    <camera name="cam" pos="{cam_pos}" fovy="44"
            xyaxes="1 0 0  0 0 1"/>
  </worldbody>

  <tendon>
    <!-- Critical diagonal C-B: triangulates frame until removed at render time. -->
    <spatial name="diag_CB" stiffness="{K_DIAG}" damping="{D_DIAG}"
             springlength="{CB_LEN:.5f}" width="0.001"
             rgba="0.42 0.44 0.46 0" limited="false">
      <site site="s_C"/>
      <site site="s_B"/>
    </spatial>
  </tendon>

  <equality>
    <connect name="pin_B" body1="leg_DB" body2="anchor_B"
             anchor="{DB[0]:.4f} 0 {DB[1]:.4f}"
             solref="0.002 1" solimp="0.99 0.999 0.0001"/>
  </equality>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "truss_collapse.xml")
with open(out_path, "w") as f:
    f.write(xml)

print(f"Wrote {out_path}")
print("  Complete trapezoid + diagonal C-B (removed at t≈0.8 s during render)")
print(f"  Load mass {M_LOAD} kg on top member (offset {LOAD_OFFSET_X} m)")
print(f"  Diagonal |C-B|={CB_LEN:.3f} m  stiffness={K_DIAG}")
print("Render 3.0 s (member removal is automatic):")
print(
    "  python3 render.py --scene scenes/truss_collapse.xml "
    "--out out/new_scenes/truss_collapse.mp4 --duration 3.0"
)
print("8-frame grid:")
print(
    "  python3 make_grid.py --scene scenes/truss_collapse.xml "
    "--out out/truss_collapse_grid.png "
    "--duration 3.0 --cols 4 --rows 2"
)
