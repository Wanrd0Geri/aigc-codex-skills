---
name: aigc-natural-language-prompt
description: Use for language-only AIGC prompt cleanup when the user asks for 自然语言提示词, 导演讲戏式提示词, prompt 更自然, 去 AI 味, 去模板腔, 不要参数堆叠, or a rough image/video prompt needs visible subject-action-space logic before specialist drafting. Do not use for a final Seedance/Doubao/Dreamina prompt, ready image-edit or reverse prompt, or visual diagnosis; route those requests to their specialist skills.
---

# AIGC Natural Language Prompt

Use this skill to turn a rough AIGC idea, parameter list, old prompt, or abstract mood description into a natural-language prompt that reads like a director describing a shot to a camera, animation, lighting, or editing team.

Natural language does **not** mean casual, literary, longer, or more poetic. It means executable visual language: describe what the current frame can see or hear, what has already been established by a previous shot, how the subject acts inside the space, and which continuity anchor is useful when shots need to connect.

This skill is not a mandatory final rewrite layer for every AIGC prompt. Use it when the user asks for natural-language cleanup, when a prompt contains template voice, AI-flavored filler, ambiguous visual logic, unsupported causality, or when another AIGC skill needs a targeted language diagnosis. Do not rewrite a prompt just to force a uniform house style.

Cross-skill routing in this file assumes the companion AIGC skills are installed. If a named skill is unavailable, apply its core constraint yourself instead of blocking.

## Workflow

1. Identify the target artifact. Route a request for a final Seedance/Doubao/Dreamina prompt, ready image-edit prompt, reverse prompt, or visual diagnosis before rewriting. Continue here only when language cleanup, critique, or a pre-specialist visual core is the requested artifact.
2. Read the source prompt and separate:
   - visible facts already present in the prompt
   - abstract intent that must become visible
   - platform/style constraints that belong in a global setup
   - platform reference anchors that start with `@`, such as `@图1`, `@视频1`, `@音频1`, or file-name anchors like `@庠序场景.png`, that must remain literal
   - unsupported off-screen causes or spatial claims
   - AI-flavored filler, template slots, decorative transitions, or forced summary endings
   - prompt-engineering filler that should be removed or translated
3. Run the Prompt Safety Preflight before rewriting: lock reference anchors, subject count, character names, shot numbers, duration, dialogue, explicit ending/edit cues, action order, scene location, reference roles, and platform constraints that must survive cleanup.
4. Choose the rewrite intensity and scope. Default to `standard + shot-preserving` unless the user asks for a lighter or stricter edit.
5. Apply the natural-language criteria before rewriting. Read `references/natural-language-criteria.md` when the user asks what counts as natural language, when quality is uncertain, or when the prompt contains camera/source/space ambiguity.
6. Use `references/rewrite-patterns.md` when converting parameter stacks, abstract mood words, platform words, off-screen causality, multi-character action, AI writing cliches, protected anchors, or multi-shot cleanup.
7. Read `references/examples.md` only when the user asks for examples, when calibrating a new pattern, or when the output shape is unfamiliar.
8. Write the final prompt in Chinese by default. Use English or bilingual output only when the user asks or the target model requires it.
9. Run the Two-Pass Review before output: first verify production facts did not drift, then remove residual AI-flavored phrasing if it is still present.
10. When cleanup is complete and specialist work still remains, add one short handoff note. Do not add it for prompt-only output, and do not perform the specialist's final formatting inside this skill.

## Prompt Safety Preflight

Before changing wording, identify the parts that are production controls rather than style. Preserve them exactly unless the user explicitly asks to change them:

- literal `@...` anchors (see Reference Anchor Protection below)
- subject and character count; character names, identity labels, reference-image roles, shot numbers, shot count, duration, timing, dialogue, lyrics, narration text, required silence, and explicit ending/edit cues such as black frame, fade, freeze, or loop point
- main action order, camera relation, scene location, movement direction, visible previous-state handoff, and continuity anchors needed by the next shot
- platform constraints that affect generation control; remove only decorative or redundant platform terms when they do not change the output

Cleaning may soften role wording around a protected span, but it must not normalize, translate, rename, reorder, or drop the protected span itself.

## Reference Anchor Protection

