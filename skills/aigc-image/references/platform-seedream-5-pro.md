# Seedream 5.0 Pro Prompt Adapter

Last verified against official Dreamina and BytePlus public guidance on 2026-07-15. The available prompt guidance is a product workflow guide, not a complete API specification. Do not invent or hardcode an API model id, maximum prompt length, maximum reference count, or unsupported control.

## Provider delta

- Use the minimum-sufficient shape from `SKILL.md`. Public guidance favors a clear purpose, subject, scene, decisive composition, and only the visual treatment that changes the result.
- Bind every reference image to a specific role; never use only `参考以上图片`.
- Keep aspect ratio and resolution in Dreamina settings instead of restating them as `8K`, `32K`, or quality boosters.
- The public sources do not justify a hardcoded API model id, prompt-length limit, reference-count limit, or claim that English outperforms Chinese. Do not invent them.
- Follow the language-block contract in `SKILL.md`.

Official sources and evidence boundary:

- <https://dreamina.capcut.com/seedream/seedream-5-0-pro>
- <https://dreamina.capcut.com/seedream/seedream-5-0-pro-prompt>
- <https://dreamina.capcut.com/seedream/how-to-use-seedream-5-0-pro>
- <https://ai.byteplus.com/en/product/Seedream>
