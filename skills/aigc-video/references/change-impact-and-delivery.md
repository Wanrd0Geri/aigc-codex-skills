# Change Impact And Complete Delivery

Load this reference whenever the user modifies, optimizes, or repairs an accepted/current prompt, shot, sequence, shared field, or observed result. The rule is: review the whole relevant current version, recompute only the affected closure, and deliver complete executable units.

## Required source

Before final recompilation of a generated shot/prompt or revision of an existing operation command, obtain the latest complete affected unit plus any active assets, current structure versions, applicable `SceneSpatialContract`, and neighboring boundary states needed for continuity. A structural request increments and rebuilds its affected version through the review mode in `SKILL.md`; final recompilation still requires the current complete unit. Preserve unchanged content from that unit. If the user supplies only a replacement phrase and the complete current affected unit is unavailable, ask for the unit.

For new or structurally changed source-video operations, use the boundary precedence in `video-contracts.md`: an old generation prompt may fill only the non-authoritative unresolved fields allowed there, never source-boundary facts. Strict edit needs target/interval, change, and preservation boundary; extension needs source boundary plus a structure-resolved new segment; bridge needs both boundaries plus a structure-resolved transition. For wording-only optimization that preserves structure and boundaries, the complete current command is the affected unit; request media only for a source-dependent claim.

## Impact pass — VIDEO-IMPACT-01

1. Record the literal change and its authoritative source.
2. Compare it with the latest complete current unit, its actually recorded acceptance if any, or its source-preservation boundary; identify the smallest changed field. A first source edit needs no old generation prompt or fabricated accepted version.
3. For every touched prior corrective clause, decide `still_active`, `supplemented`, or `superseded`. A new statement supersedes an old one only when both govern the same field/scope and their meanings cannot coexist, or the user explicitly replaces it. A refinement or added condition supplements it. Recency, changed wording, or omission from the latest message alone does not cancel an accepted fact.
4. If replacement versus supplementation is result-changing and not uniquely inferable, route the exact ambiguity through `IntentFactGate`. Otherwise record the evidence and continue.
5. Follow only the dependencies below until no downstream field changes.
6. Lock every unaffected exact or semantic field; preserve its value and, when already executable, its wording.
7. Apply `VIDEO-STATE-01`: preserve actual `confirmed` or `source_preserved` only while all structure fields stay stable; a structural closure creates version 1 from null or increments the affected version, clears its acceptance, and returns it to `pending` under this request's scoped review mode.
8. Invalidate and recheck only touched dynamics, light/composite, sound, performance, Diagram, or specialist dependencies. Record `changed_fields`, `invalidated_fields`, and `rechecked_fields` in the existing ChangeSet. A detail pass may not write outside the current structural envelope or reuse an invalidated combat `design_ready`.
9. Recompile every complete affected unit, then run applicable continuity and platform checks across its boundaries. Language-only cleanup performs protected-difference checks without new adapter or craft passes.

After dependency closure and before delivery, render only the current semantic state: keep each `still_active` fact once, merge each `supplemented` fact into its owning current statement, and remove only `superseded` wording plus diagnosis, duplicate micro-controls, and repeated global facts. Planning-derived shot-internal timing is removable only during substantive recompilation; language-only cleanup protects it under `VIDEO-LITERAL-01`. Preserve every explicit current-user/source internal time, accepted lock, boundary state, and visible endpoint. Keep at most one local negative only when an observed failure has no equivalent positive control. This cleanup changes presentation density, not the accepted structure.

Do not freely reinterpret the whole project. A full review means checking all relevant dependencies, not rewriting correct content.

## Incremental structure delivery

The first structure confirmation for a request shows the complete current table. After an accepted `structure_version` exists, a revision still rebuilds and checks the complete current MotionSpec and dependency closure internally, but the user-facing review is a delta view:

