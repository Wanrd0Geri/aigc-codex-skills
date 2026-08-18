---
name: aigc-video
description: Use when the user wants a final ready-to-paste Seedance, Doubao, Dreamina-family, or explicitly platform-neutral video prompt from a brief, references, script, storyboard, project context, or generated result; including text/reference-to-video,首尾帧, editing, extension, bridging, prompt optimization,白模,绿幕,多宫格分镜,智能编辑,高级编辑,超长视频,时间戳, dialogue/lip sync, continuity, dynamic-world physical interaction, previsualization, review, and failure recovery. This skill owns the final video artifact. Language-only cleanup of an existing platform-neutral prompt without new production decisions belongs to aigc-prompt-rewrite.
---

# AIGC Video

Create one executable final video prompt from one protected production specification. Preserve source facts and continuity internally; render them through the active platform's grammar only at the end.

## Task routing

Load only the references required by the request.

| Condition | Read |
| --- | --- |
| Any Seedance-family output | `references/seedance-2-rules.md` |
| Any new/reference generation; any task that renders a structure-confirmation table; any edit, extension, or bridge that must inherit source world state; or any optimization that changes visible motion or physical interaction | + `references/world-dynamics.md` |
| Seedance version limits, duration, input counts, or feasibility | + `references/seedance-capability-matrix.md` |
| Strict edit, extension, or bridge | + `references/seedance-2-video-operations.md` |
| 白模、绿幕、多宫格、音色参考、局部标注或超长视频 | + `references/seedance-2.5-special-workflows.md` |
| Multiple assets, boundaries, overlapping roles, or A/B output | + `references/video-contracts.md` |
| Performance, camera movement, framing, optics, lighting, dialogue, or lip sync | + `references/shot-craft.md` |
| Complex blocking, occlusion, action handoff, or terminal composition | + `references/single-segment-quality-control.md` |
| Modifying, optimizing, or repairing an accepted/current prompt, shot, sequence, or shared field | + `references/change-impact-and-delivery.md` |
| The user requests or supplies a staging Diagram; repeated geometry failure; or high-risk blocking cannot be expressed unambiguously in text | + `references/blocking-diagram.md` |
| Product, UGC, VFX, one-take, educational, or previsualization pattern | + `references/task-patterns.md` |
| Emotional, memory, or subjective intent | + `references/vibe-expression.md` |
| Performance intent absent or materially ambiguous | + `references/collaboration-and-performance.md` |
| AI-flavored prose or an explicit natural-wording request | + `references/language-lint.md` |
| An observed failed or unstable result is supplied | + `references/failure-recovery.md` |
| Comparing with the observed 即梦 optimizer format or maintaining this Skill | + `references/seedance-2.5-optimizer-example.md` |

## Defaults and precedence

- Respond in Chinese and lead with the result.
- Default to 即梦 Seedance 2.5 when the request is not explicitly platform-neutral and names no platform or version. Use the 2.0 legacy rules only when the user explicitly selects 2.0 or 2.0 Fast.
- Every new, reference-generated, structurally rebuilt, extended, or bridged visible unit passes the same structure confirmation before performance is enriched. There is no simple-shot, text-complete, speed, or explicit-skip exception. A previously accepted structure may remain confirmed only while the current operation preserves it.
- Deliver one final prompt in one fenced code block only after the affected structure is confirmed. While structure confirmation is pending, deliver only the compact structure table and one grouped confirmation request.
- In final prompts, default to plain upload-order labels such as `图片1`、`视频1`、`音频1`; do not output `@` handles or UUIDs unless the current user explicitly requests them for that output.
- For Seedance 2.5 new/reference generation, apply the adapter's standing subtitle/background-music policy. It does not apply to edit, extension, or bridge preservation.
- Favor restrained performance and do not add unsupported people, props, gestures, emotions, or events.
- Treat dynamic-world modeling as a required prompt-building step, not optional atmosphere polish. For every task record `world_activity` as `active | inherited | intentionally_still`; new/reference generation defaults to `active`, while edit, extension, and bridge inherit source behavior unless the requested operation changes it.
- Apply authority per field: current user > active project/source > explicitly authorized readable-asset dimension > personal default > platform default.

## 1. Classify the task

Record the platform/version, output mode, and one base task kind:

- new text-to-video
- image or multimodal reference generation
- strict video edit
- video extension
- bridge or track completion

Record optimization, project scope, Vibe, A/B, previsualization, ultra-long mode, and `world_activity` separately. They do not replace the base task kind. Platform-neutral final prompts remain owned here but receive no Seedance-specific syntax.

Record per shot or generated operation segment:

