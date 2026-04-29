---
name: cinematic-storyboard-enhancer
description: Write bilingual image-to-image edit prompts for Nano Banana series (currently Nano Banana Pro / Gemini image editor) or ChatGPT image editor series (currently ChatGPT Images 2.0) after diagnosing why a storyboard, keyframe, concept art, or AI still lacks cinematic quality, while preserving the subject. Use when the user has an image and explicitly wants an edit prompt, image repair prompt, cinematic enhancement prompt, color/lighting prompt, Nano Banana prompt, ChatGPT Images prompt, OpenAI image prompt, Gemini image prompt, or before/after cinematic transformation. If the user only says the image feels wrong, ugly, AI-looking, or "说不上来哪里怪" and does not ask for an edit prompt yet, prefer aigc-shot-diagnose first.
---

# Cinematic Storyboard Enhancer

This skill turns a flat-looking storyboard or AI-generated still into a cinematic frame by **diagnosing what's wrong**, then **writing a precise image-to-image prompt** that fixes it while preserving the subject the user already likes.

## When to use

The user has an image (usually a storyboard panel, keyframe, or AI-generated still) that *almost* works but feels uncinematic — washed out, lit wrong, color-polluted, with subjects that look pasted on top of the background. They want a prompt they can paste into **Nano Banana series** or **ChatGPT image editor series** to fix it.

If the user only wants to understand why an image feels wrong and has not asked for a ready edit prompt, route the task to `aigc-shot-diagnose` first.

The user does NOT want you to redraw the image yourself. They want a **diagnosis report + a ready-to-paste prompt**.

## The core philosophy

A "cinematic" image is not a style — it's a set of disciplined choices a real cinematographer makes about light, color, and atmosphere. Most AI-generated images fail to feel cinematic because they violate one or more of these choices. Your job is to identify *which* choices are being violated, name them in cinematography vocabulary, and write a prompt that corrects them surgically without destroying what already works.

The output is always **two artifacts**:
1. **A diagnosis report** — what's wrong, in plain language plus cinematography terms
2. **A bilingual edit prompt (中文 + English)** — image-to-image instructions in `[Preserve] / [Transform] / [Avoid]` format, tuned for the user's chosen target model

## Workflow

### Step 1 — Read the source image carefully

Before diagnosing anything, describe what's actually in the frame, neutrally. This forces you to look instead of pattern-matching. Cover:

- **Subject & blocking**: who/what is in frame, where they are, what action
- **Composition**: camera angle, focal length feel, framing (close/medium/wide), rule-of-thirds or centered, depth layers (foreground / midground / background)
- **Light**: direction of the dominant light, hardness (hard shadow edges vs soft falloff), apparent source (sun / moon / window / fire / fill)
- **Color**: dominant hue family, secondary hue, where saturation lives, whether shadows and highlights agree on a temperature
- **Atmosphere**: fog/haze density, where it sits in depth, whether it adds depth or flattens depth
- **Mood read**: what the image currently *says* emotionally, in one sentence

If the user uploaded a **second image as a reference target**, do this same neutral read for it too, then explicitly note 5-8 differences. Those differences become the transformation list.

If the user provides a handoff block from `aigc-shot-diagnose`, use it as the starting diagnosis. Verify it against the image, correct only obvious mismatches, and avoid repeating a full diagnosis unless the handoff is missing or clearly insufficient.

### Step 2 — Diagnose against the 8 cinematic dimensions

Read `references/diagnostic-dimensions.md` and walk through each of the 8 dimensions in order. For each, write one of:

- ✅ **Working** — leave alone
- ⚠️ **Weak** — needs adjustment, describe how
- ❌ **Broken** — actively hurting the image, must be fixed

Be specific. "Lighting feels off" is not a diagnosis. "The key light is hard, top-down, and over-saturated cyan, while the subject's fill light disagrees in temperature — this is what makes the foreground figures feel pasted on" is a diagnosis.

The 8 dimensions are:
1. Light direction & hardness
2. Lighting ratio & black point
3. Color temperature unity (removing color pollution)
4. Overall exposure & midtone control
5. Atmospheric perspective (haze / fog logic)
6. Subject-environment light integration
7. Compositional depth & layer rhythm
8. Color emotion consistency

### Step 3 — Decide what to preserve vs. transform

