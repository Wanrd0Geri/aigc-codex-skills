---
name: aigc-image
description: Analyze readable images and compile or language-repair source-faithful image-edit prompts for GPT Image, Gemini/Nano Banana, Seedream, or another multimodal image editor. Use for image diagnosis, local edits, focus and depth, optical effects, perspective, composition, placement, lighting, palette, material integration, cleanup, or language-only cleanup of an existing image-edit prompt. Also use to ask one artifact question when a static-visual or generic AIGC prompt-cleanup request does not reveal whether it is image generation, image editing, or video. Require readable images for source-dependent claims. Do not perform text-to-image generation, reverse prompting, Midjourney parameter prompting, or final video prompting here; route after the artifact is known.
---

# AIGC Image Editor

Own three terminal artifacts: `diagnose`, `edit-prompt`, and `perform-edit`. Language-only cleanup of an existing image-edit prompt remains `edit-prompt`; it does not require the source image unless the requested wording depends on unseen pixels. Diagnose first only when the user asks why, the requested effect lacks visible support, or the correct edit module is uncertain. Keep the model-facing prompt smaller than the internal analysis.

If the user asks for text-to-image generation, reverse prompting, Midjourney syntax, or a final video prompt, route to the matching specialized skill instead of expanding this skill.

If the user names a project, episode, scene, shot, or current project source and those facts constrain the edit, run `aigc-project-context` first. Consume its `ImageContext` in the same task as source locks and reference roles; do not rebuild the project-source ledger. Do not load project context for unrelated standalone edits.

## 1. Gate the source and terminal artifact

Before any source-dependent claim, confirm that the actual image is readable in the current context.

- A filename, URL label, old summary, prompt, or remembered image is not the source image.
- A text-only edit request may be drafted only when it does not claim facts about an unseen image.
- For language-only cleanup of an existing edit prompt, read [references/language-lint.md](references/language-lint.md). Preserve its exact and semantic locks before changing prose. If the user also requests a new visual decision, leave language-only mode and run the normal evidence and capability workflow.
- For several images, assign each one a narrow role such as scene base, identity, object, composition, or semantic palette.
- If the user asks for an actual edit, use the available image-editing capability. If the user asks for a prompt, do not call the editing capability.
- If the request says only `处理一下`, `优化一下`, or otherwise leaves the terminal artifact unclear, state the likely interpretation and ask whether the user wants diagnosis, an edit prompt, or the edit performed.
- If the supplied text could describe image generation, image editing, or video and no base image, edit target, or motion contract resolves the artifact, do not force it into image editing. Ask one focused artifact question. When several requested visual media or style systems are materially incompatible, ask which dominant medium or target owns the result before routing to its specialist.
- If the same ambiguous text also lacks an executable visible subject, event, or setting, combine the artifact choice and the missing visible choice into that one focused question. Add no author voice, scene, posture, light, sound, or other visual fact before the user answers.

Choose one terminal artifact:

- `diagnose`: explain the visible failure and rank the smallest useful fixes; no prompt unless requested.
- `edit-prompt`: return one ready-to-paste edit instruction.
- `perform-edit`: compile the same closed edit contract internally, call the available image-editing capability with the actual source, then inspect the result against the contract.
- `diagnose -> edit-prompt`: inspect once, diagnose briefly, then compile the authorized repair.

🔴 **CHECKPOINT · 🛑 STOP** when the required image is missing, a required region is unreadable, or image roles would produce materially different edits. Ask one focused question and do not fabricate the source-dependent result.

## 2. Build one source ledger

Record only visible or user-supplied facts:

- subject count, identity traits, pose, gaze, contact, objects, text, and marks
- composition, crop, subject scale, foreground/midground/background, current sharp planes, and occlusion order
- light sources, direction, softness, shadow behavior, exposure hierarchy, color relationships, and atmosphere
- medium, material behavior, edge quality, texture, and visible defects

Classify control:

- `exact lock`: exact text, protected identity, subject count, and user-quoted values
- `semantic lock`: pose, relationship, composition, camera relation, medium, and reference role
- `editable`: only the properties authorized in this request
- `unresolved`: a choice that would produce a materially different result

The visible source overrides older handoff prose. The latest user instruction releases only the locks it names.

For products and packaging, additionally lock silhouette and proportions, closure geometry, material and color identity, exact label copy and hierarchy, crop, scale, set, contact shadow, and unrequested props unless the user releases them.

Read [references/reference-roles-and-text.md](references/reference-roles-and-text.md) whenever multiple images, text, labels, logos, or watermarks are involved.

## 3. Diagnose and select atomic capabilities

For diagnosis, read [references/mode-diagnose.md](references/mode-diagnose.md). Load [references/diagnostic-dimensions.md](references/diagnostic-dimensions.md) or [references/production-design-dimensions.md](references/production-design-dimensions.md) only when that lens contains a real finding.

For any edit, read:

1. [references/mode-edit.md](references/mode-edit.md)
2. [references/edit-contract.md](references/edit-contract.md)
3. [references/capability-router.md](references/capability-router.md)
4. only the capability files selected by the router

Each capability owns its trigger, evidence gate, variables, canonical fragment, prohibited drift, and fallback. A request for one capability never authorizes another.

## 4. Enforce evidence gates

Run every selected capability's evidence gate before compiling.

