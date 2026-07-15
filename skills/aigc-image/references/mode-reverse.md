# Reverse mode

Use this mode to reconstruct or adapt a readable source image as a complete text-to-image specification.

## Canonical still specification

Compile one internal source of truth:

- subjects: count, visible traits, relationships, pose, gaze, contact
- environment: assigned place, visible objects, foreground/midground/background
- conditions: weather, time, atmosphere
- image system: light, color, material, medium, shape, edge, texture
- camera: framing, angle, crop, scale, depth
- text: only verified and authorized target text
- locks: fields required for faithful recreation
- vary: only fields the user asks to change

Every language and platform version derives from this same specification. Adapt sentence density or syntax only; never change facts between versions.

## Writing

Render the smallest complete reconstruction of the target:

1. State the image goal only when it affects the output form.
2. Start with subjects, their visible relationship, and the decisive action or pose.
3. Add the setting and only the spatial relationships needed to rebuild the composition.
4. Add camera, light, color, material, medium, texture, weather, or atmosphere only when each field is visible and distinctive enough to affect the match.
5. Put exact authorized text in quotes and state its location or typographic role.

Do not populate every field merely because the canonical specification contains it. A simple single-subject frame may need only 1-3 natural sentences. Use short labeled blocks only for multi-reference roles, exact typography, dense layouts, or several independent spatial constraints.

Translate abstract mood or quality language into the few visible properties that create it in this frame. Prefer concrete subjects, actions, spatial relations, and distinctive image properties over adjective chains; do not repeat near-synonyms.

Do not claim professions, relationships, motives, place names, eras, or identities from weak visual evidence. Express appearance rather than certainty.

For a standalone text-to-image variation, keep every lock and rewrite the complete minimum-sufficient prompt with the requested change. Do not return only a patch note. If the task is an image-reference edit or an ongoing generation turn, use edit semantics and write only the smallest next instruction.

Text-to-image must rebuild the complete target. Do not say `preserve the rest of the source image` unless the named platform is actually using an image reference.

## Language and platform

Follow the bilingual output contract in `SKILL.md`. Preserve exact visible copy in its original language in both alternatives unless the user asks to translate it.

Keep `--` flags outside both prompt bodies. Keep model/version, aspect ratio, resolution, quality, seed, and UI/API choices outside whenever the target surface exposes separate controls. If it does not and one value materially affects the deliverable, state only that requirement once in natural language rather than appending a parameter stack.

When several platforms can use the same specification, provide one shared bilingual pair. Split versions only when reference syntax or a material prompting strategy differs. Follow the provider-loading rule in `SKILL.md`; use `references/generation-platform-adapters.md` for unknown, Midjourney, or genuine multi-platform delivery.
