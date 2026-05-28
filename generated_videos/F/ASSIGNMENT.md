# Assignment for F

**Round:** 2026-05-24

## Your tasks this round

- [ ] **galileo_pendulum_peg** — see `BACKLOG.md` for hints
- [ ] **horizontal_vs_dropped_balls** — see `BACKLOG.md` for hints
- [ ] **chain_jet_classic** — see `BACKLOG.md` for hints
- [ ] **rolling_disc_inscribes_cycloid** — see `BACKLOG.md` for hints
- [ ] **bucket_of_water_overhead_swing** — see `BACKLOG.md` for hints
- [ ] **two_marbles_curved_track_collision** — see `BACKLOG.md` for hints
- [ ] **planetary_gear_train** — see `BACKLOG.md` for hints
- [ ] **gear_train_2_gears** — see `BACKLOG.md` for hints
- [ ] **four_bar_linkage** — see `BACKLOG.md` for hints
- [ ] **ratchet_pawl** — see `BACKLOG.md` for hints
- [ ] **chain_unspooling_from_pile** — see `BACKLOG.md` for hints
- [ ] **triple_block_friction_chain** — see `BACKLOG.md` for hints
- [ ] **chain_on_scale_falling** — see `BACKLOG.md` for hints
- [ ] **two_bodies_on_incline_string** — see `BACKLOG.md` for hints
- [ ] **double_atwood** — see `BACKLOG.md` for hints
- [ ] **galileo_inclined_plane_squared** — see `BACKLOG.md` for hints
- [ ] **rolling_dumbbell** — see `BACKLOG.md` for hints

See `BACKLOG.md` for full details on each scene (physics, hints, similar
existing scenes to copy from).

## How to do this (5-step recipe)

1. Read **`CLAUDE.md`** end-to-end. It's short and tells you the workflow and
   conventions. If you're letting an AI agent do the heavy lifting, point it at
   `CLAUDE.md` first — that's what it's designed for.

2. For each task above:
   - Find a similar existing scene under `scenes/` and copy it as your
     starting point. **Never write from scratch.**
   - Adapt it to your physics. Match the visual style in
     `docs/style_guide.md` **verbatim** — same purple skybox, same cream
     floor, same warm wood, same camera framing rules.
   - Render + verify:
     ```
     python3 render.py    --scene scenes/<name>.xml --out out/new_scenes/<name>.mp4 --duration T
     python3 make_grid.py --scene scenes/<name>.xml --out out/<name>_grid.png       --duration T --cols 4 --rows 2
     ```
   - **OPEN the grid PNG** and confirm the physics looks right. Iterate
     parameters until it does (usually 2–5 iterations).

3. Fill in `RETURN.md` at the root of this folder — what you finished, what
   got stuck, any new gotchas you hit.

4. Tar up the entire folder and send it back:
   ```
   tar czf my_return_2026-05-24.tar.gz physics_video_gen/
   ```

## Hard rules — do not break these

- **Only ADD files in these locations:**
  - `scenes/*.xml`
  - `scenes/gen_*.py`
  - `out/new_scenes/*.mp4`
- **Do NOT modify** any other file. If you need to suggest changes to
  `BACKLOG.md`, `DIARY.md`, `docs/gotchas.md`, etc., write your suggestion
  in `RETURN.md` and the master keeper will merge it.
- **Do NOT swap your assigned scenes** for different ones. If a task is
  impossible, mark it incomplete in `RETURN.md` and explain why.
- **Visual style is non-negotiable.** Same skybox, floor, lights, wood
  tones, accent palette as existing scenes. If you're tempted to invent a
  new color, don't.

## Common pitfalls already documented

See `docs/gotchas.md` — 18 traps your predecessors hit. Reading it takes
5 minutes and will save you hours of debugging.
