#### `cantilever_load_curve` — Structures
**Physics:** A cantilever beam under a tip load deflects in proportion to the load (Hooke's law for the beam): δ = FL³/(3EI). Heavier load = more deflection.
**Setup:** A horizontal beam clamped at one end (like beam_buckling but horizontal). A movable load at the free end progressively gets heavier.
**Motion:** Static or quasi-static: at low load, beam barely deflects; at high load, beam visibly bends.
**Template:** `beam_buckling.xml`. Re-use the discretized beam.
**Hints:** Beam horizontal, one end pinned to a wall. Mass at tip varies (could just render 3 separate scenes or one with progressive mass via tendons). Render 2 s.