- If visible evidence supports the edit, fill the capability variables from the image and user instruction.
- If evidence is missing but a smaller physical repair works, recommend that repair.
- If the user explicitly authorizes a stylized or non-physical overlay, state the released physical constraint outside the prompt, then compile the requested effect.
- If exact identity, text, logo, or texture is unreadable, request a clearer source when exact recovery matters; otherwise restrict reconstruction to verifiable features.

🔴 **CHECKPOINT · 🛑 STOP** before releasing identity, subject count, exact text, camera, composition, or physical light/depth consistency when the user has not clearly authorized that release.

## 5. Compose one edit contract

The shared semantic order is:

1. `Input roles` — only for multiple images or a non-obvious base image
2. `Target` — exact object, region, plane, or whole-image property
3. `Change` — one operation and its visible endpoint
4. `Integration` — only the perspective, contact, occlusion, light, shadow, material, edge, or depth relationships changed pixels require
5. `Keep` — costly locks plus one general unchanged boundary

This is an internal contract, not a mandatory heading set. Omit empty or unnecessary blocks.

- One capability: render its complete standalone prompt.
- Several compatible capabilities: merge their fragments into one prompt; state input roles and shared locks once.
- Never concatenate several complete templates.
- If capabilities conflict, follow the dependency order in `capability-router.md`. If the conflict releases a protected lock, stop at the checkpoint.

Use concrete visible endpoints. Translate `更高级`, `更自然`, `电影感`, or `质感更好` into motivated light, readable depth, controlled contrast, coherent material response, or another source-supported result. Do not leave mood adjectives as executable instructions.

For an existing prompt that is already clear and executable, return it unchanged. Do not expand mature wording merely to prove that cleanup occurred.

## 6. Adapt only when needed

The canonical contract uses ordinary natural language and must remain usable by an unknown multimodal image editor. Do not depend on JSON, provider weights, negative-prompt fields, camera-brand shorthand, or invented color codes.

When the user names a provider, read only its adapter:

- [references/platform-gpt-image-2.md](references/platform-gpt-image-2.md)
- [references/platform-nano-banana.md](references/platform-nano-banana.md)
- [references/platform-seedream-5-pro.md](references/platform-seedream-5-pro.md)

For an unknown provider, keep the canonical natural-language contract and invent no provider syntax. Keep model, aspect ratio, resolution, quality, output format, seed, and API/UI controls outside the visual prompt when the target surface exposes separate controls.

## 7. Output

- Default to one prompt in the user's language.
- Return an English semantic mirror only when requested; treat the two languages as alternatives, never one combined prompt.
- For `prompt only`, return only the requested fenced prompt block or blocks.
- For `diagnose`, return visible evidence, root cause, smallest repair, and readiness when requested; do not append an unrequested prompt.
- For `perform-edit`, show the edited image and summarize only the material change and preserved locks.

Non-photoreal media keep their own design logic. Do not force live-action camera, film-stock, skin, grain, or grading language onto illustration, animation, stylized 3D, graphic design, or product cleanup.

## 8. Verify before delivery

Check that:

- every source-dependent claim is visible or explicitly supplied
- every reference contributes only its assigned attributes
- only authorized properties changed
- selected capabilities passed their evidence gates
- capability order is valid and repeated locks were merged
- exact visible text remains exact; unreadable text was not invented
- prompt settings remain outside the visual instruction when possible
- language-only cleanup preserved every exact lock, reference role, target, endpoint, integration relation, provider control, and unchanged boundary
- the response contains exactly the requested artifact

Read [references/validation-status.md](references/validation-status.md) before claiming that a capability or prompt is verified. Static validation or prompt forward-testing does not prove edited-image quality.

## Failure recovery

| Trigger | First action | If unresolved |
| --- | --- | --- |
| Required image missing | Request the actual image or useful crop. | Return no source-dependent diagnosis or edit prompt. |
| Image roles ambiguous | Offer the most likely mapping and ask one role question. | Keep unassigned attributes unavailable. |
| Requested effect fails its evidence gate | Name the missing evidence and propose the smallest physical repair. | Require explicit authorization before a stylized non-physical overlay. |
| Exact face, text, logo, or texture is unreadable | Request a clearer source or crop. | Reconstruct only verifiable features and state the risk outside the prompt. |
| Too many edits conflict | Order them by dependency and recommend stages. | If the user keeps one pass, include all authorized edits and state the stability risk outside the prompt. |
| Provider behavior is undocumented | Use the canonical natural-language contract. | Do not invent syntax, limits, or reliability claims. |
| Generated result drifts | Compare the result against Target, Change, Integration, and Keep. | Revise one failed capability or shared dependency; do not rewrite unrelated modules. |
| Language-only request needs an unseen visual choice | Name the missing visible variable and ask one focused question. | Preserve the source prompt; do not invent an edit decision. |

## Avoid

- Do not diagnose from filenames, memory, summaries, or prompt prose.
- Do not treat cinematic quality as automatic halo, flare, and bokeh stacking.
- Do not force a fixed effect count when the visible image supports a different count.
- Do not import the whole content of a narrowly assigned reference.
- Do not repeat full-source descriptions or exhaustive lock lists in a surgical edit.
- Do not restate the same boundary as both a positive lock and a negative keyword tail.
- Do not promise exact recovery from unreadable pixels.
- Do not call an editing tool when the user asked only for a prompt.
- Do not return only a prompt when the user asked for the edit to be performed.
- Do not route image-edit language cleanup to a generic rewrite Skill or change provider controls merely to sound natural.
