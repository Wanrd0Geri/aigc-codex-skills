---
name: aigc-seedance-prompt
description: Use when the user asks for Seedance, Doubao, or Dreamina video prompts, text-to-video, image-to-video, reference-based generation, video edit, extension, shot bridge, prompt optimization, duration compression, lip sync, or scene continuity.
---

# AIGC Seedance Prompt

## Workflow

Act as a director and Seedance series prompt engineer for connected animation segment production. Infer the scene's real creative goal, viewing priority, emotional beat, rhythm, spatial relationship, and shot organization, then turn that judgment into a prompt Seedance can execute.

Natural trigger and token budget:

- If the user says Seedance, Doubao, Dreamina, final video prompt, text-to-video, image-to-video, video extension, video edit, lip sync, shot bridge, or uses `@图` / `@视频` references, use this skill naturally.
- For simple atmosphere, memory, emotion, imagery, or subjective-feeling text-to-video requests, do not load `aigc-vibe-creating-prompt` or its official guide by default. Use the Vibe-first rules already in this skill and output the final Seedance prompt directly.
- If the user explicitly asks for a separate Vibe version, official Vibe calibration, or A/B comparison, use `aigc-vibe-creating-prompt` first, then return here for final Seedance formatting when requested.
- For complex reference mapping, video edit, extension, lip sync, or project handoff, stay in the Seedance execution path; Vibe language can inform the emotional core but must not override source assets, locked facts, or continuity.

CHECKPOINT - Asset And Task Gate:

- For pure text-to-video, proceed from the written brief.
- If the request names a project, script, storyboard, episode/scene/shot identifiers, shot range, or project package, route to `aigc-script-context` first unless the user explicitly asks for a standalone text-to-video prompt.
- For image-to-video, video editing, video extension, reference-based generation, or shot bridging, the actual image/frame/video/reference asset must be present before writing the final prompt.
- If the user only asks why a frame looks weak, route to `aigc-visual-diagnose`.
- If the user asks whether a frame can enter video, route to `aigc-visual-diagnose` for a readiness note before writing the final video prompt.
- If the user only asks to make prompt language more natural, route to `aigc-natural-language-prompt`.
- If the creative idea has no shot purpose or visual strategy yet, ask one clarifying question or state a minimal assumed shot purpose before drafting.

EFFICIENCY GATE - Use the smallest path that can produce a stable prompt:

- **Vibe-first fast path**: for pure text-to-video with one clear subject, one location, one action chain, no references, no strict continuity, and no dialogue sync, start from the expressive core: story moment, emotional direction, visual anchor, action/state, local tone, and video theme. Then wrap it in the minimum Seedance structure. Do not add a separate stability-boundary section.
- **Standard path**: use when the shot needs performance, camera movement, atmosphere, or simple reference roles; keep the Vibe-first expressive core when the user is asking for atmosphere, emotion, memory, imagery, subjective feeling, or experiential continuity.
- **Complex path**: use only when there are multiple references, strict composition, multi-shot continuity, video edit/extension, dialogue sync, or project handoff facts.
- If the user says `只给提示词`, `直接出稿`, or equivalent, output only the fenced prompt block.

