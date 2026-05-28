#### `arch_vs_beam_load_compare` — Arch vs beam / compression vs bending

**Physics:** An arch transfers vertical load to its foundations through compressive forces along the arch axis (no bending). A flat beam under the same load must resist bending moments that grow as span². The arch is vastly more efficient for wide spans.
**Setup:** Two side-by-side structures spanning 0.60 m: (a) Semi-circular arch of 10 wedge-shaped blocks (same as arch_compression.xml), with a 1 kg central load. (b) Flat beam of 10 rectangular blocks (each 0.06×0.04×0.04 m) connected by weak hinges (stiffness = 500 N/m), spanning the same width, with the same 1 kg central load.
**Motion:** Render 4 s. Arch holds the load — stable. Beam sags progressively and eventually collapses under the load. Camera: side view showing both structures, fovy = 45.
**Template:** `arch_compression.xml` (arch) + `cantilever_load_curve.xml` (beam). x-separate structures by 0.8 m.
**Hints:** Beam hinges must be weak enough to show deflection under 1 kg but stiff enough to not collapse instantly. stiffness = 500 N/m gives visible sag in ~1 s. The arch requires careful initial geometry so blocks interlock cleanly.

---
