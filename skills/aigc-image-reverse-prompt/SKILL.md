---
name: aigc-image-reverse-prompt
description: Use when the user provides an image and asks to 反推, reverse-engineer, 复刻, 仿写, imitate, or adapt it into bilingual Chinese-English text-to-image prompts for Midjourney, 即梦, Nano Banana/Gemini, GPT Image, ChatGPT Images, or related image models.
---

# AIGC Image Reverse Prompt

Use this skill to turn a source image into highly faithful bilingual Chinese-English text-to-image prompts, then adapt those prompts to the user's target model or requested variation.

The core rule: describe the image as a production-ready visual specification, not as a loose mood board. Capture the visible facts first, lock the elements that must stay, then change only what the user asks to change.

## Hard Requirement

Before writing any reverse prompt, confirm the actual image is present in the current context. If no image is attached or visible, ask the user to provide the image. Do not reverse-prompt from memory, a filename, or a text summary alone.

CHECKPOINT - Image Presence Gate:

- If the actual image is missing, stop and ask for the image.
- If the user provides only a filename, link text, or written description, ask for the image unless the task is explicitly to improve that text description.
- If the user asks to edit the source image rather than reproduce or adapt it, route to `aigc-image-edit-prompt`.
- If the user asks why the source image looks weak, route to `aigc-visual-diagnose`.
- If the user asks whether the image can enter video production, route to `aigc-shot-diagnosis-pipeline`.

If the user provides multiple images, identify each image's role before drafting:

- source image to reproduce
- style reference
- character reference
- pose/composition reference
- variation target

If image roles are ambiguous, ask one short question naming the likely default, such as "Use image 1 as the source and image 2 as style reference?"

## Workflow

1. Read the image neutrally before prompt writing.
2. Build a faithful visual inventory.
3. Separate locked elements from flexible elements.
4. Choose the target platform format.
5. Write the ready-to-use prompt.
6. Run the accuracy check before output.

## Failure Branches

- If the image is missing, do not produce a reverse prompt from memory, filename, or a handoff note; ask for the image.
- If the user gives several images without roles, assign the safest default only when obvious; otherwise ask one role question before drafting.
- If a requested variation would break the source image's identity, relationship, or composition, warn briefly and preserve the higher-priority locked elements.
- If the target platform is unclear, output the general bilingual prompt and keep platform settings in `平台建议`.
- If the user asks for Midjourney parameters, provide them only in `平台建议`; never append `--` flags to the English prompt block.
- If the source contains readable text, logos, watermark, protected characters, celebrity likeness, or private-person identity, describe visible traits and avoid inventing names, brand claims, or ownership assumptions.
- If the image is too abstract or ambiguous to identify subject relationship, state the uncertainty in `图像反推要点` and avoid over-claiming.

## Visual Inventory

Cover these dimensions. Do not output every heading if the user asked for prompt only, but use the full checklist internally.

| Dimension | What to capture |
| --- | --- |
| Subject | number of people or objects, age range, gender presentation, body type, face direction, hair, clothing, accessories, distinctive features |
| Relationships | who is close to whom, hierarchy, intimacy, conflict, gaze lines, physical contact, social role, group arrangement |
| Action | current pose, gesture, movement, object interaction, facial expression, visible emotional state |
| Environment | location type, era, architecture, terrain, interior/exterior, props, foreground/midground/background layers |
| Weather | sunny, overcast, rain, snow, fog, wind, humidity, dust, smoke, wet ground, visible sky state |
| Atmosphere | quiet, tense, romantic, lonely, festive, surreal, documentary, cinematic, commercial, editorial |
| Light | source direction, hardness, contrast, rim light, backlight, fill, shadow density, time of day |
| Color | dominant palette, accent colors, saturation, temperature, black point, highlight color, grade style |
| Composition | framing, camera height, angle, lens feel, depth of field, symmetry, negative space, crop, aspect ratio |
| Medium | photoreal, fashion photo, movie still, documentary, animation, concept art, product render, illustration |
| Texture | skin, fabric, metal, glass, water, dust, film grain, painterly surface, clean digital render |

