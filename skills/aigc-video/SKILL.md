---
name: aigc-video
description: Use when the user wants a final ready-to-paste Seedance, Doubao, Dreamina-family, or explicitly platform-neutral video prompt from a brief, references, script, storyboard, project context, or generated result; including text/reference-to-video,首尾帧, editing, extension, bridging, prompt optimization,白模,绿幕,多宫格分镜,智能编辑,高级编辑,超长视频,时间戳, dialogue/lip sync, continuity, previsualization, review, and failure recovery. This skill owns the final video artifact. Language-only cleanup of an existing platform-neutral prompt without new production decisions belongs to aigc-prompt-rewrite.
---

# AIGC Video

Create one executable final video prompt from one protected production specification. Preserve source facts and continuity internally; render them through the active platform's grammar only at the end.

## Task routing

Load only the references required by the request.

| Condition | Read |
| --- | --- |
| Any Seedance-family output | `references/seedance-2-rules.md` |
| Seedance version limits, duration, input counts, or feasibility | + `references/seedance-capability-matrix.md` |
| Strict edit, extension, or bridge | + `references/seedance-2-video-operations.md` |
| 白模、绿幕、多宫格、音色参考、局部标注或超长视频 | + `references/seedance-2.5-special-workflows.md` |
| Multiple assets, boundaries, overlapping roles, or A/B output | + `references/video-contracts.md` |
| Performance, camera movement, dialogue, or lip sync | + `references/shot-craft.md` |
| Complex blocking, occlusion, action handoff, or terminal composition | + `references/single-segment-quality-control.md` |
| Product, UGC, VFX, one-take, educational, or previsualization pattern | + `references/task-patterns.md` |
| Emotional, memory, or subjective intent | + `references/vibe-expression.md` |
| Performance intent absent or materially ambiguous | + `references/collaboration-and-performance.md` |
| AI-flavored prose or an explicit natural-wording request | + `references/language-lint.md` |
| An observed failed or unstable result is supplied | + `references/failure-recovery.md` |

## Defaults and precedence

- Respond in Chinese and lead with the result.
- Default to 即梦 Seedance 2.5 when the request is not explicitly platform-neutral and names no platform or version. Use the 2.0 legacy rules only when the user explicitly selects 2.0 or 2.0 Fast.
- Deliver one final prompt in one fenced code block.
- Do not invent music, subtitles, ambience, or action sound. Preserve source-backed audio and exact spoken dialogue when active.
- Favor restrained performance and do not add unsupported people, props, gestures, emotions, or events.
- Apply authority per field: current user > readable asset or literal platform handle > active project/source > personal default > platform default.

## 1. Classify the task

Record the platform/version, output mode, and one base task kind:

- new text-to-video
- image or multimodal reference generation
- strict video edit
- video extension
- bridge or track completion

Record optimization, project scope, Vibe, A/B, previsualization, and ultra-long mode separately. They do not replace the base task kind. Platform-neutral final prompts remain owned here but receive no Seedance-specific syntax.

## 2. Build evidence, material roles, and locks

Classify each asset as readable, label-only, or missing. Assign every supplied asset one operational role or retain it as evidence only. Never silently drop or merge an asset.

Preserve a literal platform handle such as `@图1`, `@视频1`, `@音频1`, `@UUID`, or a filename exactly when the user or platform supplies it. When only upload order is known, use plain ordered labels such as `图片1`, `视频1`, and `音频1`; never invent an `@` handle.

For new or reference generation, compile one material-responsibility map using `素材标签：具体用途`:

```text
【素材职责】
图片1：罗大娘的外貌与服装。
图片2：苏云的外貌、服装与竹背篓。
图片3：仅补充苏云的浅白色瞳孔。
图片4：镜头顺序、构图、人物站位与遮挡关系。
```

- Bind each material once, then use semantic character, prop, and scene names in the timeline.
- Name the exact borrowed dimensions; never write a bare `图片2：参考图`.
- Do not write `定义为` when one unambiguous subject already has a supplied name. Use `图片1中[稳定特征]的主体作为[角色名]` only when selecting among multiple subjects or merging several sources for one identity.
- If a material applies only to one interval, state that interval in its responsibility line rather than repeating the label in every shot.
- Keep unassigned dimensions internal. Externalize a targeted exclusion only for a user/source lock, a direct material conflict, a platform requirement, or an observed failure.

Classify facts as exact, semantic, mutable, or unresolved. Exact dialogue, visible text, material handles, durations, edit intervals, shot order, and explicit ending cues must not drift. Read `references/video-contracts.md` for the complete internal contracts.

## 3. Resolve duration and feasibility

For every Seedance 2.5 new or reference generation, obtain the intended total duration before final rendering. If it is missing, ask for it; do not invent it. This includes previsualization when the final prompt is expected to use the unified timeline formula.

Judge action load, subject load, reference load, dialogue occupancy, framing feasibility, and continuity before drafting.

