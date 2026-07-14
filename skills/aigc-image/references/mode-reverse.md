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

1. Start with subjects and their visible relationship.
2. Place them in the environment with explicit layer relationships.
3. Describe pose, action, gaze, expression, and contact.
4. State weather, atmosphere, light, color, and material as visible conditions.
5. Add camera and medium after the scene is clear.

Do not claim professions, relationships, motives, place names, eras, or identities from weak visual evidence. Express appearance rather than certainty.

For a variation, keep every lock and rewrite the complete prompt with the requested change. Do not return only a patch note.

Text-to-image must rebuild the complete target. Do not say `preserve the rest of the source image` unless the named platform is actually using an image reference.

## Language and platform

Default to one Chinese and one English prompt with the same visual meaning. Keep `--` flags, model/version settings, aspect ratio, seed, and UI choices outside both prompt bodies.

When several platforms can use the same specification, provide one shared bilingual pair. Split versions only when reference syntax or a material prompting strategy differs. Read `references/generation-platform-adapters.md` for named platforms.
