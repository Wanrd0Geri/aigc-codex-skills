---
name: aigc-image-edit-prompt
description: Write image-to-image edit prompts for Nano Banana/Gemini image editors or ChatGPT/OpenAI image editors only when the actual source image is present or attached. Use when the user has an image and explicitly wants a repair/edit/cinematic enhancement prompt while preserving subject identity. If the user only asks why an image feels wrong, route to aigc-visual-diagnose first.
---

# AIGC Image Edit Prompt

This skill turns a flat-looking storyboard or AI-generated still into a cinematic frame by **diagnosing what's wrong**, then **writing a precise image-to-image prompt** that fixes it while preserving the subject the user already likes.

## When to use

The user has an image (usually a storyboard panel, keyframe, or AI-generated still) that *almost* works but feels uncinematic — washed out, lit wrong, color-polluted, with subjects that look pasted on top of the background. They want a prompt they can paste into **Nano Banana series** or **ChatGPT image editor series** to fix it.

If the user only wants to understand why an image feels wrong and has not asked for a ready edit prompt, route the task to `aigc-visual-diagnose` first.

The user does NOT want you to redraw the image yourself. They want a **diagnosis report + a ready-to-paste prompt**.

## The core philosophy

A "cinematic" image is not a style — it's a set of disciplined choices a real cinematographer makes about light, color, and atmosphere. Most AI-generated images fail to feel cinematic because they violate one or more of these choices. Your job is to identify *which* choices are being violated, name them in cinematography vocabulary, and write a prompt that corrects them surgically without destroying what already works.

The default output has **two artifacts** unless the user asks for prompt-only output:
1. **A diagnosis report** — what's wrong, in plain language plus cinematography terms
2. **A bilingual edit prompt (中文 + English)** — image-to-image instructions in `[Preserve] / [Transform] / [Avoid]` format, tuned for the user's chosen target model

## Workflow

### Step 1 — Read the source image carefully

Before writing any edit prompt, confirm the actual source image or frame is present in the current context. If it is not present, do **not** write a prompt from a text-only handoff summary; ask the user to re-attach the image and confirm the frame first. A handoff summary is context, never a substitute for the source image.

Before diagnosing anything, describe what's actually in the frame, neutrally. This forces you to look instead of pattern-matching. Cover:

- **Subject & blocking**: who/what is in frame, where they are, what action
- **Composition**: camera angle, focal length feel, framing (close/medium/wide), rule-of-thirds or centered, depth layers (foreground / midground / background)
- **Light**: direction of the dominant light, hardness (hard shadow edges vs soft falloff), apparent source (sun / moon / window / fire / fill)
- **Color**: dominant hue family, secondary hue, where saturation lives, whether shadows and highlights agree on a temperature
- **Atmosphere**: fog/haze density, where it sits in depth, whether it adds depth or flattens depth
- **Medium**: live-action photoreal, 2D animation, stylized 3D, illustration, concept art, product render, or mixed media.
- **Mood read**: what the image currently *says* emotionally, in one sentence

If the user uploaded a **second image as a reference target**, do this same neutral read for it too, then explicitly note 5-8 differences. Those differences become the transformation list.

If the user provides a handoff block from `aigc-visual-diagnose`, use it as the starting diagnosis. Verify it against the image, correct only obvious mismatches, and avoid repeating a full diagnosis unless the handoff is missing or clearly insufficient.

### Step 2 — Diagnose the highest-impact cinematic problems

Read `references/diagnostic-dimensions.md` as an internal scan. Check all 8 dimensions, then rank the findings by how much they hurt the image. Do not output a full 8-row matrix unless the user explicitly asks for detailed grading.

In the user-facing diagnosis, name only the decisive findings: usually the top 3 issues, or up to 5 for a complex image. Be specific. "Lighting feels off" is not a diagnosis. "The key light is hard, top-down, and over-saturated cyan, while the subject's fill light disagrees in temperature" is a diagnosis.

Identify the medium before choosing vocabulary. For live-action photoreal images, cinematography terms such as lighting ratio, black point, film stock, or lens feel may help. For 2D animation, stylized 3D, illustration, or game-cutscene frames, redefine quality around clean silhouette, readable color blocks, design consistency, material hierarchy, character identity stability, and rhythmized motion. Drop photoreal vocabulary such as film grain, IRE, film stock, anamorphic compression, or realistic skin texture when it would push the edit away from the intended non-photoreal style.

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

Read `references/prompt-templates.md` for the current model templates and adaptive surface-cleanliness controls. For later model versions, apply the closest template unless the user provides newer constraints.

Read `references/cinematic-language.md` only when you need precise cinematography vocabulary. Do not load it just to produce generic "more cinematic" phrasing; use it to sharpen specific lighting, color, lens, atmosphere, or grade choices.

