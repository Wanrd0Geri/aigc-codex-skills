# Seedance 2.5 Prompt Adapter

Use this file for every default Seedance-family final prompt. Default to 即梦 Seedance 2.5. Use the legacy note at the end only when the user explicitly selects Seedance 2.0 or 2.0 Fast.

Source basis:

- [【即梦】Seedance 2.5 使用手册](https://bytedance.larkoffice.com/wiki/RXh5ww6EqighMdkVTMccm2d4n7e), document updated 2026-07-31 and checked 2026-08-02.
- [Volcengine, Doubao Seedance 2.0 系列提示词指南](https://www.volcengine.com/docs/82379/2222480?lang=zh), checked 2026-07-21.

Re-check version-specific limits after a provider update. Read `seedance-capability-matrix.md` for dated limits and recommendations.

## Material responsibilities

The official 2.5 formula is `素材编号（按上传顺序） + 具体用途`. Render it as a compact colon map.

When the user or platform supplies a literal handle, preserve it exactly:

```text
@c6e53a11-75de-416e-ace9-3f96093fab0c：罗大娘的外貌与服装。
```

When only upload order exists, do not invent an `@` handle:

```text
图片1：罗大娘的外貌与服装。
图片2：苏云的外貌、服装与竹背篓。
图片3：仅补充苏云的浅白色瞳孔。
视频1：动作节奏、人物动线和镜头移动。
音频1：说话音色与语速。
```

- Give every material a specific job: identity/appearance, wardrobe, prop, environment, layout, light, material, action, motion, camera, timing, effect, audio, voice, text, or graphic.
- Consolidate all authorized jobs from the same material into one line.
- Bind materials once, then use semantic names in the timeline.
- Use `作为[角色名]` only when selecting one subject among several or combining several sources for one character. Do not add routine `定义为` wording.
- A storyboard or multi-panel sheet must name its authorized dimensions such as shot order, framing, blocking, screen direction, and occlusion. Do not treat it as a generic style reference.
- If one material applies only to a time interval, write that interval in the responsibility line.

## Unified generation structure

Use the same structure for every known-duration Seedance 2.5 new/reference generation:

```text
【素材职责】
[only when materials exist]

【全局设定】
[overall goal, scene, style, relationships, global camera principle, and active sound/text]

【时间轴分镜】
镜头1（0–5秒）：[framing/camera]；[current visible state and space]；[action/performance/dialogue]；[camera's visible result]；[visual focus when needed]；[ending or handoff].

【全局锁定】
[only when cross-shot locks or necessary targeted exclusions exist]
```

Do not open with `生成一段N秒的……`. Duration belongs in the time ranges and remains an exact production fact.

## Timeline rules

- Use `镜头N（开始–结束秒）：` for 5-second, 15-second, 30-second, and ultra-long outputs alike.
- Start at 0, use continuous non-overlapping ranges, and end exactly at total duration.
- Use decimals only when sub-second control is materially required.
- Use frame ranges only for frame-accurate sync, and state the active frame rate and total frame count.
- Keep one readable beat and one main camera strategy per shot. A short cut may carry an instantaneous state or action phase.
- When a cut continues one event, state the inherited phase and advance it. Do not repeat approach, wind-up, launch, contact, or another completed onset.
- For previsualization, use the same timeline formula once total duration is known; establish the selected representative state at cut-in.

## Shot sentence order

Use this stable order:

1. shot size, angle, and camera mode
2. subject's current visible state and material spatial relationship
3. action, performance, dialogue, and causal response
4. main camera movement and the visible result it creates
5. visual focus only when several visible elements compete
6. ending state or next-shot handoff

Omit an irrelevant field instead of inserting filler. A self-explanatory `固定机位` needs no restatement; a push, pan, crane, rack focus, orbit, or track should state what becomes larger, smaller, revealed, hidden, sharp, or repositioned.

## Audio and visible text

Use official information markers only when active:

- dialogue: `{台词}`
- sound effect: `<音效>`
- music: `（音乐）`
- subtitle: `【字幕】`

Preserve exact dialogue and speaker ownership. Keep the mouth visible when lip sync matters. Do not write an `无音乐、无字幕` policy sentence merely to state a default; put a targeted instruction in `【全局锁定】` only when the user/source requires it or a real result failed.

For visible text, state exact content, timing, frame position, appearance method, and only necessary style. Use a dedicated material responsibility for exact logo, typography, or layout.

## Control and repetition

- Put appearance, environment, and material jobs in the global sections once.
- Put per-shot visibility, blocking, occlusion, action phase, dialogue, and ending in the timeline.
- Treat internal viewer priority and rendered `画面重心` as one field.
- Put necessary negative instructions in `【全局锁定】` once.
- Do not repeat a material label, global scene description, character appearance, camera rule, or negative instruction in every shot.
- A longer prompt is acceptable when it adds distinct executable information. Different wording of the same fact is redundancy, not stronger control.

## UI parameters

Keep resolution, frame rate, and aspect-ratio settings outside the prompt when the UI exposes them. If the user requires an aspect ratio inside an ultra-long prompt, place it in `【全局设定】` without adding a duration-specific section. Never infer it.

## Seedance 2.0 legacy note

When the user explicitly selects 2.0 or 2.0 Fast:

- keep the same protected facts and material-responsibility map
- preserve user-supplied timing, but do not promise 2.5-level second accuracy
- apply the 2.0 limits from `seedance-capability-matrix.md`
- do not expose 2.5-only modes such as ultra-long generation or advanced editing as available
