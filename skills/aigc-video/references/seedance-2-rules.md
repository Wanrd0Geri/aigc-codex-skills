# Seedance 2.5 Prompt Adapter

Use this file for every default Seedance-family final prompt. Default to 即梦 Seedance 2.5. Use the legacy note at the end only when the user explicitly selects Seedance 2.0 or 2.0 Fast.

Source basis:

- [【即梦】Seedance 2.5 使用手册](https://bytedance.larkoffice.com/wiki/RXh5ww6EqighMdkVTMccm2d4n7e), document updated 2026-07-31 and checked 2026-08-02.
- Reusable observations from a user-supplied 即梦官网提示词优化助手 output, recorded in `seedance-2.5-optimizer-example.md` on 2026-08-03. They support plain colon headings, integer timestamp ranges, ordinary quotation marks for dialogue, and inline environmental/action sound. Treat them as one observed optimizer pattern, not universal mandatory grammar.
- [Volcengine, Doubao Seedance 2.0 系列提示词指南](https://www.volcengine.com/docs/82379/2222480?lang=zh), checked 2026-07-21.

Re-check version-specific limits after a provider update. Read `seedance-capability-matrix.md` for dated limits and recommendations.

## Material responsibilities

Use `素材编号（按上传顺序） + 具体用途`. Build this map internally. For Seedance new/reference generation, never render a generic `参考素材：` block: put subject-reference materials in `主体：`, scene-reference materials together with the environment in `场景：`, look/style references in `风格：`, and motion, camera, storyboard, audio, text, or time-scoped roles in their owning `情节` shot or active audio/text sentence. `主体：` is required whenever any character, animal, product, vehicle, or key prop appears anywhere in the clip. Omit it only for a clip that remains a pure environment or empty shot from beginning to end.

For one coarse white-model video that governs the whole clip, place one natural unheaded reference sentence before `主体：` and name only the dimensions actually borrowed. Put subject/prop correspondence in `主体：`; put an actual supplied or described environment in `场景：`; do not mention an absent scene, light, material, guide, or other unborrowed dimension merely to exclude it.

Default final labels are plain upload-order labels. Treat a supplied `@` handle, UUID, or filename as internal mapping evidence and normalize it to `图片1`、`视频1` or `音频1`. Preserve a literal handle only when the current user explicitly requests it for the current output. If upload order is unknown and the map matters, ask instead of guessing.

```text
主体：
图片1：罗大娘的外貌与服装。
图片2：苏云的外貌、服装与竹背篓。
图片3：仅补充苏云的浅白色瞳孔。

场景：
图片4：竹林山路的地形、晨雾与侧逆光。
```

- Give every material a specific job: identity/appearance, wardrobe, prop, environment, layout, light, material, action, motion, camera, timing, effect, audio, voice, text, or graphic.
- Consolidate all authorized jobs from the same material into one line.
- Bind materials once, then use semantic names in the timeline.
- For Seedance new/reference generation, never render a generic `参考素材：` heading. `主体：` owns every visible character, animal, product, vehicle, or key prop, including explicit identity, appearance, wardrobe, material, and prop references. Render it even when the opening frame is empty but a subject enters later. In the exceptional text-only case, use the available stable source-backed description and do not invent missing appearance. `场景：` owns explicit scene references and the persistent location, topology, materials, light, atmosphere, and ambience. `风格：` owns look/style references. Motion, camera, storyboard, audio, text, and interval-only roles stay in their owning shot or active audio/text sentence. Later shots use semantic names and repeat only visible changes or continuity-critical state. Never ask the user which equivalent layout to use.
- Use `作为[角色名]` only when selecting one subject among several or combining several sources for one character. Do not add routine `定义为` wording.
- A storyboard or multi-panel sheet must name its authorized dimensions such as shot order, framing, blocking, screen direction, and occlusion. Do not treat it as a generic style reference.
- If one material applies only to a time interval, write that interval in the responsibility line.

## Unified generation structure

Use the same ordered structure for every known-duration Seedance 2.5 new/reference generation. `主体：` is conditionally required by visible subject presence; omit the other optional headings when they have no material information. Never leave a heading empty or fill it with invented prose.

```text
主体：
[required whenever any character, animal, product, vehicle, or key prop appears; omit only for a clip that remains a pure environment or empty shot throughout]

场景：
[optional: scene-reference materials plus time, location, topology, light, atmosphere, and persistent ambience]

风格：
[optional: medium, palette, material, and texture]

情节：
[required]
镜头1（0-5秒）：[framing/camera]；[current visible state and space]；[action/performance/dialogue/local sound]；[camera's visible result]；[visual focus when needed]；[ending or handoff].

[standing final sentence for new/reference generation]
不添加字幕，不添加背景音乐。
```

Do not open with `生成一段N秒的……`. Duration belongs in the time ranges and remains an exact production fact.

Never render a `全局补充：` heading. Put an owned whole-clip requirement naturally in `主体：`, `场景：`, `风格：`, or `情节：`. If a genuine cross-shot control has no better owner, append it once as a natural unheaded sentence after the last shot and before the standing subtitle/music sentence.

## Timeline rules

- Use `镜头N（开始-结束秒）：` for 5-second, 15-second, 30-second, and ultra-long outputs alike.
- Start at 0, use continuous non-overlapping ranges, and end exactly at total duration.
- Use integer-second boundaries by default. Never introduce decimals; preserve them only when the current user or an exact source explicitly requires sub-second timing.
- If locked shot count and duration cannot give every shot a positive integer range, ask for a longer duration or restructuring permission instead of using decimals.
- Use frame ranges only for frame-accurate sync, and state the active frame rate and total frame count.
- Keep one readable beat and one main camera strategy per shot. A short cut may carry an instantaneous state or action phase.
- Put stable subject information and explicit subject references in `主体：`. An empty opening frame does not suppress the field when a subject appears later. Shots use the semantic name and state only visible changes or continuity-critical inheritance.
- When a cut continues one event, state the inherited phase and advance it. Do not repeat approach, wind-up, launch, contact, or another completed onset.
- For previsualization, use the same timeline formula once total duration is known; establish the selected representative state at cut-in.
- For a coarse white-model video, inherit the source duration, shot order, and cuts without asking for or separately writing total duration. Reuse exact ranges only when they are readable; otherwise preserve the source order without inventing seconds.

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

Use the natural-language pattern demonstrated by the observed optimizer example:

- dialogue: `角色说道：“台词。”`
- persistent ambience: write it inside `场景：`
- local sound effect: write it inside the relevant shot
- music or subtitle: label it in ordinary Chinese only when active

Do not create a standalone sound section. Preserve exact dialogue and speaker ownership. Keep the mouth visible when lip sync matters.

For Seedance 2.5 new/reference generation, end the prompt with the standalone sentence `不添加字幕，不添加背景音乐。` outside any heading and do not attach it to the final shot. A background-music or subtitle field becomes active only through the current user, an active project/source requirement, or a reference input explicitly assigned the `audio` or `text` borrowed dimension. The mere presence of music or subtitles in a readable asset does not activate that field. Apply precedence separately: active background music removes only `不添加背景音乐`; active subtitles remove only `不添加字幕`; when both are active, omit the standing sentence. Edit, extension, and bridge preserve source-backed audio/text under their operation rules and never receive this standing generation sentence automatically. `不添加字幕` bans subtitle overlays, not source-backed signs, logos, titles, or other diegetic visible text. `不添加背景音乐` does not suppress active dialogue, ambience, or action sound. A current instruction to omit all sound-policy prose overrides rendering the background-music clause for that output.

For visible text, state exact content, timing, frame position, appearance method, and only necessary style. Use a dedicated material responsibility for exact logo, typography, or layout.

## Control and repetition

- Put subject-reference responsibility and stable subject facts in `主体：`; put scene-reference materials and persistent environment in `场景：`; put a look/style reference in `风格：`; and put motion/camera/storyboard roles in their owning shot. Never render a generic `参考素材：` heading or restate the same appearance later.
- Put per-shot visibility, blocking, occlusion, action phase, dialogue, and ending in the timeline.
- Treat internal viewer priority and rendered `画面重心` as one field.
- Never render a `全局补充：` heading. Place a whole-clip fact in its owning field; if a genuine cross-shot control has no better owner, append it once as a natural unheaded sentence before the standing subtitle/background-music sentence.
- Do not repeat a material label, global scene description, character appearance, camera rule, or negative instruction in every shot.
- A longer prompt is acceptable when it adds distinct executable information. Different wording of the same fact is redundancy, not stronger control.

## UI parameters

Keep resolution, frame rate, and aspect-ratio settings outside the prompt when the UI exposes them. If the user requires an aspect ratio inside an ultra-long prompt, place it in `场景：` without adding a duration-specific section. Never infer it.

## Seedance 2.0 legacy note

When the user explicitly selects 2.0 or 2.0 Fast:

- keep the same protected facts and material-responsibility map
- preserve user-supplied timing, but do not promise 2.5-level second accuracy
- apply the 2.0 limits from `seedance-capability-matrix.md`
- do not expose 2.5-only modes such as ultra-long generation or advanced editing as available
