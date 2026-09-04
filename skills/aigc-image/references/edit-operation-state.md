# Dependent edit operations and result state

Read for dependent edits, source/target conflicts, object changes with associated effects, or actual editing. A single independent cleanup needs only its target, authorized change and Keep; do not instantiate a full record for it. These fields are internal, not mandatory output or provider syntax.

## IMG-STATE-01 — Evidence state and dependencies

Keep the target specification separate from the image's current appearance under `IMG-EVIDENCE-01` in [../SKILL.md](../SKILL.md). Use three states for facts consumed by operations:

| State | Meaning | Allowed use |
| --- | --- | --- |
| `observed` | Read from an identified actual source image within its assigned role. | Establish current pixels and readable relationships; qualify interpretation separately. |
| `planned` | A target result with an authorized producing operation. | Supply a later condition in a joint prompt; never claim it already exists. |
| `verified` | Inspected on a specific actual candidate and passed the named check. | Supply that checked condition to a later actual edit; other fields remain unchecked. |

User/project target text is an authoritative target, not proof that those letters are already in the image. A plausible interpretation is not a direct observation. Track an unresolved value only when competing choices would change the result materially; do not require exact hidden lighting or depth measurements for a bounded visible repair.

For each dependent operation, retain only necessary fields (`target`, `endpoint`, `permission_source`, and a fact's `state` are field names, not required output headings):

- `id`, target and requested endpoint; permission source or named release
- `reads`: relevant source facts or another operation's output
- `writes`: authorized property changes and attributable support
- `produces`: the planned condition made available downstream
- `checks`: the visible endpoint and costly invariants to inspect

Build order from reads and writes. An operation cannot justify its own missing evidence with its desired effect: glow requires an observed emitter or a separately authorized operation creating one. No producer means the evidence gate remains unresolved. If dependencies form a cycle, jointly specify the shared visual system when its targets are compatible; if a material choice remains contradictory, ask rather than invent a state.

When an upstream write changes a consumed fact, mark it `recheck_required: true`, recompute it from the updated plan, and propagate only through its consumers. This is a recheck marker, not a fourth evidence state. Replace a superseded verified value with the new planned target until an actual candidate passes the relevant check; record `image_id` and `check_id` for such verification. Preserve unaffected source facts and target locks.

| Changed property | Re-evaluate when consumed |
| --- | --- |
| object presence, placement, scale or projection | contact, owned shadow/reflection, occlusion, local material integration |
| camera relation, crop or frame position | projection-dependent placement, source-to-image-center flare axis, protected screen regions |
| source position, output, occlusion or exposure | receiving surfaces, shadows, reflection, halo and flare support |
| grade or material response | light/highlight color and intensity used by later optical effects |
| focal plane or depth ordering | sharp/defocused regions and eligible bokeh highlights |
| removal revealing or replacing a region | observations of the new background and operations that consume that region |

For a joint prompt, render compatible planned dependencies causally without claiming visual verification. For staged actual edits, inspect the intermediate image and update only checked fields to `verified` before consuming them. If the lamp is not created or is in the wrong place, repair that operation before adding its glow.

### Result tracking

Retain the original locked source and assigned references, the current candidate, and the checked successes/failures. A candidate does not replace identity, exact text or design targets merely because it was generated later. If a candidate drifts, repair against the locked baseline while retaining unrelated successful edits where feasible; do not use the drifted candidate as a new identity target. Recheck affected dependents after repair.

End actual editing when the requested change and costly invariants pass. If an attempted repair repeats the same failure without a new supported correction, show the best candidate with the unresolved issue; do not iterate indefinitely or claim completion. Follow-up user changes update only named targets and dependent checks.

## IMG-SUPPORT-01 — Attributable affected regions

An object's edit scope includes the smallest readable region needed to make that operation coherent: its body, newly exposed/occupied background, edge transition, contact influence, and shadows or reflections attributable to that object. Identify ownership from the image and operation; do not equate spatial proximity with ownership.

- Removal clears the object and its identifiable owned shadow/reflection, then restores those local surfaces. It does not preserve a ghost reflection merely because it lies outside the object's silhouette.
- Movement clears the old attributable effects and establishes new contact, occlusion, shadow and reflection at the authorized destination using the scene's retained lighting.
- Replacement updates only effects whose source geometry, material or placement changed; unrelated objects and the global lighting system stay protected.
- A user explicitly keeping an anomalous reflection/shadow defines a stylized target; preserve that choice instead of automatically physicalizing it.

If ownership is uncertain, use the visible unambiguous support or ask one focused question when excluding/including the region would materially alter the result. Never widen integration to the whole image merely to ensure consistency. A hard lock on a necessary support region is a real conflict under `IMG-AUTH-01`.

## Worked dependency

Request: add one warm lamp on the right wall, illuminate nearby plaster and give that lamp restrained glow; keep the person and framing.

`A add lamp → B local light response → C source-attached glow`: A produces a planned emitter; B reads its position/output and produces the local exposure relationship; C consumes that emitter and exposure. The original image need not already contain the lamp. Keep comes from the whole request, so C's standalone lighting default cannot cancel B. If A moves later, refresh B and C, but retain the person's identity lock. In actual staged editing, C waits for the emitter to be inspected in A/B's result.
