# Change Impact And Complete Delivery

Load this reference whenever the user modifies, optimizes, or repairs an accepted/current prompt, shot, sequence, shared field, or observed result. The rule is: review the whole relevant current version, recompute only the affected closure, and deliver complete executable units.

## Required source

Before final recompilation of a generated shot/prompt or revision of an existing operation command, obtain the latest complete affected unit plus any active assets, current structure versions, applicable `SceneSpatialContract`, and neighboring boundary states needed for continuity. A structural request increments and rebuilds its affected version through the review mode in `SKILL.md`; final recompilation still requires the current complete unit. Preserve unchanged content from that unit. If the user supplies only a replacement phrase and the complete current affected unit is unavailable, ask for the unit.

For new or structurally changed source-video operations, use the boundary precedence in `video-contracts.md`: an old generation prompt may fill only the non-authoritative unresolved fields allowed there, never source-boundary facts. Strict edit needs target/interval, change, and preservation boundary; extension needs source boundary plus a structure-resolved new segment; bridge needs both boundaries plus a structure-resolved transition. For wording-only optimization that preserves structure and boundaries, the complete current command is the affected unit; request media only for a source-dependent claim.

## Impact pass

1. Record the literal change and its authoritative source.
2. Compare it with the latest accepted version and identify the smallest changed field.
3. For every touched prior corrective clause, decide `still_active`, `supplemented`, or `superseded`. A new statement supersedes an old one only when both govern the same field/scope and their meanings cannot coexist, or the user explicitly replaces it. A refinement or added condition supplements it. Recency, changed wording, or omission from the latest message alone does not cancel an accepted fact.
4. If replacement versus supplementation is result-changing and not uniquely inferable, route the exact ambiguity through `IntentFactGate`. Otherwise record the evidence and continue.
5. Follow only the dependencies below until no downstream field changes.
6. Lock every unaffected exact or semantic field; preserve its value and, when already executable, its wording.
7. Decide whether each affected structure version stays `confirmed` or increments and returns to `pending`; preserve the current request's scoped review mode.
8. Re-resolve `world_dynamics_review` when the change touches a driver, response, stability lock, or boundary phase.
9. Recompile every complete affected unit, then run continuity and platform checks across its boundaries.

After dependency closure and before delivery, render only the current semantic state: keep each `still_active` fact once, merge each `supplemented` fact into its owning current statement, and remove only `superseded` wording plus diagnosis, duplicate micro-controls, repeated global facts, and planning-derived shot-internal timing. Preserve every explicit current-user/source internal time, accepted lock, boundary state, and visible endpoint. Keep at most one local negative only when an observed failure has no equivalent positive control. This cleanup changes presentation density, not the accepted structure.

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

| Changed field | Recheck before rendering |
| --- | --- |
| `SceneSpatialContract` region, separator, portal, connectivity, fixed object, world distance, height, or locked cross-shot world relation | increment its `spatial_version`; recheck every consuming `scene_spatial_ref`, world path, boundary position, shot framing, visible roster, occlusion, light relation, and conflicting Diagram scope until the next stable spatial boundary |
| `SceneSpatialContract` fixed light-source identity or world location | increment its `spatial_version`, then follow the light-source closure below; preserve structure confirmation only while every listed structure field remains unchanged, including camera/framing, viewer priority and focal-plane state, visibility/blocking, route, dialogue/narration owner, locked action boundary, and endpoint |
| visible roster, material offscreen presence, identity, position, blocking-critical pose, facing, path, depth, or Diagram version | framing/crop, screen order, occlusion, offscreen causal clue, gaze and body axis, action route/contact, light-facing side, visible endpoint, and neighboring handoff |
| camera position, viewpoint owner, angle, shot size, axis side, movement, or optical zoom | visible envelope, viewpoint-character self-visibility, over-the-shoulder foreground, target and mouth visibility, screen direction, occlusion, gaze readability, perspective, depth compression, focus behavior, world-light relation, and boundaries |
| viewer priority, focal-plane/depth-of-field state, or supported focus shift | framing/crop, subject dominance, secondary-subject visibility, focal plane, action readability, ending image, and any neighboring handoff that inherits the priority |
| locked action or endpoint | timing, performance tactic, contact/physics, world response and residual, terminal state, and next-shot opening |
| dialogue, narration, voice, subtitle/visible text, sound/music, or seam phase | exact content and owner, active/completed state, mouth visibility, speaking time, text position/timing, listener task/reaction, sound continuity, and cut allocation |
| performance intention | primary carrier, gaze target, posture/contact, listener response, rhythm, and endpoint; reopen structure only when this closure changes a structure field defined in `SKILL.md` |
| light source, world direction, intensity, exposure, or light/composite integration | subject lit/shadow sides, appearance-reference baked light, contact/cast shadow, ground and nearby receivers, eye/catch lights, material highlights, background exposure, depth/atmosphere, moving-light receivers, camera-visible exposure relation, and adjacent-shot continuity |
| world driver, physical response, or stability lock | set affected dynamics reviews to `pending`; recheck mode, reachable visible receivers, necessary mechanics, phase, delay/amplitude, residual state, rendered scope, and cross-shot handoff |
| duration or shot count | every shot-heading range, explicitly locked internal time, action/dialogue capacity, cut boundary, operation interval, and endpoint |
| shared style, scene, platform, or global policy | every shot or operation using that field and the adapter grammar |
| asset role, upload order, or active version | every field and shot authorized by that asset; retired versions remain inactive |

