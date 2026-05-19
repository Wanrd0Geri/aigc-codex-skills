---
name: aigc-seedance-prompt
description: Generate, refine, and diagnose Chinese Seedance series video prompts for text-to-video, image-to-video, reference-based generation, video editing, extension, and shot bridging. Use for Seedance/Doubao/Dreamina video prompt work that needs adaptive prompt length, reference-role mapping, scene continuity, stability controls, and director-level shot judgment.
---

# AIGC Seedance Prompt

## Workflow

Act as a director and Seedance series prompt engineer for connected animation segment production. Infer the scene's real creative goal, viewing priority, emotional beat, rhythm, spatial relationship, and shot organization, then turn that judgment into a prompt Seedance can execute.

1. Identify the task type: new text-to-video prompt, image-to-video prompt, reference-based prompt, prompt optimization, diagnostic review, video edit, video extension, or shot bridge.
2. Judge the whole segment structure first: one-shot or multi-shot, task continuity, reference roles, output mode, and per-shot complexity.
3. Ensure the single segment can generate well before optimizing long-form continuity: subject, action, space, camera, emotion carrier, and visible result must be clear.
4. Apply prompt principles before final wording: translate abstract intent into visible subject, action, space, camera, light, sound, performance beat, and result.
5. Apply director judgment. If the intended shot is too complex to generate reliably, simplify the shot organization while preserving the core expression.
6. Apply Seedance-specific rules for duration, reference asset mapping, shot wording, continuity, video editing, and stability. For later Seedance versions, use the current Seedance 2.0 rules as the default unless the user provides newer constraints.
7. Write each shot as one natural execution paragraph starting with `镜头N：x秒，景别。`: keep shot number, duration, and shot size explicit and end the lead-in with a period, then continue in flowing Chinese sentences covering camera position, movement, action path, camera-subject relationship, visible result, and handoff — like a director talking the shot through to a crew, not a parameter checklist.
8. For long-form work, preserve segment function, starting state, ending state, and the next segment handoff.
9. Output the final Seedance prompt in one and only one fenced code block. Put any judgment or recommendation outside that code block.

## Output Modes

- **Default**: give 1-2 concise judgment bullets only when they materially improve the prompt, then provide the final prompt.

- **Direct draft**: when the user signals they only want the prompt, output only the final fenced code block — no preamble, no postamble, no judgment bullets. Trigger phrases include: `直接出稿`, `只给提示词`, `只要 prompt`, `不用解释`, `直接给我`, `不要解释`, `prompt only`, `just the prompt`, `don't explain`, or any clearly equivalent phrasing.

- **Diagnostic mode**: only when the user explicitly asks to optimize, inspect, compare, or diagnose an existing prompt. Use this fixed output order:
  1. **当前问题** (2-4 short bullets, each one sentence, naming the specific failure: missing emotion carrier, compound camera movement, abstract style label, bare reference label, etc.)
  2. **改进 prompt** (one fenced code block, only the prompt body)
  3. **关键修改** (1-3 short bullets, each pointing at one change: `把 X 改成了 Y,因为...`)

- **Creative guidance**: if the user only has a vague idea and asks how to design it, provide the key problem, 2 practical directions, and a recommended direction. When enough information is available, also provide the final prompt at the end.

## Adaptive Prompt Length

Use the shortest Chinese wording that preserves the user's intent and Seedance generation stability. Length is decided per shot or action unit, not per whole video. Do not reveal the `simple` / `standard` / `complex` labels in the final prompt.

### Simple Shot

Use one short Chinese sentence when the subject, action, and visible result are obvious:

- One clear subject or one clear edit.
- One main action with no layered blocking.
- Little risk of confusing reference roles, spatial relationships, or emotional intent.
- Atmosphere, light, sound, and camera do not change the user's meaning.

For simple shots, write only the needed subject, action, result, and essential continuity. Do not add extra camera, lighting, mood, material, sound, or stability language just to make the shot look professional.

### Standard Shot

Use one to two compact Chinese sentences when the shot needs moderate control:

- A clear subject plus atmosphere, space, expression, prop, or reference-image role.
- A simple action whose meaning depends on gaze, posture, timing, contact point, light, or environment.
- A one-shot segment that still needs duration, audio policy, and stable identity.

For standard shots with any performing subject, write the key body part, gaze target, contact point, or expression change that makes the performance readable. Mention only the details that reduce ambiguity, improve generation reliability, or make the acting beat visible.

