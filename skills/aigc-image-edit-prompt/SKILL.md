---
name: aigc-image-edit-prompt
description: Use when the user has an attached image or frame and asks for a Nano Banana/Gemini, ChatGPT/OpenAI, or other image-to-image repair/edit prompt, including cinematic frame repair, conservative cleanup, product-image cleanup, subject integration, reference matching, or prompt-only delivery while preserving protected identity, geometry, text, camera, composition, medium, or design choices.
---

# AIGC Image Edit Prompt

This skill inspects an existing image, identifies only the changes the user actually wants, and writes a precise image-to-image edit prompt that protects everything outside that edit scope. Cinematic repair is one mode, not the default for every image.

Cross-skill routing in this file assumes the companion AIGC skills are installed. If a named skill is unavailable, apply its core constraint yourself instead of blocking (e.g. without `aigc-visual-diagnose`, run the neutral read and diagnosis inside this skill).

## Scope and routing

Handle storyboard panels, keyframes, AI-generated stills, illustrations, stylized 3D frames, product images, and other source-faithful repair tasks. The deliverable is a prompt the user can paste into a **Nano Banana/Gemini** or **ChatGPT/OpenAI** image editor; do not call an image-generation tool from this skill.

If the user only wants to understand why an image feels wrong and has not asked for a ready edit prompt, route the task to `aigc-visual-diagnose` first.

Default to a concise diagnosis plus a ready-to-paste bilingual prompt. If the user asks for prompt-only output, return only the requested prompt blocks. If the user asks only for diagnosis, route to `aigc-visual-diagnose` and do not append an edit prompt.

## Core contract

Treat image editing as a closed change request:

1. **Protected facts** come from the source image and the user's explicit preserve list.
2. **Allowed changes** are only the user-named edits plus the minimum visible corrections required to make those edits coherent.
3. **Unmentioned content stays unchanged.** Do not treat lighting, grading, haze, depth, rim light, material, background, or surface texture as automatically editable.
4. **Exact text is data.** Quote every protected label, logo, number, or caption exactly and preserve its spelling, count, placement, hierarchy, and legibility unless the user asks to change it.

## Workflow

### Step 1 — Read the source image carefully

Before writing any edit prompt, confirm the actual source image or frame is present in the current context. If it is not present, do **not** write a prompt from a text-only handoff summary; ask the user to re-attach the image and confirm the frame first. A handoff summary is context, never a substitute for the source image.

CHECKPOINT - Source Image Gate:

- If no image is present, stop and ask for the image.
- If the user supplied only a diagnosis summary, use it as context but still ask for the actual source image before writing an edit prompt.
- If the user asks only "why does this look wrong" and does not ask for an edit prompt, route to `aigc-visual-diagnose`.
- If the user asks whether the frame can move into video, route to `aigc-visual-diagnose` for a readiness note before writing image-edit instructions.

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

If a handoff block conflicts with the visible image, trust the visible image and briefly note the correction before drafting.

### Failure Branches

- If the source image is missing, do not write an edit prompt from memory, filename, or diagnosis text; ask for the image.
- If the user has not chosen Nano Banana/Gemini or ChatGPT/OpenAI image editing, ask once for the target model only when the model choice materially changes the edit strategy. If the user asks for compatibility or the request should not pause on model choice, output both templates.
- If the user asks for a full redesign rather than repair, identify what can no longer be preserved before writing a prompt.
- If the requested fix would change face identity, costume, pose, camera angle, or character count, warn and rewrite the prompt to protect those elements unless the user explicitly wants them changed.
- If a prior readiness note says redesign first, do not write a repair prompt as if the frame is usable; state the redesign risk before drafting.

### Step 1.5 — Select the edit intent

Choose one path before diagnosing:

- **Conservative cleanup**: triggered by `只`, `仅`, `保持`, `不要电影感`, `不要重做`, product cleanup, dust removal, glare control, text preservation, or equivalent narrow wording. Treat the user's named changes as the complete transform whitelist. Keep every other visible fact unchanged.
- **Cinematic or art-direction repair**: use only when the user asks for cinematic quality, atmosphere, lighting redesign, visual hierarchy, or subject-environment integration. Diagnose the relevant visual system, then change only the selected high-impact items.
- **Reference matching**: when a second image is a target, transfer only the attributes the user assigns to it; do not copy identity, layout, text, material, or style from the reference unless assigned.
- **Redesign**: when face, costume, pose, camera, character count, product geometry, or scene structure must change, state which protected facts will be released before drafting.