- `structure_source`: current_text | visual_asset | inherited | unresolved
- `structure_status`: pending | confirmed
- `world_dynamics_review`: planned | source_backed | inherited | intentionally_still | unresolved

Structure fields are: shot size and camera relation; visible roster; screen order and foreground/midground/background placement; pose, facing, path, occlusion, and crop; locked action, dialogue ownership, and visible endpoint; plus only continuity-critical light or world state. `world_activity` is the task-level execution mode; `world_dynamics_review` records per-shot evidence. Neither changes the universal structure-confirmation rule.

Every newly generated or structurally rebuilt visible unit starts `pending`, whether its source is text or a visual asset and whether it is single-character, empty, simple, or complex. Explicit requests such as 「不用结构表」, 「跳过结构确认」, 「直接给我提示词」, or 「尽快输出」 do not change this status. Only an explicit user confirmation or an already accepted structure artifact marks the unit `confirmed`; silence never does.

For optimization, strict edit, or repair of an existing accepted prompt, inherit structure as `confirmed` only when the requested change preserves it. Reopen only affected shots when a change alters framing, camera side, visible roster or identity, screen order, depth, position, facing, path, occlusion, crop, dialogue ownership, locked endpoint, or a structure-bearing asset. A lighting or performance change reopens structure only when it also changes visibility, blocking, framing, or the endpoint. Read `references/change-impact-and-delivery.md` before deciding the affected range.

Extension and bridge create new visible material: the added segment or transition always starts `pending`, while readable source boundaries remain inherited. A strict edit that preserves composition can remain confirmed; a strict edit that changes a structure field reopens the affected interval. Final operation commands render only after every new or reopened unit is confirmed.

## 2. Build evidence, material roles, and locks

Classify each asset as readable, label-only, or missing. Assign every supplied asset one operational role or retain it as evidence only. Never silently drop or merge an asset.

Keep supplied filenames, platform handles, UUIDs, and upload order internally so the material mapping cannot drift. In the final prompt, normalize materials to plain ordered labels such as `图片1`, `视频1`, and `音频1`. Do not render an `@` handle or UUID merely because it appeared in the input. Preserve one literally only when the current user explicitly requests it for the current output. If upload order is unknown and the mapping matters, ask instead of guessing.

For new or reference generation, compile one material-responsibility map internally using `素材标签：具体用途`. Use the active platform adapter to decide whether that map must appear in the final prompt.

- When material responsibilities must be rendered, bind each material once under its owning field, then use semantic character, prop, and scene names in the timeline.
- Assign every fact to one rendered owner and bind each material once. The active platform adapter owns heading placement: for Seedance output, `references/seedance-2-rules.md` is the single source of truth for `主体：`/`场景：`/`风格：` ownership, subject-presence rules, and the coarse white-model opening sentence. Resolve equivalent layouts internally; never ask the user to choose among them.
- Name the exact borrowed dimensions; never write a bare `图片2：参考图`.
- Do not write `定义为` when one unambiguous subject already has a supplied name. Use `图片1中[稳定特征]的主体作为[角色名]` only when selecting among multiple subjects or merging several sources for one identity.
- If a material applies only to one interval, state that interval in its responsibility line rather than repeating the label in every shot.
- Keep unassigned dimensions internal. Externalize a targeted exclusion only for a user/source lock, an active personal default, a direct material conflict, a platform requirement, or an observed failure.

Classify facts as exact, semantic, mutable, or unresolved. Exact dialogue, visible text, material order and roles, durations, edit intervals, shot order, and explicit ending cues must not drift. Read `references/video-contracts.md` for the complete internal contracts.

Treat character identity, visible roster, screen order, foreground/background placement, occlusion, dialogue ownership, and source version as material production facts. When readable evidence does not resolve one of them, mark it unresolved and ask the user; never convert it into a bounded assumption.

## 3. Resolve duration and feasibility

For every Seedance 2.5 new or reference generation, obtain the intended total duration before final rendering. If it is missing, ask for it — grouped into the same round as the structure table when one is pending; do not invent it. This includes previsualization when the final prompt is expected to use the unified timeline formula. Exception: when a coarse white-model video supplies the whole clip's timing and cuts, inherit them without asking for or separately writing total duration. Reuse readable source ranges. When exact cut ranges are unreadable, preserve the source shot order and cuts, render ordered `镜头N：` entries without time ranges, and never invent seconds.

Judge action load, subject load, reference load, dialogue occupancy, framing feasibility, world-motion load, and continuity before drafting.

