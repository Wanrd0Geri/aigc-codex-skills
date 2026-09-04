# Edit capability router

Select the smallest set whose authorized changes fully cover the request. Read only the selected files.

| User intent or diagnosed root cause | Capability file | Evidence gate |
| --- | --- | --- |
| establish, transfer, or reconstruct focus; change depth of field | [edit-focus-depth.md](edit-focus-depth.md) | target plane is identifiable; exact recovery needs readable detail |
| add source-attached glow | [edit-halo.md](edit-halo.md) | observed emitter/intense reflection or authorized producer of one |
| add optical flare ghosts or streak | [edit-lens-flare.md](edit-lens-flare.md) | strong source enters or plausibly faces the lens |
| form background bokeh | [edit-bokeh.md](edit-bokeh.md) | observed or explicitly planned highlights behind the resolved focal plane |
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

This is a common order, not seven required passes or a substitute for this task's dependencies. Use [edit-operation-state.md](edit-operation-state.md) when one operation creates or changes what another reads: for example, adding a lamp precedes its light response and glow; removing an occluder precedes judging its exposed background. Independent changes may share one prompt. Refresh consumed evidence after upstream changes.

## Conflict rules

- Focus owns the resolved focal plane; bokeh consumes observed highlights or authorized planned highlights behind that plane.
- Lighting owns the resolved source direction and exposure hierarchy; halo and flare consume those conditions without inventing a conflicting source.
- Perspective owns projection; composition may crop or reposition only after the intended projection is fixed.
- Palette transfer owns color relationships, not luminance hierarchy, shadow geometry, material identity, or scene content unless separately authorized.
- Object insertion uses placement/contact before material integration.
- Apply `IMG-AUTH-01` in [edit-contract.md](edit-contract.md): merge authorized writes before Keep, and discard conflicting standalone defaults. Ask only about incompatible targets or unreleased user/project locks, not compatible authorized combinations.

## Cinematic routing

Translate `电影感` within the intended medium and purpose; inspect relevant relationships in this order:

1. readable subject priority and, when appropriate to the medium, focal plane
2. motivated light and shadow hierarchy
3. depth and atmospheric separation
4. coherent material response
5. only then a source-supported optical finishing effect

Repair the actual failing relationship before proposing optical finishing. If the user explicitly asks for a finishing effect, preserve that scope; do not substitute unrelated improvements or impose photographic depth on flat artwork.