For product or packaging cleanup, lock the product silhouette and proportions, material and color identity, cap/closure, exact label text and typography layout, camera, crop, scale, background/set, contact shadow, and every unrequested prop. Do not add cinematic grading, shallow depth of field, dramatic relighting, new reflections, or a rebuilt set unless explicitly requested.

### Step 2 — Diagnose the highest-impact visible problems

For cinematic or subject-integration work, read `references/diagnostic-dimensions.md` as an internal scan and rank only the relevant findings. For conservative cleanup, product, illustration, graphic, or text-preservation work, inspect the user's whitelist first and skip irrelevant cinematography dimensions. Do not output a full 8-row matrix unless the user explicitly asks for detailed grading.

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

Candidate transform areas are not permission to change them. Select only areas authorized by the user or required by the diagnosed edit: lighting, color, atmosphere, contrast, material response, surface cleanup, subject integration, or background clarity.

### Edit Strength Budget

Choose the smallest edit strength that can fix the image:

- **Light repair**: preserve composition and identity; adjust light direction, contrast, color balance, haze depth, or black point.
- **Medium repair**: preserve subject identity, pose, camera, and main environment; change lighting system, material hierarchy, integration, or background clarity.
- **Heavy repair**: use only when the user accepts redesign risk; state what may change before drafting.

Keep the final prompt surgical. Use the fewest transform and avoid directives that fully express the requested edit. If the request contains many independent changes, separate them into small edit rounds instead of overloading one prompt. If a fix does not affect the visible problem, leave it out.

### Step 4 — Choose the target model and write the bilingual edit prompt

Use one skill for both models; only the final prompt template changes.

- If the user names **Nano Banana**, **Nano Banana Pro**, **Nano Banana 2**, **Gemini image**, **Gemini Image**, or **Google image editor**, use the Gemini-family template without assuming a specific hidden version.
- If the user names **ChatGPT Images**, **gpt-image-2**, **GPT Image**, **OpenAI image**, or **ChatGPT image editor**, use the OpenAI-family template without translating a product label into an invented model behavior.
- If the user names a target model, output only that model's prompt.
- If the user does not name a model and the edit intent is clear, do not block. When both model families can use the same instructions, output one bilingual cross-platform prompt. Split into two provider versions only when the edit strategy, reference indexing, mask instruction, or platform surface genuinely differs.

Read `references/prompt-templates.md` for the current model templates and adaptive surface-cleanliness controls. For later model versions, apply the closest template unless the user provides newer constraints.

Read `references/cinematic-language.md` only when you need precise cinematography vocabulary. Do not load it just to produce generic "more cinematic" phrasing; use it to sharpen specific lighting, color, lens, atmosphere, or grade choices.

Before outputting any final edit prompt, preserve the chosen image-editor template while enforcing visible edit targets, concrete outcomes, and no keyword stuffing. Use `aigc-natural-language-prompt` only when the draft has template voice, abstract filler, unclear visual logic, or the user asks for natural-language cleanup.

Before output, run a natural-description pass on both Chinese and English prompts:

- For general natural-language rewrites or teaching requests, use `aigc-natural-language-prompt`; inside this image-edit skill, apply that standard to the edit directives while preserving `[Preserve] / [Transform] / [Avoid]`.
- Keep `[Preserve]`, `[Transform]`, and `[Avoid]`, but write each directive as an edit instruction with a visible outcome, not as a stack of labels.
- Every transform line should say what changes and where it is visible: light direction on the subject, shadow density in the background, haze depth between layers, rim light on edges, color temperature in highlights/shadows.
- Prefer the fewest high-leverage transform directives that complete the edit. Split unrelated changes into later passes so each result is easier to inspect and correct.
- Do not use generic boosters such as `make it cinematic`, `high quality`, `masterpiece`, `ultra detailed`, `高级感`, `大片感`, or `氛围拉满`. Translate them into concrete lighting, grade, contrast, atmosphere, material, or composition changes.
- Chinese and English versions should be semantic mirrors. Do not let the English become a keyword prompt while the Chinese stays natural, or vice versa.
- Before delivery, compare the Chinese and English blocks line by line: the preserved objects, transform count, locations, measurements, exact text, and avoid boundaries must match. Neither language may introduce an extra cinematographer, film stock, material, style, or edit.