- Keep one main action and one main camera strategy per generated shot.
- Preserve a user-supplied shot count and order.
- Let a very short cut carry one readable beat instead of repeating a full action cycle.
- Do not delete or reorder locked beats to make timing fit. Compress mutable description and camera complexity first.
- Treat provider stability ranges as recommendations, not hard rejection limits. Read `references/seedance-capability-matrix.md` for exact hard limits and dated recommendations.

## 4. Confirm structure, then build one canonical MotionSpec

If the requested shot itself cannot yet be identified without inventing it—for example, the required start/reference image is absent or the user has supplied only an abstract theme with no visible anchor—ask for that prerequisite first. After it arrives, the shot still starts `pending`. When a meaningful row can already be built and only a field such as duration, exact dialogue, identity, or one material relationship is missing, put that field `待确认` in the table and combine the question with the same confirmation round.

When any affected unit is `pending`, compare source-backed facts with the readable source and deliver one compact `镜头结构确认` table using exactly these columns:

| 镜头 | 构图与机位 | 人物与空间 | 动作、对白与终点 | 简短表演意图 | 光线与环境连续性 |
| --- | --- | --- | --- | --- | --- |

- `构图与机位`: shot size, angle, camera mode, and crop only.
- `人物与空间`: visible roster, order, depth, position, facing, route, occlusion, and partial visibility only when material.
- `动作、对白与终点`: locked action, exact dialogue owner and line, and the visible endpoint.
- `简短表演意图`: one concise source-backed intention; do not yet prescribe gaze micro-movement, breath, fingers, or facial choreography.
- `光线与环境连续性`: only source-backed, inherited, unresolved, explicitly still, or continuity-critical light/world facts. Use `—` when no such fact is locked; do not design the full dynamic-world or lighting pass here.

Use this table as the only review view of the MotionSpec. If evidence supports multiple materially different mappings, write `待确认` in that field and ask rather than guessing. Return only the table plus one grouped confirmation request; fold missing duration, exact dialogue, or asset questions into the same round. Do not render a platform prompt, operation command, Diagram prompt, detailed performance, optics, lighting, or receiver chain until the affected rows are confirmed.

When every affected unit is `confirmed`, define:

- overall goal and visual priority
- internal material-responsibility map and whether it must be rendered
- subject facts, scene, style, light, and only active sound/text
- the active duration rule and, when required, continuous non-overlapping time ranges
- each shot's framing/camera, visible subjects and spatial relationship, current action phase, action/dialogue, camera's visible result, visual focus, ending state, and next handoff
- the dynamic-world layer: an evidence-backed or low-risk physical driver; visible body, clothing, hair, prop, surface, atmosphere, foliage, water, light, or background receivers; their causal coupling; and any residual state that must continue
- global locks and only evidence-backed targeted exclusions

When a cut continues the same event, inherit the current phase, contact point, direction, and active effect state; advance the event instead of restarting it.

Run dynamic-world modeling every time, including when the brief names only the main subject action. Scan each readable scene image, select only the causally active visible subset, and preserve source-bounded direction, phase, disturbance, and residual continuity. Read `references/world-dynamics.md` for the complete inventory, hierarchy, evidence boundary, VFX authorization, table-cell writing, and audit rules.

Treat `intentionally_still` as a resolved result, not a skipped check. Use it for an explicit stillness lock or a format whose inspection purpose would be harmed by secondary motion. For strict edit, extension, and bridge, preserve or inherit the source's driver, direction, disturbance, and residual phase unless the user asks to change them.

## 5. Render the final prompt

Enter this stage only when every affected unit is `confirmed`. Never treat silence after a pending structure table as confirmation.

### New and reference generation

Render through the unified generation structure in `references/seedance-2-rules.md`. That adapter is the single source of truth for Seedance heading order, timeline syntax, dialogue, sound, visible text, subject-presence placement, and the standing final subtitle/music sentence. Duration changes timeline density, not the grammar, except for the explicit coarse-white-model source-timing route in `references/seedance-2.5-special-workflows.md`.

Rules:

- Treat `画面重心` as the rendered form of internal viewer priority; do not create a second explanation of the same idea.
- For a main camera movement, pair the term with its visible result. A self-explanatory fixed camera or shot size needs no redundant explanation.
- Apply the adapter's subject, scene, style, and timeline ownership without restating stable facts. Compile the complete scene-image dynamics inventory internally; render only persistent baseline motion in `场景：` and changed local interaction, event/VFX response, or residual state in the owning `情节：` shot.
- In a normal motion-bearing shot, render the minimum sufficient living-world chain supported by the brief or readable image. Camera motion alone does not satisfy this step. Omit a visible world-motion cue only when `world_activity` is `intentionally_still`, the format explicitly downscopes it, or no existing visible receiver can support one without invention.
- Do not repeat material labels in the timeline after they have appeared in `主体：`, `场景：`, or `风格：`, unless the user supplies an exact time-scoped handle requirement.

