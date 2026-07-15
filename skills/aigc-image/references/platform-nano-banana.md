# Nano Banana Prompt Adapter

Last verified against official Google guidance on 2026-07-15. If the user asks for the latest model or exact API limits, verify the current official docs before answering.

Treat `Nano Banana` as a model family. As of this snapshot:

- Nano Banana 2 / `gemini-3.1-flash-image`: default general-purpose recommendation
- Nano Banana Pro / `gemini-3-pro-image`: complex professional layouts, brand consistency, precise text, factual visuals, or dense multi-reference work
- Nano Banana 2 Lite / `gemini-3.1-flash-lite-image`: high-volume or low-latency work
- Gemini 2.5 Flash Image: legacy; use only when explicitly requested or required by the user's surface

Do not interrupt a routine prompt request merely to choose a model when the prompt strategy is identical. Mention a recommendation outside the prompt only when it materially helps.

## Provider delta

- Use the minimum-sufficient shape from `SKILL.md`. Gemini native image generation accepts conversational generation and follow-up edits; when a result is close, change one goal instead of rebuilding the prompt.
- Map multiple inputs explicitly to identity, pose, garment, object, composition, environment, or style.
- Gemini native image generation does not use the older Imagen-style negative-prompt field. Use a positive endpoint plus a compact unchanged boundary when editing.
- Keep model, aspect ratio, resolution, output format, and other API/UI controls outside the visual prompt when the surface exposes them.
- Do not claim English is superior to Chinese. Follow the language-block contract in `SKILL.md`.

Official sources:

- <https://ai.google.dev/gemini-api/docs/image-generation>
- <https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/>
- <https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana>
