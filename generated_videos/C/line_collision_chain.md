#### `line_collision_chain` — Collision
**Physics:** Newton's cradle without the strings — a row of touching balls. Striking the leftmost transmits momentum along the line; only the rightmost moves off.
**Setup:** 5 balls in a horizontal row on a frictionless track, just barely touching. Add 1 more ball arriving from the left with some velocity.
**Motion:** Incoming ball strikes, momentum "walks" down the line in an instant, the rightmost ball leaves at the incoming velocity.
**Template:** `newton_cradle.xml` (for contact tuning) + `elastic_collision.xml` (for track).
**Hints:** Use the same stiff contact + small timestep recipe as Newton's cradle (gotcha #4). Balls on freejoints, frictionless track. Energy still leaks (not perfectly elastic) but the qualitative effect is striking.
