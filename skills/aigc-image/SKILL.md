---
name: aigc-image
description: Use when the user wants a final ready-to-paste image prompt for GPT Image 2, Nano Banana, Seedream 5.0 Pro, Midjourney, or another image model from a text brief, existing prompt, readable image, frame, storyboard panel, product image, or multiple visual references; also use for visual diagnosis, production readiness, reverse prompting, source-faithful image-edit prompts, reference matching, platform adaptation, settings changes, prompt optimization, or diagnose-then-edit. Require the actual readable image only for source-dependent visual claims. Do not use when the user wants only direct generation or editing with no prompt or diagnosis artifact, or when the requested final artifact is a video prompt.
---

# AIGC Image

Own four image artifacts: `diagnose`, `generate`, `reverse`, and `edit`. Share one neutral source read and one evidence ledger whenever a readable image is involved. Keep internal control complete, but expose only the constraints the target model needs. Do not make the user route between separate image-prompt skills.

This skill analyzes images and writes prompts. If the user asks for an image to be generated or modified directly, use the available image-generation/editing capability instead of returning only a prompt.

## 1. Gate the source

Pure text-to-image generation and optimization of a text-only prompt can proceed from the brief. Before making claims about an existing image or writing a source-dependent diagnose, reverse, or edit artifact, confirm that the actual source is readable in the current context.

- A filename, URL label, old summary, diagnosis handoff, or remembered image is not the source image.
- If a required source is missing, ask the user to attach it and stop only the source-dependent workflow. Do not request an image for a complete text-to-image brief.
- If an image is small, blurred, cropped, or blocked, name the unreadable region and use only verifiable evidence.
- For multiple images, identify each role: source, identity, style axis, pose, composition, environment, edit target, or variation target.
- If roles are materially ambiguous, explain the likely mapping, recommend one interpretation, and ask one focused question.

## 2. Select the terminal artifact

Choose internally from:

- `diagnose`: explain why the frame works or fails, rank fixes, or judge `can proceed / repair first / redesign first`.
- `generate`: turn a text brief or an existing image prompt into a final text-to-image prompt without claiming an unseen source image.
- `reverse`: reconstruct or adapt the visible image as a text-to-image prompt.
- `edit`: write a closed-scope image-to-image repair or transformation prompt.
- `diagnose -> edit`: when the user explicitly asks both, inspect once, diagnose briefly, then deliver the edit prompt in the same response.

Record platform adaptation, settings changes, or optimization of an existing image prompt as operations, not additional artifacts. Preserve whether the base prompt is generation or editing. A text-only operation may proceed without the source image when it makes no new source-dependent visual claim.

If the request says only `处理一下`, `优化一下`, or otherwise leaves the final artifact unclear, state your current interpretation and ask what they want to receive. Do not guess between actual generation/editing, diagnosis, a new text-to-image prompt, reverse prompting, and an edit prompt.

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

- `exact lock`: literal text, subject count, protected identity, user-quoted names, exact reference anchors, and user-retained platform settings or values.
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
| generate | none | one named provider file; for unknown, Midjourney, or genuine multi-platform delivery, `references/generation-platform-adapters.md` |
| reverse | `references/mode-reverse.md` | for one supported provider, its matching file below; for unknown, Midjourney, or genuine multi-platform delivery, `references/generation-platform-adapters.md` plus only the files for supported providers the user named |
| edit | `references/mode-edit.md` | `references/edit-platform-templates.md` only for `controlled` or `specification`; one named provider file; for multi-platform delivery, `references/generation-platform-adapters.md`; `references/cinematic-language.md` only for applicable cinematic repair |
| diagnose -> edit | diagnose references, then edit references | read the image only once |

Provider files: `references/platform-gpt-image-2.md`, `references/platform-nano-banana.md`, and `references/platform-seedream-5-pro.md`. For a single-provider request, load only its matching file. For a genuine multi-platform request, load the router and only the matching files for the supported providers explicitly named; never load an unmentioned provider file.

Do not load cinematic vocabulary for product cleanup, simple dust/glare removal, graphic design, or non-photoreal work unless the user requests that treatment.

## 6. Communicate creative uncertainty

Do not optimize for silence. When a creative ambiguity changes identity, expression, composition, medium, reference roles, edit scope, or the meaning of the result:

1. State the visible evidence.
2. State your current interpretation.
3. Name the meaningful alternatives.
4. Recommend one direction and explain why.
5. Ask 1-3 related questions together.

Resolve formatting, ordinary platform wording, and non-material technical details yourself.

## 7. Use the minimum sufficient prompt

The evidence ledger may be detailed; the delivered prompt must not be detailed merely to display expertise. Include only information that changes the target image, protects a costly invariant, assigns a reference role, or makes an ambiguity executable.

Compile the model-facing prompt in this order and stop as soon as it is sufficient:

