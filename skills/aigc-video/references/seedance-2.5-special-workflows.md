# Seedance 2.5 Special Workflows

Load only for ultra-long generation, white-model workflows, green screen, multi-panel storyboards, voice reference, local annotations, viewpoint changes, or music removal.

## Contents

1. Ultra-long generation
2. White-model workflows
3. Green screen
4. Multi-panel storyboard
5. Voice and audio reference
6. Advanced local annotation
7. Viewpoint and camera editing
8. Background-music removal

## Ultra-long generation

Use the same generation formula as an ordinary 5–30 second prompt:

```text
【素材职责】
[only when materials exist]

【全局设定】
[scene, style, relationships, continuity principle, active audio/text, and explicitly supplied aspect ratio when it must be stated]

【时间轴分镜】
镜头1（0–N秒）：...

【全局锁定】
[only when needed]
```

- Do not infer duration or aspect ratio. Express total duration through the final time range; keep aspect ratio in the UI unless the user requires it in the prompt.
- Keep all ranges continuous and end exactly at total duration.
- Divide by story or action beats, not equal mathematical chunks.
- Re-state only genuine cross-segment locks globally. Do not copy the full character appearance into every segment.
- If action density is too high, simplify mutable camera/detail before deleting locked beats.

## White-model workflows

### Coarse white model

Use when layout, blocking, shot order, and camera path matter more than detailed geometry. The provider currently reports better overall usability for coarse white-model guidance than fine white-model guidance.

```text
【素材职责】
视频1：粗白模的人物动线、空间站位、动作节奏与运镜路径。
图片1：角色外貌与服装。
图片2：场景材质、光线与最终画面风格。
```

Then use the unified time-axis formula. Preserve the white model's layout and movement, while applying only the appearance/style dimensions assigned to the other assets.

### Fine white model

Use only when the source explicitly provides detailed limb poses or action paths worth following.

- Describe the complete limb sequence, contact points, directions, and endpoints that must survive rendering.
- Remove rig tracks, motion-path lines, camera cones, labels, and other planning overlays from the final image.
- Do not assume every fine-control marker will transfer reliably; mention the stability tradeoff when it matters.

```text
视频1：精细白模的完整肢体动作、接触点、运动方向和镜头路径；不继承轨迹线、辅助标记与相机锥体。
```

## Green screen

Assign the green-screen source to subject motion, timing, or performance only. Assign the replacement environment separately.

```text
视频1：主体表演、动作节奏和身体轮廓。
图片1：替换后的场景、光线方向与环境色。
```

State the visible integration result: matched contact shadow, edge light, perspective, and ground relationship when those are material. Do not repeat a generic `去绿` instruction in every shot.

## Multi-panel storyboard

Treat the sheet as structured shot evidence, not a generic style image:

```text
图片1：按分格顺序提供镜头顺序、景别、构图、人物站位、动作节点与遮挡关系。
```

- Preserve the supplied panel order and count unless the user asks to restructure it.
- Translate each panel into a continuous time range.
- Use separate assets for identity, style, or environment unless the storyboard is explicitly authoritative for those dimensions.

## Voice and audio reference

```text
音频1：角色A的音色、语速与说话节奏。
视频1：角色A的口型节奏与表演停顿。
```

Use only the dimensions the user assigns. Preserve exact dialogue separately; voice reference does not authorize rewriting the words. Keep the mouth visible and allow enough stable face time when lip sync matters.

## Advanced local annotation

Use advanced annotation syntax only when the interface or user actually supplies a marked region, path, or inside/outside relationship. Do not invent annotation identifiers.

```text
严格编辑视频1：在标注区域内将[原对象]改为[新对象]；标注区域外的主体、构图、动作、运镜、光线和声音保持不变。
```

For additions, state whether the element is inside, outside, attached to, following, or occluded by the marked region. For removals, name the fill result and the preservation boundary.

## Viewpoint and camera editing

Use the strict-edit formula. State the target view and the visible consequence, then preserve unrelated content:

```text
严格编辑视频1：0–6秒将机位调整为角色左后方跟拍，使角色保持画面右侧、前方道路逐步展开；人物动作、行进方向、场景光线和声音保持不变。
```

Do not combine `固定机位` with a tracking move. If the new view crosses the action axis, state the visible crossing or preserve screen direction explicitly.

## Background-music removal

Use a narrow audio edit:

```text
严格编辑视频1：移除全片背景音乐；保留人物对白、环境声和动作音效，画面内容与节奏不变。
```

Do not say `移除所有声音` unless that is the user's actual request. The provider's improved BGM control supports this targeted instruction; it does not justify a generic audio-negative list.
