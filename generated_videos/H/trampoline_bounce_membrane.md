#### `trampoline_bounce_membrane` — Multi-bounce on elastic surface
**Physics:** A ball bouncing on an elastic membrane — surface flexes, ball bounces multiple times with progressive energy loss.
**Setup:** Membrane: 8×8 grid of small masses with springs between (similar to mexican_hat_drum but smaller, with damping). Edges fixed. Ball dropped from above.
**Motion:** Ball strikes membrane, bounces back up, falls again, bounces several times with decaying amplitude.
**Template:** `mexican_hat_drum_modes.xml` (grid + springs) + `bowling.xml` (ball).
**Hints:** Membrane damping for energy loss. Render 4 s. 3/4 camera.