## Preserve vs Vary

Always produce or mentally maintain two lists:

- **Lock**: elements required for accurate recreation: subject count, relationship, main pose, camera angle, framing, core environment, light direction, color palette, style/medium.
- **Vary**: elements the user explicitly wants changed, or low-risk elements such as season, clothing color, time of day, background details, prop variants, mood intensity, platform format.

If the user asks for a flexible variant, keep the lock list stable and rewrite only the requested variable. Example: if they say "换成下雨天", keep characters, relationship, pose, camera angle, and color logic while adding rain, wet surfaces, softer reflections, and weather-appropriate atmosphere.

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
- End with medium/style. Do not append command-style parameters such as `--ar`, `--style`, `--v`, seed values, quality flags, or aspect-ratio flags to the English prompt.

For identity-sensitive images:

- Describe visible appearance and styling; do not claim a real person's identity unless the user explicitly provided or requested it.
- For private people, preserve identity through visible traits: face shape, hair, clothing, pose, and expression.

For text-to-image models:

- Do not use image-edit phrasing such as "preserve the original image" unless the target model accepts image references.
- If the target platform supports image references, mention which parts the reference should control: character, pose, style, composition, or environment.

## Platform Adaptation

Read `references/platform-adapters.md` when the user names a target model or when you need to output multiple platform versions.

Default routing:

- **Midjourney**: concise English prompt with visual hierarchy; keep any Midjourney settings outside the English prompt block.
- **即梦 / Jimeng**: Chinese natural-language prompt with direct visual description and fewer parameter tags.
- **Nano Banana / Gemini image**: natural-language prompt with explicit composition, subject relationship, and style constraints.
- **GPT Image / ChatGPT Images**: natural-language prompt with detailed scene logic, clean constraints, and optional negative instructions only when useful.

If the user does not name a platform, output a general bilingual Chinese-English prompt plus a short note that it can be adapted to Midjourney, 即梦, Nano Banana, or GPT Image.

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

If the user says "只给提示词", "直接给 prompt", "不要分析", "prompt only", or similar, output only two fenced text blocks: one Chinese prompt and one English prompt. The English block still must not contain `--` parameters.

### Variation Request

If the user asks to change an element, output the revised prompt directly. Add only a short note if the change risks breaking the source image's identity, relationship, or composition.

### Platform-Specific Request

If the user names exactly one target platform, output only the prompt format for that platform plus the required bilingual counterpart unless the user asks for comparison. Do not produce four platform versions by default.

If the user asks for multi-platform adaptation, keep one shared visual inventory and then adapt wording for each platform without changing the locked subject count, relationship, pose, environment, light direction, color palette, or composition.

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

## Common Mistakes

- Replacing relationship with vague labels like "friends", "couple", or "family" without describing distance, gaze, posture, or contact.
- Saying "cinematic" instead of naming light direction, shadow density, lens feel, color grade, and atmosphere.
- Overfitting to style words while missing the actual action and spatial layout.
- Adding story causes that are not visible in the image.
- Using Midjourney-style keyword stacks for GPT Image or 即梦 when natural sentences would be more controllable.
- Treating text-to-image prompts like image-edit prompts; text-to-image must rebuild the whole image from description.
- Putting Midjourney-style `--ar`, `--style`, `--v`, or seed parameters in the English prompt instead of keeping settings separate.
- Letting the English prompt become a keyword stack while the Chinese prompt remains natural prose.
- Adding unrequested story background, motivations, character names, text, logos, or extra subjects that are not visible.
- Treating a target-platform parameter note as part of the English prompt body.
- Producing four platform variants when the user only asked for one platform.
- Omitting uncertainty when the image content is genuinely ambiguous.

## Reference Files

- `references/platform-adapters.md` - platform-specific prompt formats for Midjourney, 即梦, Nano Banana/Gemini, and GPT Image/ChatGPT Images.
