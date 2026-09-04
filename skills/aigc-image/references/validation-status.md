# Capability validation status

Do not call a prompt or capability verified without matching evidence.

## Status definitions

- `draft`: written but not structurally checked.
- `structure-checked`: routing, variables, locks, references, and fallback passed static review.
- `prompt-forward-tested`: a realistic multimodal request produced the intended prompt and refusal behavior; edited-image quality remains untested.
- `output-verified:<provider>`: the prompt was run on the named provider and the edited image passed task-specific visual checks.
- `cross-model-output-verified`: the same semantic contract passed representative output checks on GPT Image, Gemini/Nano Banana, and Seedream.

Lint, JSON parsing, reference checks, or a judge preference prove structure only. They do not prove image quality.

## Recorded evidence before the operation-state revision

The records below describe historical prompt behavior, not a rerun of the revised permission, planned-state, support-region or optics rules. Their fixture/output paths were not recorded here; treat them as inherited claims until the original artifacts are available. New rule-tagged scenarios in `test-prompts.json` and `regression-prompts.json` are acceptance specifications, not evidence of execution or a passing result.

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

## 2026-09-05 operation-state revision evidence

Four independent prompt-forward cases used one readable mirror-table fixture: combined relocation/grade, added lamp/light/glow, object removal with attributable effects, and an explicit incompatible color-lock request. All four candidate prompts passed an independent version-blind semantic review. This supports `prompt-forward-tested` only for those cases; it does not promote every capability above.

Two actual candidate edits were also produced with the built-in `image_gen.imagegen` provider (model and seed not exposed), each with one sample, alongside two raw-brief direct-generation controls. The added-lamp candidate passed the visible checks in that sample. Both removal samples removed the cup and its reflection but changed protected wall texture, so strict preservation failed. The raw-brief lamp reflection remained uncertain. No general `output-verified` or cross-provider status is awarded.

The lens-flare correction, mature-image diagnosis, marked cleanup, and broader style/material cases remain structurally checked or pending their own input/output evidence. See the repository companion evidence index at `evals/evidence/2026-09-05.md` for snapshot, prompt, source, output, review, and archive provenance.

For a new verification record, include the rule IDs, Skill revision, actual request and image roles, fixture location/hash, model or provider configuration, complete prompt/result artifact, and per-invariant judgment. Distinguish assistant-reported trace from inspected tool/image evidence. Do not promote `planned` facts or a syntactically valid scenario to `output-verified`.
