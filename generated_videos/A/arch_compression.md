#### `arch_compression` — Statics
**Physics:** A Roman arch supports a heavy load above by transferring the weight through compressive force along its curved spine. Remove the keystone and the arch collapses.
**Setup:** Roman semi-circular arch made of N wedge-shaped blocks; a heavy load on top. Compare with-keystone vs without-keystone.
**Motion:** With keystone in place, the arch holds the load indefinitely. Without (drop the keystone), the arch buckles inward.
**Template:** `block_overhang.xml`. Programmatic generator likely needed.
**Hints:** Use ~10-12 wedge-shaped blocks per arch. Block-block friction tuned moderately. Initial qpos placing each block precisely. Render 4 s. Side view.
