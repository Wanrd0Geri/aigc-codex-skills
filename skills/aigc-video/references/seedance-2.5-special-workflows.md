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

Reuse the canonical ordered generation structure and optional-heading rules from `seedance-2-rules.md`. Ultra-long mode changes timeline density and continuity load, not the formula.

- Do not infer duration or aspect ratio. Express total duration through the final time range; keep aspect ratio in the UI unless the user requires it in the prompt.
- Apply the adapter's canonical timeline rules without creating an ultra-long variant.
- Divide by story or action beats, not equal mathematical chunks.
- Re-state only genuine cross-segment locks globally. Do not copy the full character appearance into every segment.
- If action density is too high, simplify mutable camera/detail before deleting locked beats.

## White-model workflows

### Coarse white model

Use when layout, blocking, shot order, and camera path matter more than detailed geometry. Render one natural unheaded reference sentence before `主体：`. Name only what is actually borrowed, such as movement, blocking, camera, or cuts; include light only when the user explicitly assigns it.

```text
参考视频1的人物动作、站位、移动路线、运镜和切镜。

主体：
视频1中的黄色粗模对应图片1中的苏云，蓝色粗模对应图片2中的罗大娘。

场景：
参考图片3中的竹林山路。
```

Put color/shape-to-character or prop correspondence at the start of `主体：`. Use a supplied scene reference in `场景：`, or write the requested scene directly from text. When neither exists, do not discuss the coarse model's missing scene or pre-emptively list viewport elements to exclude.

When final character images are assigned only to identity, appearance, wardrobe, or prop, do not inherit their presentation pose. Keep action, blocking, and performance owned by the coarse model, storyboard, or current user instruction. Borrow pose or action from a character image only when that dimension is explicitly authorized.

Inherit the source video's duration, shot order, and cuts. Do not ask for or separately write total duration. Reuse exact shot ranges only when they are readable. When cut ranges are unreadable, preserve the source order and cuts and write ordered `镜头N：` entries without time ranges; never invent seconds. If the model has articulated limbs, wings, or a tail, describe the complete action process through preparation, movement, contact, and endpoint instead of naming only the result.

If a detailed white-model animation is supplied in the future, require planning overlays to be cleaned before use, then follow the provider's basic instruction to render the white-model animation into the final finished video. Do not create prompt-side exclusions for tracks, axes, camera cones, labels, or controls.

## Green screen

Assign the green-screen source to subject motion, timing, or performance only. Assign the replacement environment separately.

```text
主体：
视频1：主体表演、动作节奏和身体轮廓。

场景：
图片1：替换后的场景、光线方向与环境色。
```

State the visible integration result: matched contact shadow, edge light, perspective, and ground relationship when those are material. Do not repeat a generic `去绿` instruction in every shot.

## Multi-panel storyboard

Treat the sheet as structured shot evidence, not a generic style image:

```text
图片1：按分格顺序提供镜头顺序、景别、构图、人物站位、动作节点与遮挡关系。
```

- Preserve the supplied panel order and count unless the user asks to restructure it.
- Translate each panel through the adapter's canonical timeline without changing panel order.
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
