# Platform Adapters

Use this reference only after the image has been read and the core visual inventory is clear.

## Midjourney

Best for concise English prompts with strong visual hierarchy.

Structure:

```text
[main subject and relationship], [specific action and pose], [environment and spatial layers], [weather and atmosphere], [lighting], [color palette], [camera/framing/lens feel], [medium/style]
```

Guidelines:

- Put the most important subject relationship in the first clause.
- Use concrete nouns and visible modifiers.
- Keep the prompt compact; Midjourney weakens when overloaded with long explanatory sentences.
- Do not append `--` parameters, aspect-ratio flags, version flags, seed values, or quality flags to the English prompt. If useful, mention them separately as platform settings outside the prompt block.
- If the user asks for Midjourney settings, suggest them separately in platform notes; do not attach them to the English prompt.

## 即梦 / Jimeng

Best for Chinese natural-language prompts that read like a visual director briefing.

Structure:

```text
[画面主体与人物关系]。[动作、表情、视线、姿态]。[环境、天气、时间、空间层次]。[光影、色调、氛围]。[构图、镜头、景别、风格]。避免新增人物、文字、logo 和不相关道具。
```

Guidelines:

- Use complete Chinese visual sentences.
- Avoid English parameter piles.
- Keep relationship, action, environment, light, and color in the main prompt body.
- Add negative constraints only for common failures: extra fingers, extra people, warped face, unwanted text, logo, watermark, messy background.

## Nano Banana / Gemini Image

Best for explicit natural-language visual instructions with clear control priorities.

Structure:

```text
Create a text-to-image scene showing [subject relationship and main action]. The setting is [environment, weather, time]. Keep the composition [framing and camera angle]. Use [lighting] with [color palette and atmosphere]. Render it as [medium/style]. Do not add [unwanted elements].
```

Guidelines:

- Natural sentences work better than comma-only keyword stacks.
- State the full scene because text-to-image cannot preserve anything from a source unless a reference image is provided.
- If using reference images, specify their roles: character identity, pose, composition, style, or environment.
- Use moderate negative constraints; too many negatives can pull attention away from the main scene.

## GPT Image / ChatGPT Images

Best for detailed scene logic, exact relationships, and controlled variations.

Structure:

```text
Generate a [medium/style] image of [subject relationship] in [specific environment]. [Describe the exact pose, gesture, gaze, and action]. The scene takes place during [time/weather], with [lighting direction and quality]. The color palette is [dominant colors and grade]. Frame it as [camera height, distance, angle, lens feel, composition]. Keep the image free of [unwanted additions].
```

Guidelines:

- Use clear, grammatical instructions.
- Include relationship and spatial layout explicitly.
- Use "Do not add..." only for likely model errors such as extra people, readable text, logos, watermarks, mismatched costumes, or changed expressions.
- For user-requested variations, write a complete replacement prompt rather than a patch note.

## General Multi-Platform Prompt

When platform is unknown, output both Chinese and English by default. The English prompt must be natural prompt text only, without `--` parameters.

```text
[主体与人物关系]，[动作、表情、视线、姿态]，位于[环境、天气、时间、空间层次]。画面采用[构图、景别、镜头角度]，[光源方向、光质、阴影]，[主色调、辅助色、饱和度、氛围]，[媒介/风格]。避免新增人物、文字、logo、水印和不相关道具。
```

Then provide a matching English version as a semantic counterpart, not a literal word-by-word translation. Keep platform settings outside the English prompt block.