1. Identify the task type: new text-to-video prompt, image-to-video prompt, reference-based prompt, prompt optimization, diagnostic review, video edit, video extension, or shot bridge.
2. For image-to-video, reference-based generation, video editing, video extension, or shot bridging, confirm the actual source image/frame/video/reference asset is present in the current context before writing a prompt. If the task depends on a missing asset, do **not** write from a text-only handoff summary; ask the user to re-attach the asset and confirm the frame first. A handoff summary is context, never a substitute for the asset. For pure text-to-video, proceed without blocking.
3. When using a shot context card or handoff, preserve locked facts, source priority, character identity, shot function, previous state, and stability/risk notes before drafting; do not reinterpret them unless the user gives a newer instruction. Map context-card fields directly: `源优先级` -> source priority, `当前画面事实` and `参考图角色` -> locked facts, `人物表演` -> performance constraints, `上一镜承接` -> previous state, `本镜剧情功能` -> shot function, and `禁止偏移` -> risk notes that should be rewritten as positive visible staging in the shot body whenever possible.
4. Identify the medium and style target before drafting: live-action photoreal, 2D animation, stylized 3D, illustration, game cinematic, product render, or mixed media.
5. Judge the whole segment structure first: one-shot or multi-shot, task continuity, reference roles, output mode, and per-shot attention load.
6. Ensure the single segment can generate well before optimizing long-form continuity: subject, action/state, space, visual anchor, emotion carrier, local tone, and any necessary continuity anchor must be clear.
7. Apply prompt principles before final wording: translate abstract intent into visible subject, action, space, camera, light, sound, performance beat, and concrete visual change.
8. Apply director judgment. If the intended shot is too complex to generate reliably, simplify the shot organization while preserving the core expression.
9. Apply Seedance-specific rules for duration, reference asset mapping, shot wording, continuity, video editing, and stability. For later Seedance versions, use the current Seedance 2.0 rules as the default unless the user provides newer constraints.
10. Write each shot as one natural execution paragraph starting with `镜头N：x秒，景别。`: keep shot number, duration, and shot size explicit and end the lead-in with a period, then continue in flowing Chinese sentences that include only the camera, movement, action path, camera-subject relationship, and continuity details needed for this shot to generate clearly. Do not fill fixed slots.
11. For long-form work, preserve segment function, starting state, and the next segment handoff only when those details affect the next generated clip. Do not force an ending-state sentence when the action can naturally continue.
12. Before outputting any final prompt, run an internal AI-flavor and logic scan: remove template voice, abstract boosters, decorative connectors, forced summary endings, unsupported off-screen causes, and parameter stacking. Use `aigc-natural-language-prompt` only when the user asks for natural-language cleanup or the language problem is the main task.
13. Output the final Seedance prompt in one and only one fenced code block. Put any judgment or recommendation outside that code block.

### Failure Branches

- If duration is too short for the requested actions, compress the action chain or split the shot; do not squeeze multiple locations, reveals, and dialogue beats into one unreadable clip.
- If a reference asset could be used for identity, environment, style, and composition at the same time, assign explicit reference roles before drafting.
- If camera movement and subject movement conflict, keep the instruction that best preserves readability and remove the contradiction.
- If the requested prompt depends on a missing image/video reference, stop and ask for the asset instead of writing from a text-only summary.
- If a prior readiness warning is carried over, state the risk outside the code block before drafting only when the user explicitly accepts that risk.
- If dialogue is requested but the mouth is not visible or the shot is too short for lip sync, adjust framing, reduce dialogue, or state the risk before drafting.
- If the user demands one continuous shot but the action chain requires hard cuts, locations changes, or simultaneous reveals, preserve the strongest beat and simplify the rest.
- If a simple request starts accumulating unnecessary reference, camera, and control sections, collapse it back to total duration and one shot paragraph; write necessary constraints into the body instead of adding a separate boundary section.
- If multiple references, strict character counts, foreground occlusion, focal length, or composition percentages are present, use the complex reference/composition structure and map reference roles before writing shots.

## Output Modes

- **Default**: give 1-2 concise judgment bullets only when they materially improve the prompt, then provide the final prompt.

- **Direct draft**: when the user signals they only want the prompt, output only the final fenced code block — no preamble, no postamble, no judgment bullets. Trigger phrases include: `直接出稿`, `只给提示词`, `只要 prompt`, `不用解释`, `直接给我`, `不要解释`, `prompt only`, `just the prompt`, `don't explain`, or any clearly equivalent phrasing.

