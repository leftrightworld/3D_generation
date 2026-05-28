#### `spool_with_string` — Rotation / counter-intuitive
**Physics:** A spool with string wrapped underneath — pulling the string horizontally rolls the spool TOWARD you (not away). Surprising visual.
**Setup:** Spool (cylinder with a smaller axle) on the floor. String wraps under the axle and exits horizontally toward +x. Pull the string by ramping a tension.
**Motion:** Spool rolls in +x direction while string unwinds and the spool's axle moves toward you.
**Template:** `marble.xml` + `maxwell_wheel.xml`.
**Hints:** No actuator needed if you set the spool's initial qvel so it's already in motion. Alternatively, attach the string end to a stationary point and give the spool a small push so the tension acts. Camera: side view.
