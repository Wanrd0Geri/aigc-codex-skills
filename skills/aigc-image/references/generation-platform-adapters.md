# Platform Adapter Router

Use this reference for an unknown platform, Midjourney, or a genuine multi-platform request. For GPT Image 2, Nano Banana, or Seedream 5.0 Pro alone, load only the matching provider file named in `SKILL.md`.

## Multi-platform delivery

Build one canonical visual specification. If every named platform accepts the same natural-language scene or edit instruction, return one shared Chinese block and one shared English block. Do not create nearly identical provider versions to demonstrate adaptation.

Split provider versions only when one of these materially differs:

- reference-image labels or role syntax
- exact text or layout grammar
- edit versus generation semantics
- a platform-specific field the user must paste into the prompt because their surface has no separate control

Keep model, aspect ratio, resolution, quality, output format, seed, and API/UI settings outside the prompt body whenever the target surface exposes separate controls. If it does not and one value materially affects the deliverable, state only that requirement once in natural language rather than appending a parameter stack. A Chinese and English pair are alternative inputs, not a bilingual prompt to concatenate.

## Unknown platform

Use the minimum sufficient natural-language structure:

1. image goal when it affects the result
2. subject, visible relationship, and action
3. setting and decisive spatial relationship
4. only the necessary composition, light, material, color, or style
5. exact text and critical constraints only when present

Do not invent unsupported platform syntax or settings. Ask for the platform only when its reference or editing grammar would materially change the artifact.

## Midjourney

Keep the prompt short, simple, and specific. Put the main subject and relationship first, then action, setting, and only the decisive visual style. Keep `--` parameters outside both language prompt bodies and provide one copy-ready suffix only when the user asks for settings.

Official source:

- <https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics>