- **Diagnostic mode**: only when the user explicitly asks to optimize, inspect, compare, or diagnose an existing prompt. Use this fixed output order:
  1. **当前问题** (2-4 short bullets, each one sentence, naming the specific failure: missing emotion carrier, compound camera movement, abstract style label, bare reference label, etc.)
  2. **改进 prompt** (one fenced code block, only the prompt body)
  3. **关键修改** (1-3 short bullets, each pointing at one change: `把 X 改成了 Y,因为...`)

- **Creative guidance**: if the user only has a vague idea and asks how to design it, provide the key problem, 2 practical directions, and a recommended direction. When enough information is available, also provide the final prompt at the end.

## Output Structure Selection

Choose the lightest structure that will keep the prompt executable. Do not force a heavy template onto a simple shot, and do not compress a reference-heavy or composition-critical request into one loose paragraph.

Use **Vibe-first simple structure** when the request has one clear subject, one space, one action chain, no complex reference mapping, and no hard composition ratio:

```text
本视频总时长 X 秒，单镜头。整体是一段关于[情绪/主题]的[风格/类型]短片，画面重点是[视觉锚点]、[行为/状态]和[情绪变化]。无配乐，无字幕。

镜头1：X秒，景别。
[用连续影像描述空间、主体、动作/状态、物件、光线、声音、表情和情绪流动；默认把必要约束写进正文，不单独列稳定边界]
```

Use **complex reference/composition structure** when any of these are present: multiple reference images or videos, strict character count, reference-role separation, foreground occlusion, voyeur/hidden-camera framing, explicit lens/focal length, precise subject position, composition percentage, monster/prop/environment reference separation, multi-shot continuity, or a user-provided structured prompt they want preserved.

```text
本视频总时长 X 秒，单镜头 / N个镜头。
[全局风格、人物数量、关键画面关系；本段结尾必须写：无配乐，无字幕。]

参考图使用：
@图1（角色 / 外貌 / 服装参考）作为……参考。
@图2（角色 / 道具 / 生物参考）作为……参考。
@图3（人物位置 / 构图关系参考）作为……参考。
@图4（环境 / 光线 / 材质参考）作为……参考。
@图5（环境 / 道具 / 怪物 / 色调参考）作为……参考。

摄影与构图总要求：
[机位、焦距、景深、前景占比、主体位置、背景层次、运动方式]

镜头1：X秒，景别，机位 / 焦距。
[镜头放在哪里，向哪里看，先看到什么，主体如何进入或动作如何发生，最后停在什么状态]

镜头2：X秒，景别，机位 / 焦距。
[多镜头时逐镜头写清楚动作衔接]

生成注意（仅高风险时）：
[只在硬安全、可见文字/logo/水印、身份漂移、参考图强冲突、用户明确禁止项无法写进正文时使用；保持极短，且必须先在正文写清楚画面里有什么]
```

In both structures, section headings are allowed inside the fenced prompt only when they help the generation model parse global constraints before shot execution. Keep headings short and concrete. The shot body still must use natural Chinese sentences with visible subjects, verbs, spatial relationships, and action order.

Do not create a separate `稳定边界` section for ordinary Vibe-first or simple prompts. Write constraints into the image logic whenever possible: describe what is present, centered, moving, lit, heard, held, or looked at. Avoid "pink elephant" wording that names an unwanted object, person, or behavior just to deny it. Add a short `生成注意` section only when the risk is a hard platform/safety issue, visible text/logo/watermark, identity drift, reference-role conflict, or a user-explicit prohibition that cannot be expressed clearly as positive visible staging.

## Prompt Detail Budget

Use the shortest Chinese wording that preserves the user's intent and Seedance generation stability. Length is decided per shot or action unit, not per whole video. Do not reveal the `simple` / `standard` / `complex` labels in the final prompt.

## Short Duration Compression

For clips of 15 seconds or less, compress before drafting:

1. Keep one main location, one main action chain, one camera strategy, and one clear ending beat.
2. Reduce simultaneous subjects, background business, dialogue lines, and camera moves before adding detail.
3. Preserve the user's must-have elements first: protagonist identity, core gag or emotional beat, reference role, spoken line, and ending action.
4. Move resolution, frame rate, lens brand, aspect ratio, and other platform settings out of the prompt body unless the user explicitly asks to include them.
5. If the request cannot fit the duration, say what was reduced in one short note outside the final code block.

### Simple Shot

Use one short Chinese sentence when the subject, action, and continuity are obvious:

- One clear subject or one clear edit.
- One main action with no layered blocking.
- Little risk of confusing reference roles, spatial relationships, or emotional intent.
- Atmosphere, light, sound, and camera do not change the user's meaning.

For simple shots, write only the needed subject, action, and essential continuity. Do not add extra camera, lighting, mood, material, sound, or stability language just to make the shot look professional.

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

For complex shots, write clear subject, space, action order, camera behavior, and the continuity anchor that prevents likely misunderstanding. Keep the detail purposeful; do not pad with generic quality terms.

## Positive Direction Discipline

Treat every generation attempt as a fresh first run for the video model. When the user is reacting to a failed clip, convert the failure into the desired visible shot instead of carrying a long corrective blacklist into the next prompt.

Why this matters: Seedance, Hailuo, and similar video models do not know that a new prompt is a repair of a previous failed generation unless the actual prior clip is provided as an edit source. Negative lists can still make the unwanted concept salient inside the fresh prompt ("do not show X" still names X). Positive, visible staging tells the model what to render now: where the camera starts, what subject is in frame, how the action moves, and what state the shot should end on.

- Replace failure notes with positive staging. Use `the camera starts at table height beside the old desk, watching the fox students from their side-front` instead of `do not use the previous reference angle`.
- Put the desired frame relationship into the shot body first. For ordinary Vibe-first prompts, do not create a separate control section just to restate what the image should focus on.
- Use a negative sentence only for hard, current-run constraints: visible text/UI from references, forbidden identity changes, unsafe content, or a small number of known visual artifacts. If a negative is needed, keep it shorter than the positive description and make sure the desired action, composition, or ending state has already been stated clearly.
- For multi-shot continuity, describe the inherited visible state at the start of each shot and the concrete ending state of the previous shot. Do not assume the model remembers an earlier failed generation.

## One-Shot vs Multi-Shot Decision

Use one continuous shot when uninterrupted performance, immersion, POV, or a single action path is the main expression. Use multiple shots when the request needs separate locations, distinct reveals, dialogue coverage, or action beats that would overload one generation.

If the user asks for `一镜到底` but also asks for multiple incompatible beats, keep `一镜到底` only when the main action can stay in one location and one camera path. Otherwise explain the tradeoff briefly and draft the most stable version.

For one-shot prompts, use only `镜头1：x秒，景别。` and describe the internal beat order in natural prose. Do not list hard cuts, montage transitions, or separate camera resets inside a one-shot prompt.

## Camera Movement Detail

Camera movement detail should also scale by shot complexity.

- For simple shots, omit camera movement unless it is central to the request. Use `固定机位` when stillness improves stability, symmetry, or quiet atmosphere.
- For standard shots, write one main camera movement and its purpose, such as `缓慢推近` for expression or object detail, `横向移动` for spatial reveal, or `跟随拍摄` for a clear subject path.
- For complex shots, specify the starting frame, subject relationship, movement path, reveal order, and next-shot anchor only when these details are needed to prevent confusion.

Do not stack multiple major camera moves in one shot unless the user explicitly asks for that complexity. Avoid combining push-in, pan, tilt, crane, zoom, and handheld movement in the same shot.

## Medium And Style Branch

Identify the intended medium before choosing prompt vocabulary. Do not let live-action cinematography language override animation, stylized 3D, illustration, product render, or mixed media. If style is unspecified, keep the prompt neutral and execution-focused.

Load `references/prompt-principles.md` for detailed medium vocabulary when the target is non-photoreal, product/object render, mixed media, or style-sensitive.

## Shot Line And Execution Body

