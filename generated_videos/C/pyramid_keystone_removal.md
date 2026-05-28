#### `pyramid_keystone_removal` — Statics
**Physics:** A pyramid of blocks held together by gravity and friction; remove a load-bearing block and the structure collapses.
**Setup:** ~10 blocks stacked in a pyramidal arrangement (4 on bottom, 3 on next, etc.). At some moment, one block is removed (via temporary support that disappears).
**Motion:** Pyramid initially static; after key block removal, it collapses progressively.
**Template:** `block_overhang.xml`.
**Hints:** Initially over-constrain so the stack is stable (high friction, soft contacts). To "remove" a block, just don't render it or use a slide joint with init-qvel to slide it out. Render 3 s.