Preserve literal platform reference anchors that start with `@` — ordered labels such as `@图1`, `@视频1`, `@音频1`, and file-name anchors such as `@庠序场景.png` — exactly as written. Cleanup may soften the role wording after an anchor (for example `@图1控制角色外貌` -> `@图1作为角色外貌参考`), but must never remove `@`, rename, translate, reorder, or rewrite the anchor as `参考图1`, `图1`, or a plain file name.

## Rewrite Intensity

Pick the smallest intensity that fixes the real failure.

- `minimal`: remove local AI-flavored filler, template openings, empty ending summaries, repeated quality boosters, or parameter clutter while keeping the original structure.
- `standard`: convert abstract mood, taste words, and prompt-engineering language into visible subject-action-space-control language. This is the default.
- `aggressive`: use only when the prompt is mostly a parameter stack, has incompatible mediums, unclear spatial logic, or missing subject/action relations. Preserve protected spans first, then rebuild the visible prompt.

Do not escalate to `aggressive` just because a prompt contains a few words like `电影感`, `高级感`, or `宿命感`; translate those words into visible carriers inside the current structure when possible.

## Prompt Scope

Scope controls how much structure may change.

- `in-place`: keep sentence count, shot count, order, and paragraph structure. Only lower the wording inside each sentence.
- `shot-preserving`: keep the same shot count, shot order, duration, dialogue, and main action beats, but allow sentence-level cleanup inside each shot. This is the default for multi-shot or Seedance-like prompts.
- `structural`: allow merging, splitting, reordering, or deleting empty prompt sentences only when the user asked for a full rewrite or when the source cannot be made executable without restructuring.

If the source has numbered shots, a storyboard range, or a clear action chain, default to `shot-preserving`. Never reduce three shots to one paragraph unless the user asks for a condensed single prompt.

## Two-Pass Review

Run these checks before final output:

1. **Production-fact pass**: verify every protected anchor, subject count, character, duration, dialogue line, explicit ending/edit cue, shot count, action order, scene location, reference role, and continuity requirement is still present and has not drifted.
2. **Residual-AI pass**: only after pass 1, remove remaining AI writing cliches that do not control generation: generic `高级感/电影感/质感拉满`, `这不仅是...更是...`, forced conclusion sentences, narrator explanations, rule-of-three padding, and abstract intent explanations that the camera cannot see.

The second pass must stay light. Do not rewrite the whole prompt again, add new facts, or change protected spans to make the text sound more human.

## Humanizer Boundary

This skill can borrow AI-writing cleanup signals, but it is not a general prose humanizer. AIGC prompt cleanup should improve generation control, not author voice.

Do not add first-person commentary, humor, personal opinions, literary digressions, intentional messiness, or “more human” chat tone. Do not turn a prompt into an essay about the image. If a humanizer-style request conflicts with visual executability, keep the executable prompt and state the boundary briefly only when needed.

### CHECKPOINT - Do Not Over-Route

Use this skill as a selective language cleanup layer, not as a universal last pass.

- If the user already has a clear final Seedance request, route to `aigc-seedance-prompt`.
- If the user has an image and wants a repair prompt, route to `aigc-image-edit-prompt`.
- If the user has an image and wants reverse prompting, route to `aigc-image-reverse-prompt`.
- If the user asks why a frame looks bad, route to `aigc-visual-diagnose`.
- If the user asks what comes next in production, answer briefly only when it is obvious; otherwise route to `aigc-visual-diagnose` for frame readiness, `aigc-image-edit-prompt` for repair prompts, `aigc-script-context` for long script/storyboard context, or `aigc-seedance-prompt` for final video prompts.

### Failure Branches

- If the source prompt is too vague to rewrite without inventing visible content, state the missing visible variable and ask one question.
- If the user asks only for cleanup and the target platform changes the final shape, write the natural-language core and leave model-specific formatting to the specialist skill. If the requested artifact is already the final specialist output, route before rewriting.
- If a rough prompt mixes several incompatible mediums or styles, choose the dominant visible target and list the discarded conflict.
- If the user asks for prompt-only output, do not include diagnosis, handoff, or teaching notes.
- If the source prompt is already short, clear, and executable, make the smallest useful rewrite instead of expanding it into director prose.

## Output Modes

### Default

Use this structure unless the user asks for prompt only:

````markdown
## 自然语言标准
[3-5 bullets naming the standards used for this rewrite.]

## 原提示词问题
[2-5 bullets naming the specific failures: parameter stack, abstract mood, unsupported off-screen source, unclear cut, forced ending summary, AI-flavored filler, etc.]