- keep the same canonical eight-column header from `SKILL.md` and show only affected shot rows;
- keep the same compact field ownership as the first table; do not use a changed cell to paste repair history, exclusion stacks, repeated appearance, or internal validation prose;
- put 1–3 concise `变更摘要` bullets before the table;
- prefix changed content in its cell with `【本轮修改】`;
- prefix only dependency-closure consequences with `【联动修改】`;
- in an affected row, write an unchanged cell as `沿用已确认` instead of repeating old text;
- end with exactly: `未列出的镜头与未标注字段沿用已确认版本，已完成内部全量校验。`

Compact revision skeleton:

```text
变更摘要：
- [直接改动]
- [仅在依赖闭包实际变化时写联动]

| 镜头 | 构图与机位 | 画面重心 | 人物与空间 | 动作与终点 | 简短表演意图 | 声音 | 光影、合成与环境连续性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 受影响镜头 | 【本轮修改】... / 沿用已确认 | 【联动修改】... / 沿用已确认 | ... | ... | ... | ... | ... |

未列出的镜头与未标注字段沿用已确认版本，已完成内部全量校验。
```

If the dependency closure crosses a handoff, widen the affected rows and summary to that complete sequence. If no dependency field actually changes, do not add `【联动修改】`. A changed structure field still increments its version and follows the current `structure_review_mode`; the delta view does not turn a pending version into confirmed.

## Dependency closure

Dependency invalidation grants a duty to recheck, not permission to rewrite another locked field. For each proposed consequence, distinguish a derived result of the authorized change from a new subject action or scene event. Recompute the former; change the latter only when the current request authorizes that field. A dependency appearing in `invalidated_fields` or `rechecked_fields` does not make it mutable, and `【联动修改】` is not an authorization source.

For a camera-only change, recalculate framing, visibility/occlusion, projected screen positions, focus and the visible response to the existing light from the preserved world state and performance. Do not add a head turn, body turn, gaze shift, gesture, repositioning, or extra action to make a locked beat more readable. Choose a camera solution within the authorized range, or preserve the action with its actual visibility limit. If two locked requirements still cannot coexist, use the existing IntentFactGate for that concrete conflict; do not add a routine approval round. When the user explicitly permits an action adjustment, change only that authorized action scope and propagate its actual dependencies normally.

For a strict edit to an existing target’s color, material, appearance, or removal, the authorized target change also covers its necessary visible, attributable derived support within the same edit interval: for example, the color of that target in an existing reflection, or removal of that target's existing reflection/contact shadow when the target is removed. Establish each relation from readable source evidence or the current user's explicit source description; include only the support actually present and changed by this edit. A color-only edit does not by itself change shadow geometry, the light source, receiver material, or unrelated reflections. Do not add hypothetical reflections, shadows, bounce light, or a whole-scene physical-design pass merely because an object changes.

Record these target-owned consequences in the existing ChangeSet and render the necessary ones in the complete operation. A reflection may lie on another surface: preserve that surface's geometry/material and all unrelated regions while leaving the target's reflected result inside the edit scope. Ordinary “everything else stays” does not freeze this necessary target-owned support; do not lock an entire tabletop or mirror so broadly that the requested change cannot propagate to its own visible reflection. An explicit lock on that specific reflection or shadow has separate authority: preserve an intentional nonphysical mismatch when explicitly requested, or route a real conflict with requested physical consistency through the existing IntentFactGate. This adds no routine confirmation gate.