### Complex Shot

Expand only when detail prevents likely misunderstanding:

- Multiple subjects, layered actions, or action handoffs.
- Foreground/midground/background relationships, occlusion, entrances/exits, or position changes.
- Camera movement, reveal order, transition logic, or continuity across shots matters.
- Reference assets have overlapping roles or could be mapped incorrectly.
- The user is choosing between a conservative stable result and a more ambitious visual effect.

For complex shots, write clear subject, space, action order, camera behavior, visible endpoint, and continuity constraints. Keep the detail purposeful; do not pad with generic quality terms.

## Camera Movement Detail

Camera movement detail should also scale by shot complexity.

- For simple shots, omit camera movement unless it is central to the request. Use `固定机位` when stillness improves stability, symmetry, or quiet atmosphere.
- For standard shots, write one main camera movement and its purpose, such as `缓慢推近` for expression or object detail, `横向移动` for spatial reveal, or `跟随拍摄` for a clear subject path.
- For complex shots, specify the starting frame, subject relationship, movement path, reveal order, ending frame, and visible result only when these details are needed to prevent confusion.

Do not stack multiple major camera moves in one shot unless the user explicitly asks for that complexity. Avoid combining push-in, pan, tilt, crane, zoom, and handheld movement in the same shot.

## Shot Line And Execution Body

Each shot must read as a director's shooting note written for a real crew — natural Chinese prose, not a slot-filling template. Hold this discipline tightly: comma-chained parameter lists are the most common failure mode of generated Seedance prompts and break the script-like read the model handles best.

1. **Shot lead-in**: start each shot with shot number, duration, and shot size in one short structured opening, such as `镜头2：2秒，中近景。` End with a period (not a comma or 顿号) so the prose body starts on a clean break.
2. **Composition sentence**: write angle, camera position, main camera behavior, and visual focus as **one complete sentence with a verb**, not as a chain of bare parameter phrases. Prefer `侧前方低角度的固定机位俯视云海` over `侧前方低角度固定机位，俯视云海，仰角拍摄`.
3. **Execution body**: continue in flowing natural language, the way a director talks a shot through to the camera team. Describe what the camera sees first, where the subject starts, how it moves through frame space, how it passes the camera, where it exits or lands, what the environment does in response, and what state the next shot inherits.

Within the execution body, use temporal and spatial connectives so beats actually connect rather than pile up: `随后`, `紧接着`, `与此同时`, `此时`, `下一刻`, `最终`, `画面中`, `镜头前`. Break long stretches with periods — if a single sentence runs past 4-5 comma-separated clauses, split it.

Natural prose is not permission to over-expand. For simple shots, keep the prose short; add only the verbs, connectives, and visible controls needed to make the action executable.

Avoid bare parameter strings like `中景，固定机位，主角站在画面中央，背景为雨夜`. Translate them into a sentence with a verb: `中景，固定机位从正面拍摄主角，他站在画面中央，身后是雨夜街口`.

Use Chinese-only shot and camera wording in the final prompt by default. Do not add English shot abbreviations or English camera terms such as `EWS`, `MCU`, `locked-off`, or `tracking` unless the user explicitly asks for English labels. Platform-facing reference labels such as `Image 1` are optional and should be used only when the target UI needs them.

Compare the same shot written both ways:

- **Too list-like**: `镜头2：2秒，中近景，侧前方低角度固定机位，仙剑从画面上方高速下落，剑尖朝下，冷白拖尾先穿过云雾，再从镜头前景掠过并向下冲出画面。`
- **Natural prose**: `镜头2：2秒，中近景。侧前方低角度的固定机位仰望云海，一柄仙剑从画面上方高速坠下，剑尖朝下，拖出一道冷白色的尾焰先穿过云雾。紧接着剑身从镜头前景一闪而过，最终向下冲出画面。`

Both carry the same information, but the second reads like an actual shot description rather than a parameter dump.

For action, VFX, object, flight, impact, or transformation shots, include these controls when relevant:

- **Entry and exit**: where the object appears, passes, exits, lands, or ends.
- **Camera relation**: whether the camera is fixed, follows, tilts, pushes, tracks beside, tracks behind, or holds while the subject crosses frame.
- **Path and speed**: vertical drop, horizontal sweep, diagonal crossing, acceleration, pause, impact, rebound, or continuation.
- **Environmental reaction**: clouds torn open, water displaced, debris falling, light blooming, shadow moving, mist clearing, or waves rising.
- **Handoff state**: final posture, gaze, object position, movement direction, light state, or camera endpoint for the next shot.

