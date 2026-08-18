# Seedance 2.5 Video Operations

Load only for strict editing, extension, or seamless transition. Keep these operational commands separate from the new-generation timeline formula.

Use plain upload-order labels such as `视频1`, `图片1`, and `音频1` by default. Keep supplied handles or UUIDs only in the internal mapping; render one literally only when the current user explicitly requests it for the current output.

## Structure and delivery

- A strict edit that preserves framing, camera side, visible roster, position, depth, facing, route, occlusion, crop, dialogue ownership, and endpoint inherits confirmed structure. If any of those fields changes, reopen only the affected interval and wait for its structure confirmation.
- An extension creates a new visible segment. Inherit the readable source opening/ending boundary, but confirm the added segment's own structure before writing the command.
- A bridge creates a new transition. Inherit both source boundaries, but confirm the transition's structure before writing the command.
- After confirmation, return one complete operation command. Never return only the changed phrase, interval field, or preservation sentence.

Use `change-impact-and-delivery.md` when modifying or repairing an existing command.

## Strict edit

Use one stable formula:

```text
[目标视频] + [对象与具体变化] + [作用时间] + [保留边界]
```

Example:

```text
严格编辑视频1：3–7秒将角色右手的黑色雨伞改为透明长柄伞；人物身份、表演、身体动作、镜头运动、场景光线和原有声音保持不变。
```

- add: name the new element, interval when needed, frame position, relation, and visible action
- modify: name the original object or attribute and the replacement result
- remove: name what disappears, the fill/reveal result, and the smallest preservation boundary
- preserve only fields that the edit could disturb; do not append a full global-lock inventory
- when marked regions actually exist, use the local-annotation rules in `seedance-2.5-special-workflows.md`

Unmentioned content should remain unchanged, but write an explicit preservation boundary for high-cost identity, action, camera, audio, or composition fields that the requested edit could plausibly disturb.

## Extension

Use one stable formula:

```text
[源视频] + [向前/向后] + [继承的接缝状态] + [新增时间轴] + [新增终点]
```

Examples:

```text
向后延长视频1：承接原视频结尾人物仍向左奔跑、右脚刚落地、镜头平行跟随的状态。新增0–5秒……；结尾停在……。
```

```text
向前延长视频1：新增片段的结尾收束到原视频开头的人物位置、朝向、动作阶段、光线和机位关系，再无缝接入原视频。
```

- append-after inherits the source ending BoundaryState
- prepend-before creates a predecessor whose ending converges on the source opening; never use the source ending as the prepend boundary
- the original source segment is not regenerated; describe only required, unreadable seam facts
- use a continuous one-take extension for the same action, dialogue, emotion, or movement path
- use a cut-based extension when the new material changes scene, time, major action phase, or narrative viewpoint
- repeated extension can degrade identity and image quality; mention this only when the plan actually uses repeated passes
- the added segment's confirmed structure owns its framing, roster, route, action/dialogue, and endpoint; performance and world response are enriched only afterward

Follow the current duration rules in `seedance-capability-matrix.md`.

## Seamless transition / bridge

The official 2.5 workflow is a two-video boundary task:

```text
[前序视频] + [可见过渡过程] + [后序视频]
```

Example:

```text
视频1结尾的镜头继续向前穿过门框，门框贴近镜头形成短暂暗场；暗场内保持同一向前速度和方向，逐渐显出视频2开头的街道透视与晨光，接入视频2时人物位置、镜头高度和运动方向一致。
```

Start from video 1's ending state and converge on video 2's opening state. Carry only the needed subject motion, camera motion, light, material, shape, or source-backed sound. A transition must be visible and causal; avoid a bare `自然过渡`.

Before rendering this formula, confirm the transition's own camera/framing, visible roster, spatial path, action, and terminal convergence. Do not treat two readable source boundaries as confirmation of the unseen bridge between them.

Do not infer that the general ten-video input allowance means one bridge accepts ten endpoints. If the user wants a chain of three or more source videos, plan separate pairwise bridges or verify the current interface first.

## Combined intent

When one asset supplies a reference dimension and another is the operational target, keep both roles explicit:

```text
图片1：新服装的颜色、剪裁与材质。
严格编辑视频1：2–8秒将角色服装替换为图片1中的服装；人物身份、动作、运镜、场景与声音保持不变。
```

The image is a reference input with named dimensions. The video is the edit target, not a style reference.
