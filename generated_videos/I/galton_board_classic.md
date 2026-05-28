#### `galton_board_classic` — Statistics / multi-body
**Physics:** Many balls dropped through a grid of pegs end up distributed in a binomial (approximate normal) distribution at the bottom.
**Setup:** Grid of small pegs (5-7 rows, triangular layout). Funnel above releases balls one at a time (or many at once). Catchment bins below collect them.
**Motion:** Each ball bounces left/right at each peg level; net path leads to a bell-curve distribution in the bins.
**Template:** `dominoes.xml` (peg layout) + `bowling.xml` (balls).
**Hints:** Pegs as small cylinders. ~20 balls in the funnel. Render 5-6 s.
