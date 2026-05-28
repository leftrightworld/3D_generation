#### `marble_run_multistage` — Energy / multi-stage track

**Physics:** A marble run converts gravitational PE to KE on ramps, briefly stores KE as rotational energy on the helix, then delivers a collision to a target — demonstrating energy bookkeeping across multiple conversion stages.
**Setup:** Three-stage track: (1) Straight launch ramp, L = 0.5 m at 30° slope (height drop = 0.25 m). (2) Helical descent, 3 turns, helix radius R = 0.06 m, pitch 0.04 m/turn (total descent = 0.12 m, track length ~1.2 m). (3) Flat exit rail 0.2 m long leading to stationary target ball (M = 0.05 kg, R = 0.012 m). Marble: R = 0.010 m, M = 0.020 kg. Released from top of ramp.
**Motion:** render 5 s. Marble rolls down ramp, enters helix, spirals down, exits onto flat rail, and collides with target ball — which flies off. Camera: 3/4 isometric view capturing all three stages.
**Template:** `bead_on_helix.xml` (helix geometry) + `marble.xml` (ball) + `elastic_collision.xml` (target). gen_marble_run.py assembles all three track sections. Helix from `bead_on_helix.xml` gen script. Ramp and rail from box geoms.
**Hints:** Helix inner diameter must be > 2.5 × marble diameter (0.025 m vs. 0.02 m marble diameter — use R_helix = 0.06 m, tube inner R = 0.013 m). Marble transitions from ramp to helix: ensure smooth joint (chamfer the entry). At target collision, use stiff contacts for clean elastic bounce. See gotchas.md §helix_track and §track_transitions.

---
