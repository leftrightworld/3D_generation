#### `bowling_10pin_full` — Multi-body collision

**Physics:** A bowling ball strike initiates a cascade of rigid-body collisions among 10 pins; the exact outcome depends sensitively on ball entry point and angle — perfect centre strike often leaves corner pins standing due to deflection geometry.
**Setup:** Standard 10-pin triangle: pins in 4-3-2-1 formation, spacing 0.305 m (pin centre to centre). Each pin: capsule R = 0.028 m, half-height 0.077 m, M = 1.5 kg. Ball: sphere R = 0.108 m, M = 7.0 kg. Ball positioned 2.0 m in front of the head pin, init-qvel: vx = 5 m/s (along alley axis), vy = 0, vz = 0. Floor static friction 0.3. Pin bases ~0 m from floor (pins stand on the lane).
**Motion:** render 4 s. Ball strikes the head pin, cascade collision ensues. All 10 pins scatter. Camera: front view, pos (0, −3, 0.5), fovy = 38, looking down the alley.
**Template:** `bowling.xml`. gen_bowling_10pin.py places all 10 pins at regulation triangle positions. Each pin is an independent body with freejoint (falls over when hit). Ball has freejoint. High contact stiffness for authentic pin action.
**Hints:** Regulation pin spacing: 0.305 m. Triangle row positions: row 1 at y=0 (1 pin), row 2 at y=0.305 (2 pins, x=±0.1525), row 3 at y=0.61 (3 pins, x=0,±0.305), row 4 at y=0.915 (4 pins, x=±0.1525, ±0.4575). Ball launch 2 m in front of head pin. See gotchas.md §bowling_pin_contacts.

---
