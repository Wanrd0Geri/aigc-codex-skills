# Seedance 2.0 Prompt Rules

Use these rules when drafting the final Seedance prompt.

## Official Notes And Platform Defaults

- Seedance series workflows may include text-to-video, image-to-video, multimodal references, video editing, video extension, and shot continuation. The current rules are based on Seedance 2.0 / 2.0 Fast; confirm platform-specific UI/API limits when the user targets a specific provider or later version.
- Common generation settings such as resolution and aspect ratio are selected in the platform UI. Do not write aspect ratio, frame ratio, or canvas ratio in the final prompt unless the user explicitly asks to include it. Use the user's requested segment duration when provided. For long-form work, generate connected segments and split only when the target platform's duration limit requires it.
- Treat real recognizable human faces, celebrity likeness, trademarked characters, and protected IP cautiously. If the user references such material, keep the prompt generic or ask for rights-safe handling when needed.
- Do not expose asset IDs as visual subjects. Build a semantic bridge from each reference asset to its visual role.
- Every final Seedance prompt opening overview must end with `无配乐，无字幕。` This does not mean silence: keep diegetic speech, environment sound, and necessary action sound when they are part of the shot.

## Final Prompt Shape

Put the final Seedance prompt in one fenced code block. The code block contains only the executable prompt body, not explanations or internal rules. Short headings such as `参考图使用` or `生成注意` are allowed only when they help parse complex references or high-risk constraints.

Write the prompt as **natural Chinese prose**, not a parameter list. The shot lead-in (`镜头N：x秒，景别。`) is the only structured marker — everything after it should read as complete sentences a director would say to a crew. See SKILL.md `Shot Line And Execution Body` for the writing-style discipline.

Recommended shape:

```text
本视频总时长 X 秒，单镜头 / N个镜头。整体是一段关于[情绪/主题]的[风格/类型]短片，画面重点是[视觉锚点]、[行为/状态]和[情绪变化]。无配乐，无字幕。

镜头1：x秒，景别。一句话写清角度、机位、运镜方向与画面重点，紧接着用一到两句自然语言描述主体动作、表演细节与空间关系；只有在承接下一镜头或下一段时，才补充必要的姿态、位置、视线、光线或运动方向锚点。

镜头2：x秒，景别。同样的写法——先一句空间与机位的设定，再用自然语言推进动作和镜头变化，最后给出可与下一段衔接的姿态、位置或光线状态。
```

Use integer durations and shot counts. Keep subjects and actions concrete. Do not write a plot synopsis or a parameter checklist. Natural prose should stay efficient: simple shots can remain short, and added wording must improve action clarity, continuity, or generation stability. Do not let any single sentence run for more than 4-5 comma-separated clauses; if a sentence stretches longer, break it with a period and continue with a connective such as `随后`、`紧接着`、`此时` or `与此同时`.

## Reference Asset Mapping

Use stable, ordered labels for references:

- Chinese collaboration labels: `@图1`, `@图2`, `@视频1`, `@视频2`, `@音频1`, `@音频2`.
- Existing platform anchors from the user's prompt, including file-name anchors such as `@庠序场景.png`, must be preserved exactly unless the user asks to relabel them.
- If the user writes `图1`, `参考图1`, or `第一张图` without `@`, normalize it to the matching platform anchor such as `@图1` when that mapping is clear.
- Platform-facing labels when the target UI requires them: `Image 1`, `Image 2`, `Video 1`, `Video 2`, `Audio 1`, `Audio 2`. Omit them in ordinary Chinese-only prompts unless useful for asset mapping.

After every reference label, immediately attach a semantic noun or role to prevent ambiguity:

- Good: `@图1（白衣少年角色参考）站在画面左侧`
- Good: `@图2（老宅场景参考）作为空间与光线参考`
- Good: `@视频1（原始镜头参考）向后平滑延长`
- Good: `@视频1（剪辑节奏与现场音参考）作为动作停顿和环境声参考`
- Good: `@音频1（节奏参考）仅作为剪辑节奏和情绪强度参考`
- Good: `@图3（产品外观与标识参考）作为商品形状、材质和logo参考`
- Good: `@图4（字体与版式参考）仅在用户明确需要文字画面时使用`
- Avoid: `asset-xxx 跑向前方`
- Avoid: `@图1 走向`
- Avoid: `参考 @视频1`
- Avoid: `参考图1控制角色外貌`
- Avoid: changing `@庠序场景.png` into `庠序场景.png` or `参考图1` without preserving `@`
- Avoid: bare labels without a character, object, scene, first-frame, or end-frame role.

When multiple references are provided, assign each a clear responsibility. Common roles include character, face, costume, scene, prop, lighting, action, camera movement, edit rhythm, effect behavior, first frame, end frame, style, product appearance, typography, BGM, sound effect, voice tone, or spoken rhythm. Keep the most important 1-3 responsibilities unless the user explicitly needs more.

For video references, name the exact layer being reused:

- Camera: movement path, lens feel, framing, or one-take structure.
- Action: choreography, gesture timing, performance rhythm, or object motion.
- Edit rhythm: cuts, pauses, impact beats, or music synchronization.
- Effects: transformation behavior, particles, destruction, liquid, smoke, light, or transition logic.
- Sound: environment sound, action sound, voice tone, BGM rhythm, or beat timing.

For audio references, define whether they serve as BGM, beat sync, sound effect, voice tone, speech pace, or emotional rhythm reference. Do not add music or voiceover just because audio exists; use it only when the user requests or the reference role requires it.

For long images, collages, or grids, recommend splitting them into single references. If the user proceeds without splitting, clarify which sub-area or visual role each reference should carry.

## Shot Wording

Each shot should prioritize:

- Shot number, duration, and shot size as a short structured opening ending in a period: `镜头N：x秒，景别。`
- Angle, camera position, main camera movement, and visual focus written as one complete Chinese sentence with a verb, immediately after the lead-in.
- Main action, written as natural sentences with subject and verb.
- Performance details woven into the action prose, not stacked as separate slots.
- Visible action or state change when it improves readability; continuity anchors only when the next shot depends on them.
- Spatial relationships and reference roles named explicitly inside the sentences where they apply.

Only add sound when it materially affects rhythm, action, or presence. Use `声音：` after the relevant shot description.

## Chinese Shot And Camera Terms

Use Chinese terms consistently across all shots unless the user explicitly asks for bilingual labels.

**景别**：大特写、特写、中近景、中景、中远景、远景、大远景。

**角度/机位**：高空俯拍、低角度仰拍、侧前方角度、正面角度、背面角度、贴近海面、贴近主体上方半侧、远处海平面视角。

**运镜**：固定机位、手持、缓慢推近、推近、后拉、横摇、垂直下摇、跟随拍摄、横向移动、升降、环绕。

Use only one main camera movement per shot. Put the shot size, camera position, and movement near the beginning of the shot paragraph, then explain the real movement in natural language.

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

- Name the source as `@视频1（原始镜头参考）`.
- Continue from the source clip's ending posture, movement direction, light state, and camera momentum.
- Define the next visible action and the minimum continuity anchor needed to continue.

For shot bridge:

- Write the visible transition, not "接下一段".
- Specify how the camera, subject motion, or visual element carries from the previous clip into the next.

## Stability Defaults

For ordinary Vibe-first or simple prompts, do not add a separate `稳定边界` section. Place necessary constraints inside the shot body by describing what is present, centered, moving, lit, heard, held, or looked at. Use a short `生成注意` section only for hard safety, visible text/logo/watermark, identity drift, reference-role conflict, or a user-explicit prohibition that cannot be expressed as positive visible staging.

- Subject identity remains clear through clothing, silhouette, position, or prop anchors.
- Facial features, body structure, and movement stay natural.
- Costume, props, light direction, and spatial relationship remain continuous.
- The frame stays clean, with readable action and a clear visual focus.
- Action handoffs remain physically coherent between shots and connected segments.
