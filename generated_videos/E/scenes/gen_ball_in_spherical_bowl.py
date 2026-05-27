"""
Generate scenes/ball_in_spherical_bowl.xml — thin hemispherical shell bowl + ball oscillation.

Bowl: translucent thin shell (inner + outer mesh), opening upward.
  x = R sin(phi) cos(theta)
  y = R sin(phi) sin(theta)
  z = R (1 - cos(phi))          (MuJoCo z-up; phi=0 bottom, phi=pi/2 rim)

Collision: inner surface mesh. Ball oscillates on y=0 meridian.
"""
import math
import os

BOWL_R = 0.30
BALL_R = 0.030
BALL_M = 0.012

SHELL_T = 0.0035
RIM_T = 0.010
N_PHI = 22
N_THETA = 40
N_COLL = 40          # invisible meridian collision strips (physics only)
COLL_W = 0.014
COLL_T = 0.006

CHORD_OVERLAP = 1.12

THETA0 = 0.35
G = 9.81
EFF_R = BOWL_R - BALL_R
OMEGA = math.sqrt(G / (1.4 * EFF_R))
PERIOD = 2 * math.pi / OMEGA
DURATION = 4.0

script_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(script_dir, "ball_in_spherical_bowl.xml")


def wall_thickness(phi):
    """Thin wall everywhere; slightly thicker near the rim."""
    if phi >= math.pi / 2 - 0.12:
        return RIM_T
    return SHELL_T


def shell_point(phi, theta, r_offset=0.0):
    """Point on sphere centered at (0, 0, BOWL_R); phi=0 at bottom."""
    st, ct = math.sin(phi), math.cos(phi)
    cth, sth = math.cos(theta), math.sin(theta)
    r = BOWL_R + r_offset
    x = r * st * cth
    y = r * st * sth
    z = BOWL_R - r * ct
    return x, y, z


