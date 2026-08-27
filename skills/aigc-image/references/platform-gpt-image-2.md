# GPT Image edit adapter

Last reviewed against official OpenAI image-edit guidance on 2026-08-27. If the user asks for the latest model name or exact API limits, verify the current official docs before answering.

## Provider delta

- Use the universal edit contract from `SKILL.md`. For conservative edits, state `change only X`, the visible endpoint, and the costly invariants; finish with one general unchanged boundary.
- Make small iterative changes when the previous result is close. Restate the important invariants on every follow-up edit to reduce drift.
- For exact text, quote the copy and specify placement or typographic role only as needed. For multiple inputs, map each image to one narrow role.
- Keep size, quality, output format, background, and other API controls outside the visual prompt when the surface exposes them.
- Do not add diffusion-style quality stacks or generic negative-tag tails.
- Do not claim English is superior to Chinese. Follow the language-block contract in `SKILL.md`.

Official sources:

- <https://developers.openai.com/api/docs/models/gpt-image-2>
- <https://developers.openai.com/api/docs/guides/image-generation>
- <https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide>