### Edit, extension, and bridge

Do not force operational commands into the generation formula. Use their own compact stable formulas from `references/seedance-2-video-operations.md`:

- edit: target + change + interval + preservation boundary
- extension: source + direction + inherited boundary + new timeline + ending
- bridge: predecessor + visible transition + successor boundary

Return one complete operation command. A structure-preserving strict edit may render immediately from its inherited confirmation. Extension, bridge, and any structure-changing strict edit render only after the new or reopened segment has been confirmed.

### Platform-neutral

Preserve the same MotionSpec and requested structure, but omit Seedance handles, markers, capability claims, and operation grammar.

## 6. Expression and language

Preserve a mature prompt when its production meaning is already complete. Otherwise, after required structure confirmation, translate emotional intent into visible body/contact, gaze, breath/pause, expression, distance, object handling, light, or sound response. Do not add flashbacks, symbols, people, or plot events merely to display emotion.

Use complete natural Chinese sentences inside the stable structure. Remove repeated boosters, background explanations that cannot be seen, and different wordings of the same lock. `结构固定` does not mean `每个字段必须写满`.

## 7. Validate and deliver

Check in this order:

1. every affected `structure_status` is `confirmed`; no pending row renders a final prompt or operation command
2. every source-backed structure or dynamic fact has been compared with its readable source; ambiguity remains unresolved rather than guessed
3. exact dialogue, text, duration, interval, shot order, material order, and roles are preserved; every material is accounted for and bound once
4. every visible character, animal, product, vehicle, or key prop has the adapter's required `主体：` owner; pure environment remains the only omission case
5. adapter structure and task grammar pass for timeline, dialogue, sound, visible text, edit, extension, bridge, or platform-neutral output
6. framing, roster, screen order, depth, occlusion, action phase, prop contact, endpoint, and handoff remain coherent
7. `world_activity` and every per-shot `world_dynamics_review` are resolved; the detailed `references/world-dynamics.md` audit and any `光线与环境连续性` cell pass
8. no duplicate ownership, unsupported invention, stale asset fact, reference leakage, synchronized whole-frame motion, or decorative motion list remains
9. static optics and lighting direction are coherent; camera movement or a cut has not moved the world light source
10. every modification passed the impact-closure audit and its delivery is at least one complete affected shot, complete affected sequence, complete prompt, or complete operation command
11. `agents/openai.yaml`, reference routing, and regression cases remain consistent after maintenance

If a check fails, repair the smallest failed field internally and run the full affected-unit checks again. Never expose a field-only patch: re-render at least the complete affected shot, or the complete affected sequence/prompt/operation when the impact crosses that boundary. While structure confirmation is pending, deliver only the compact table and one confirmation request. Otherwise, default delivery is at most one useful judgment or risk sentence followed by the complete Chinese deliverable in one fenced code block.

## Stop conditions

Ask one grouped question and wait only when:

- required structure confirmation is pending
- a required asset or boundary state is missing
- a final Seedance 2.5 new/reference prompt lacks total duration and no coarse-white-model source-timing exception applies
- required exact dialogue, narration, or visible text is missing
- hard locks conflict
- a materially required environment-dynamics field from a visual asset remains unresolved
- two well-supported creative readings would materially change the result

## Avoid

- Do not output `@` handles or UUIDs by default. Use plain upload-order labels; preserve a literal handle only on an explicit current-user request.
- Do not create a second non-timestamped generation default; only the explicit unreadable-cut coarse-white-model route may use ordered `镜头N：` entries without time ranges.
- Do not use `定义为` as routine boilerplate.
- Do not repeat material responsibilities inside every shot.
- Do not write the same camera, appearance, visual priority, or prohibition globally and per shot.
- Do not expose choices between synonymous wording, equivalent field layouts, or duplicate placements. Resolve them by field ownership and ask only when different outcomes or hard locks materially conflict.
- Do not expose EvidenceLedger, ReferenceMap, LockLedger, or MotionSpec names in the final prompt.
- Do not infer character identity, visible roster, screen order, occlusion, dialogue ownership, or which similarly named asset is current when the evidence is insufficient.
- Do not treat `风吹、树叶摇曳、衣摆飘动、水面泛起涟漪` or similar motion nouns as a universal suffix. Select only existing receivers, connect them through one cause, vary response by material and depth, and keep the main action dominant.
- Do not animate every visible element, give unrelated objects identical timing, reverse an inherited wind or flow direction at a cut, or make all motion stop exactly when the subject stops.
- Do not narrate previous failures, revisions, tests, or debugging intent inside the current executable prompt.
