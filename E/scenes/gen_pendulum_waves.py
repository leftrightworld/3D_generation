"""
Procedurally generate scenes/pendulum_waves.xml: N pendulums of carefully
chosen lengths hung from a horizontal bar.  All released together at the
same angle; their slightly-different periods make them gradually go out of
phase, producing the classic traveling-wave / standing-wave / re-sync
sequence.

Choice of lengths: pendulum i completes (K+i) oscillations in the chosen
sync-window W.  Then T_i = W / (K+i)  and  L_i = g * T_i^2 / (4 pi^2).
At t = W (the window), all pendulums have completed an integer number of
oscillations and resync.  In between you see waves.
"""
import math
import os

# --- choices ----------------------------------------------------------------
N      = 14            # number of pendulums
W      = 30.0          # sync window in seconds (all back in phase at t = W)
K      = 25            # oscillation count of the slowest (longest) pendulum

# --- bar ---------------------------------------------------------------------
BAR_Z       = 2.00     # mount height
BAR_XHALF   = 0.95     # bar half-length in x (extends from -BAR_XHALF to +BAR_XHALF)
SPACING     = 2 * BAR_XHALF / (N - 1)

g = 9.81
BOB_R = 0.022
ROD_R = 0.0035


def length_i(i):
    T = W / (K + i)
    return g * T * T / (4 * math.pi * math.pi)


# --- pendulum bodies ---------------------------------------------------------
bodies = []
for i in range(N):
    x_i = -BAR_XHALF + i * SPACING
    L_i = length_i(i)
    bodies.append(f'''    <body name="p{i}" pos="{x_i:.4f} 0 {BAR_Z:.4f}">
      <joint name="j{i}" type="hinge" axis="1 0 0" damping="0.0008"/>
      <geom type="capsule" fromto="0 0 0  0 0 -{L_i:.4f}" size="{ROD_R}"
            material="rod_mat" contype="0" conaffinity="0"/>
      <geom type="sphere" pos="0 0 -{L_i:.4f}" size="{BOB_R}" mass="0.020"
            material="bob_warm" contype="0" conaffinity="0"/>
    </body>''')

bodies_xml = "\n".join(bodies)


# --- bar geometry (the mounting rod) -----------------------------------------
# Posts pushed well past the last pendulum (10 cm overhang) so the outermost
# bobs don't clip into the post bodies during their swing.
POST_X = BAR_XHALF + 0.10
bar_xml = f'''    <geom name="bar" type="capsule" fromto="-{POST_X:.4f} 0 {BAR_Z:.4f}  {POST_X:.4f} 0 {BAR_Z:.4f}" size="0.012"
          material="frame_wood"/>'''

# Two end-posts holding the bar up.
posts_xml = f'''    <geom type="box" size="0.035 0.035 1.00"
          pos="-{POST_X:.4f} 0 {BAR_Z * 0.5:.4f}" material="frame_wood"/>
    <geom type="box" size="0.035 0.035 1.00"
          pos=" {POST_X:.4f} 0 {BAR_Z * 0.5:.4f}" material="frame_wood"/>'''


xml = f"""<mujoco model="pendulum_waves">
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"/>

  <visual>
    <headlight diffuse="0 0 0" ambient="0.50 0.48 0.55" specular="0 0 0"/>
    <rgba haze="0.94 0.91 0.90 1"/>
    <global azimuth="120" elevation="-12" offwidth="1920" offheight="1080" fovy="38"/>
    <quality shadowsize="8192" offsamples="8"/>
    <map shadowclip="5" shadowscale="0.7"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="flat"
             rgb1="0.74 0.68 0.86" rgb2="0.74 0.68 0.86"
             width="512" height="512" mark="none" markrgb="0 0 0"/>
    <material name="floor_mat"  rgba="0.94 0.91 0.90 1" specular="0" shininess="0"/>
    <material name="frame_wood" rgba="0.78 0.65 0.40 1" specular="0.12" shininess="0.15"/>
    <material name="rod_mat"    rgba="0.30 0.27 0.24 1" specular="0" shininess="0"/>
    <material name="bob_warm"   rgba="0.92 0.74 0.36 1" specular="0.4" shininess="0.55"/>
  </asset>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

{posts_xml}
{bar_xml}

{bodies_xml}

    <!-- Camera: 3/4 view from above-and-front.  World +x reads as image right
         (so bobs fan across the screen horizontally), and the pendulum swing
         in y now reads as up-down motion across the screen — that's what
         makes the wave pattern visible. -->
    <camera name="cam" pos="0 -1.8 3.6" fovy="40"
            xyaxes="1 0 0   0 0.688 0.726"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "pendulum_waves.xml")
with open(out_path, "w") as f:
    f.write(xml)

# Also emit the init-qpos string (all pendulums start at the same angle).
init_angle = 0.30  # ~17 deg
qpos_str = ",".join([f"{init_angle}"] * N)
print(f"Wrote {out_path}  (N={N}, lengths {length_i(0):.3f}..{length_i(N-1):.3f} m)")
print(f"Suggested --init-qpos: \"{qpos_str}\"")
print(f"Suggested duration: {W:.1f}s (full re-sync window) or shorter")
