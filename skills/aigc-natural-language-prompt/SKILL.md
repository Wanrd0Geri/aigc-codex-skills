---
name: aigc-natural-language-prompt
description: Rewrite rough AIGC ideas, keyword stacks, parameter-heavy prompts, or old image/video prompts into natural-language, director-style prompts, and act as the required final language pass before any AIGC skill outputs a prompt. Use when the user asks for natural-language prompts, director-style prompts, prompt more natural, no parameter stacking, 自然语言提示词, 导演讲戏式提示词, prompt 更自然, 不要参数堆叠, or wants to improve prompt narration logic and visible image logic before handing off to Seedance, image editing, or another AIGC specialist skill.
---

# AIGC Natural Language Prompt

Use this skill to turn a rough AIGC idea, parameter list, old prompt, or abstract mood description into a natural-language prompt that reads like a director describing a shot to a camera, animation, lighting, or editing team.

Natural language does **not** mean casual, literary, longer, or more poetic. It means executable visual language: describe what the current frame can see or hear, what has already been established by a previous shot, how the subject acts inside the space, and what visible state the shot ends on.

When another AIGC skill is about to output a final prompt, this skill's contract is the required final language pass. The user should not need to invoke it manually.

## Workflow

1. Identify the target artifact: general AIGC prompt, still-image prompt, image-edit prompt, Seedance/video prompt, multi-shot sequence, or prompt-language critique.
2. Read the source prompt and separate:
   - visible facts already present in the prompt
   - abstract intent that must become visible
   - platform/style constraints that belong in a global setup
   - unsupported off-screen causes or spatial claims
   - prompt-engineering filler that should be removed or translated
3. Apply the natural-language criteria before rewriting. Read `references/natural-language-criteria.md` when the user asks what counts as natural language, when quality is uncertain, or when the prompt contains camera/source/space ambiguity.
4. Use `references/rewrite-patterns.md` when converting parameter stacks, abstract mood words, platform words, off-screen causality, or multi-character action.
5. Read `references/examples.md` only when the user asks for examples, when calibrating a new pattern, or when the output shape is unfamiliar.
6. Write the final prompt in Chinese by default. Use English or bilingual output only when the user asks or the target model requires it.
7. If the final target is clearly Seedance, image editing, visual diagnosis, or creative direction, either hand off to the relevant specialist skill or provide a short handoff note after the natural-language rewrite.

## Output Modes

### Default

Use this structure unless the user asks for prompt only:

````markdown
## 自然语言标准
[3-5 bullets naming the standards used for this rewrite.]

## 原提示词问题
[2-5 bullets naming the specific failures: parameter stack, abstract mood, unsupported off-screen source, unclear cut, missing action endpoint, etc.]

## 改写提示词
```text
[ready-to-copy natural-language prompt]
```

## 后续交接
[If useful: which specialist skill should handle platform-specific drafting next, or "可直接使用".]
````

### Direct Prompt

If the user says `只给提示词`, `直接出稿`, `不要解释`, `prompt only`, or equivalent, output only one fenced code block containing the rewritten prompt.

### Teaching Or Comparison

If the user asks what natural language means, asks for examples, or wants to align standards, show before/after examples and explain the writing logic. Do not produce a final production prompt unless requested.

## Natural-Language Contract

The rewritten prompt must obey these rules:

- Describe only what the current shot can see or hear, or what a previous shot has clearly established.
- Use complete visual sentences with a visible subject, action, spatial relationship, and result.
- Convert abstract words into visible carriers: posture, gaze, contact point, distance, light, shadow, material, sound, timing, or environmental reaction.
- Do not invent off-screen causes. If the source is not visible or established, write the visible result instead.
- For cuts and shot changes, state how the current shot enters the scene: from which previous view, current camera side, framing, and visible retained objects.
- For multiple characters, assign identity, position, role, action, reaction, and endpoint before writing chaotic group movement.
- Keep style terms in global constraints when they matter, but make shot bodies concrete: what enters frame, what moves, what reacts, and what remains at the end.

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
- final shots without a visible ending state