| Changed field | Recheck before rendering |
| --- | --- |
| `SceneSpatialContract` region, separator, portal, connectivity, fixed object, world distance, height, or locked cross-shot world relation | increment its `spatial_version`; recheck every consuming `scene_spatial_ref`, world path, boundary position, shot framing, visible roster, occlusion, light relation, and conflicting Diagram scope until the next stable spatial boundary |
| `SceneSpatialContract` fixed light-source identity or world location | increment its `spatial_version`, then follow the light-source closure below; preserve structure confirmation only while every listed structure field remains unchanged, including camera/framing, viewer priority and focal-plane state, visibility/blocking, route, dialogue/narration owner, locked action boundary, and endpoint |
| visible roster, material offscreen presence, identity, position, blocking-critical pose, facing, path, depth, or Diagram version | framing/crop, screen order, occlusion, offscreen causal clue, gaze and body axis, action route/contact, light-facing side, visible endpoint, and neighboring handoff |
| camera position, viewpoint owner, angle, shot size, axis side, movement, or optical zoom | recompute visible envelope, viewpoint-character self-visibility, over-the-shoulder foreground, target/mouth visibility, projected screen direction, occlusion, gaze readability, perspective, depth compression, focus behavior, world-light relation, and boundaries from the preserved subject action and world state; visibility loss alone does not authorize a compensating action |
| viewer priority, focal-plane/depth-of-field state, or supported focus shift | framing/crop, subject dominance, secondary-subject visibility, focal plane, action readability, ending image, and any neighboring handoff that inherits the priority |
| locked action or endpoint | timing, performance tactic, contact/physics, world response and residual, terminal state, next-shot opening, and any CombatHandoff/StateRelay dependencies |
| combat body/contact, support, action phase, weapon grip/owner, form/VFX or opponent/environment state | invalidate affected handoff mechanics/direction, relay rows and audit findings; recheck both boundary endpoints and inherited later states until stable; use the CombatHandoff mapping in `video-contracts.md` |
| dialogue, narration, voice, subtitle/visible text, sound/music, or seam phase | exact content and owner, speech visibility, independent lip-sync demand, active/completed state, audible speaking time, mouth visibility only when sync is required, text position/timing, listener task/reaction, sound continuity, and cut allocation |
| performance intention | primary carrier, gaze target, posture/contact, listener response, rhythm, and endpoint; reopen structure only when this closure changes a structure field defined in `SKILL.md` |
| strict-edit target color, material, appearance, or removal | target-visible result plus only existing attributable reflections, shadows, transmitted/revealed areas, or local response that this specific change necessarily alters; preserve unrelated receiver surfaces, lighting, motion, and interval boundaries under the strict-edit support rule above |
| light source, world direction, intensity, exposure, light/composite applicability, or integration | set affected light review to `pending`; classify applicability under `VIDEO-LIGHT-01`, then recheck physical source/receivers/exposure or the actual non-physical layer/edge/color continuity and adjacent boundaries. Resolve physical review before delivery; N/A is legal only for explicit non-physical imagery |
| world driver, physical response, or stability lock | set affected dynamics reviews to `pending`; recheck mode, reachable visible receivers, necessary mechanics, phase, delay/amplitude, residual state, rendered scope, and cross-shot handoff |
| duration or shot count | every shot-heading range, explicitly locked internal time, action/dialogue capacity, cut boundary, operation interval, and endpoint |
| shared style, scene, platform, or global policy | every shot or operation using that field and the adapter grammar |
| asset role, upload order, or active version | every field and shot authorized by that asset; retired versions remain inactive |

## Structure reopening

Create version 1 when a previously unversioned `source_preserved` edit becomes structural; otherwise increment only affected structure versions, clear acceptance for the new version, and set them to `pending` when the closure changes shot size, camera relation, a deliberate camera move or optical zoom, viewer priority, focal-plane/depth-of-field state, supported focus shift, visible roster, material offscreen presence, screen order, depth, position, blocking-critical pose, facing, route, occlusion, crop, dialogue/narration ownership, locked action boundary, endpoint, a `SceneSpatialContract` fact that changes one of those fields, or another structure-bearing asset. A spatial-version update limited to a fixed light anchor follows lighting closure and preserves structure while the visible structure fields remain stable. Text-specified and visually read changes follow the same rule.

