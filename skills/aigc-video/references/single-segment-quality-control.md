# Single Segment Quality Control

Use this reference for complex subjects, blocking, occlusion, overloaded action, or continuity-sensitive Seedance prompts. A long-form sequence only works if each segment can generate clearly on its own.

## Contents

1. Quality order and complexity downgrade
2. Duration budget and positive staging
3. Final check and failure checklist
4. Minimal example

## Quality Order

Check the segment in this order:

1. Subject: the main subject has stable identity anchors.
2. Action: each shot has one main visible action.
3. Space: left/right, near/far, foreground/background, and key object positions are clear.
4. Camera: each shot has one shot size, one angle, and at most one main camera movement.
5. Emotion carrier: emotion is shown through gaze, pause, breath, hand movement, posture, light, or sound.
6. Readability: each shot has a clear visible action or state change when the action would otherwise be ambiguous.
7. Handoff: if this is part of a longer sequence, preserve only the posture, gaze, object position, movement direction, light state, or camera position the next segment must inherit.

If one of these is missing, fix it before adding style, atmosphere, or continuity details.

## Complexity Downgrade

When the requested shot includes multiple people, large action, occlusion, complex position changes, similar-looking subjects, or compound camera movement, simplify only mutable execution fields:

- Propose splitting the action into more than one shot when structure is not locked; obtain approval before changing a locked shot plan.
- Use fixed camera or one simple camera movement.
- Reduce the number of active subjects only when they are not locked; otherwise make their roles and positions clearer and flag the stability risk.
- Keep the main subject's size and screen position stable.
- Give each important subject a position or prop anchor.
- Make the action readable before starting the next action; use an endpoint only when overlapping actions would confuse the model.

## Duration Budget

Before drafting, back-calculate how many readable beats the requested duration can hold. Do not compress too many actions into a short segment.

Rough timing:

- one readable action beat: about 2-3 seconds
- one camera movement plus one action: about 3-4 seconds
- one expression or attention transition: about 1-2 seconds on its own
- one object interaction with contact and reaction: about 2-3 seconds
- one multi-character handoff or chase beat: about 3-5 seconds

If the requested duration cannot hold all beats, simplify mutable camera and description first, then recommend extending or splitting. Never delete, merge, or reorder locked actions, subjects, dialogue, or shots without approval. Preserve the visible start state, main action, and necessary continuity anchor instead of squeezing several beats into one unreadable shot.

Use this timing only as an internal feasibility budget. State total duration once in the final prompt, but do not assign exact seconds to every generated shot by default. The official guide warns that precise time ranges are unstable; keep exact ranges for targeted source-video edits or an explicit timing-critical request.

## Positive Visible Staging

Describe only the minimum visible staging needed to preserve a user/source lock or make the main action readable before considering any negative warning list:

- `主角从画面左侧前景走到中央。`
- `固定机位从正面拍摄，人物在画面内完成转身。`
- `前景角色停在桌边，背景角色抬头看向门口。`
- `UFO缓慢下降，光束落在主人公前方地面。`

Add exact step counts, unchanged orientation, fixed subject scale, or precise effect paths only when the current user, active source, continuity, or an observed failure makes them necessary.

## Final Check

Before returning the final prompt, silently scan against the failure checklist below. In addition, verify these segment-level points:

- Each shot has one main action and one main camera movement.
- The duration can realistically hold the number of action, camera, expression, and handoff beats.
- Generated shots use event order rather than exact per-shot timestamps unless the task is a targeted edit or explicitly timing-critical.
- Reference generation uses `参考`; video editing and extension address the source video directly without `参考`.
- The final shot includes a continuity anchor only when a next segment depends on posture, gaze, object position, movement direction, light state, or camera position.
- Subject identity anchors are stable (clothing, silhouette, prop, or position) for every important subject.
- Spatial relationships (left/right, foreground/background, near/far) are stated where they affect the action.
- Every reference contributes only its assigned attributes; no color, material, text, identity, lighting, style, or composition has leaked from an unrelated role.
- Global camera, focal-length, framing, foreground-ratio, subject-position, and composition locks agree with every per-shot label.
- Every style or medium explicitly named by the user is preserved and translated into visible production choices.
- The user's initiating action remains visible; `回到/进入/抵达/打开/离开/发现/转向` is not silently converted into an already-completed starting state.
- Internal `forbidden/unassigned` reference fields have not been copied into the prompt; multi-reference anchors are summarized once before the shots unless a role changes.
- Every negative or restrictive sentence passes the admission test: user/source lock, platform requirement, direct active-reference conflict, or observed generation failure.
- Deleting any remaining restriction would change identity, material space, locked action order, exact dialogue, or the required ending; otherwise delete it.
- Secondary particles, cloth/hair motion, effect micro-detail, and connective physics remain open unless they are source-locked or central to the requested result.

If anything is missing, fix it before adding style or atmosphere details.

## Failure Checklist

These are the failure modes most likely to break a Seedance prompt. Use this extended scan for complex, reference-heavy, or unstable drafts:

- **Parameter-list writing style** — e.g. `镜头1：中景，固定机位，主角站在画面中央，背景是雨夜，主角抬头，雨水打湿肩膀`. Comma-chained slots without verbs break the script-like read Seedance handles best. Rewrite as flowing sentences with verbs and connectives, ending the structured lead-in with a period: `镜头1：中景。固定机位从正面拍摄，主角站在画面中央，身后是雨夜的街口。他抬起头，雨水打湿了他的肩膀。`
- **Exact timing on every generated shot** — e.g. `镜头1：0-3秒`、`镜头2：3-6秒`. Keep total duration and shot order, then express timing as action sequence by default. Preserve exact time ranges for targeted edits and for a user-explicit timing-critical request.
- **Writing aspect ratio, resolution, or frame rate inside the prompt** — these belong in the platform UI, not the prompt body. Only include if the user explicitly asks.
- **Bare reference labels** — e.g. `参考@图1`. In the reference summary, always attach a semantic role: `参考@图1的白衣少年外观`.
- **Unscoped reference intent** — e.g. `参考 @视频1`. State whether the reference serves as camera movement, action, edit rhythm, effect behavior, sound, or character performance reference.
- **Edit or extension miswritten as reference generation** — do not write `参考@视频1` when changing or continuing that clip. Use `严格编辑@视频1`、`向后延长@视频1` or `生成@视频1之后的内容`.
- **Environment reference overriding shot design** — keep camera, framing, and starting image sourced independently from an environment-only reference. State an override in the final prompt only when active references directly conflict or an observed result copied the wrong composition.
- **Reference-role leakage** — a silhouette-only asset cannot supply material, color, text, brand, lighting, identity, or function. Enforce that whitelist internally; do not turn every unavailable attribute into a visible exclusion list.
- **Effect/entity type confusion** — if an energy, smoke, light, shadow, or liquid effect becomes a physical person or object, keep its assigned silhouette, scale, position, and action while using one sufficient positive description of its source-supported non-solid material and attachment. If that resolves the type, omit synonymous negative restatements. Do not add flatness, runes, geometric substructure, anatomy, or a new emitter to distinguish it.
- **Global composition drift** — fixed long lens, fixed camera, fixed foreground percentage, fixed subject position, or locked framing must remain consistent across shot labels and descriptions. Do not change shot size merely to create variety.
- **Compound camera movement in one shot** — e.g. mixing push, pan, and tracking-like following in a single shot. Pick one main movement; if multiple are needed, split into multiple shots.
- **Conflicting camera or edit instructions** — e.g. requesting `固定机位` and `环绕镜头` in the same shot, or `一镜到底` while also listing hard cuts. Resolve the priority before drafting.
- **Duration-complexity mismatch** — e.g. placing several locations, transformations, dialogue beats, and camera moves inside 4-5 seconds. Reduce actions, split shots, or extend the segment.
- **Unrequested subject inflation** — do not add background staff, crowds, bystanders, vehicles, animals, or decorative business just because the location could contain them. Keep only subjects and objects required by the user's action or continuity.
- **Inventing style labels not established by the user or references** — e.g. `三渲二`, `UE5风格`, `照片级写实`, `cel shading`, `cinematic`. If style is unspecified, write neutral execution quality only.
- **Deleting an explicit style because no style reference is attached** — a user-named medium or style is already established. Preserve it and translate it into material, silhouette, lighting, and motion behavior.
- **Negative tag lists** — e.g. `不要模糊，不要变形，不要失真`. First describe what is visible and desired: `主体清晰可辨，身体结构自然，动作物理合理`. Keep identity, subject-count, continuity, and reference-role controls inside the existing positive staging or reference map. Run this failure check silently; do not turn it into `生成注意` or a negative tail. Add one short warning sentence only for an explicit user/source prohibition, an observed generation failure, a direct active-reference conflict, or an unavoidable platform/safety issue that cannot be phrased as positive staging.
- **Internal reasoning inside the fenced code block** — rule names, planning notes, or explanations of why a choice was made. The code block contains only the executable prompt body.
- **Abstract taste words without a visible carrier** — e.g. `氛围感强烈`, `极具张力`. Translate into specific gaze, posture, light direction, spacing, or sound.
- **Flat performance labels** — e.g. `he looks sad` or `the fox acts funny`. Replace with body part, contact point, gaze path, expression transition, movement direction, and only the anchor needed for the next beat.
- **Audio drift** — include only user/source/project-supplied audio or spoken dialogue required for lip sync. The no-music/no-subtitle default prevents additions but does not require a literal policy sentence. When the user asks for no sound description, keep all optional audio wording out of later revisions.
- **Plot synopsis** — describing what happens before or after the clip, character backstory, or narrative arcs the camera cannot see. Stay inside what the camera frames during the segment duration.
- **Identifiable real people, celebrity likenesses, trademarked characters, or protected IP** — keep generic or ask the user for rights-safe handling.
- **Treating reference-image prompts like text-to-video prompts** — preserve literal `@...` anchors and give each a positive assigned role. In a multi-reference prompt, bind them once in a compact summary and use semantic names in the shots; state an override only for a direct conflict.
- **Overusing natural-language cleanup** — do not run a separate cleanup pass unless the user asks or the draft has visible language defects.

## Minimal Example

```text
本视频总时长 8 秒，两个镜头。夜晚开阔地，巨大的飞行器从云层下方缓慢下降，冷蓝色光束落向地面，画面重点是 UFO 的体量、地表被光束压低的空气感，以及主人公抬头仰望的反应。

参考图使用：
参考@图1的飞行器外形与材质，参考@图2的环境与地表空间，参考@图3的主人公外观。

镜头1：远景。低角度固定机位贴近开阔地面拍摄，地面位于前景，云层和UFO位于画面中央上方。远处云层被冷蓝色光线照亮，UFO从云层下方缓慢下降到画面中央，地面草叶被气流压低，少量尘土向外扩散，光束落点保持在画面中景范围内。

镜头2：中近景。机位来到主人公侧前方并缓慢推近，人物站在画面左侧前景，UFO光束落在画面右上方。他身体朝向天空中的UFO，衣摆被风向后带起，右手手指轻轻收紧。冷蓝色光线从上方照到他的脸侧，他缓慢抬头看向光束，最后停在仰望姿态，为下一段保留清楚的姿态接点。
```
