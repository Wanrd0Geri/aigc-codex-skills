# Protected video language lint

Natural language means executable visual language, not poetry, casual tone, or a longer prompt.

## Adapter-prep normalization

Change only mutable spans:

- replace keyword chains with complete visual sentences
- give camera directions a visible subject and spatial relationship
- translate supported abstract intention into posture, gaze, contact, distance, light, material, sound, timing, or environment response
- remove promotional boosters, template introductions, forced conclusions, rule-of-three padding, and unsupported causes
- break sentences with too many independent clauses

Make no change when the wording is already clear and executable.

## Protected spans

Never change the value or meaning of:

- literal `@...` anchor labels, operational roles, boundary scopes, and borrowed dimensions; duplicate reference-input mentions may be consolidated into one reference summary without changing them
- subject count, identity, shot ids/count/order
- duration, timing, edit interval
- dialogue, narration, lyrics, visible text
- user/source/project-locked silence, music, subtitle, sound, ending, freeze, fade, black frame, or loop cues
- task type and Seedance edit/extend/bridge grammar
- action order, screen direction, inherited state, end handoff
- user-retained camera or composition controls

Do not turn `严格编辑@视频1` or `向后延长@视频1` into `参考@视频1` merely because the latter reads more smoothly.

## Post-adapter audit

After rendering, inspect rather than rewrite. Check for:

- residual empty adjectives such as `高级感`, `氛围拉满`, `史诗感`
- abstract emotion with no supported carrier
- parameter stacks in the prompt body
- unsupported off-screen causality
- decorative ending summaries
- long sentences that obscure action order

Patch only the failing sentence, then re-run exact and semantic lock checks. Never perform a full final rewrite.
