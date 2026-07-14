# Edit mode

Treat image editing as a closed change request.

## Change set

- `Preserve`: source facts and user locks outside the requested edit.
- `Transform`: only user-authorized changes plus the minimum visible correction needed to integrate them.
- `Avoid`: concrete drift risks that cannot be expressed clearly as preserve/transform instructions.
- `Released locks`: identity, pose, costume, camera, composition, count, geometry, or text the user explicitly allows to change.

Unmentioned content remains unchanged. Lighting, grade, haze, depth, material, background, surface texture, and props are not automatically editable.

## Select the edit intent

- Conservative cleanup: named changes are the complete whitelist.
- Cinematic or art-direction repair: change only diagnosed high-impact systems.
- Reference matching: transfer only the attributes assigned to the target reference.
- Redesign: state released locks before drafting.

Default protections include face/identity, hair, costume, props, pose, blocking, character count, camera, framing, and useful design choices.

For products and packaging, additionally protect silhouette and proportions, material/color identity, closure geometry, exact label copy and hierarchy, crop, scale, set, contact shadow, and unrequested props.

## Edit budget

Use the fewest coherent transforms:

- light repair: local light/color/contrast/haze/surface correction
- medium repair: system-level light/material/integration changes while identity, pose, camera, and environment remain
- heavy repair: only after redesign locks are released

When unrelated changes would overload one pass, recommend a staged order and explain the benefit. Do not silently drop an authorized change or split the deliverable without approval; if the user keeps one integrated pass, include the full requested change set and state the stability risk outside the prompt.

## Output

Load `references/edit-platform-templates.md`. Keep `[Preserve] / [Transform] / [Avoid]` as structure, but write complete instructions with visible results. Exact text is quoted and protected. Chinese and English must contain the same preserve list, transform count, locations, and boundaries.

Surface-fragmentation controls are a diagnosed heuristic, not a universal provider rule. Use them only when noisy micro-texture, broken edges, painterly buildup, or patchwork rendering is visible or strongly implied by the requested style.
