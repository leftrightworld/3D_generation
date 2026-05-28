#### `pulled_block_string_around_peg` — Redirect force
**Physics:** A string going around a fixed peg redirects the pulling direction without changing magnitude (if frictionless). A vertical pull lifts a horizontal block.
**Setup:** Heavy block (M=1 kg) on a frictionless floor with a slide joint along x. Tendon from the block goes UP around a fixed peg at world (0.5, 0, 0.5), then HORIZONTAL to a downward-falling counterweight (M=0.5 kg) on a slide joint along z.
**Motion:** Counterweight falls; string pulls block; block slides horizontally as counterweight descends.
**Template:** `atwood.xml` + `capstan_effect.xml`.
**Hints:** Tendon wraps naturally. Side view. Render 3 s.
