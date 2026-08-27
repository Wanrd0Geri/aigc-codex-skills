# Capability validation status

Do not call a prompt or capability verified without matching evidence.

## Status definitions

- `draft`: written but not structurally checked.
- `structure-checked`: routing, variables, locks, references, and fallback passed static review.
- `prompt-forward-tested`: a realistic multimodal request produced the intended prompt and refusal behavior; edited-image quality remains untested.
- `output-verified:<provider>`: the prompt was run on the named provider and the edited image passed task-specific visual checks.
- `cross-model-output-verified`: the same semantic contract passed representative output checks on GPT Image, Gemini/Nano Banana, and Seedream.

Lint, JSON parsing, reference checks, or a judge preference prove structure only. They do not prove image quality.

## Current matrix

| Capability | Status | Evidence |
| --- | --- | --- |
| focus/depth | `prompt-forward-tested` | local readable focus fixture; prompt behavior only |
| background bokeh | `prompt-forward-tested` | local readable highlight fixture; forced-count regression identified |
| semantic palette transfer | `prompt-forward-tested` | local scene and 3x4 palette fixtures; prompt behavior only |
| halo/flare/bokeh evidence refusal | `prompt-forward-tested` | local overcast fixture; unsupported stack refused |
| halo | `structure-checked` | output test pending |
| lens flare | `structure-checked` | output test pending |
| perspective | `structure-checked` | output test pending |
| composition | `structure-checked` | output test pending |
| placement/contact | `structure-checked` | output test pending |
| lighting | `structure-checked` | output test pending |
| palette-card generation | `structure-checked` | output test pending |
| color grade/temperature | `structure-checked` | output test pending |
| material integration | `structure-checked` | output test pending |
| object change/cleanup | `structure-checked` | output test pending |

Update this matrix only after reviewing the actual test artifact and recording the provider plus tested invariant. A successful run on one image does not establish universal reliability.
