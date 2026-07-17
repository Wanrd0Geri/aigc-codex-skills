# GPT Image 2 Prompt Adapter

Last verified against official OpenAI guidance on 2026-07-15. If the user asks for the latest model or exact API limits, verify the current official docs before answering.

As of this snapshot, `gpt-image-2` is OpenAI's current most capable API image model. Do not infer an API model slug merely from a ChatGPT product-surface label.

## Provider delta

- Use the minimum-sufficient generation or edit shape from `SKILL.md`; GPT Image 2 accepts clear natural-language briefs and does not need diffusion-style quality or negative-tag tails.
- For exact text, quote the copy and specify placement or typographic role only as needed. For multiple inputs, map each image to one narrow role.
- Keep size, quality, output format, background, and other API controls outside the visual prompt when the surface exposes them.
- Current official guidance says GPT Image 2 automatically uses high input fidelity. Do not add `input_fidelity` to a GPT Image 2 settings suggestion.
- Do not claim English is superior to Chinese. Follow the language-block contract in `SKILL.md`.

Official sources:

- <https://developers.openai.com/api/docs/models/gpt-image-2>
- <https://developers.openai.com/api/docs/guides/image-generation>
- <https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide>
