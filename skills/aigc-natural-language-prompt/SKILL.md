---
name: aigc-natural-language-prompt
description: Use when the user asks for natural-language AIGC prompt cleanup, 自然语言提示词, 导演讲戏式提示词, prompt 更自然, 去 AI 味, 去模板腔, 不要参数堆叠, or a rough image/video prompt needs visible subject-action-space logic before specialist drafting.
---

# AIGC Natural Language Prompt

Use this skill to turn a rough AIGC idea, parameter list, old prompt, or abstract mood description into a natural-language prompt that reads like a director describing a shot to a camera, animation, lighting, or editing team.

Natural language does **not** mean casual, literary, longer, or more poetic. It means executable visual language: describe what the current frame can see or hear, what has already been established by a previous shot, how the subject acts inside the space, and which continuity anchor is useful when shots need to connect.

This skill is not a mandatory final rewrite layer for every AIGC prompt. Use it when the user asks for natural-language cleanup, when a prompt contains template voice, AI-flavored filler, ambiguous visual logic, unsupported causality, or when another AIGC skill needs a targeted language diagnosis. Do not rewrite a prompt just to force a uniform house style.

## Workflow

1. Identify the target artifact: general AIGC prompt, still-image prompt, image-edit prompt, Seedance/video prompt, multi-shot sequence, or prompt-language critique.
2. Read the source prompt and separate:
   - visible facts already present in the prompt
   - abstract intent that must become visible
   - platform/style constraints that belong in a global setup
   - unsupported off-screen causes or spatial claims
   - AI-flavored filler, template slots, decorative transitions, or forced summary endings
   - prompt-engineering filler that should be removed or translated
3. Apply the natural-language criteria before rewriting. Read `references/natural-language-criteria.md` when the user asks what counts as natural language, when quality is uncertain, or when the prompt contains camera/source/space ambiguity.
4. Use `references/rewrite-patterns.md` when converting parameter stacks, abstract mood words, platform words, off-screen causality, or multi-character action.
5. Read `references/examples.md` only when the user asks for examples, when calibrating a new pattern, or when the output shape is unfamiliar.
6. Write the final prompt in Chinese by default. Use English or bilingual output only when the user asks or the target model requires it.
7. If the final target is clearly Seedance, image editing, visual diagnosis, or creative direction, either hand off to the relevant specialist skill or provide a short handoff note after the natural-language rewrite. Do not add this handoff when the user asked for prompt-only output.

### CHECKPOINT - Do Not Over-Route

Use this skill as a selective language cleanup layer, not as a universal last pass.

- If the user already has a clear final Seedance request, route to `aigc-seedance-prompt`.
- If the user has an image and wants a repair prompt, route to `aigc-image-edit-prompt`.
- If the user has an image and wants reverse prompting, route to `aigc-image-reverse-prompt`.
- If the user asks why a frame looks bad, route to `aigc-visual-diagnose`.
- If the user asks what comes next in production, route to `aigc-project-planner` or `aigc-shot-diagnosis-pipeline` depending on whether the scope is project-level or single-frame.

### Failure Branches

- If the source prompt is too vague to rewrite without inventing visible content, state the missing visible variable and ask one question.
- If the platform target changes the output shape, write the natural-language core first and leave model-specific formatting to the specialist skill.
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
- Remove AI-flavored prose when it does not control the image: promotional adjectives, rule-of-three padding, "not only...but also..." logic, generic conclusions, and explanations of creative intent that the camera cannot see.

## Seedance Preprocessing Boundary

When the source prompt is clearly intended for Seedance but the user asks only for natural-language cleanup, output the cleaned visual core rather than a final Seedance prompt.

Preserve:

- duration, subject identity, main action chain, visible camera relation, dialogue content, and necessary reference roles
- only the continuity anchor needed by the next shot or segment

Remove or translate:

- platform settings such as resolution, frame rate, lens brand, or aspect ratio
- abstract taste words such as `电影感`, `高级感`, `氛围拉满`, or `质感拉满`
- unsupported causes, plot synopsis, and decorative ending summaries

End with a short handoff note to `aigc-seedance-prompt` only when the user has not asked for prompt-only output.

## Specialist Boundaries

- Use `aigc-seedance-prompt` after this skill when the user needs final Seedance/Doubao/Dreamina platform wording, reference mapping, duration, video edit, extension, or shot bridge handling.
- Use `aigc-image-edit-prompt` after this skill when the user has an image and needs a ready `[Preserve] / [Transform] / [Avoid]` edit prompt.
- Use `aigc-creative-director` first when the concept has no story, shot purpose, or visual strategy yet.
- Use `aigc-visual-diagnose` first when the user mainly asks why an image looks weak, cheap, AI-looking, or visually wrong.

## Quality Check

Before final output, scan for these failures:

- comma-chained parameter lists
- unsupported phrases like `风从门口吹来` when the door is not visible or established
- vague style boosters such as `高级感`, `电影感`, `质感拉满`, `high quality`, `masterpiece`, or `ultra detailed`
- emotional labels without visible carriers
- camera directions without a visible subject or frame relationship
- group action without roles, positions, paths, or reactions
- forced ending-state summaries that do not help the next shot connect
- missing continuity anchors only when the next shot depends on pose, gaze, object position, movement direction, light state, or camera position
- over-expanded rewrites that change a compact usable prompt into a long creative brief
- Seedance-specific final formatting when the user only asked for natural-language cleanup