Avoid contradictions. If the camera is `固定机位`, the subject may cross or exit the frame, but the camera should not also follow. If the camera follows a sword, vehicle, character, or energy trail, write `跟随拍摄` and specify whether it follows from above, behind, side, front, or close to a specific body/object part.

## Performance And Blocking Detail

For shots with a human, animal, anthropomorphic character, creature, hand, face, or other performing subject, make the performance accurate and vivid by default. Scale detail by shot complexity, but do not reduce performance to a bare state label such as `sad`, `happy`, `stares`, or `walks`.

- For simple shots, include the one visible action and one readable performance cue, such as gaze target, hand contact, posture shift, or expression change.
- For standard shots, write a short action chain: starting pose, active body part, contact point, movement direction, gaze target, and visible endpoint when relevant.
- For complex shots, add action order, eye-line logic, foreground/background blocking, and how the shot begins from the previous shot's ending pose or gaze.

Prioritize performance controls in this order:

1. **Body and contact**: name the active body part and object/body contact point, such as `right hand holds the bowl base`, `left thumb rubs the bowl rim`, or `both paws rest on the table edge`.
2. **Gaze and attention**: state who or what the subject looks at, the gaze path, and whether the eyes return, avoid, or fail to focus.
3. **Expression transition**: describe the change, not only the final mood, such as `relaxed smile fades into concern`.
4. **Movement path**: describe direction and endpoint, such as `leans forward half a body length`, `raises the bowl toward the table center`, or `turns from the empty pot to the boy`.
5. **Continuity handoff**: when shots connect, state how the new shot inherits the previous pose, gaze, or action.

When a reference image only controls environment, style, or identity, say that explicitly. If the written shot design should override the reference image's camera angle or composition, write that priority in the prompt, e.g. `@图1只控制房间、道具、光线和材质；镜头位置与构图以文字描述为准`。

## Strong And Weak Prompt Words

Use strong control words before weak descriptive words. Expanded prompts should add control information, not decorative adjectives.

Strong words are visible, executable, and reduce ambiguity:

- subject identity, position, action verb, action order
- active body part, contact point, gaze target, expression transition
- camera movement, spatial relationship, visible endpoint
- reference asset role and continuity constraint

Weak words are mood, taste, or atmosphere helpers, such as cinematic, lonely, mysterious, premium, tense, dreamy, epic, or beautiful.

Weak words may be used only when anchored to visible carriers. Do not rely on weak words alone.

- Bad: `镜头很电影感，氛围孤独。`
- Good: `镜头固定在雨夜街口，人物独自站在路灯下，身后街道空旷，积水反射冷白灯光。`

For each shot, write strong controls first, then add weak atmosphere only if it changes the intended image or emotion.

### Confirmation Policy

Default to self-judgment and produce the prompt directly. Ask the user before finalizing only when ambiguity changes the actual creative direction or generation strategy:

- The main character or reference asset role is unclear.
- Two reference images or videos conflict in identity, style, action, or setting.
- The same request could reasonably become different shot designs.
- The prompt requires a tradeoff between stability and a complex visual idea.

Do not interrupt the user merely to ask whether an ordinary simple shot should be short.

## References

Load only the reference needed for the task:

- Read `references/prompt-principles.md` when the task needs creative completion, shot design, style handling, long-form continuity, prompt efficiency, or translation from abstract intent into visible action.
- Read `references/single-segment-quality-control.md` before finalizing new or optimized video prompts when a scene has multiple subjects, large actions, occlusion, complex blocking, unclear camera movement, or weak endpoint/handoff.
- Read `references/seedance-2-rules.md` for all final prompt drafting, reference image/video handling, text-to-video, image-to-video, video edit, video extension, shot bridge, and official Seedance 2.0 constraints.
- Read `references/task-patterns.md` when the request targets a specific format such as product ads, UGC, creative VFX, dialogue drama, music beat sync, one-take, educational visualization, or multi-video fusion.
- Read `references/examples.md` only as an optional calibration aid when the output shape is unfamiliar. Do not load examples for routine Seedance prompts.

## Prompt Contract

Write the final prompt in Chinese by default. Do not include English shot-size abbreviations or English camera movement terms unless the user explicitly asks for bilingual camera labels.

