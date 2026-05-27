"""
Procedurally generate scenes/beam_buckling.xml: a slender vertical column
discretized into N rigid segments joined by torsional hinge springs, with a
heavy block on top.  When the axial load Mg exceeds the Euler critical load
P_cr ≈ π²EI/(4L²), the column buckles sideways.

Discretized cantilever model
----------------------------
   * Base of the column is pinned to a fixed base block by a hinge with
     stiffness k (elastic clamp — represents bending stiffness of the lowest
     half-segment).
   * (N-1) inter-segment hinges, each also with stiffness k and damping d.
   * Equivalent bending stiffness EI_eff ≈ k · L_seg = k · L / N.
   * Euler critical load (pin-free cantilever): P_cr = π² EI / (4 L²).

Parameters (tuned for a clean ~3 s bow to a curved equilibrium that does NOT
fall flat — margin must stay near 1 or the load swings the top past the
horizontal and the column collapses to the floor instead of holding a static
bow):
   N         = 10
   L         = 1.0
   k         = 29.0  N·m/rad  (margin too high → collapse; this gives ~1.10)
   d         = 0.35  damping per hinge (high → overdamped, settles smoothly)
   m_seg     = 0.025 kg
   m_top     = 0.55  kg
   seed      = 0.005 rad (~0.3°) at every hinge — small so the early frames
               look near-vertical before the instability grows
   → EI_eff ≈ 2.90,  P_cr ≈ 7.16 N
   → applied load ≈ (0.55 + 10·0.025)·9.81 ≈ 7.85 N
   → margin       ≈ 1.10× critical (just above → slow visible bow)
"""
import math
import os

# ---- parameters ------------------------------------------------------------
N         = 10        # number of segments
L         = 1.0       # total column length
SEG_L     = L / N

CROSS_W   = 0.012     # cross-section (square)
CROSS_H   = 0.012
M_SEG     = 0.025     # per-segment mass
M_TOP     = 0.55      # top payload mass
TOP_EDGE  = 0.075     # cube edge of the payload

K_HINGE   = 26.0      # hinge stiffness (N·m/rad)
D_HINGE   = 0.30      # hinge damping  (N·m·s/rad) — enough to suppress
                      # post-buckling oscillation but not so much it slows
                      # the growth phase
SEED      = 0.015     # initial angle per hinge (rad, ~0.86° each → cum 8.6°)

BASE_W    = 0.20      # base block half-extent (xy)
BASE_H    = 0.04      # base block half-height
BASE_TOP  = 2 * BASE_H  # world z of the base top

# Derived (printed for sanity)
EI_eff    = K_HINGE * SEG_L
P_cr      = math.pi**2 * EI_eff / (4 * L**2)
P_load    = (M_TOP + N * M_SEG) * 9.81
print(f"EI_eff={EI_eff:.3f}  P_cr={P_cr:.3f} N  load={P_load:.3f} N  margin={P_load/P_cr:.2f}x")


# ---- segment XML emitter ---------------------------------------------------
def segment_body(i):
    """Recursively build the chain: segment i contains segment i+1 nested inside.
    Each segment's local origin is at its bottom (where its hinge sits)."""
    indent = "      " + "  " * i
    joint = (f'{indent}<joint name="h{i}" type="hinge" axis="0 1 0" '
             f'stiffness="{K_HINGE}" damping="{D_HINGE}"/>')
    geom = (f'{indent}<geom name="seg{i}" type="box" '
            f'pos="0 0 {SEG_L/2:.4f}" '
            f'size="{CROSS_W/2:.4f} {CROSS_H/2:.4f} {SEG_L/2:.4f}" '
            f'material="column" mass="{M_SEG}"/>')
    if i < N - 1:
        child_pos_z = SEG_L
        child = (f'{indent}<body name="seg{i+1}_body" pos="0 0 {child_pos_z:.4f}">\n'
                 f'{segment_body(i+1)}\n'
                 f'{indent}</body>')
        return f"{joint}\n{geom}\n{child}"
    else:
        # Top segment: attach the payload block rigidly at the top.
        top = (f'{indent}<geom name="top_mass" type="box" '
               f'pos="0 0 {SEG_L + TOP_EDGE/2:.4f}" '
               f'size="{TOP_EDGE/2:.4f} {TOP_EDGE/2:.4f} {TOP_EDGE/2:.4f}" '
               f'material="payload" mass="{M_TOP}"/>')
        return f"{joint}\n{geom}\n{top}"


chain_xml = segment_body(0)


# ---- initial qpos: small angle at every hinge to seed buckling direction ---
init_qpos = ",".join(f"{SEED}" for _ in range(N))


xml = f"""<mujoco model="beam_buckling">
  <!-- Euler beam buckling: a slender column discretized into {N} segments
       joined by torsional hinge springs (stiffness={K_HINGE}, damping={D_HINGE}).
       A heavy block ({M_TOP} kg) sits on top.  Applied load ({P_load:.2f} N)
       exceeds the Euler critical load ({P_cr:.2f} N) by {P_load/P_cr:.2f}×, so
       the small initial perturbation grows into a smooth buckled curve. -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.001" gravity="0 0 -9.81" integrator="implicitfast"/>

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
    <material name="wood"      rgba="0.93 0.82 0.58 1" specular="0.1" shininess="0.1"/>
    <material name="wood_dark" rgba="0.78 0.65 0.40 1" specular="0.1" shininess="0.1"/>
    <material name="column"    rgba="0.86 0.78 0.55 1" specular="0.30" shininess="0.4"/>
    <material name="payload"   rgba="0.86 0.34 0.30 1" specular="0.35" shininess="0.4"/>
  </asset>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"/>

    <!-- Fixed base block (the column is pinned to its top face). -->
    <geom type="box" pos="0 0 {BASE_H:.4f}"
          size="{BASE_W/2:.4f} {BASE_W/2:.4f} {BASE_H:.4f}"
          material="wood_dark"/>

    <!-- Column: nested chain of {N} segments connected by torsional hinges.
         All hinges rotate about the y-axis, so buckling deflection is in
         the x-direction (visible directly in a side-view camera). -->
    <body name="seg0_body" pos="0 0 {BASE_TOP:.4f}">
{chain_xml}
    </body>

    <!-- Side view from -y with slight 3/4 tilt, pulled back so the FULL
         column (z 0 to ~1.15) and the bow direction (+x up to ~0.7 m) all
         stay inside the frame at fovy=40. -->
    <camera name="cam" pos="0.70 -2.80 0.75" fovy="40"
            xyaxes="0.985 0.158 0   -0.011 0.069 0.998"/>
  </worldbody>
</mujoco>
"""

out_path = os.path.join(os.path.dirname(__file__), "beam_buckling.xml")
with open(out_path, "w") as f:
    f.write(xml)
print(f"Wrote {out_path}")
print(f"Use:  python3 render.py --scene scenes/beam_buckling.xml "
      f"--out out/new_scenes/beam_buckling.mp4 --duration 4.0 "
      f"--init-qpos \"{init_qpos}\"")