- Keep one main action and one main camera strategy per generated shot.
- Preserve a user-supplied shot count and order.
- Let a very short cut carry one readable beat instead of repeating a full action cycle.
- Do not delete or reorder locked beats to make timing fit. Compress mutable description and camera complexity first.
- Treat provider stability ranges as recommendations, not hard rejection limits. Read `references/seedance-capability-matrix.md` for exact hard limits and dated recommendations.

## 4. Build one canonical MotionSpec

Silently define:

- overall goal and visual priority
- material-responsibility map
- global scene, style, light, and only active sound/text
- total duration and continuous, non-overlapping time ranges
- each shot's framing/camera, visible subjects and spatial relationship, current action phase, action/dialogue, camera's visible result, visual focus, ending state, and next handoff
- global locks and only evidence-backed targeted exclusions

When a cut continues the same event, inherit the current phase, contact point, direction, and active effect state; advance the event instead of restarting it.

## 5. Render the final prompt

### New and reference generation

Use the same formula for 5-second, 15-second, 30-second, and ultra-long generation. Duration changes the number and density of timeline segments, not the structure.

```text
【素材职责】          仅在有素材时出现
[素材标签]：[具体用途]。

【全局设定】
[整体目标、场景、风格、人物关系、贯穿镜头原则和 active sound/text]

【时间轴分镜】
镜头1（0–5秒）：[景别与机位]；[主体当前状态与空间关系]；[动作、表演与台词]；[主要运镜产生的可见结果]；[必要的画面重心]；[结束状态或下一镜承接点]。

【全局锁定】          仅在存在跨镜硬锁或必要禁止项时出现
[贯穿全片且未在上文充分表达的锁定内容]
```

Rules:

- Time ranges must start at zero, remain continuous without gaps or overlaps, and end exactly at the requested duration.
- Use the fixed field order above. Omit a non-material field instead of filling it with decorative prose.
- Treat `画面重心` as the rendered form of internal viewer priority; do not create a second explanation of the same idea.
- For a main camera movement, pair the term with its visible result. A self-explanatory fixed camera or shot size needs no redundant explanation.
- Keep character appearance and material roles global. Repeat in a shot only a visible change or a continuity-critical state.
- Do not repeat material labels in the timeline after the responsibility map unless the user supplies an exact time-scoped handle requirement.
- Put all necessary negative instructions in `【全局锁定】` once; never scatter a generic negative list across shots.

For Seedance-family dialogue use `{台词}`; use `<音效>`、`（音乐）`、`【字幕】` only when active. Read `references/seedance-2-rules.md` for the complete adapter.

### Edit, extension, and bridge

Do not force operational commands into the generation formula. Use their own compact stable formulas from `references/seedance-2-video-operations.md`:

- edit: target + change + interval + preservation boundary
- extension: source + direction + inherited boundary + new timeline + ending
- bridge: predecessor + visible transition + successor boundary

### Platform-neutral

Preserve the same MotionSpec and requested structure, but omit Seedance handles, markers, capability claims, and operation grammar.

## 6. Expression and language

Preserve a mature prompt when its production meaning is already complete. Otherwise translate emotional intent into visible body/contact, gaze, breath/pause, expression, distance, object handling, light, or sound response. Do not add flashbacks, symbols, people, or plot events merely to display emotion.

Use complete natural Chinese sentences inside the stable structure. Remove repeated boosters, background explanations that cannot be seen, and different wordings of the same lock. `结构固定` does not mean `每个字段必须写满`.

## 7. Validate and deliver

Check in this order:

1. exact dialogue, text, duration, interval, shot order, and literal-handle preservation
2. every supplied material accounted for and bound once with a specific responsibility
3. unified formula used for every known-duration new/reference generation
4. timeline starts at zero, has no gap/overlap, and ends at total duration
5. framing, visible roster, spatial relationship, action phase, endpoint, and handoff continuity
6. correct task grammar for edit, extension, bridge, or platform-neutral output
7. no duplicate global setting, material binding, visual-priority explanation, negative rule, or appearance description
8. no unsupported invention or reference leakage
9. `agents/openai.yaml`, reference routing, and regression cases remain consistent with this file after maintenance

If a check fails, repair only the failed field and run the checks again. Default delivery is at most one useful judgment or risk sentence followed by one Chinese final prompt in one fenced code block.

## Stop conditions

Ask one grouped question and wait only when:

- a required asset or boundary state is missing
- a final Seedance 2.5 new/reference prompt lacks total duration
- required exact dialogue, narration, or visible text is missing
- hard locks conflict
- two well-supported creative readings would materially change the result

## Avoid

- Do not invent `@` handles from upload order.
- Do not keep both timestamped and non-timestamped generation defaults.
- Do not use `定义为` as routine boilerplate.
- Do not repeat material responsibilities inside every shot.
- Do not write the same camera, appearance, visual priority, or prohibition globally and per shot.
- Do not expose EvidenceLedger, ReferenceMap, LockLedger, or MotionSpec names in the final prompt.
- Do not narrate previous failures, revisions, tests, or debugging intent inside the current executable prompt.
