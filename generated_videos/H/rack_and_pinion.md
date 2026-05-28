#### `rack_and_pinion` — Mechanism
**Physics:** A gear (pinion) meshed with a flat toothed bar (rack) converts rotation to linear translation.
**Setup:** Pinion: small cylinder R=0.05 m on a hinge. Rack: long box with a slide joint (along x). Joint equality couples pinion rotation to rack translation: rack_x = -R_pinion · pinion_angle.
**Motion:** Pinion driven by init-qvel; rack translates uniformly.
**Template:** `gear_train_2_gears.xml` + `slider_crank_mechanism.xml`.
**Hints:** Top-down camera. Render 3 s.
