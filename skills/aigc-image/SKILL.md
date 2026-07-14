---
name: aigc-image
description: Use when the user provides an image, frame, keyframe, storyboard panel, product image, or multiple visual references and wants visual diagnosis, production readiness, reverse-engineered bilingual text-to-image prompts, source-faithful image-edit prompts, reference matching, or a combined diagnose-then-edit workflow. Require the actual readable image for visual claims. Do not use when the user wants Codex to perform the image edit or generation itself, or when the requested final artifact is a video prompt.
---

# AIGC Image

Own three image-prompt artifacts: `diagnose`, `reverse`, and `edit`. Share one neutral image read and one evidence ledger across the selected workflow. Do not make the user repeat the image or route between separate image skills.

This skill analyzes images and writes prompts. If the user asks Codex to actually generate or modify an image, use the available image-generation/editing capability instead of returning only a prompt.

## 1. Gate the source

Confirm the actual source image is readable in the current context before making visual claims or writing a source-dependent prompt.

- A filename, URL label, old summary, diagnosis handoff, or remembered image is not the source image.
- If the source is missing, ask the user to attach it and stop the source-dependent workflow.
- If an image is small, blurred, cropped, or blocked, name the unreadable region and use only verifiable evidence.
- For multiple images, identify each role: source, identity, style axis, pose, composition, environment, edit target, or variation target.
- If roles are materially ambiguous, explain the likely mapping, recommend one interpretation, and ask one focused question.

## 2. Select the terminal artifact

Choose internally from:

- `diagnose`: explain why the frame works or fails, rank fixes, or judge `can proceed / repair first / redesign first`.
- `reverse`: reconstruct or adapt the visible image as a text-to-image prompt.
- `edit`: write a closed-scope image-to-image repair or transformation prompt.
- `diagnose -> edit`: when the user explicitly asks both, inspect once, diagnose briefly, then deliver the edit prompt in the same response.

If the request says only `处理一下`, `优化一下`, or otherwise leaves the final artifact unclear, state your current interpretation and ask what they want to receive. Do not guess between actual editing, diagnosis, reverse prompting, and an edit prompt.

If the requested final artifact is a video prompt, let `aigc-video` own the result; provide only image facts or readiness context that materially affects that video task.

## 3. Compile one image fact ledger

Read the frame neutrally before judging it:

- subjects, exact count, visible identity traits, action, pose, gaze, contact, and blocking
- framing, camera relation, crop, subject scale, negative space, foreground/midground/background
- light direction and softness, contrast, color hierarchy, atmosphere, and material response
- medium and design language: photoreal, 2D, stylized 3D, illustration, product render, or mixed media
- text, labels, logos, marks, and their legibility
- what emotion the current image visibly communicates, separated from narrative speculation

Classify every detail:

- `visible`: directly supported and safe to use.
- `inferred`: plausible but not certain; phrase as appearance, not fact.
- `uncertain`: unreadable or ambiguous; omit or flag outside the prompt.

Then classify control:

- `exact lock`: literal text, subject count, protected identity, user-quoted names, or exact reference anchors.
- `semantic lock`: pose, action, relationship, composition, camera relation, medium, and assigned reference role.
- `editable`: only the fields the user authorizes changing.
- `unresolved`: a choice that would produce materially different outputs.

The current visible image overrides an old handoff summary. The latest user instruction overrides older preferences only for the fields it addresses.

## 4. Enforce reference and text boundaries

Treat each reference role as an attribute whitelist. Unassigned attributes are unavailable.

- Composition authorizes geometry, placement, scale, crop, overlap, depth, and negative space; it does not authorize identity, environment, palette, material, light, text, or style.
- Style must be split into assigned axes such as medium, shape language, edge quality, surface flatness, texture density, palette, lighting, or finish.
- Identity does not authorize pose, camera, environment, or lighting.
- Environment does not authorize character identity or camera changes.

For text and marks:

- Preserve fully legible, authorized text exactly.
- Never complete partly legible text from expectation.
- Describe unreadable text only by visible size, color, and placement when needed.
- Do not guess logos, brands, or watermark wording; do not reproduce a watermark.

Read `references/reference-roles-and-text.md` whenever multiple references, visible text, labels, logos, or watermarks are present.

## 5. Load only the selected craft

| Selected workflow | Required reference | Conditional references |
| --- | --- | --- |
| diagnose | `references/mode-diagnose.md` | `references/diagnostic-dimensions.md`, `references/production-design-dimensions.md` |
| reverse | `references/mode-reverse.md` | `references/generation-platform-adapters.md` when a platform is named |
| edit | `references/mode-edit.md`, `references/edit-platform-templates.md` | `references/cinematic-language.md` only for applicable cinematic repair |
| diagnose -> edit | diagnose references, then edit references | read the image only once |

Do not load cinematic vocabulary for product cleanup, simple dust/glare removal, graphic design, or non-photoreal work unless the user requests that treatment.

## 6. Communicate creative uncertainty

Do not optimize for silence. When a creative ambiguity changes identity, expression, composition, medium, reference roles, edit scope, or the meaning of the result:

1. State the visible evidence.
2. State your current interpretation.
3. Name the meaningful alternatives.
4. Recommend one direction and explain why.
5. Ask 1-3 related questions together.

Resolve formatting, ordinary platform wording, and non-material technical details yourself.

## 7. Output the requested artifact

- `diagnose`: neutral observation -> likely intention -> decisive findings -> top fixes -> readiness when requested. Do not append a prompt unless requested.
- `reverse`: default to semantically matched Chinese and English prompt blocks. Keep platform settings outside prompt bodies.
- `edit`: default to concise judgment plus bilingual `[Preserve] / [Transform] / [Avoid]` instructions. Use the fewest transforms that complete the request.
- `prompt only`: return only the requested prompt block or blocks, with no diagnosis, routing note, or teaching wrapper.

Non-photoreal media keep their own design logic. Do not force film stock, realistic skin, IRE, lens-brand, or live-action grading language onto animation, illustration, stylized 3D, or graphic work.

## 8. Final check

Before delivery, verify:

- every visual claim comes from the readable image or is clearly marked as inference
- subject count, identity, pose, action, composition, text, and reference roles did not drift
- edit mode changes only authorized fields and states any released protection explicitly
- reverse mode rebuilds the whole target image rather than using edit-language shortcuts
- Chinese and English prompts are semantic mirrors when both are requested
- no platform parameter stack, unsupported backstory, new person, prop, logo, text, or style leakage appeared
- the response contains exactly the artifact the user requested

## Failure recovery

| Trigger | First action | If unresolved |
| --- | --- | --- |
| Missing or unreadable source | Request the actual image or a useful crop. | Return no visual diagnosis or source-dependent prompt. |
| Ambiguous multi-image roles | Offer the most likely mapping and ask one role question. | Keep unassigned fields neutral. |
| Requested edit releases identity, pose, camera, or count | Name the released locks before drafting. | Treat it as redesign, not conservative repair. |
| No visible functional failure | Say the image works for the stated intention. | Separate optional taste refinements; do not manufacture problems. |
| Too many independent edits | Explain the conflict and recommend a staged order. | Ask before splitting; if the user keeps one integrated pass, include every requested edit and state the stability risk rather than silently dropping changes. |

## Avoid

- Do not call an image-generation tool when the user asked only for a prompt.
- Do not return only a prompt when the user asked Codex to perform the edit.
- Do not diagnose from filenames, memory, or handoff prose.
- Do not import the whole content of a reference assigned to one narrow role.
- Do not turn every image into live-action cinema.
- Do not rewrite a source-faithful edit as a new text-to-image scene.
