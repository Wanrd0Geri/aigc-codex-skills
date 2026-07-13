---
name: aigc-image-reverse-prompt
description: Use when the user provides an image and asks to 反推, reverse-engineer, 复刻, 仿写, imitate, or adapt it into bilingual Chinese-English text-to-image prompts for Midjourney, 即梦, Nano Banana/Gemini, GPT Image, ChatGPT Images, or related image models.
---

# AIGC Image Reverse Prompt

Use this skill to turn a source image into highly faithful bilingual Chinese-English text-to-image prompts, then adapt those prompts to the user's target model or requested variation.

The core rule: describe the image as a production-ready visual specification, not as a loose mood board. Capture the visible facts first, lock the elements that must stay, then change only what the user asks to change.

Cross-skill routing in this file assumes the companion AIGC skills are installed. If a named skill is unavailable, apply its core constraint yourself instead of blocking.

## Hard Requirement

Before writing any reverse prompt, confirm the actual image is present in the current context. If no image is attached or visible, ask the user to provide the image. Do not reverse-prompt from memory, a filename, or a text summary alone.

CHECKPOINT - Image Presence Gate:

- If the actual image is missing, stop and ask for the image.
- If the user provides only a filename, link text, or written description, ask for the image unless the task is explicitly to improve that text description.
- If the user asks to edit the source image rather than reproduce or adapt it, route to `aigc-image-edit-prompt`.
- If the user asks why the source image looks weak, route to `aigc-visual-diagnose`.
- If the user asks whether the image can enter video production, route to `aigc-visual-diagnose` for a readiness note before writing video prompts.

If the user provides multiple images, identify each image's role before drafting:

- source image to reproduce
- style reference
- character reference
- pose/composition reference
- variation target

If image roles are ambiguous, ask one short question naming the likely default, such as "Use image 1 as the source and image 2 as style reference?"

Treat every reference role as an attribute whitelist. Build this map before drafting:

| Reference | Allowed attributes | Forbidden attributes |
| --- | --- | --- |
| Image 1 | only the attributes assigned by the user | every unassigned attribute |
| Image 2 | only the attributes assigned by the user | every unassigned attribute |

Apply these role boundaries literally:

- **Composition** authorizes only framing, crop/aspect ratio, camera height/angle, subject position and scale, overlap/occlusion, negative space, depth/layer arrangement, and geometric mass distribution. It never authorizes object identity, environment/location, weather/time, lighting, palette, material, text, or style unless those are assigned separately. Preserve an upper-right circle as geometry, for example; do not silently turn it into a moon.
- **Style** must be split into the requested axes: medium, shape language, edge quality, surface flatness, texture density, palette, lighting, or finish. `Clean large color blocks and flat surfaces` authorizes color-block organization and surface flatness, not the reference subject, silhouette, product geometry, label, wording, specific palette, lighting, or layout.
- If a target-defining semantic field is unassigned, keep it neutral and geometric rather than borrowing it from a reference. Ask one question only when that semantic choice is essential; otherwise use abstract shapes or blank spatial layers. Never name forbidden reference content inside the prompt merely to negate it.

## Workflow

1. Read the image neutrally before prompt writing.
2. Build a faithful visual inventory and source-truth ledger.
3. Separate locked elements from flexible elements.
4. Build one canonical scene specification.
5. Adapt only its expression to the target platform and language.
6. Write the ready-to-use prompt.
7. Run the accuracy check before output.

## Source-Truth Ledger

Before drafting, sort every observation into three internal buckets:

- **Visible fact**: directly observable count, shape, position, pose, gaze, contact, color, light direction, readable text, or material behavior. Only visible facts enter the prompt by default.
- **Inference**: likely age, gender presentation, relationship, social role, era, narrative cause, emotion, brand, or location identity. Include only when visual evidence is strong and phrase it as appearance, not certainty.
- **Uncertain**: occluded, tiny, blurred, ambiguous, or partly legible content. Omit it or state the ambiguity outside the prompt; never complete it from expectation.

Run a text and mark gate for every source and reference:

- Fully legible text assigned to the target: quote it verbatim, preserving case, line breaks, count, and placement.
- Partly legible text: record only certain characters outside the prompt; represent the target area as small unreadable text unless the user supplies the exact copy.
- Unreadable text, ambiguous logo, or watermark: describe only its visible size, color, and placement when composition needs it; do not guess the name or wording. Do not reproduce a watermark.
- Text from a reference whose assigned role excludes text: do not quote or negate its literal wording inside the generation prompt. State only that the reference supplies its assigned attributes and contributes no text or branding.

## Failure Branches

