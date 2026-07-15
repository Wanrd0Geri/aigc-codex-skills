# Seedance 2.0 Core Prompt Rules

Use this file for every Seedance 2.0 / 2.0 Fast final prompt. Load `seedance-2-video-operations.md` additionally only for edit, extension, or bridge tasks, and `failure-recovery.md` only after an observed failure.

Source basis: [Volcengine, Doubao Seedance 2.0 系列提示词指南](https://www.volcengine.com/docs/82379/2222480?lang=zh), checked 2026-07-15. Re-check version-specific limits when the provider or model changes.

## New and reference generation

Use `参考` only when borrowing a dimension for new generation:

- `参考@图1中的[主体/环境/效果]，生成……`
- `参考@视频1的[动作/运镜/风格/音效]，生成……`
- `参考@音频1中的[音色/说话节奏]，生成……`

Never use a bare `参考@视频1`; name the borrowed dimension.

## Prompt construction

Treat the provider's advanced formula as a selection checklist, not a template to fill. Put the subject and action first, then only the space, atmosphere, camera, style, audio, text, or constraint that changes this clip.

- State total duration once. For generated shots, use event order or `前段 / 中段 / 后段` rather than exact per-shot ranges by default.
- Keep one main camera movement per shot. Use standard terms such as `中景`、`特写`、`全景`、`缓慢推近`、`平稳横移` or `固定机位` only when useful.
- Express performance through one supported body/contact, gaze, pause/breath, expression, distance, object, light, or sound carrier.
- Leave particles, cloth/hair response, effect microphysics, and secondary decoration open unless locked or central.

## Subjects and reference roles

When an asset contains several possible subjects, define the needed one with two or three stable static traits. Keep the same semantic label thereafter.

Preserve literal anchors such as `@图1`、`@视频1`、`@音频1` and filename anchors. Attach a narrow role immediately. A silhouette reference does not authorize color/material; identity does not authorize pose/composition; environment does not authorize camera, action trajectory, or mandatory landmark visibility.

For multi-reference generation, bind each anchor once in one compact positive reference summary, then use semantic names in the shots. Repeat an anchor only when its role changes, ambiguity remains, or task grammar requires it. Use only assets with a clear job; do not fill the input limit.

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
