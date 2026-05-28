#### `tumbling_book` — Free rigid body / intermediate axis
**Physics:** Same physics as Dzhanibekov, demonstrated with a book/rectangular slab. Spinning about the medium-length axis is unstable.
**Setup:** Rectangular slab in zero gravity, init-qvel about its intermediate axis (with small perturbation).
**Motion:** Spins ~1 s about intermediate axis, then suddenly flips, then again.
**Template:** Same as `dzhanibekov_effect` but with a rectangular slab geom.
**Hints:** Different shape but same physics. Render 5 s.
