#### `double_atwood` — Constraint
**Physics:** Atwood machine where one of the two masses is itself an Atwood machine. Three masses, complex coupled dynamics.
**Setup:** Top pulley at world (0, 0, 1.5). Left side: heavy mass M_h = 0.8 kg on a slide joint. Right side: a second pulley at world (0.3, 0, 0.9) (hanging on the right rope), with two masses m1=0.3 kg, m2=0.2 kg on slide joints below it. Joint equalities couple slides.
**Motion:** All 3 masses move; left mass goes down or up depending on net imbalance; right side masses also move relative to each other.
**Template:** `atwood.xml`.
**Hints:** Two joint equalities chained. Render 3-4 s.
