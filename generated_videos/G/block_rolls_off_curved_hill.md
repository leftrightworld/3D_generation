#### `block_rolls_off_curved_hill` — Energy → projectile
**Physics:** Block at the top of a smooth curved hill slides down by gravity, then becomes a projectile when the hill ends.
**Setup:** Curved hill: a "ramp-then-cliff" shape (smooth slope going down, then a sharp drop to flat ground). Block placed at the top, friction zero.
**Motion:** Block slides down the slope, reaches the cliff edge, flies off as a projectile, lands somewhere ahead on the ground.
**Template:** `brachistochrone.xml` + `bowling.xml`.
**Hints:** Programmatic gen for the hill shape. Render 1.5 s.