## 改写提示词
```text
[ready-to-copy natural-language prompt]
```

## 后续交接
[If useful: which specialist skill should handle platform-specific drafting next, or "可直接使用".]
````

### Direct Prompt

If the user says `只给提示词`, `直接出稿`, `不要解释`, `prompt only`, or equivalent, output only one fenced code block containing the rewritten prompt.

### Lightweight Rewrite

If the user only says `改自然点`, `去 AI 味`, `不要参数堆叠`, `prompt 更自然`, or similar, default to a compact answer:

````markdown
## 改写提示词
```text
[rewritten prompt]
```
````

Do not include standards, diagnosis, or handoff unless the source prompt has a real logic problem the user needs to see.

### Teaching Or Comparison

If the user asks what natural language means, asks for examples, or wants to align standards, show before/after examples and explain the writing logic. Do not produce a final production prompt unless requested.

## Natural-Language Contract

The rewritten prompt must obey these rules:

- Describe only what the current shot can see or hear, or what a previous shot has clearly established.
- Use complete visual sentences with a visible subject, action, spatial relationship, and result.
- Convert abstract words into visible carriers: posture, gaze, contact point, distance, light, shadow, material, sound, timing, or environmental reaction.
- Do not invent off-screen causes. If the source is not visible or established, write the visible result instead.
- For cuts and shot changes, state how the current shot enters the scene: from which previous view, current camera side, framing, and visible retained objects.
- For multiple characters, assign identity, position, role, action, reaction, and only the continuity anchor needed to keep the movement readable.
- Keep style terms in global constraints when they matter, but make shot bodies concrete: what enters frame, what moves, what reacts, and what a later shot needs to inherit.
- Follow Reference Anchor Protection for every `@...` anchor.
- Remove AI-flavored prose when it does not affect the generated image: promotional adjectives, rule-of-three padding, "not only...but also..." logic, generic conclusions, and explanations of creative intent that the camera cannot see.

## Seedance Preprocessing Boundary

When the source prompt is clearly intended for Seedance but the user asks only for natural-language cleanup, output the cleaned visual core rather than a final Seedance prompt.

Preserve:

- duration, subject identity and count, main action chain, visible camera relation, dialogue content, required silence, explicit ending/edit cues, literal `@...` reference anchors, and necessary reference roles
- only the continuity anchor needed by the next shot or segment

Remove or translate:

- platform settings such as resolution, frame rate, lens brand, or aspect ratio
- abstract taste words such as `电影感`, `高级感`, `氛围拉满`, or `质感拉满`
- unsupported causes, plot synopsis, and decorative ending summaries

End with a short handoff note to `aigc-seedance-prompt` only when the user has not asked for prompt-only output.

## Specialist Boundaries

- Use `aigc-seedance-prompt` after this skill when the user needs final Seedance/Doubao/Dreamina platform wording, reference mapping, duration, video edit, extension, or shot bridge handling.
- Use `aigc-image-edit-prompt` after this skill when the user has an image and needs a ready `[Preserve] / [Transform] / [Avoid]` edit prompt.
- If the concept has no story, shot purpose, or visual strategy yet, ask one clarifying question or turn the available idea into visible subject-action-space logic before rewriting.
- Use `aigc-visual-diagnose` first when the user mainly asks why an image looks weak, cheap, AI-looking, or visually wrong.

## Quality Check

Before final output, scan for these failures:

- comma-chained parameter lists; vague style boosters such as `高级感`, `电影感`, `质感拉满`, `high quality`, `masterpiece`, `ultra detailed`
- unsupported off-screen causes, like `风从门口吹来` when the door is not visible or established
- emotional labels without visible carriers; camera directions without a visible subject or frame relationship
- changed subject count or unrequested people, animals, or character-like background figures; group action without roles, positions, paths, or reactions
- decorative ending summaries that do not help the next shot connect; never remove an explicit user-locked black frame, fade, freeze, loop point, or end pose; flag missing continuity anchors when the next shot depends on pose, gaze, object position, movement direction, light state, or camera position
- over-expanded rewrites that change a compact usable prompt into a long creative brief; humanizer-style additions such as first-person opinion, humor, or author commentary
- shot-preserving failures, such as reducing a multi-shot prompt into one undifferentiated paragraph
- missing or normalized-away reference anchors (violations of Reference Anchor Protection)
- Seedance-specific final formatting when the user only asked for natural-language cleanup