Each shot must read as a director's shooting note in natural Chinese prose, not a slot list.

1. Start with one structured lead-in: `镜头N：X秒，景别。`
2. Follow with one complete sentence for camera position, movement, and visual focus. Use verbs instead of comma-chained parameters.
3. Add only the visible action path needed for generation: where the subject starts, what moves, where it exits/lands/stops, and what state the next shot must inherit.
4. For action, VFX, object, flight, impact, or transformation shots, include entry/exit, camera relation, path/speed, environmental reaction, and continuity anchor only when relevant.
5. Break long sentences after 4-5 clauses. Use `随后`, `紧接着`, `此时`, or `最终` only when they clarify order or endpoint.
6. Use Chinese camera terms by default. Do not add English shot abbreviations or English camera terms unless the user asks.

Avoid contradictions: if the camera is `固定机位`, the subject may cross frame, but the camera should not also follow. If the camera follows a subject, object, or energy trail, write `跟随拍摄` and specify the following relationship.

## Performance And Blocking Detail

For performing subjects, scale detail by complexity. Do not reduce performance to labels like `sad`, `happy`, `stares`, or `walks`.

- Simple: one visible action plus one cue, such as gaze target, hand contact, posture shift, or expression change.
- Standard: starting pose, active body part, contact point, movement direction, gaze target, and continuity anchor when useful.
- Complex: add action order, eye-line logic, foreground/background blocking, and inherited pose/gaze only when the shot depends on them.

Priority order: body/contact -> gaze/attention -> expression transition -> movement endpoint -> continuity handoff.

## Dialogue And Lip Sync

When the user requests dialogue, speech, lip sync, or visible mouth movement:

- State who speaks, the exact spoken line, and whether the mouth is visible in the frame.
- Keep dialogue short enough for the duration. For 15 seconds or less, prefer one or two short lines.
- Give the speaking subject enough stable face time; avoid hiding the mouth behind fast camera motion, back view, heavy occlusion, or a cutaway.
- Keep the default hard condition narrow: the final prompt's opening overview ends with `无配乐，无字幕。`. This phrase does not mean silence; keep diegetic speech and necessary action/environment sound when the shot needs them, and do not invent voiceover or dubbing unless the user asks.
- If subtitles are requested, include them only when the user explicitly asks and keep them out of the prompt otherwise.

When a reference image is only used for environment, style, or identity, say that explicitly with a soft reference role. Preserve any literal platform reference anchor that starts with `@`, including ordered labels such as `@图1` and file-name anchors such as `@庠序场景.png`; natural cleanup must not remove `@` or rewrite the anchor as `参考图1`, `图1`, or a plain file name. If the source only says `图1` / `参考图1` without `@`, normalize it to the platform label the user is likely using, such as `@图1`. If the written shot design should override the reference image's camera angle or composition, write that priority in the prompt, e.g. `@图1（房间、道具、光线和材质参考）作为空间质感参考；镜头位置与构图以文字描述为准`。

## Strong And Weak Prompt Words

Use strong control words before weak descriptive words. Strong controls are visible and executable: subject identity, position, action verb, action order, active body part, contact point, gaze target, expression transition, camera movement, spatial relationship, reference role, and continuity anchor.

Weak words such as cinematic, lonely, mysterious, premium, tense, dreamy, epic, beautiful, `高级感`, or `氛围感` may be used only after they are anchored to visible carriers. Load `references/prompt-principles.md` when abstract intent needs detailed translation.

## AI-Flavor And Logic Pass

Before returning a final prompt, do a concise language and logic scan: every sentence should name something visible/audible, performable, lit, framed, timed, or inherited by a connected segment. Remove prompt-flavored filler, unsupported off-screen causes, forced conclusion sentences, and abstract explanations that do not control generation.

For heavy natural-language cleanup, use `aigc-natural-language-prompt`. For Seedance-specific language examples and logic checks, load `references/prompt-principles.md`.

### Confirmation Policy