This is the most important judgment call. Most AI-image users get burned because they ask the model to "improve" the image and it redraws faces, changes poses, swaps costumes. Your prompt must explicitly lock down what's working.

Default lock-list (preserve unless user says otherwise):
- All character faces, hair, identity features
- Costume design, props, accessories
- Pose, blocking, character positions in frame
- Camera angle and framing
- Number and identity of characters (no adding/removing)

Default transform-list (these are fair game):
- Lighting (direction, hardness, color, intensity)
- Color grade (temperature, saturation, contrast)
- Atmosphere (fog density, depth gradient)
- Black point and highlight roll-off
- Edge light / rim light on subjects (to integrate them with environment)

### Step 4 — Choose the target model and write the bilingual edit prompt

Use one skill for both models; only the final prompt template changes.

- If the user says **Nano Banana**, **Nano Banana Pro**, **Gemini image**, **Gemini 3 Pro Image**, **Google image editor**, or a later Nano Banana/Gemini image version, use the Nano Banana template.
- If the user says **ChatGPT Images 2.0**, **GPT image 2.0**, **GPT image**, **OpenAI image**, **ChatGPT image editor**, or a later ChatGPT/OpenAI image editor version, use the ChatGPT Images template.
- If the user names a target model, output only that model's prompt.
- If the user does not name a model, ask once which model they plan to use. If they do not answer, ask for compatibility, or want to compare, output both versions.

Read `references/prompt-templates.md` for the current template structure for Nano Banana Pro and ChatGPT Images 2.0. For later model versions, apply the closest template and mention briefly that the version-specific behavior is based on the current documented template unless the user provides newer constraints.

Read `references/cinematic-language.md` for the precise vocabulary to reach for. Vague words ("moody", "epic", "cinematic") are weak — these models respond much better to specific cinematography terms ("low-key lighting at 1:8 ratio", "teal-and-shadow grade with lifted blacks at IRE 12", "single soft moonlight key from camera-left at 30°").

Output **both Chinese and English** versions. They should be semantic mirrors, not literal translations — Chinese and English cinematography vocabulary don't map 1:1, and each language has terms the models recognize better.

### Step 5 — Present the result

Use this structure for the final response:

```
## 视觉诊断
[Step 1 neutral read in 3-4 sentences]

## 八维评估
[Table or list with status for each dimension]

## 核心问题
[Top 3 issues, ranked by impact]

## 优化策略
[What to preserve, what to change, in plain language]

## 中文提示词
[Full prompt in Chinese, formatted for the chosen model]

## English Prompt
[Full prompt in English, formatted for the chosen model]

## 使用说明
[Which model this is tuned for, how to paste it, what to expect]
```

If outputting both models, keep the diagnosis and strategy shared in Chinese, then provide separate Nano Banana and ChatGPT Images prompt sections.

## What good looks like

A good output for this skill should make the user think: "Ah, *that's* why my image felt off — I wouldn't have been able to name it, but now I can." The diagnosis should teach them cinematography vocabulary while solving their immediate problem. The prompt should produce an image that looks like a deliberate creative choice, not a "filtered" version of the original.

## What to avoid

- **Don't be vague.** "Make it more cinematic" in the output prompt is failure — the prompt itself must be specific enough that another cinematographer could shoot it.
- **Don't redraw the user's image yourself.** This skill outputs a prompt; it does not call image generation tools.
- **Don't change what the user didn't ask to change.** If the diagnosis says "the costume is fine" then the [Preserve] block must explicitly protect the costume.
- **Don't pile on every possible improvement.** Pick the 3-5 highest-leverage changes. A surgical prompt outperforms a maximalist one — image editors lose precision when given too many transformation directives at once.
- **Don't translate Chinese cinematography vocabulary literally into English.** "电影感" is not "movie feeling" — it's "cinematic quality" or, more precisely, named techniques like "low-key lighting", "anamorphic compression", "film stock emulation".

## Reference files

- `references/diagnostic-dimensions.md` — Full criteria for the 8 dimensions, with examples of "working / weak / broken" for each
- `references/cinematic-language.md` — Vocabulary library: lighting terms, color grading terms, lens language, atmosphere terms, in both Chinese and English
- `references/prompt-templates.md` — Current prompt structure templates for Nano Banana Pro and ChatGPT Images 2.0, with model-specific quirks documented