Apply `structure_review_mode` from the current logical request after each increment. `review_required` displays the affected structure rows. `direct_authorized` rebuilds them internally and continues after required evidence and hard decisions resolve. The authorization remains request-scoped and never records confirmation.

A non-structural change may preserve a genuinely accepted version or retain first-edit `source_preserved`; it never invents confirmation. Examples include expressive posture inside the accepted blocking envelope, restrained performance refinement, static light/composite refinement, sound wording, or material response that leaves every structure field intact. Recompute every dependent field and deliver the complete affected unit.

A Diagram candidate that conflicts with a resolved structure retires. Any replacement follows the hypothesis, criterion, and stopping rule in `blocking-diagram.md`. Reopen structure only when new evidence reveals a structural ambiguity. A Diagram never writes or increments `SceneSpatialContract`; a changed contract instead invalidates only the Diagram scopes that depend on the changed facts.

When one changed endpoint becomes another shot's opening, or one shared state continues across cuts, expand the closure until the next stable unaffected boundary. Never stop at a shot boundary merely because the user's wording named one shot. For combat, rebind affected relay rows to both current endpoint versions and rebuild only stale handoff fields before restoring `design_ready`. A later shot whose structure remains unchanged keeps confirmation even when its incoming boundary is rechecked; nonstructural dependency changes still require fresh affected checks.

## Delivery scope — VIDEO-DELIVERY-01

- `complete_shot`: the change and all dependencies remain inside one shot.
- `complete_sequence`: a handoff, shared state, dialogue timing, light/world continuity, or position persists across several shots.
- `complete_prompt`: a shared material map, scene/style rule, platform grammar, total duration, shot count, or global policy changes.
- `complete_operation`: strict edit, extension, or bridge; include target/source, interval or direction, full requested change or new segment, inherited boundary, and preservation boundary.

Internal diagnosis may be field-level. External delivery is never a standalone replacement sentence, field, or negative addendum. Do not rewrite unaffected shots when a smaller complete scope is sufficient.

Record `delivery_form: replacement | standalone` in ChangeSet. A `replacement` is a complete affected shot/sequence intended to replace the corresponding unit inside an identified latest complete parent prompt; retain `parent_artifact_ref` and the unchanged global bindings it consumes. Briefly identify that replacement scope outside the prompt when needed. Its local state is complete, but it is not a separate runnable prompt without its parent. A `standalone` artifact includes every required global material, scene, style, audio, or standing-policy binding for the delivered units; if those dependencies cannot be supplied within the selected unit, widen to a complete prompt. An operation is standalone when its own target/source, change/new segment, interval, and boundaries are complete.

Run renderability over the full current MotionSpec first, then over the delivered artifact in its declared context. A global dependency may be consumed from the identified parent only for a replacement; a standalone output cannot rely on an omitted global heading or an unspecified earlier prompt. This distinguishes complete local state from complete external dependencies without creating a second MotionSpec.

## Final audit

- The latest complete current unit was used.
- Every dependency in the closure was checked; each changed field has current authorization or is a derived consequence that preserves the locked action/world state. Recheck status alone never authorizes a new action.
- Reopened structure passed the review mode and delivery gate in `SKILL.md` before performance/final rendering.
- Every changed `SceneSpatialContract` incremented only its affected spatial closure.
- Every changed dynamics field completed a fresh review and mode decision where required.
- Every changed light/composite field completed the applicable review under `VIDEO-LIGHT-01`; a narrow strict edit checks only its actual target-owned support, and its preservation wording does not freeze that support or authorize unrelated relighting.
- Unaffected facts and active wording did not drift.
- Cross-shot boundaries still agree.
- Superseded repair wording is removed; derived shot-body time ranges are normalized only in substantive recompilation, while language-only exact spans stay unchanged.
- The artifact is complete at the selected scope: a replacement identifies its current parent and needs no old sentence hunt, while a standalone output contains all required bindings. No sentence patch masquerades as a runnable prompt.