Default to self-judgment and produce the prompt directly. Ask the user before finalizing only when ambiguity changes the actual creative direction or generation strategy:

- The main character or reference asset role is unclear.
- Two reference images or videos conflict in identity, style, action, or setting.
- The same request could reasonably become different shot designs.
- The prompt requires a tradeoff between stability and a complex visual idea.

Do not interrupt the user merely to ask whether an ordinary simple shot should be short.

## References

Load references only when they materially change the answer:

- Read `references/prompt-principles.md` when the task needs creative completion, shot design, style handling, long-form continuity, prompt efficiency, or translation from abstract intent into visible action.
- Read `references/single-segment-quality-control.md` before finalizing new or optimized video prompts when a scene has multiple subjects, large actions, occlusion, complex blocking, unclear camera movement, or weak continuity.
- Read `references/seedance-2-rules.md` when the task needs reference image/video handling, video edit, video extension, shot bridge, official Seedance 2.0 constraints, or a complex final prompt. For simple pure text-to-video, use the rules already in this SKILL.md.
- Read `references/task-patterns.md` when the request targets a specific format such as product ads, UGC, creative VFX, dialogue drama, music beat sync, one-take, educational visualization, or multi-video fusion.
- Read `references/examples.md` only as an optional calibration aid when the output shape is unfamiliar. Do not load examples for routine Seedance prompts.
- Use `aigc-natural-language-prompt` as the cross-skill standard when the user is primarily asking how to make prompt language more natural, director-style, visible, and non-parameterized rather than asking for Seedance-specific final drafting.

## Prompt Contract

Write the final prompt in Chinese by default. Do not include English shot-size abbreviations or English camera movement terms unless the user explicitly asks for bilingual camera labels.

The final prompt should normally start with duration and scene overview, and the opening overview paragraph must end with `无配乐，无字幕。` for every final Seedance prompt. This phrase does not mean silence: diegetic speech, environment sound, and necessary action sound may still be written when the shot needs them.

For ordinary pure text-to-video requests, use the Vibe-first simple structure: one overview paragraph that names the emotional theme, visual anchors, action/state, and local tone, then each shot as a natural Chinese paragraph beginning with `镜头N：x秒，景别。` and continuing in flowing sentences with verbs and connectives. Do not add a separate `稳定边界` section for these prompts.

For complex reference-heavy or composition-critical requests, use the complex structure: total duration and global constraints, a short `参考图使用` section for literal `@...` role mapping, camera/composition requirements when necessary, and shot paragraphs. Add `生成注意` only for high-risk constraints that cannot be integrated into the shot body. For a true one-shot design, use only `镜头1：x秒，景别。` and describe the internal continuous action order in prose.

Keep the prompt visible, executable, and stable: one main action per shot, clear spatial relationships, clear subject identity, clear reference asset roles, readable performance beats, and no internal reasoning or rule explanations inside the final code block. Use production shorthand and abstract taste words only for internal planning; translate them into visible shot, action, light, space, body/contact detail, gaze, expression transition, camera-subject relationship, action path, environmental reaction, sound, and only the edit-handoff details that matter.

### Final Guardrails

Before returning a final prompt, keep these high-frequency checks in the main path:

- Write shot bodies as natural Chinese prose with visible subjects and verbs, not comma-chained parameter lists.
- Preserve literal `@...` anchors and immediately attach each one to a semantic role.
- Keep one main action and one main camera movement per shot; split overloaded beats instead of compressing them.
- Describe what is in the frame before considering what to exclude. Avoid broad negative "do not show X" wording unless X is a hard safety, text/logo/watermark, identity-drift, or user-explicit risk.
- Replace negative tag lists and abstract taste words with positive visible staging and concrete carriers.

For the full Chinese camera term list and extended failure checklist, load `references/seedance-2-rules.md` and `references/single-segment-quality-control.md` only when the task is complex, reference-heavy, or the draft is failing one of these guardrails.