def build_shell_mesh():
    """Thin hemispherical shell: inner + outer surfaces, phi in [0, pi/2]."""
    verts = []
    inner, outer = [], []

    for i in range(N_PHI + 1):
        phi = i * (math.pi / 2.0) / N_PHI
        wt = wall_thickness(phi)
        rin, rout = [], []
        for j in range(N_THETA):
            theta = j * 2.0 * math.pi / N_THETA
            rin.append(len(verts) // 3)
            verts.extend(shell_point(phi, theta, 0.0))
            rout.append(len(verts) // 3)
            verts.extend(shell_point(phi, theta, wt))
        inner.append(rin)
        outer.append(rout)

    faces = []
    for i in range(N_PHI):
        for j in range(N_THETA):
            j1 = (j + 1) % N_THETA
            il, il1 = inner[i][j], inner[i][j1]
            il2, il3 = inner[i + 1][j1], inner[i + 1][j]
            ol, ol1 = outer[i][j], outer[i][j1]
            ol2, ol3 = outer[i + 1][j1], outer[i + 1][j]
            faces.extend([il, il3, il1, il1, il3, il2])      # inner
            faces.extend([ol, ol1, ol3, ol1, ol2, ol3])      # outer
            faces.extend([il, ol, ol1, il, ol1, il1])         # side at ring i
            faces.extend([il3, il2, ol2, il3, ol2, ol3])     # side at ring i+1

    vert_str = " ".join(f"{v:.5f}" for v in verts)
    face_str = " ".join(str(f) for f in faces)
    return vert_str, face_str


def collision_meridian_geoms():
    """Invisible collision arc on y=0 meridian (not rendered as bowl geometry)."""
    geoms = []
    for i in range(N_COLL):
        phi = -math.pi / 2 + (i + 0.5) * math.pi / N_COLL
        r_seg = BOWL_R + COLL_T * 0.5
        x = r_seg * math.sin(phi)
        z = BOWL_R - r_seg * math.cos(phi)
        half_len = CHORD_OVERLAP * BOWL_R * math.pi / N_COLL * 0.5
        geoms.append(
            f'    <geom type="box" pos="{x:.4f} 0 {z:.4f}" '
            f'euler="0 {-phi:.5f} 0" '
            f'size="{half_len:.4f} {COLL_W * 0.5:.4f} {COLL_T * 0.5:.4f}" '
            f'rgba="0 0 0 0" contype="1" conaffinity="1"/>'
        )
    return "\n".join(geoms)


def segment_inner_top(x):
    best = -1e9
    half_len = CHORD_OVERLAP * BOWL_R * math.pi / N_COLL * 0.5
    for i in range(N_COLL):
        phi = -math.pi / 2 + (i + 0.5) * math.pi / N_COLL
        sx = (BOWL_R + COLL_T * 0.5) * math.sin(phi)
        if abs(x - sx) <= half_len + BALL_R:
            best = max(best, BOWL_R * (1.0 - math.cos(phi)))
    return best


def ball_center_on_surface(theta):
    x = EFF_R * math.sin(theta)
    z_top = segment_inner_top(x)
    if z_top > -1e8:
        z = z_top + BALL_R
    else:
        z = EFF_R * (1.0 - math.cos(theta)) + BALL_R
    return x, z


def camera_axes(pos, target):
    up = (0.0, 0.0, 1.0)
    z_ax = tuple(target[i] - pos[i] for i in range(3))
    zn = math.sqrt(sum(v * v for v in z_ax))
    z_ax = tuple(-v / zn for v in z_ax)
    x_ax = (
        up[1] * z_ax[2] - up[2] * z_ax[1],
        up[2] * z_ax[0] - up[0] * z_ax[2],
        up[0] * z_ax[1] - up[1] * z_ax[0],
    )
    xn = math.sqrt(sum(v * v for v in x_ax))
    x_ax = tuple(v / xn for v in x_ax)
    y_ax = (
        z_ax[1] * x_ax[2] - z_ax[2] * x_ax[1],
        z_ax[2] * x_ax[0] - z_ax[0] * x_ax[2],
        z_ax[0] * x_ax[1] - z_ax[1] * x_ax[0],
    )
    return x_ax, y_ax


shell_v, shell_f = build_shell_mesh()
coll_xml = collision_meridian_geoms()

bx0, bz0 = ball_center_on_surface(THETA0)
cam_pos = (0.48, -0.58, 0.34)
cam_target = (0.0, 0.0, 0.12)
cam_x, cam_y = camera_axes(cam_pos, cam_target)

xml = f"""<mujoco model="ball_in_spherical_bowl">
  <!-- Thin hemispherical shell R={BOWL_R} m, ball R={BALL_R} m.
       T ≈ {PERIOD:.2f} s. Render {DURATION} s. -->
  <compiler angle="radian" coordinate="local" autolimits="true"/>
  <option timestep="0.0005" gravity="0 0 -9.81" integrator="implicitfast"
          impratio="5" cone="elliptic"/>

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
    <material name="bowl_shell" rgba="0.96 0.90 0.58 0.38" specular="0.25" shininess="0.35"/>
    <material name="bob_red" rgba="0.92 0.42 0.18 1" specular="0.45" shininess="0.55"/>
    <mesh name="bowl_shell" vertex="{shell_v}" face="{shell_f}"/>
  </asset>

  <default>
    <geom friction="0.10 0.006 0.0001" solref="0.002 1" solimp="0.97 0.99 0.001"/>
  </default>

  <worldbody>
    <light pos="0 0 12" dir="-0.30 0.55 -1" directional="true" castshadow="true"
           diffuse="0.85 0.82 0.78" specular="0.15 0.15 0.15"/>
    <light pos="0 0 8" dir="0.40 -0.30 -1" directional="true" castshadow="false"
           diffuse="0.28 0.28 0.34" specular="0 0 0"/>

    <geom name="floor" type="plane" size="40 40 0.1" material="floor_mat"
          contype="0" conaffinity="0"/>

    <!-- Translucent thin hemispherical shell (visual only) -->
    <geom type="mesh" mesh="bowl_shell" material="bowl_shell"
          contype="0" conaffinity="0"/>

    <!-- Invisible meridian collision (physics) -->
{coll_xml}

    <body name="ball" pos="{bx0:.4f} 0 {bz0:.4f}">
      <joint name="ball_free" type="free"/>
      <geom name="ball_geom" type="sphere" size="{BALL_R}" mass="{BALL_M}"
            material="bob_red"/>
    </body>

    <camera name="cam" pos="{cam_pos[0]:.2f} {cam_pos[1]:.2f} {cam_pos[2]:.2f}" fovy="40"
            xyaxes="{cam_x[0]:.3f} {cam_x[1]:.3f} {cam_x[2]:.3f}  {cam_y[0]:.3f} {cam_y[1]:.3f} {cam_y[2]:.3f}"/>
  </worldbody>
</mujoco>
"""

with open(xml_path, "w") as f:
    f.write(xml)

print(f"Wrote {xml_path}")
print(f"  BOWL_R={BOWL_R}, BALL_R={BALL_R}, EFF_R={EFF_R:.3f}")
print(f"  Period ≈ {PERIOD:.2f} s, render {DURATION} s")
