#### `two_marbles_curved_track_collision` — Energy + collision
**Physics:** Two marbles in a frictionless U-shaped track oscillate, meet at the bottom with equal speeds, elastically collide (swap velocities), and oscillate again — perpetual motion (ideally).
**Setup:** U-shaped parabolic track (`z = 0.4·x²` for x ∈ [-0.4, 0.4]), built from ~20 box segments via programmatic gen. Two marbles (R=0.02 m, M=0.04 kg) placed at the rim on opposite sides; both released from rest.
**Motion:** Slide down → meet at bottom → elastic collision → scatter back to original heights → repeat.
**Template:** `brachistochrone.xml` (curved track) + `elastic_collision.xml` (stiff contact).
**Hints:** Marble friction zero. Stiff contact (solref="-200000 -20"). Render 4 s — multiple oscillations. Side view, pos (0, -1.5, 0.4), fovy 40.
