# Platform Adapters

Use this reference only after the image has been read and the canonical scene specification is clear. These are skill delivery conventions informed by official platform guidance, not exclusive vendor grammars or cross-platform quality rankings.

## Midjourney

Official guidance favors short, simple, specific prompts that describe what should appear. The field order below is this skill's compact template, not required syntax.

Structure:

```text
[main subject and relationship], [specific action and pose], [environment and spatial layers], [weather and atmosphere], [lighting], [color palette], [camera/framing/lens feel], [medium/style]
```

Guidelines:

- Prioritize the main subject and visible relationship before secondary styling details.
- Use concrete nouns and visible modifiers.
- Keep the prompt compact and specific; remove explanatory prose that does not describe a visible target.
- Midjourney accepts parameters at the end of a prompt. This skill's bilingual output contract keeps `--` parameters outside the English visual-prompt block so the scene text stays semantically aligned with Chinese.
- If the user asks for Midjourney settings, put a copy-ready settings suffix in `平台建议` rather than silently mixing it into only one language block.

## 即梦 / Jimeng

The official product supports Chinese prompting and reference-image transformations. The structure below is a local clear-Chinese template; public guidance does not establish a mandatory grammar or negative-prompt mechanism.

Structure:

```text
[画面主体与人物关系]。[动作、表情、视线、姿态]。[环境、天气、时间、空间层次]。[光影、色调、氛围]。[构图、镜头、景别、风格]。避免新增人物、文字、logo 和不相关道具。
```

Guidelines:

- Use clear Chinese visual descriptions.
- Keep unsupported parameter piles out of the scene description.
- Keep relationship, action, environment, light, and color in the main prompt body.
- State the desired visible target first. Add a short exclusion only when it protects a source fact or reference boundary in this task; do not append a generic defect list.

## Nano Banana / Gemini Image

Official guidance supports natural-language image instructions, reference inputs, conversational iteration, specific context, and stepwise handling of complex tasks.

Structure:

```text
Create a text-to-image scene showing [subject relationship and main action]. The setting is [environment, weather, time]. Keep the composition [framing and camera angle]. Use [lighting] with [color palette and atmosphere]. Render it as [medium/style]. Do not add [unwanted elements].
```

Guidelines:

- Use clear, specific, consistently structured instructions rather than relying on disconnected keyword piles.
- State the full scene because text-to-image cannot preserve anything from a source unless a reference image is provided.
- If using reference images, specify their roles: character identity, pose, composition, style, or environment.
- Prefer a positive visible target for exclusions; keep a short explicit prohibition only when positive staging cannot protect the boundary.

## GPT Image / ChatGPT Images

Use this format for either the ChatGPT Images product surface or OpenAI GPT Image API visual prompting. Do not infer an API model slug from a ChatGPT product label.

Structure:

```text
Generate a [medium/style] image of [subject relationship] in [specific environment]. [Describe the exact pose, gesture, gaze, and action]. The scene takes place during [time/weather], with [lighting direction and quality]. The color palette is [dominant colors and grade]. Frame it as [camera height, distance, angle, lens feel, composition]. Keep the image free of [unwanted additions].
```

Guidelines:

- Use clear instructions; short sentences, paragraphs, labels, and structured blocks are all acceptable when the scene logic remains explicit.
- Include relationship and spatial layout explicitly.
- State critical invariants and use targeted exclusions for likely drift; do not append a generic negative list.
- For a standalone text-to-image variation, write a complete replacement prompt. In a real multi-turn image context, a short incremental instruction is valid; restate critical anchors only when drift appears.

## General Multi-Platform Prompt

When platform is unknown, this skill's delivery contract outputs both Chinese and English. This is a workflow choice, not a claim that every platform requires bilingual input. The English prompt block contains natural scene text only, without `--` parameters.

```text
[主体与可见关系]，[动作、表情、视线、姿态]，位于[环境、天气、时间、空间层次]。画面采用[构图、景别、镜头角度]，[光源方向、光质、阴影]，[主色调、辅助色、饱和度、氛围]，[媒介/风格]。[仅在本任务需要时加入针对性边界]
```

Then provide a matching English version as a semantic counterpart, not a literal word-by-word translation. Keep platform settings outside the English prompt block.
