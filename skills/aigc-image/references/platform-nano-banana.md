# Nano Banana Prompt Adapter

Last reviewed against official Google image-edit guidance on 2026-08-27. Treat `Nano Banana` as a product/model family rather than guessing an API model slug. If the user asks for the latest model or exact limits, verify current official documentation.

## Provider delta

- Use the universal edit contract from `SKILL.md`. When a result is close, change one goal instead of rebuilding the whole prompt.
- Map multiple inputs explicitly to identity, pose, garment, object, composition, environment, or style.
- Use a positive endpoint plus a compact unchanged boundary; do not depend on a separate negative-prompt field.
- Keep model, aspect ratio, resolution, output format, and other API/UI controls outside the visual prompt when the surface exposes them.
- Do not claim English is superior to Chinese. Follow the language-block contract in `SKILL.md`.

Official sources:

- <https://ai.google.dev/gemini-api/docs/image-generation>
- <https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/>
- <https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana>
