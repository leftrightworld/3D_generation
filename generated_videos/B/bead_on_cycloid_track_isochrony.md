#### `bead_on_cycloid_track_isochrony` — Constraint
**Physics:** A bead on a cycloid track has the same period regardless of release point — the cycloid is the tautochrone.
**Setup:** A cycloid-shaped track (programmatic generation from cycloid equation); a bead placed at different starting positions reaches the bottom in the same time.
**Motion:** Three beads released from different positions on the cycloid; they all reach the bottom (or center) simultaneously.
**Template:** `brachistochrone.xml`. Reuse cycloid generator.
**Hints:** Multiple beads released from different heights but on the same track. Render 1.5 s (cycloid is fast). Side view.
