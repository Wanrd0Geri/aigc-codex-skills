# Seedance 2.0 Prompt Rules

Use this file as the version-specific rulebook for Seedance 2.0 / 2.0 Fast prompts.

Source basis: [Volcengine, Doubao Seedance 2.0 系列提示词指南](https://www.volcengine.com/docs/82379/2222480?lang=zh), checked 2026-07-15. The official page reported an update time of 2026-06-08. Treat platform limits as current facts to re-check when the provider or model version changes.

## Contents

1. Task intent syntax
2. Prompt construction
3. Subject and reference binding
4. Audio and visible text
5. Editing, extension, and bridging
6. Stability and troubleshooting
7. Final prompt shape

## 1. Task Intent Syntax

Classify the task before describing the shot. Seedance uses the wording to distinguish a new generation that borrows a reference from an edit or extension of an existing clip.

### Multimodal Reference / New Generation

Use `参考` and name the exact dimension being borrowed:

- Image: `参考@图1中的[主体]，生成……`
- Video: `参考@视频1的[动作 / 运镜 / 风格 / 音效]，生成……`
- Audio: `参考@音频1中的音色，生成……`

Do not write a bare `参考@视频1`. State whether the source provides action, camera movement, effect behavior, rhythm, sound, style, or another specific layer.

### Video Editing

Address the source directly; do not introduce it with `参考`:

- Add: describe the new element, appearance time, and frame position.
- Modify: `严格编辑@视频1，将[原特征]修改为[新特征]。`
- Delete: name the deleted element and briefly state what remains unchanged.

Unmentioned parts of an edit remain unchanged by default. Add continuity requirements only where the edit could disturb identity, camera movement, lighting, action rhythm, sound, or background geometry.

### Video Extension

Address the source directly; do not write `参考@视频1`:

- `向后延长@视频1，生成……`
- `向前延长@视频1，生成……`
- `生成@视频1之后的内容，……`

### Shot Bridge / Track Completion

Write the sources in order and describe the visible bridge:

`@视频1，[过渡画面与动作]，接@视频2。`

The official guide states that track completion accepts at most three input videos whose combined duration is no more than 15 seconds. Re-check this limit for another provider or a later model version.

### Combined Task

When one asset is a reference and another is the edit target, keep both intents explicit:

`参考@图1的[参考维度]，严格编辑@视频1，[具体编辑内容]。`

## 2. Prompt Construction

Use the official advanced formula as a selection checklist, not a requirement to pad every prompt:

`精准主体 + 动作细节 + 场景环境 + 光影色调 + 镜头运镜 + 视觉风格 + 画质 + 约束条件`

Keep only fields that change generation behavior. Put the subject and action first, then space and atmosphere, then how the camera records them.

### Shot Sequence

- For a complex clip, use `镜头1`、`镜头2`、`镜头3` in event order.
- State the total requested duration once. Do not allocate exact seconds to every generated shot by default.
- The official guide says precise time instructions such as `0-3秒` are unstable and may produce abnormal results. Use action order, shot order, or `前段 / 中段 / 后段` instead.
- Exact time ranges remain appropriate for a targeted edit to an existing video. Use a precise generated-event timestamp only when the user explicitly prioritizes it, and note the drift risk briefly outside the prompt.
- Inside each shot, order the useful controls as: camera or cut -> subject action and expression -> position or spatial change -> audio.
- Use at most one main camera movement per shot. Standard terms such as `中景`、`特写`、`全景`、`缓慢推近`、`平稳横移` and `固定机位` are sufficient.

### Action and Emotion

- Name the active body part and the motion's amplitude, speed, or force when useful: `缓慢抬手`、`快速转头`、`用力蹬地`、`微微低头`.
- Prefer small, continuous actions when they can express the idea; large explosive movement raises failure risk.
- State the physical handoff between actions: `借着转身惯性顺势抬手`.
- Externalize emotion through posture, gaze, breath, facial tension, or object handling instead of writing only `悲伤`、`紧张` or `愤怒`.

## 3. Subject And Reference Binding

### Define Subjects

When an asset contains multiple possible subjects, define the needed one with two or three stable static traits:

`将@图1中穿红色连衣裙、戴草帽的女人定义为张红。`

After defining a subject, use the same label every time. In a simple unregistered case, bind the subject to its asset each time, such as `张三@图1`.

Do not use an Asset ID as the subject name. Asset IDs do not replace `@图N` or `@视频N`; build a semantic bridge from the asset anchor to its visual role.

### Assign Reference Roles

Preserve literal anchors such as `@图1`、`@视频1`、`@音频1` and `@文件名.png`. If the user writes `图1` or `参考图1` and the mapping is clear, normalize it to the platform anchor.

Attach a semantic role immediately:

- `@图1（人物面部参考）`
- `@图2（服装与全身体态参考）`
- `@视频1（运镜与动作节奏参考）`
- `@音频1（音色与说话节奏参考）`

Treat every role as an attribute whitelist. A silhouette reference does not authorize color or material; an identity reference does not authorize pose or composition; an environment reference does not authorize camera placement.

Place the most important precision reference early in the prompt. For character identity, prefer one clean face close-up plus one full-body image. Avoid multi-view or three-view sheets: the official troubleshooting guide warns that they can increase identity drift or duplicate characters.

Use only the assets that have a clear job. The official guide recommends a typical total of four to five assets: one or two character images, one scene image, one camera-reference video, and one audio reference. Do not fill the input limit; excess sources create priority conflicts.

## 4. Audio And Visible Text

Use the official information markers:

- Music: `（背景中播放着快节奏的摇滚乐）`
- Sound effect: `<远处传来狗叫声>`
- Dialogue: `{你好，世界}`
- Subtitle: `【第一章：启程】`

Keep dialogue in one language except for proper nouns. For a non-Chinese/non-English line, name the language before the braces, for example `用日语说道{こんにちは}`.

This production workflow defaults to `无配乐，无字幕。`; it is a delivery policy, not a Seedance capability limit. Dialogue, room tone, environment sound, and action sound remain allowed. Use music or subtitle markers only when the user explicitly overrides the policy.

Seedance 2.0 can generate common visible text. When the user explicitly requests it, write: content + appearance timing + frame position + appearance method + color/style if needed. Prefer common characters and avoid rare characters or special symbols. For subtitles, state that the bottom subtitle follows the spoken rhythm. For logos or exact typography, use a dedicated visual reference when possible.

## 5. Editing, Extension, And Bridging

### Editing

For a targeted edit, specify the source, time range when needed, frame position, exact change, and only the continuity layers at risk:

`在@视频1的3-7秒画面左下角增加一只缓慢走过的黑猫，人物动作、机位、光线和原有环境声保持不变。`

### Extension

Continue from the source ending posture, movement direction, light state, narrative state, audio character, and camera momentum. The official guide says Seedance automatically takes the needed connection portion from the input; the original source segment is not regenerated.

Use extension for a continuous scene, long dialogue, emotional progression, or a single movement path. Prefer separate generation and editing for a scene change, action turn, chase, fight, or montage.

Repeated extension can accumulate quality loss, especially on faces. Limit repeated continuations and prefer a clean high-quality source or image reference when possible.

### Bridge

Write the visible transition rather than `接下一段`. Describe how subject motion, camera motion, material, light, shape, or sound carries from one source into the next.

## 6. Stability And Troubleshooting

- **Identity drift**: use a clean face close-up plus a full-body reference, define the face and styling roles separately, and place the face reference early.
- **Duplicate / twin characters**: define each character and its source clearly; prefer one person per reference image and avoid multi-view sheets. If strict uniqueness is essential, add one concise global constraint after positive staging.
- **More than four referenced people**: expect lower stability. Group characters into images with no more than four people per group, then use those grouped images for video generation.
- **Style drift**: state the target style explicitly. For stronger control, first convert source images to the target style.
- **Unexpected subtitles, logos, or watermarks**: use short constraints such as `保持无字幕`、`不要生成Logo`、`不要生成水印`; remove unnecessary source text before generation when possible.
- **Specific effect logic**: provide a reference video for the effect's shape and motion instead of relying on abstract prose.
- **Voice mismatch**: pair the audio anchor with a concise voice description and keep the requested line's tone close to the source audio.
- **Prompt overload**: do not paste a full screenplay. Keep only the subject, visible action, shot order, camera, audio, and constraints that affect this clip.

## 7. Final Prompt Shape

Put one executable prompt in one fenced code block. Keep explanations outside it.

Simple new generation:

```text
本视频总时长 X 秒，单镜头。整体场景、主体、核心动作与视觉重点。无配乐，无字幕。

镜头1：景别。用自然中文写清机位或一种运镜、主体动作、空间关系、表演与必要声音。
```

Complex reference generation may add a short subject/reference map before the shots. A targeted edit starts directly with `严格编辑@视频N` or `在@视频N的[区间]……`; an extension starts with `向前 / 向后延长@视频N` or `生成@视频N之后的内容`.

Keep aspect ratio, resolution, frame rate, and other platform settings out of the prompt unless the user explicitly asks to include them. Use positive visible staging first; add at most one short negative sentence for visible text/logo/watermark, a safety issue, or a strict uniqueness constraint that cannot be expressed positively.