## Structure reopening

Increment only affected structure versions and set them to `pending` when the closure changes shot size, camera relation, a deliberate camera move or optical zoom, viewer priority, focal-plane/depth-of-field state, supported focus shift, visible roster, material offscreen presence, screen order, depth, position, blocking-critical pose, facing, route, occlusion, crop, dialogue/narration ownership, locked action boundary, endpoint, a `SceneSpatialContract` fact that changes one of those fields, or another structure-bearing asset. A spatial-version update limited to a fixed light anchor follows lighting closure and preserves structure while the visible structure fields remain stable. Text-specified and visually read changes follow the same rule.

Apply `structure_review_mode` from the current logical request after each increment. `review_required` displays the affected structure rows. `direct_authorized` rebuilds them internally and continues after required evidence and hard decisions resolve. The authorization remains request-scoped and never records confirmation.

A non-structural change may inherit confirmation. Examples include expressive posture inside the accepted blocking envelope, restrained performance refinement, static light/composite refinement, sound wording, or material response that leaves every structure field intact. Recompute every dependent field and deliver the complete affected unit.

A Diagram candidate that conflicts with a resolved structure retires. Any replacement follows the hypothesis, criterion, and stopping rule in `blocking-diagram.md`. Reopen structure only when new evidence reveals a structural ambiguity. A Diagram never writes or increments `SceneSpatialContract`; a changed contract instead invalidates only the Diagram scopes that depend on the changed facts.

When one changed endpoint becomes another shot's opening, or one shared state continues across cuts, expand the closure until the next stable unaffected boundary. Never stop at a shot boundary merely because the user's wording named one shot.

## Delivery scope

- `complete_shot`: the change and all dependencies remain inside one shot.
- `complete_sequence`: a handoff, shared state, dialogue timing, light/world continuity, or position persists across several shots.
- `complete_prompt`: a shared material map, scene/style rule, platform grammar, total duration, shot count, or global policy changes.
- `complete_operation`: strict edit, extension, or bridge; include target/source, interval or direction, full requested change or new segment, inherited boundary, and preservation boundary.

Internal diagnosis may be field-level. External delivery is never a standalone replacement sentence, field, or negative addendum. Do not rewrite unaffected shots when a smaller complete scope is sufficient.

## Final audit

- The latest complete current unit was used.
- Every dependency in the closure was checked.
- Reopened structure passed the review mode and delivery gate in `SKILL.md` before performance/final rendering.
- Every changed `SceneSpatialContract` incremented only its affected spatial closure.
- Every changed dynamics field completed a fresh review and mode decision where required.
- Every changed light/composite field completed a fresh review and shared-response check where required.
- Unaffected facts and active wording did not drift.
- Cross-shot boundaries still agree.
- Superseded repair wording and derived shot-body time ranges have been removed; only explicit current-user/source internal timing remains.
- The delivered artifact is complete at the selected scope and executable without locating an old sentence.