1. `target`: name the exact subject, object, region, or whole-image goal.
2. `visible endpoint`: state what the result should visibly become, using concrete nouns, verbs, and spatial relations.
3. `integration`: add only the reconstruction, contact, perspective, occlusion, light, shadow, or material behavior needed to make changed pixels belong in the image.
4. `locks`: name only costly or likely-to-drift invariants, then use one general `everything else unchanged` boundary in edit mode.

Translate abstract intent such as `更高级`, `更有电影感`, `更自然`, or `质感更好` into visible consequences before delivery. Do not leave a mood adjective as the only instruction, invent unsupported visual treatment, explain the diagnosis inside the prompt, or repeat the same boundary in both positive and negative language.

Choose the lightest useful shape internally:

- `surgical`: one local edit or one simple scene. Use 1-3 direct natural-language sentences. Do not add section headings or restate the whole source image.
- `controlled`: several linked changes or identity, geometry, layout, brand, or text locks. Use compact `Change` and `Keep` sections. Add one short exclusion only for a likely drift that those sections cannot prevent.
- `specification`: multi-reference compositing, exact typography, dense layout, or several independent spatial relationships. Use short labeled blocks so roles and constraints remain auditable.

Do not fill subject, camera, lens, lighting, palette, material, atmosphere, and style fields just because a template contains them. Omit any field that the user, readable source, or intended result does not make consequential. Prefer one coherent visual direction over competing style words.

For an image that is already close, write the smallest next edit instead of rebuilding a longer master prompt. Keep model name, aspect ratio, resolution, quality, output format, seed, and API/UI controls outside the visual prompt unless the target surface has no separate control and the user needs the value embedded. Delete any sentence whose removal would not change the visible result, protect a real failure boundary, or clarify a reference role.

## 8. Output the requested artifact

- `diagnose`: neutral observation -> likely intention -> decisive findings -> top fixes -> readiness when requested. Do not append a prompt unless requested.
- `generate`: default to one minimum-sufficient Chinese prompt and one English semantic mirror in separate fenced blocks.
- `reverse`: default to semantically matched Chinese and English alternatives. Put the `中文` and `English` labels outside two separate fenced code blocks; never combine both languages in one block.
- `edit`: default to one compact Chinese edit instruction and one semantically matched English alternative. Put the `中文` and `English` labels outside two separate fenced code blocks. Use headings inside the prompt only when the controlled or specification shape needs them.
- `one language only`: return one fenced block in the requested language.
- `prompt only`: return only the language label or labels and the requested fenced prompt block or blocks, with no diagnosis, routing note, or teaching wrapper.

The bilingual blocks are alternatives for copying, not one bilingual prompt to submit together. Preserve exact visible copy in its original language in both versions unless the user explicitly requests translation.

Non-photoreal media keep their own design logic. Do not force film stock, realistic skin, IRE, lens-brand, or live-action grading language onto animation, illustration, stylized 3D, or graphic work.

## 9. Final check

Before delivery, verify:

- every visual claim comes from the readable image or is clearly marked as inference
- generate mode is grounded in the supplied brief or existing prompt and does not pretend to have inspected an image
- subject count, identity, pose, action, composition, text, and reference roles did not drift
- edit mode changes only authorized fields and states any released protection explicitly
- reverse mode rebuilds the whole target image rather than using edit-language shortcuts
- Chinese and English prompts are semantic mirrors when both are requested
- Chinese and English occupy separate fenced blocks and are not concatenated into one model input
- no empty template section, repeated synonym, generic quality stack, generic negative list, or full-source restatement makes the prompt longer than the task requires
- every prompt sentence changes the visible target, protects a real boundary, or assigns a necessary role
- no platform parameter stack, unsupported backstory, new person, prop, logo, text, or style leakage appeared
- requested platform settings are preserved outside the visual prompt whenever the target surface exposes separate controls
- the response contains exactly the artifact the user requested

## Failure recovery

| Trigger | First action | If unresolved |
| --- | --- | --- |
| Missing or unreadable required source | Request the actual image or a useful crop. | Return no visual diagnosis or source-dependent prompt; continue only if the user instead chooses text-only generation. |
| Ambiguous multi-image roles | Offer the most likely mapping and ask one role question. | Keep unassigned fields neutral. |
| Requested edit releases identity, pose, camera, or count | Name the released locks before drafting. | Treat it as redesign, not conservative repair. |
| No visible functional failure | Say the image works for the stated intention. | Separate optional taste refinements; do not manufacture problems. |
| Too many independent edits | Explain the conflict and recommend a staged order. | Ask before splitting; if the user keeps one integrated pass, include every requested edit and state the stability risk rather than silently dropping changes. |

## Avoid

- Do not call an image-generation tool when the user asked only for a prompt.
- Do not return only a prompt when the user asked for the edit to be performed.
- Do not diagnose from filenames, memory, or handoff prose.
- Do not import the whole content of a reference assigned to one narrow role.
- Do not turn every image into live-action cinema.
- Do not rewrite a source-faithful edit as a new text-to-image scene.
