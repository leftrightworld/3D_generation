#### `multi_link_chain_vertical_collapse` — Free fall / chain
**Physics:** A vertical chain standing straight up topples over progressively under gravity; the top accelerates while the base remains in place initially.
**Setup:** Chain of 20 links stacked vertically at world (0, 0, z=0.05 to z=1.05), hinged together. Bottom link pinned to the floor. Initial perturbation: top link tilted 2°.
**Motion:** Top tips and falls, pulling lower links along; full collapse to the floor.
**Template:** `dominoes.xml` + `beam_buckling.xml`.
**Hints:** Hinge damping 0.005 per joint. Render 2.5 s. Side view.
