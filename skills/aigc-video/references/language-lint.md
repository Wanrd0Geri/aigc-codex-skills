# Protected video language lint

Natural language means executable visual language, not poetry, casual tone, or a longer prompt.

## Lock ledger and intervention

Classify the existing prompt before changing prose:

- `exact`: every supplied literal anchor, filename, material label, provider token, dialogue, narration, lyrics, visible text, number, duration, interval, shot id, shot count/order, and exact ending cue
- `semantic`: task kind, platform grammar, material roles, identity/count, action order, spatial relation, camera relation, continuity, and terminal state
- `editable`: repeated boosters, tag stacks, template openings, decorative conclusions, unsupported causes, and awkward connective wording

Select the smallest action:

- `preserve`: prompt is already clear and executable; return unchanged.
- `micro-fix`: repair one local ambiguity, empty adjective, unsupported cause, or repeated phrase.
- `rebuild`: prompt is mostly tags but the same locks and task grammar can be reconstructed without a new production decision. If multiple results are plausible, ask first.

Never expand a mature prompt to prove that lint ran.

Preserve the requested output language and wrapper. If the user asks for Chinese and English prompt-only output, return two separate prompt blocks with the same action order, roles, locks, timing, and endpoint, with no diagnosis or commentary between them. If the named provider has no maintained adapter or verified current official syntax, request that syntax or offer a clearly labeled platform-neutral prompt; never relabel neutral wording as provider-ready.

## Adapter-prep normalization

Change only mutable spans:

- replace keyword chains with complete visual sentences
- give camera directions a visible subject and spatial relationship
- translate supported abstract intention into posture, gaze, contact, distance, light, material, sound, timing, or environment response
- preserve a material `ActingTask` as natural playable task logic plus visible execution; do not lint it away merely because its task is not itself a physical gesture
- remove promotional boosters, template introductions, forced conclusions, rule-of-three padding, and unsupported causes
- break sentences with too many independent clauses

Make no change when the wording is already clear and executable.

Evaluation or emotion labels such as `自然`、`灵动`、`僵硬`、`高级`、`高级感`、`沉默`、`判断`、`警觉` or `没有惊慌` cannot carry an ambiguous control on their own. When the intended difference matters to the shot, make it readable through the smallest supported body/material state, gaze or attention relation, contact, time, space, direction, process, or endpoint; otherwise omit the label. Internal diagnosis may use these labels, but the final executable prompt must not contain the diagnosis or review rationale.

## Protected spans

Never change the value or meaning of:

- source-to-upload-order mapping, final material labels, operational roles, boundary scopes, and borrowed dimensions; duplicate reference-input mentions may be consolidated into one responsibility line without changing them
- subject count and identity; source shot ids in the internal traceability map; prompt shot count/order while rendered headings normalize only to contiguous local indices
- current-user/source/project-locked duration, shot-heading ranges, exact shot-internal timing, and edit interval
- dialogue, narration, lyrics, visible text
- user/source/project-locked silence, music, subtitle, sound, ending, freeze, fade, black frame, or loop cues
- task type and Seedance edit/extend/bridge grammar
- action order, screen direction, inherited state, end handoff
- user-retained camera or composition controls

Do not turn `严格编辑视频1` or `向后延长视频1` into `参考视频1` merely because the latter reads more smoothly. Normalizing a supplied handle or UUID to `视频1` must not change which asset the command targets.

For a new/reference-generation artifact, the standing user lock in `SKILL.md` supersedes lower-authority brief, project/source, or reference music/subtitle content: remove those instructions and retain the final no-subtitle/no-BGM policy. A current-user request to add BGM or subtitles that does not explicitly revise the standing rule is a direct conflict; return it through the intent/fact gate instead of silently repairing a partial final artifact. Language-only cleanup may preserve already embedded source music/subtitles only when the artifact is an edit, extension, or bridge operation rather than new generation.

Planning-derived or earlier-model shot-body subdivisions are not protected merely because they appear in the current wording. Preserve them only when the current user, an authoritative source, or the accepted version specifically records them as timing locks; otherwise let the adapter replace them with causal phase language during complete-unit recompilation.

## Post-adapter audit

After rendering, inspect rather than rewrite. Check for:

- residual empty adjectives such as `高级感`, `氛围拉满`, `史诗感`
- abstract emotion with no supported carrier
- a material dialogue/reaction task that exists only in analysis while the rendered shot contains gestures without their purpose or feedback logic
- a material emotional/experiential progression, shared relationship change, or cross-shot performance state that exists only in analysis and has no observable owner in the affected timeline
- an authorized beat-to-action mapping that was analyzed but is absent from the owning shot, or music/lyrics leaked from a rhythm-only reference
- source/project shot ids rendered as Seedance headings instead of contiguous prompt-local `镜头1..N`
- structure-table content leaking across field ownership or carrying repair history and exclusion stacks
- parameter stacks in the prompt body
- unsupported off-screen causality
- decorative ending summaries
- long sentences that obscure action order

Patch only the failing sentence internally, then re-run exact and semantic lock checks across the complete affected unit. Preserve correct wording instead of freely rewriting it, but follow `change-impact-and-delivery.md` for external delivery: return at least the complete affected shot or the wider complete sequence, prompt, or operation when dependencies cross that boundary. Never deliver the sentence patch by itself.

Before delivery, delete every new noun, verb, number, subject, effect, camera move, light source, sound, or ending unsupported by the source prompt or current readable evidence. If lock safety and smooth prose conflict, preserve the lock.
