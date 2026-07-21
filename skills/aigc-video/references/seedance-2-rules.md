# Seedance 2.0 Core Prompt Rules

Use this file for every Seedance 2.0 / 2.0 Fast final prompt. Load `seedance-2-video-operations.md` additionally only for edit, extension, or bridge tasks. Load `failure-recovery.md` only when the user supplies an observed failed/unstable result, paired results, or another concrete prior-result error; never load it as a first-attempt checklist.

Source basis: [Volcengine, Doubao Seedance 2.0 系列提示词指南](https://www.volcengine.com/docs/82379/2222480?lang=zh), checked 2026-07-21 against the provider page updated 2026-07-20. Re-check version-specific limits when the provider or model changes.

## New and reference generation

Use `参考` only when borrowing a dimension for new generation:

- `参考@图1中的[主体/环境/效果]，生成……`
- `参考@视频1的[动作/运镜/风格/音效]，生成……`
- `参考@音频1中的[音色/说话节奏]，生成……`

Never use a bare `参考@视频1`; name the borrowed dimension.

## Prompt construction

Treat the provider's advanced formula as a selection checklist, not a template to fill. Follow the viewer-priority clause order in `SKILL.md`; do not interpret formula order as guaranteed numeric model weighting.

- State total duration once. For generated shots, use event order or `前段 / 中段 / 后段` rather than exact per-shot ranges by default.
- Keep one main camera movement per shot. Use standard terms such as `中景`、`特写`、`全景`、`缓慢推近`、`平稳横移` or `固定机位` only when useful.
- Express performance through one supported body/contact, gaze, pause/breath, expression, distance, object, light, or sound carrier.
- Leave particles, cloth/hair response, effect microphysics, and secondary decoration open unless locked or central.

## Reference-input binding

Apply this section only to anchors whose operational role is `reference_input`. Start-frame sources and end-frame targets use their boundary assignment; strict-edit targets, extension sources, and bridge inputs use the direct grammar in `seedance-2-video-operations.md`. None belongs in the ordinary reference summary unless the user explicitly assigns the same anchor a separate `reference_input` role.

Give every identity/appearance reference subject one semantic name. When the asset has one unambiguous subject, use:

`参考@图1中主体的[已授权身份/外貌属性]，并将其定义为[角色名]。`

When a readable asset or user/source description contains several possible subjects and the supplied names or visible labels do not already resolve selection, select the needed one with two or three supplied stable static traits:

`参考@图1中[两三个稳定静态特征]的[主体]的[已授权身份/外貌属性]，并将其定义为[角色名]。`

Either sentence is the explicit `identity`, `appearance`, or combined binding; replace the bracket with only the authorized attribute wording and do not add a second redundant identity-reference sentence. Keep the same semantic label thereafter. A supplied name or readable in-image label may resolve subject selection, but it is selection evidence rather than authorized visible text in the output. Define the visible subject, not the whole image, when the image also contains scenery or unrelated people. For `anchor_only`, use the user-assigned semantic label or subject name without inventing traits; if the intended subject remains ambiguous, ask for the missing visible state.

Borrow only the authorized dimension. A silhouette reference does not authorize color/material; identity does not authorize pose/composition; environment does not authorize camera, action trajectory, or mandatory landmark visibility.

When a group image and a dedicated subject image both contain the same person, resolve the overlap independently for every authorized field. Treat the user-named roster and semantic labels as user locks, not as identity or relationship borrowed from the group image. A group input may still own one named-subject field such as wardrobe while a dedicated input owns another such as face/appearance; never route all fields merely by subject or asset type. In the rendered reference summary, bind each overlapping field only to its final owning anchor—do not first bind it to one image and then write an override chain. Do not inherit contact-sheet layout, text labels, display poses, white background, group composition, or blocking unless the user separately authorizes those dimensions.

Bind non-identity references by the exact atomic dimensions they are allowed to supply. Slash-separated items below are alternatives to select explicitly, not package authorization:

- environment: `以@图2作为[场景环境/空间布局/光影色调]参考。`
- wardrobe or prop: `参考@图3中的[服装/道具]，用于[角色名/可见用途]。`
- motion or camera: `参考@视频1的[动作/运镜/节奏]。`
- effect: `参考@视频2的[特效形态/生成轨迹/运动逻辑]。`
- audio: `参考@音频1中的[音色/说话节奏]。`
- text or graphic: `参考@图4中的[标识图形/字形/版式]，用于[可见文字或图形用途]。`

For multi-reference generation, place these bindings in one compact positive reference summary and normally mention each reference-input anchor once, then use semantic names in the shots. Consolidate multiple authorized dimensions from the same anchor into one binding when possible. Every binding phrase must name its borrowed dimension; the identity-definition sentence above satisfies this requirement by naming the selected identity and/or appearance attributes. Do not write a bare `以@图2作为参考` or `参考@视频1`. Repeat an anchor only when a later assignment materially changes its borrowed dimension, ambiguity remains, or task grammar requires it. Use only assets with a clear job; do not fill the input limit.

## Audio and visible text

Use official information markers when active:

- dialogue: `{台词}`
- sound effect: `<音效>`
- music: `（音乐）`
- subtitle: `【字幕】`

This workflow does not add optional audio, music, or subtitles by default. That is a production preference, not a Seedance capability limit, and does not require an `无配乐/无字幕` policy sentence.

For requested visible text, state exact content, timing when material, frame position, appearance method, and only necessary visual character. Preserve common legible characters and use a visual reference for exact logo/typography when possible.

## Final prompt shape

Return one executable prompt in one fenced code block. A simple new generation normally needs one setup sentence and one natural shot paragraph. A complex reference generation may add one compact reference map before its shots.

Keep aspect ratio, resolution, frame rate, and other UI/API settings outside the prompt unless the user explicitly asks to embed a value and the target surface has no separate control. Use positive visible staging first; admit one short negative only for an explicit lock, platform requirement, direct reference conflict, or observed failure that cannot be resolved positively.
