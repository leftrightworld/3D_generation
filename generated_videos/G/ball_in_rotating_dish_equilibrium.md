#### `ball_in_rotating_dish_equilibrium` — Rotating frame
**Physics:** A ball in a parabolic dish spinning at constant ω settles at a radius where centrifugal "gravity" balances the dish's slope (a stable orbit).
**Setup:** Parabolic dish (`z = 4·r²` for r ∈ [0, 0.15]) rotating about its vertical axis at ω=6 rad/s. Ball (R=0.012, M=0.01 kg) inside, initial position near the rim with tangential velocity matching the dish.
**Motion:** Ball orbits with the dish at an equilibrium radius.
**Template:** `rotating_fluid.xml` (rotating container).
**Hints:** Dish via programmatic gen. Heavy dish bottom. Render 5 s. 3/4 camera from above.