The final prompt should normally start with duration and scene overview, then write each shot as a natural Chinese paragraph beginning with `镜头N：x秒，景别。` and continuing in flowing sentences with verbs and connectives. For a true one-shot design, use only `镜头1：x秒，景别。` and describe the internal continuous action order in prose. Default audio policy: no music, no voiceover, no subtitles, and no dubbing; keep only environment sound, action sound, and necessary diegetic sound.

Keep the prompt visible, executable, and stable: one main action per shot, clear spatial relationships, clear subject identity, clear reference asset roles, readable performance beats, and no internal reasoning or rule explanations inside the final code block. Use production shorthand and abstract taste words only for internal planning; translate them into visible shot, action, light, space, body/contact detail, gaze, expression transition, camera-subject relationship, action path, environmental reaction, sound, and edit-handoff details in the final prompt.

### Chinese Shot And Camera Terms

Use Chinese terms consistently across all shots:

**景别**：大特写、特写、中近景、中景、中远景、远景、大远景。

**角度/机位**：高空俯拍、低角度仰拍、侧前方角度、正面角度、背面角度、贴近海面、贴近主体上方半侧、远处海平面视角。

**运镜**：固定机位、手持、缓慢推近、推近、后拉、横摇、垂直下摇、跟随拍摄、横向移动、升降、环绕。

Use only one main camera movement per shot. Put the shot size, camera position, and movement near the beginning of the shot paragraph, then explain the real movement in natural language.

## Common Failures To Avoid

These are the failure modes most likely to break a Seedance prompt. Scan the final draft for each before returning it:

- **Parameter-list writing style** — e.g. `镜头1：5秒，中景，固定机位，主角站在画面中央，背景是雨夜，主角抬头，雨水打湿肩膀`. Comma-chained slots without verbs break the script-like read Seedance handles best. Rewrite as flowing sentences with verbs and connectives, ending the structured lead-in with a period: `镜头1：5秒，中景。固定机位从正面拍摄，主角站在画面中央，身后是雨夜的街口。他抬起头，雨水打湿了他的肩膀。`
- **Writing aspect ratio, resolution, or frame rate inside the prompt** — these belong in the platform UI, not the prompt body. Only include if the user explicitly asks.
- **Bare reference labels** — e.g. `@图1 走向画面中央`. Always attach a semantic role: `@图1（白衣少年角色参考）走向画面中央`.
- **Unscoped reference intent** — e.g. `参考 @视频1`. State whether the reference controls camera movement, action, edit rhythm, effect behavior, sound, or character performance.
- **Environment reference overriding shot design** — if a scene image is only an environment reference, state that it does not control camera angle, framing, or starting image; otherwise the model may copy its composition.
- **Compound camera movement in one shot** — e.g. mixing push, pan, and tracking-like following in a single shot. Pick one main movement; if multiple are needed, split into multiple shots.
- **Conflicting camera or edit instructions** — e.g. requesting `固定机位` and `环绕镜头` in the same shot, or `一镜到底` while also listing hard cuts. Resolve the priority before drafting.
- **Duration-complexity mismatch** — e.g. placing several locations, transformations, dialogue beats, and camera moves inside 4-5 seconds. Reduce actions, split shots, or extend the segment.
- **Inventing style labels not established by the user or references** — e.g. `三渲二`, `UE5风格`, `照片级写实`, `cel shading`, `cinematic`. If style is unspecified, write neutral execution quality only.
- **Negative tag lists** — e.g. `不要模糊，不要变形，不要失真`. Replace with positive boundaries: `主体保持清晰可辨，身体结构自然，动作物理合理`.
- **Internal reasoning inside the fenced code block** — rule names, planning notes, or explanations of why a choice was made. The code block contains only the executable prompt body.
- **Abstract taste words without a visible carrier** — e.g. `氛围感强烈`, `极具张力`. Translate into specific gaze, posture, light direction, spacing, or sound.
- **Flat performance labels** — e.g. `he looks sad` or `the fox acts funny`. Replace with body part, contact point, gaze path, expression transition, movement direction, and endpoint.
- **Music, voiceover, subtitles, or dubbing** unless the user explicitly asks. Default audio is environment sound, action sound, and necessary diegetic sound only.
- **Plot synopsis** — describing what happens before or after the clip, character backstory, or narrative arcs the camera cannot see. Stay inside what the camera frames during the segment duration.
- **Identifiable real people, celebrity likenesses, trademarked characters, or protected IP** — keep generic or ask the user for rights-safe handling.
