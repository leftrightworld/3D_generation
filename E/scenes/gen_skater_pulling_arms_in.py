"""
Generate scenes/skater_pulling_arms_in.xml — connected dumbbell rotor:
  mass --- rod --- hub --- rod --- mass

Two large cuboid masses slide radially along fixed guide rods under spring
tension, demonstrating I·ω ≈ const with a large visible radius change.
"""
import os

# ---- layout ------------------------------------------------------------------
HUB_Z = 0.22
R_EXT = 0.60            # initial mass-center radius (m)
R_RET = 0.14            # spring equilibrium radius (m)
ROD_HALF = 0.68         # fixed guide rod half-span from center (m) → 1.36 m total

MASS_HALF = 0.045       # cuboid half-size → 0.09 m block (smaller, rod-dominated)
SLEEVE_HALF = 0.050     # sleeve capsule half-length on each block
HUB_R = 0.035           # hub cylinder radius
HUB_H = 0.025           # hub half-height

M_HUB = 0.04            # kg — small hub
M_SLIDE = 0.70          # kg per sliding block (dominates I change)

# ---- dynamics ----------------------------------------------------------------
K_SLIDE = 12.0
D_SLIDE = 2.5
D_SPIN = 0.0002
OMEGA0 = 1.4

# Oblique top-down: sees x-y rotation plane, full rotor in frame.
CAM_POS = "0.7 -1.0 0.75"
CAM_XYAXES = "0.857 0.514 0  -0.184 0.307 0.934"
CAM_FOVY = 40

XML = f"""<mujoco model="skater_pulling_arms_in">
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"/>

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
    <material name="wood" rgba="0.93 0.82 0.58 1" specular="0.1" shininess="0.1"/>
    <material name="hub_mat" rgba="0.22 0.22 0.24 1" specular="0.4" shininess="0.5"/>
    <material name="rod_mat" rgba="0.82 0.58 0.30 1" specular="0.15" shininess="0.2"/>
    <material name="bob_red" rgba="0.86 0.34 0.30 1" specular="0.35" shininess="0.4"/>
    <material name="bob_blue" rgba="0.30 0.50 0.78 1" specular="0.35" shininess="0.4"/>
  </asset>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <geom type="cylinder" fromto="0 0 0  0 0 {HUB_Z:.3f}" size="0.04" material="wood"
          contype="0" conaffinity="0"/>

    <!-- Single connected rotor: hub + full guide rods + two sliding blocks -->
    <body name="rotor" pos="0 0 {HUB_Z:.3f}">
      <joint name="hub_spin" type="hinge" axis="0 0 1" damping="{D_SPIN}"/>

      <!-- Small central hub -->
      <geom name="hub" type="cylinder" size="{HUB_R:.3f} {HUB_H:.3f}"
            material="hub_mat" mass="{M_HUB}" contype="0" conaffinity="0"/>

      <!-- Fixed guide rods through hub — always span the full arm length -->
      <geom name="rod_pos" type="capsule"
            fromto="{HUB_R:.3f} 0 0  {ROD_HALF:.3f} 0 0" size="0.013"
            material="rod_mat" contype="0" conaffinity="0"/>
      <geom name="rod_neg" type="capsule"
            fromto="{-HUB_R:.3f} 0 0  {-ROD_HALF:.3f} 0 0" size="0.013"
            material="rod_mat" contype="0" conaffinity="0"/>

      <!-- +x sliding mass: body origin = mass center, rides on the rod -->
      <body name="mass_pos">
        <joint name="slide_pos" type="slide" axis="1 0 0"
               range="{R_RET:.3f} {R_EXT:.3f}"
               stiffness="{K_SLIDE}" springref="{R_RET:.3f}" damping="{D_SLIDE}"/>
        <!-- Sleeve segment: rod visually passes through the block -->
        <geom name="sleeve_pos" type="capsule"
              fromto="{-SLEEVE_HALF:.3f} 0 0  {SLEEVE_HALF:.3f} 0 0" size="0.012"
              material="rod_mat" contype="0" conaffinity="0"/>
        <geom name="block_pos" type="box" size="{MASS_HALF:.3f} {MASS_HALF:.3f} {MASS_HALF * 0.75:.3f}"
              mass="{M_SLIDE}" material="bob_red" contype="0" conaffinity="0"/>
      </body>

      <!-- -x sliding mass: mirrored slide axis -->
      <body name="mass_neg">
        <joint name="slide_neg" type="slide" axis="-1 0 0"
               range="{R_RET:.3f} {R_EXT:.3f}"
               stiffness="{K_SLIDE}" springref="{R_RET:.3f}" damping="{D_SLIDE}"/>
        <geom name="sleeve_neg" type="capsule"
              fromto="{-SLEEVE_HALF:.3f} 0 0  {SLEEVE_HALF:.3f} 0 0" size="0.012"
              material="rod_mat" contype="0" conaffinity="0"/>
        <geom name="block_neg" type="box" size="{MASS_HALF:.3f} {MASS_HALF:.3f} {MASS_HALF * 0.75:.3f}"
              mass="{M_SLIDE}" material="bob_blue" contype="0" conaffinity="0"/>
      </body>
    </body>

    <camera name="cam" pos="{CAM_POS}" fovy="{CAM_FOVY}"
            xyaxes="{CAM_XYAXES}"/>
  </worldbody>
</mujoco>
"""

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "skater_pulling_arms_in.xml")
    with open(out, "w", encoding="utf-8") as f:
        f.write(XML)
    print(f"Wrote {out}")
    print(f"Radius: {R_EXT:.2f} m (extended) -> {R_RET:.2f} m (retracted)")
    print(f"init-qpos: 0,{R_EXT},{R_EXT}")
    print(f"init-qvel: {OMEGA0},0,0")
