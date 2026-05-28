#### `truss_collapse` — Structures
**Physics:** A 2D truss is statically determinate; removing one member shifts the load through alternate paths or, if the truss becomes a mechanism, collapses entirely.
**Setup:** Triangulated 2D truss (Pratt or Warren style, ~5-7 members) holding a load. One member is "removed" (or always missing) — truss collapses.
**Motion:** Truss with all members: holds load. Without: collapses.
**Template:** `dominoes.xml` + `block_overhang.xml`.
**Hints:** Members as rigid rods connected by hinges. Programmatic generator. Render 3 s.
