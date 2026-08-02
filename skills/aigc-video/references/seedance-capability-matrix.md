# Seedance Capability Matrix

Use this file only for version limits, feasibility, or duration questions. Keep three kinds of evidence separate:

- **hard limit**: the product rejects or does not expose the input/mode beyond this boundary
- **official recommendation**: the product may accept more, but stability is expected to decline
- **workflow inference**: a production judgment derived from the limits; never present it as an official rule

Source basis: [【即梦】Seedance 2.5 使用手册](https://bytedance.larkoffice.com/wiki/RXh5ww6EqighMdkVTMccm2d4n7e), updated 2026-07-31 and checked 2026-08-02. Re-check after a provider update.

## Seedance 2.5 hard limits

| Capability | Boundary |
| --- | --- |
| Native generation | 4–30 seconds; 97–721 frames |
| Ordinary extension | Source video must be no longer than 30 seconds; repeated extension may reach 60 seconds total |
| Ultra-long mode | 30–180 seconds |
| Image inputs | Up to 30 |
| Video inputs | Up to 10; combined duration up to 30 seconds; each video 2–30 seconds |
| Audio inputs | Up to 10; combined duration up to 30 seconds; each audio 2–30 seconds |
| All multimodal inputs | Up to 50 total |
| Pure-audio input | Supported |
| Output resolution | 480p or 720p |

The general video-input count does not redefine every operation. In particular, the official seamless-transition workflow is described with two videos: a predecessor and a successor.

## Seedance 2.5 official recommendations

These are stability guidance, not rejection limits:

- image subjects: 1–8 is the recommended stable range; 9–12 may be less stable
- audio/video subjects: 1–5 is the recommended stable range; 6–10 may be less stable
- audio/video references: 5–10 seconds are generally recommended
- ordinary edit input: no more than 20 seconds is recommended
- reference images for editing: 1–5 are recommended; 6–8 may be attempted with lower stability

When the user's request is accepted by a hard limit but exceeds a recommendation, deliver the best faithful prompt and mention the stability tradeoff briefly. Do not reject it as impossible.

## Prompt-control evidence

- Seedance 2.5 accepts second-based time ranges and uses them in official multi-shot examples.
- The provider reports improved negative control for subtitles and background music. Treat this as a targeted capability, not proof that long generic negative lists are universally reliable.
- Upload-order labels are sufficient for responsibility binding and are the default final form. Do not output a supplied `@` handle or UUID unless the current user explicitly requests it.

## Seedance 2.0 legacy boundaries

Apply only when the user explicitly selects 2.0 or 2.0 Fast:

- native generation: 4–15 seconds
- image inputs: up to 9
- video inputs: up to 3, combined duration up to 15 seconds
- audio inputs: up to 3, combined duration up to 15 seconds
- all multimodal inputs: up to 12
- pure-audio input: unsupported

Do not infer a 2.0 output resolution or expose a 2.5-only mode without current provider evidence.

## Workflow inferences

- More accepted assets do not mean more useful assets. Assign one clear responsibility to every retained asset and remove only true duplicates or conflicts.
- Long duration does not need a different prompt grammar. It needs more timeline segments, lighter density per segment, and explicit global continuity locks.
- Very short duration does not justify dropping timestamps. Use fewer segments and one readable beat per segment.
- If the exact current UI differs from this file, the visible current UI wins and this file must be updated before making a hard-limit claim.