Before outputting any final edit prompt, preserve the chosen image-editor template while enforcing visible edit targets, concrete outcomes, and no keyword stuffing. Use `aigc-natural-language-prompt` only when the draft has template voice, abstract filler, unclear visual logic, or the user asks for natural-language cleanup.

Before output, run a natural-description pass on both Chinese and English prompts:

- For general natural-language rewrites or teaching requests, use `aigc-natural-language-prompt`; inside this image-edit skill, apply that standard to the edit directives while preserving `[Preserve] / [Transform] / [Avoid]`.
- Keep `[Preserve]`, `[Transform]`, and `[Avoid]`, but write each directive as an edit instruction with a visible outcome, not as a stack of labels.
- Every transform line should say what changes and where it is visible: light direction on the subject, shadow density in the background, haze depth between layers, rim light on edges, color temperature in highlights/shadows.
- Prefer 3-7 high-leverage transform directives. More directives usually make image editors average the request instead of following it.
- Do not use generic boosters such as `make it cinematic`, `high quality`, `masterpiece`, `ultra detailed`, `高级感`, `大片感`, or `氛围拉满`. Translate them into concrete lighting, grade, contrast, atmosphere, material, or composition changes.
- Chinese and English versions should be semantic mirrors. Do not let the English become a keyword prompt while the Chinese stays natural, or vice versa.

For ChatGPT Images 2.0 / GPT-image style outputs, explicitly check whether the source or desired edit risks **碎裂感 / fragmented rendering**: noisy micro-texture, visible brush strokes, painterly surface buildup, broken edges, over-detailed ornaments, or patchwork concept-art texture. If present, use the adaptive surface-cleanliness controls in `references/prompt-templates.md`. Add only the level needed for the image:

- Clean source, prevention only: a light preserve/transform guard that keeps the source's clean surface quality and clear large shapes.
- Mild issue: 1-2 positive structure terms in `TRANSFORM`.
- Clear issue: 2-3 positive terms plus 1-3 matching negatives.
- Severe issue: a compact `surface cleanliness` directive plus targeted negatives.

Do not paste the whole texture-control vocabulary into every prompt. If the diagnosis is about lighting, color, depth, or subject integration and the surfaces are already clean, omit heavy negative terms.

Output **both Chinese and English** versions by default. If the user asks for one language only, provide that language and keep the same edit intent.

### Step 5 — Present the result

Use this default structure for the final response:

```
## 视觉诊断
[Step 1 neutral read in 3-4 sentences]

## 核心问题
[Top 3 issues, ranked by impact. Use up to 5 only when needed.]

## 优化策略
[What to preserve, what to change, in plain language]

## 中文提示词
[Full prompt in Chinese, formatted for the chosen model]

## English Prompt
[Full prompt in English, formatted for the chosen model]

## 使用说明
[Which model this is tuned for, how to paste it, what to expect]
```

If the user asks for a full diagnostic matrix, add `## 八维评估` before `## 核心问题`. Otherwise keep the detailed rubric internal.

If outputting both models, keep the diagnosis and strategy shared in Chinese, then provide separate Nano Banana and ChatGPT Images prompt sections.

## What good looks like

A good output for this skill should make the user think: "Ah, *that's* why my image felt off — I wouldn't have been able to name it, but now I can." The diagnosis should teach them cinematography vocabulary while solving their immediate problem. The prompt should produce an image that looks like a deliberate creative choice, not a "filtered" version of the original.

## What to avoid

- **Don't be vague.** "Make it more cinematic" in the output prompt is failure — the prompt itself must be specific enough that another cinematographer could shoot it.
- **Don't redraw the user's image yourself.** This skill outputs a prompt; it does not call image generation tools.
- **Don't change what the user didn't ask to change.** If the diagnosis says "the costume is fine" then the [Preserve] block must explicitly protect the costume.
- **Don't pile on every possible improvement.** Pick the 3-5 highest-leverage changes. A surgical prompt outperforms a maximalist one — image editors lose precision when given too many transformation directives at once.
- **Don't translate Chinese cinematography vocabulary literally into English.** "电影感" is not "movie feeling" — it's "cinematic quality" or, more precisely, named techniques like "low-key lighting", "anamorphic compression", "film stock emulation".
- **Don't let the final prompt read like a parameter dump.** Keep the block structure, but make the wording describe visible edits a model can apply to the source image.

## Reference files

- `references/diagnostic-dimensions.md` — internal 8-dimension scan; output only the highest-impact findings unless the user asks for full grading.
- `references/prompt-templates.md` — current model templates plus adaptive surface-cleanliness controls.
- `references/cinematic-language.md` — optional vocabulary lookup for precise lighting, color, lens, and atmosphere terms.
