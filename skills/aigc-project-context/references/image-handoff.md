# ImageContext handoff

Use only for a project-backed image diagnosis, image-edit prompt, or performed edit. Keep the envelope internal unless the user requests it.

```yaml
schema_version: "1.0"
project: "<id/title>"
context_status: "validated | pending | stale_fallback"
scope: "<episode/scene/shot or asset scope>"
provenance:
  - field: "<field>"
    source: "<source id + record/file coordinate>"
    retrieved_at: "<timestamp or snapshot date>"
    freshness: "live | local_current | cache_validated | snapshot"
base_image:
  anchor: "<user-visible image label>"
  role: "scene_base | asset_base | unresolved"
locks:
  exact: []
  semantic: []
editable: []
scene_facts: []
composition_depth_facts: []
light_color_material_facts: []
reference_inputs:
  - anchor: "<image label>"
    roles: []
    may_control: []
    must_not_control: []
exclusions: []
open_decisions: []
```

## Rules

- Include only fields required by the requested image edit.
- Preserve exact text, identity, subject count, scene geometry, and user/source locks.
- Use composition or lighting facts only when supported by assigned readable evidence.
- A reference role never expands `may_control`.
- A hand-drawn storyboard may constrain framing, blocking, depth, and screen direction; it does not automatically control identity, final material, color, lighting, or detail.
- A white-background character sheet may constrain identity, wardrobe, and local material; it does not control scene lighting, camera, environment, or composition.
- `stale_fallback` permits a clearly dated fallback, not a claim about the current production state.

## Role crosswalk

Keep each anchor unchanged. Normalize only these roles and whitelisted controls:

- `scene_base` or `asset_base`: owns the pixels being edited; it does not donate a second style or identity.
- `storyboard` or `composition_reference`: may control `framing`, `blocking`, `depth`, `screen_direction`, and `composition` only when readable.
- `identity_reference` or `character_reference`: may control `identity`, `appearance`, `wardrobe`, and explicitly readable local `material`; it may not control scene light, camera, environment, or composition.
- `palette_reference`: may control only the explicitly mapped semantic color zones; it may not control geometry, identity, lighting direction, or exposure unless separately assigned.
- `lighting_reference`: may control `light_direction`, `light_quality`, `color_temperature`, or `contrast_relation` only when individually assigned; it may not control identity, composition, or material design.
- `material_reference`: may control only the named object's assigned `material`, `texture`, or `finish`.

`roles` classifies why the image is present. `may_control` is the smaller executable whitelist. Unlisted, contradictory, or unreadable dimensions stay in `must_not_control` or `open_decisions`; never infer them from the role name alone.

`aigc-image` consumes this envelope as source locks and reference roles, then owns diagnosis, edit capability selection, prompt composition, provider adaptation, execution, and result inspection.