For ChatGPT/OpenAI GPT Image outputs, check whether the source or desired edit risks **碎裂感 / fragmented rendering**: noisy micro-texture, visible brush strokes, painterly surface buildup, broken edges, over-detailed ornaments, or patchwork concept-art texture. This is a diagnosed failure heuristic, not a universal provider property. If present, use the adaptive surface-cleanliness controls in `references/prompt-templates.md`. Add only the level needed for the image:

- Clean source, prevention only: a light preserve/transform guard that keeps the source's clean surface quality and clear large shapes.
- Mild issue: 1-2 positive structure terms in `TRANSFORM`.
- Clear issue: 2-3 positive terms plus 1-3 matching negatives.
- Severe issue: a compact `surface cleanliness` directive plus targeted negatives.

Do not paste the whole texture-control vocabulary into every prompt. If the diagnosis is about lighting, color, depth, or subject integration and the surfaces are already clean, omit heavy negative terms.

Output **both Chinese and English** versions by default. If the user asks for one language only, provide that language and keep the same edit intent.

### Step 5 — Present the result

Use this compact default structure for the final response:

```
## 判断
[1-2 sentences naming the decisive visible problem and edit strength]

## 中文提示词
[Full prompt in Chinese, formatted for the chosen model]

## English Prompt
[Full prompt in English, formatted for the chosen model]

```

If the user asks for detailed analysis, expand to `视觉观察 -> 核心问题 -> 优化策略 -> prompts`. If the user asks for a full diagnostic matrix, add `八维评估`. Otherwise keep the detailed observation and rubric internal. Add usage instructions only when the paste workflow or provider difference is not obvious.

If outputting both models, keep the diagnosis and strategy shared in Chinese, then provide separate Nano Banana and ChatGPT Images prompt sections.

## What good looks like

A good output names the decisive defect without burying the user in a report, protects every source fact outside the edit scope, and gives the editor visible instructions it can execute. The result should look intentionally repaired rather than regenerated or generically filtered.

## What to avoid

- **Don't be vague.** `更高级` or `更有质感` without a visible edit target is failure. Translate it into the smallest relevant change in light, color, material, surface, depth, text, or integration.
- **Don't redraw the user's image yourself.** This skill outputs a prompt; it does not call image generation tools.
- **Don't change what the user didn't ask to change.** If the diagnosis says "the costume is fine" then the [Preserve] block must explicitly protect the costume.
- **Don't pile on every possible improvement.** Keep only the highest-leverage changes for this pass; move unrelated changes into a later pass so drift is easier to detect.
- **Don't translate Chinese cinematography vocabulary literally into English.** "电影感" is not "movie feeling" — it's "cinematic quality" or, more precisely, named techniques like "low-key lighting", "anamorphic compression", "film stock emulation".
- **Don't let the final prompt read like a parameter dump.** Keep the block structure, but make the wording describe visible edits a model can apply to the source image.
- **Don't ignore a prior readiness warning.** If the user carries over a diagnosis that says the frame should be redesigned or repaired first, state that risk before writing an edit prompt.
- **Don't use text-to-image reverse-prompt language.** This skill edits an existing image, so the prompt must protect source identity, blocking, camera, and useful design choices.
- **Don't cinematicize a conservative request.** Product cleanup, dust removal, glare control, label repair, and `不要电影感` are closed-scope edits, not invitations to redesign lighting or staging.

## Reference files

- `references/diagnostic-dimensions.md` — internal 8-dimension scan; output only the highest-impact findings unless the user asks for full grading.
- `references/prompt-templates.md` — current model templates plus adaptive surface-cleanliness controls.
- `references/cinematic-language.md` — optional vocabulary lookup for precise lighting, color, lens, and atmosphere terms.
