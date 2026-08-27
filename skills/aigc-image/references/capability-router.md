# Edit capability router

Select the smallest set whose authorized changes fully cover the request. Read only the selected files.

| User intent or diagnosed root cause | Capability file | Evidence gate |
| --- | --- | --- |
| establish, transfer, or reconstruct focus; change depth of field | [edit-focus-depth.md](edit-focus-depth.md) | target plane is identifiable; exact recovery needs readable detail |
| add source-attached glow | [edit-halo.md](edit-halo.md) | existing visible emitter or intense motivated reflection |
| add optical flare ghosts or streak | [edit-lens-flare.md](edit-lens-flare.md) | strong source enters or plausibly faces the lens |
| form background bokeh | [edit-bokeh.md](edit-bokeh.md) | existing background highlights lie behind the focal plane |
| correct convergence, horizon, or spatial projection | [edit-perspective.md](edit-perspective.md) | target geometry and intended plane are readable |
| move, crop, resize, or rebalance framing | [edit-composition.md](edit-composition.md) | user authorizes composition change |
| insert or reconcile scale, contact, overlap, and grounding | [edit-placement-contact.md](edit-placement-contact.md) | support surface and occlusion order are readable |
| repair motivated light, shadow, exposure hierarchy, or local illumination | [edit-lighting.md](edit-lighting.md) | source or intended light relationship is supported |
| generate a positional semantic palette card | [edit-palette-card.md](edit-palette-card.md) | source colors are readable |
| transfer a semantic palette, grade, or color temperature | [edit-palette-transfer.md](edit-palette-transfer.md) | base and palette roles plus mapping are readable |
| change grade, white balance, saturation hierarchy, or color temperature without a palette card | [edit-color-grade.md](edit-color-grade.md) | target color relationship and protected luminance are clear |
| reconcile material, edge, reflection, grain, or local surface response | [edit-material-integration.md](edit-material-integration.md) | target material and surrounding response are readable |
| remove, replace, add, or clean a named object or defect | [edit-object-change.md](edit-object-change.md) | target boundary and reconstruction context are readable |

## Default dependency order

Use only the stages present in the request:

1. perspective and structural geometry
2. composition, scale, placement, contact, and occlusion
3. lighting and material integration
4. semantic palette, grade, white balance, and color temperature
5. focus and depth of field
6. halo, lens flare, and bokeh
7. local cleanup

The order is a dependency rule, not a demand for seven passes. Merge compatible stages into one prompt when earlier changes do not destabilize later evidence.

## Conflict rules

- Focus owns focal planes; bokeh may consume only highlights already placed behind that plane.
- Lighting owns source direction and exposure hierarchy; halo and flare may not invent a conflicting source.
- Perspective owns projection; composition may crop or reposition only after the intended projection is fixed.
- Palette transfer owns color relationships, not luminance hierarchy, shadow geometry, material identity, or scene content unless separately authorized.
- Object insertion uses placement/contact before material integration.
- If one capability edits a property another capability protects, ask which property wins before compiling.

## Cinematic routing

Translate `电影感` in this order:

1. readable subject priority and focal plane
2. motivated light and shadow hierarchy
3. depth and atmospheric separation
4. coherent material response
5. only then a source-supported optical finishing effect

Do not use optical effects when one of the first four relationships is the actual failure.
