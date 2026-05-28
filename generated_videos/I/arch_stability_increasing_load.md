#### `arch_stability_increasing_load` — Statics / failure
**Physics:** An arch can hold up to its critical load; beyond that, individual stones slip and the structure fails.
**Setup:** Arch (like `arch_compression.xml`) with a movable load on top that grows over time (or step-increments).
**Motion:** Arch holds small load → grows → eventually buckles when load exceeds critical.
**Template:** `arch_compression.xml`.
**Hints:** Programmatic gen for the arch. Load can be a heavy mass that descends onto the arch. Render 4 s.