- If the image is missing, do not produce a reverse prompt from memory, filename, or a handoff note; ask for the image.
- If the user gives several images without roles, assign the safest default only when obvious; otherwise ask one role question before drafting.
- If a requested variation would break the source image's identity, relationship, or composition, warn briefly and preserve the higher-priority locked elements.
- If the target platform is unclear, output the general bilingual prompt and keep platform settings in `平台建议`.
- If the source contains readable text, logos, watermark, protected characters, celebrity likeness, or private-person identity, apply the source-truth and text gates: preserve only verified visible facts, never guess names or ownership, and never reproduce a watermark.
- If the image is too abstract or ambiguous to identify subject relationship, state the uncertainty in `图像反推要点` and avoid over-claiming.

## Visual Inventory

Cover these dimensions. Do not output every heading if the user asked for prompt only, but use the full checklist internally.

| Dimension | What to capture |
| --- | --- |
| Subject | number of people or objects, apparent age range or presentation only when visually supported, body shape, face direction, hair, clothing, accessories, distinctive visible features |
| Relationships | distance, gaze lines, physical contact, overlap, hierarchy in the frame, and group arrangement; do not convert these into social roles or backstory without evidence |
| Action | current pose, gesture, movement, object interaction, facial expression, visible emotional state |
| Environment | visible location type, architecture, terrain, interior/exterior, props, and foreground/midground/background layers; name era or exact place only when visibly established |
| Weather | sunny, overcast, rain, snow, fog, wind, humidity, dust, smoke, wet ground, visible sky state |
| Atmosphere | visible cues that support a quiet, tense, romantic, lonely, festive, surreal, documentary, commercial, or editorial reading; keep the emotional label secondary |
| Light | source direction, hardness, contrast, rim light, backlight, fill, shadow density, time of day |
| Color | dominant palette, accent colors, saturation, temperature, black point, highlight color, grade style |
| Composition | framing, camera height, angle, lens feel, depth of field, symmetry, negative space, crop, aspect ratio |
| Medium | photoreal, fashion photo, movie still, documentary, animation, concept art, product render, illustration |
| Texture | skin, fabric, metal, glass, water, dust, film grain, painterly surface, clean digital render |

## Preserve vs Vary

Maintain two lists: **Lock** holds source attributes required for recreation; **Vary** holds only attributes the user explicitly changes. For a variant, keep every other assigned attribute stable and rewrite the full prompt. Example: for "换成下雨天", retain subject count, relationship, pose, camera, framing, and assigned style while adding rain, wet surfaces, and weather-consistent light.

## Detail Budget

Match output detail to the user's request:

- **Prompt only**: output only Chinese and English prompt blocks; keep inventory internal.
- **Accurate recreation**: include the short inventory, locked elements, variable elements, and one bilingual prompt pair.
- **Platform adaptation**: adapt to the named platform only unless the user asks for comparison.
- **Variation**: rewrite the full prompt with the requested change; do not give a patch note that depends on the previous prompt.

Do not over-describe uncertain details. If the image is ambiguous, state uncertainty briefly and keep the prompt faithful to visible evidence.

## Prompt Writing Rules

Write prompts as visible instructions. Always output Chinese and English versions as semantic counterparts. Avoid generic boosters such as `masterpiece`, `best quality`, `电影感`, `质感拉满`, or `超高清` unless the platform specifically benefits from them. Translate those ideas into concrete light, material, composition, camera, and color choices.

For accurate recreation:

- Begin with the main subject and relationship.
- Place them in the environment with clear spatial layers.
- Describe the action and expressions before styling.
- State light, weather, atmosphere, and color as visible physical conditions.
- Add camera/framing/lens only after the visible scene is clear.
- End with medium/style, keeping platform settings out of the prompt body (see Bilingual Output Contract).

For identity-sensitive images:

- Describe visible appearance and styling; do not claim a real person's identity unless the user explicitly provided or requested it.
- For private people, preserve identity through visible traits: face shape, hair, clothing, pose, and expression.
- Do not convert a facial expression into a definite motive, personality, profession, or relationship.

For text-to-image models:

- Do not use image-edit phrasing such as "preserve the original image" unless the target model accepts image references.
- If the target platform supports image references, mention which parts the reference should control: character, pose, style, composition, or environment.

## Canonical Scene Specification

Draft one internal source of truth before writing language or platform variants: subject count and visible traits; pose/action/contact; assigned environment and layer relationships; weather/time; light/color/material; camera/framing/crop/scale; medium/shape/edge/texture; and only verified, authorized target text. Leave unassigned fields neutral rather than sourcing them from another reference.

Every bilingual and platform version must derive from this same specification. Platform adaptation may change sentence density, ordering, or settings placement; it must not change subject count, identity, pose, environment, palette, text, reference roles, or composition.

## Platform Adaptation

Read `references/platform-adapters.md` when the user names a target model or when you need to output multiple platform versions.

Default routing:

- **Midjourney**: short, clear, specific visual prompt; this skill keeps optional parameters in a separate platform note.
- **即梦 / Jimeng**: clear Chinese prompt plus explicit reference-image roles when references are used.
- **Nano Banana / Gemini image**: specific natural-language scene or edit intent with reference roles and positive visible constraints.
- **GPT Image API / ChatGPT Images**: explicit scene, composition, action, and invariants; keep the API model and ChatGPT product surface conceptually separate.

