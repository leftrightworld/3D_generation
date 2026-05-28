#### `walking_robot_passive_slope` — Passive walking
**Physics:** A 2-legged "biped" with no actuators on a gentle slope — gravity drives walking; swing leg falls forward, plants, switch sides.
**Setup:** Two rigid legs (length 0.4 m, M=0.3 kg each) hinged at a common hip joint. Place on a 5° slope. Initial pose: one leg planted, other leg swung back.
**Motion:** Walker takes 3-5 passive steps down the slope before falling.
**Template:** `triple_pendulum.xml` (link chain).
**Hints:** Slope angle critical (4-7° works); too steep → falls; too shallow → no walk. Render 4 s. Side view.
