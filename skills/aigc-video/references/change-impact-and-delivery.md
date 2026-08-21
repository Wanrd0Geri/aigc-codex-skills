# Change Impact And Complete Delivery

Load this reference whenever the user modifies, optimizes, or repairs an accepted/current prompt, shot, sequence, shared field, or observed result. The rule is: review the whole relevant current version, recompute only the affected closure, and deliver complete executable units.

## Required source

Before final recompilation of a generated shot/prompt or revision of an existing operation command, obtain the latest complete affected unit plus any active assets, confirmed structure rows, and neighboring boundary states needed for continuity. A structural request may first reopen and confirm its affected row from the user's new facts; it still cannot be finally recompiled without that current unit. Do not reconstruct unchanged content from memory. If the user supplies only a replacement phrase and the complete current affected unit is unavailable, ask for the unit rather than delivering a disconnected patch or inventing the rest.

For a source-video operation, the complete current source is the readable operational media, not an old generation prompt: strict edit needs the target video, target/interval, requested change, and preservation boundary; extension needs the source boundary plus the confirmed new segment; bridge needs both source boundaries plus the confirmed transition. Do not ask for a prior prompt merely because the operation changes video content.

## Impact pass

1. Record the literal change and its authoritative source.
2. Compare it with the latest accepted version and identify the smallest changed field.
3. Follow only the dependencies below until no downstream field changes.
4. Lock every unaffected exact or semantic field; preserve its value and, when already executable, its wording.
5. Decide whether affected structure stays `confirmed` or returns to `pending`.
6. Recompile every complete affected unit, then run continuity and platform checks across its boundaries.

Do not freely reinterpret the whole project. A full review means checking all relevant dependencies, not rewriting correct content.

## Dependency closure

| Changed field | Recheck before rendering |
| --- | --- |
| visible roster, identity, position, facing, path, depth, or Diagram version | framing/crop, screen order, occlusion, gaze and body axis, action route/contact, light-facing side, visible endpoint, and neighboring handoff |
| camera position, viewpoint owner, angle, shot size, axis side, or movement | visible envelope, viewpoint-character self-visibility, over-the-shoulder foreground, target and mouth visibility, screen direction, occlusion, gaze readability, perspective, depth compression, focus behavior, world-light relation, and boundaries |
| locked action or endpoint | timing, performance tactic, contact/physics, world response and residual, terminal state, and next-shot opening |
| dialogue, speaker, or line timing | exact text, mouth visibility, speaking time, listener task/reaction, attention handoff, and cut allocation |
| performance intention | primary carrier, gaze target, posture/contact, listener response, rhythm, and endpoint; reopen structure only if visible position, action, framing, or endpoint changes |
| light source, world direction, intensity, or exposure | subject lit/shadow sides, camera-visible bright/dark relation, eye/catch lights, highlights, reflections, background exposure, moving-light receivers, and adjacent-shot continuity |
| world driver or physical response | all reachable visible receivers, phase, delay/amplitude, residual state, and cross-shot handoff |
| duration or shot count | every time range, action/dialogue capacity, cut boundary, operation interval, and endpoint |
| shared style, scene, platform, or global policy | every shot or operation using that field and the adapter grammar |
| asset role, upload order, or active version | every field and shot authorized by that asset; retired versions remain inactive |

## Structure reopening

Return only affected rows to `pending` when the closure changes shot size or camera relation, visible roster, screen order, depth, position, facing, route, occlusion, crop, dialogue ownership, locked action boundary, endpoint, or a structure-bearing asset. Text-specified changes and visually read changes follow the same confirmation rule.

A non-structural change may inherit confirmation. Examples include restrained performance refinement, static lighting refinement, sound wording, or material response that leaves composition and endpoints intact. Even then, recompute every dependent field and deliver the complete affected unit.

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
- Reopened structure was confirmed before performance/final rendering.
- Unaffected facts and active wording did not drift.
- Cross-shot boundaries still agree.
- The delivered artifact is complete at the selected scope and executable without locating an old sentence.