If the user does not name a platform, output a general bilingual Chinese-English prompt plus a short note that it can be adapted to Midjourney, 即梦, Nano Banana, or GPT Image.

If the user names multiple platforms, do not create a language-by-platform Cartesian product by default. When the same natural-language specification works across those platforms, provide one shared bilingual pair and label the supported targets. Split into platform-specific prompt pairs only when reference syntax, parameter placement, or a material prompting strategy actually differs.

## Bilingual Output Contract

Always provide both:

- **中文提示词**: natural Chinese prompt, ready to paste.
- **English Prompt**: natural English prompt, ready to paste, with the same visual meaning as the Chinese prompt.

The English prompt must be prompt text only. Do not include `--` parameters, slash commands, aspect-ratio flags, version flags, seed values, model flags, or separate parameter notes inside the English prompt block. If platform settings are useful, put them in `平台建议`, not in the prompt.

## Output Modes

### Default

Use this structure unless the user asks for prompt only:

````markdown
## 图像反推要点
[3-6 bullets covering subject relationship, environment, light/weather, color, composition, style.]

## 锁定元素
[What must remain unchanged for accurate recreation.]

## 可变元素
[What can be changed, including the user's requested change if any.]

## 中文提示词
```text
[ready-to-use Chinese prompt]
```

## English Prompt
```text
[ready-to-use English prompt, no -- parameters]
```

## 平台建议
[Target platform and any short parameter or usage notes.]
````

### Prompt Only

If the user says "只给提示词", "直接给 prompt", "不要分析", "prompt only", or similar, output only two fenced text blocks: one Chinese prompt and one English prompt, both obeying the Bilingual Output Contract.

### Variation Request

If the user asks to change an element, output the revised prompt directly. Add only a short note if the change risks breaking the source image's identity, relationship, or composition.

### Platform-Specific Request

If the user names exactly one target platform, output only the prompt format for that platform plus the required bilingual counterpart unless the user asks for comparison. Do not produce four platform versions by default.

If the user asks for multi-platform adaptation, keep one shared inventory and canonical scene specification. Adapt wording only when needed, without changing the locked subject count, relationship, pose, environment, light direction, color palette, text, reference boundaries, or composition.

## Accuracy Check

Before final output, check:

- Does the prompt preserve the exact character count and relationship?
- Are pose, gaze, gesture, and action visible rather than abstract?
- Is the environment specific enough to rebuild the frame?
- Are weather and atmosphere physically visible?
- Are lighting direction, contrast, and color palette concrete?
- Does the camera description match the source framing?
- Did the prompt avoid adding unrequested people, props, text, logos, or background events?
- If a variation was requested, did only the requested elements change?
- Are Chinese and English prompts semantically aligned?
- Does the English prompt contain only natural prompt text and no `--` parameters or flags?
- Did every claimed fact come from visible evidence, and were inferences omitted or softened?
- Was all text handled by the legibility gate without guessed letters, brand names, or copied watermark content?
- Does each reference contribute only its assigned attributes, with composition limited to geometry and no semantic-scene, palette, material, lighting, text, subject, or layout leakage?
- Do all language and platform versions match the same canonical scene specification?

## Common Mistakes

- Replacing relationship with vague labels like "friends", "couple", or "family" without describing distance, gaze, posture, or contact.
- Saying "cinematic" instead of naming light direction, shadow density, lens feel, color grade, and atmosphere.
- Overfitting to style words while missing the actual action and spatial layout.
- Adding story causes that are not visible in the image.
- Using Midjourney-style keyword stacks for GPT Image or 即梦 when natural sentences would be more controllable.
- Treating text-to-image prompts like image-edit prompts; text-to-image must rebuild the whole image from description.
- Putting `--` parameters, seed values, or platform settings inside the English prompt body instead of `平台建议`.
- Letting the English prompt become a keyword stack while the Chinese prompt remains natural prose.
- Adding unrequested story background, motivations, character names, text, logos, or extra subjects that are not visible.
- Producing four platform variants when the user only asked for one platform.
- Producing a Chinese/English × platform Cartesian product when one shared bilingual pair expresses the same executable scene.
- Treating composition as permission to import environment objects, weather, time, light, palette, material, or text.
- Treating a style axis as permission to import the whole reference.
- Omitting uncertainty when the image content is genuinely ambiguous.
- Turning apparent age, gender presentation, relationship, profession, era, location, or emotion into certainty without visible evidence.
- Guessing missing letters, brand names, logo identity, or watermark text, or quoting forbidden reference text inside a negative instruction.

## Reference Files

- `references/platform-adapters.md` - platform-specific prompt formats for Midjourney, 即梦, Nano Banana/Gemini, and GPT Image/ChatGPT Images.
