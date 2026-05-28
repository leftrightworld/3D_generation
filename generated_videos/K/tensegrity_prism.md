#### `tensegrity_prism` — Tensegrity / tension/compression

**Physics:** Tensegrity structures separate tension members (cables) from compression members (struts), with no bending moments at nodes; the triangular tensegrity prism remains rigid under load through this purely axial force distribution.
**Setup:** Triangular tensegrity prism: 3 compression struts (capsule geoms, L = 0.20 m, R = 0.008 m, M = 0.05 kg each) oriented at ~60° from vertical. 9 cables (tendons, stiffness k = 2000 N/m, rest length set so structure is in equilibrium). Top triangle (3 top nodes) + bottom triangle (3 bottom nodes), rotated 60° relative to each other. A load plate (M = 0.5 kg) rests on the top 3 nodes.
**Motion:** render 4 s. Load applied at t = 0 via the 0.5 kg plate. Structure compresses slightly and reaches static equilibrium. Camera: 3/4 isometric view showing all 6 nodes and 3 struts clearly.
**Template:** `atwood.xml` (tendons) + `block_overhang.xml` (rigid bodies). 6 node bodies (small spheres), 3 strut bodies (capsules), 9 tendons connecting nodes. All bodies have ball joints at nodes for the struts.
**Hints:** Tensegrity equilibrium requires precise tendon rest lengths and stiffness. Pre-compute the equilibrium geometry analytically: for a triangular prism with h = 0.15 m and triangle side s = 0.10 m, derive rest lengths of the 9 cables. Enable tendon damping = 2 to suppress vibration. See gotchas.md §tendon_equilibrium.

---
