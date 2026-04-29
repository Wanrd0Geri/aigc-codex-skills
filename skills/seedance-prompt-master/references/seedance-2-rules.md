# Seedance 2.0 Prompt Rules

Use these rules when drafting the final Seedance prompt.

## Official Notes And Platform Defaults

- Seedance 2.0 / Seedance 2.0 Fast workflows may include text-to-video, image-to-video, multimodal references, video editing, video extension, and shot continuation. Confirm platform-specific UI/API limits when the user targets a specific provider.
- Common generation settings such as resolution and aspect ratio are selected in the platform UI. Do not write aspect ratio, frame ratio, or canvas ratio in the final prompt unless the user explicitly asks to include it. Use the user's requested segment duration when provided. For long-form work, generate connected segments and split only when the target platform's duration limit requires it.
- Treat real recognizable human faces, celebrity likeness, trademarked characters, and protected IP cautiously. If the user references such material, keep the prompt generic or ask for rights-safe handling when needed.
- Do not expose asset IDs as visual subjects. Build a semantic bridge from each reference asset to its visual role.
- Default audio policy: no music, no voiceover, no subtitles, and no dubbing. Keep only environment sound, action sound, and necessary diegetic sound unless the user explicitly asks for music.

## Final Prompt Shape

Put the final Seedance prompt in one fenced code block. The code block contains only the prompt body, not explanations, headings, or rules.

Recommended Chinese skeleton:

```text
时长：x秒。场景概述。无配乐，无旁白，无字幕，无配音，仅保留环境音、动作声与必要现场声。

镜头1：景别（英文缩写），角度，运镜（English camera term）。主体动作、表演细节、空间关系、可见结果。
镜头2：...
```

Use integer durations and shot counts. Keep subjects and actions concrete. Do not write a plot synopsis or a parameter checklist.

## Reference Asset Mapping

Use stable, ordered labels for references:

- Chinese collaboration labels: `@图1`, `@图2`, `@视频1`, `@视频2`, `@音频1`, `@音频2`.
- Platform-facing labels when needed: `Image 1`, `Image 2`, `Video 1`, `Video 2`, `Audio 1`, `Audio 2`.

After every reference label, immediately attach a semantic noun or role to prevent ambiguity:

- Good: `@图1（白衣少年 / Image 1 character reference）站在画面左侧`
- Good: `@图2（老宅场景 / Image 2 scene reference）作为空间与光线参考`
- Good: `@视频1（原始镜头 / Video 1 motion reference）向后平滑延长`
- Good: `@视频1（剪辑节奏与现场音 / Video 1 rhythm and sound reference）作为动作停顿和环境声参考`
- Good: `@音频1（BGM节奏 / Audio 1 beat reference）只控制剪辑节奏和情绪强度`
- Good: `@图3（产品外观与标识 / Image 3 product reference）作为商品形状、材质和logo参考`
- Good: `@图4（字体与版式 / Image 4 typography reference）仅在用户明确需要文字画面时使用`
- Avoid: `asset-xxx 跑向前方`
- Avoid: `@图1 走向`
- Avoid: `参考 @视频1`
- Avoid: bare labels without a character, object, scene, first-frame, or end-frame role.

When multiple references are provided, assign each a clear responsibility. Common roles include character, face, costume, scene, prop, lighting, action, camera movement, edit rhythm, effect behavior, first frame, end frame, style, product appearance, typography, BGM, sound effect, voice tone, or spoken rhythm. Keep the most important 1-3 responsibilities unless the user explicitly needs more.

For video references, name the exact layer being reused:

- Camera: movement path, lens feel, framing, or one-take structure.
- Action: choreography, gesture timing, performance rhythm, or object motion.
- Edit rhythm: cuts, pauses, impact beats, or music synchronization.
- Effects: transformation behavior, particles, destruction, liquid, smoke, light, or transition logic.
- Sound: environment sound, action sound, voice tone, BGM rhythm, or beat timing.

For audio references, define whether they control BGM, beat sync, sound effects, voice tone, speech pace, or emotional rhythm. Do not add music or voiceover just because audio exists; use it only when the user requests or the reference role requires it.

For long images, collages, or grids, recommend splitting them into single references. If the user proceeds without splitting, clarify which sub-area or visual role each reference should carry.

## Shot Wording

Each shot should prioritize:

- Shot size and angle.
- Camera movement, with only one main movement per shot.
- Main action.
- Performance details.
- Visible result or state change.
- Spatial relationships and reference roles.

Only add sound when it materially affects rhythm, action, or presence. Use `声音：` after the relevant shot description.

## Video Editing

For edits to an existing video, specify:

- Time range.
- Spatial location within the frame.
- What to add, delete, or change.
- What must remain continuous: character identity, lighting, camera movement, action rhythm, and background geometry.

Example pattern:

```text
在0-4秒的画面右侧增加一团缓慢扩散的冷色雾气，保持人物朝向、镜头运动、背景光线和动作节奏不变。
```

## Video Extension And Shot Bridge

For extension or continuation:

- Name the source as `@视频1（原始镜头 / Video 1 source clip）`.
- Continue from the source clip's ending posture, movement direction, light state, and camera momentum.
- Define the next visible action and endpoint.

For shot bridge:

- Write the visible transition, not "接下一段".
- Specify how the camera, subject motion, or visual element carries from the previous clip into the next.

## Stability Defaults

Naturally include positive stability constraints when useful, without turning the prompt into a negative tag list:

- Subject identity remains clear through clothing, silhouette, position, or prop anchors.
- Facial features, body structure, and movement stay natural.
- Costume, props, light direction, and spatial relationship remain continuous.
- The frame stays clean, with readable action and a clear visual focus.
- Action handoffs remain physically coherent between shots and connected segments.
