#### `symmetry_breaking_ball_on_dome` — Statics / instability
**Physics:** A ball at the very top of a smooth dome is in unstable equilibrium; tiny perturbations make it slide off, eventually flying through air.
**Setup:** A semi-spherical dome of radius R=0.20 m, half-sphere shape built from many small triangular boxes or a single half-ellipsoid geom positioned at world (0, 0, 0.20). Ball: sphere R=0.015 m, M=0.05 kg, placed on top at (0, 0, 0.215). Initial qpos: tiny horizontal offset (Δx=0.001). Friction zero.
**Motion:** Ball stays nearly still for ~0.5 s, then slides off the dome accelerating to the side, then flies through the air after losing dome contact.
**Template:** `loop_the_loop.xml` (for curved surface).
**Hints:** Dome can be approximated by half of a high-poly sphere or by stacked rings. Render 2 s. Camera: side view, pos (0.5, -0.5, 0.15), fovy 40.
