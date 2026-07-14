# Video Handoff Contract

Use this contract only when the user requests a final video prompt after project context is required. The handoff is internal: compile the card, continue with `aigc-video` in the same task, and return the user's requested final artifact rather than an instruction to invoke another workflow.

## Handoff Gate

- `validated`: continue to video production.
- `overloaded`: pass every locked beat intact and let video production handle compression, splitting, or platform limits. Do not silently choose a materially different structure.
- `pending`: continue only when the unresolved item cannot change the final production result. Otherwise discuss the uncertainty with the user before finalizing.

## Handoff Envelope

Pass only the compact production context needed for the requested range:

```yaml
artifact: final_video_prompt
project: "<project id/title>"
shot_range: "<exact episode/scene/shot ids>"
card_schema_version: "1.0"
card_status: validated
cards: "<validated compact cards>"
source_authority: "<field-scoped winners and unresolved conflicts>"
reference_map:
  - anchor: "<literal anchor or asset id>"
    state: available_readable
    role: "<narrow role>"
    may_control: ["<fields>"]
    must_not_control: ["<fields>"]
user_overrides:
  - "<current explicit instruction>"
project_defaults:
  - "<applicable field-scoped default>"
open_decisions: []
requested_platform: "<named platform or unspecified>"
output_request: "<prompt only, explanation, variants, etc.>"
```

Do not include the full script, outline, project bible, or unrelated neighboring cards.

## Downstream Ownership

The context layer locks facts and intent. `aigc-video` owns:

- final platform selection and adapter wording
- duration compression or shot splitting proposals
- video generation, editing, extension, bridging, dialogue/lip-sync, and visible-text syntax
- expression shaping that preserves the card's action, intent, and continuity
- final language lint and output formatting

Project defaults are fallbacks, not permanent locks. Apply precedence per field:

1. current user instruction
2. current readable asset within its assigned role
3. validated shot card/current production source
4. project default
5. video workflow default

## Preservation Rules

- Preserve exact shot ids, literal anchors, character identity, subject count, location, locked action order, exact dialogue, required silence, prop state, and ending handoff.
- Preserve semantic locks such as screen direction, inherited pose, gaze target, contact point, and reference-role boundaries.
- Treat `performance intent` as motivation, not permission to add backstory, flashbacks, symbols, props, lighting changes, or new actions.
- Let `visible performance` refine delivery only inside the locked action.
- Keep `anchor_only` assets literal; never claim to have inspected them.
- Keep missing or unassigned assets from controlling any field.

## Same-Task Collaboration

If a creative uncertainty remains, present the evidence, current reading, alternatives, and recommendation, then ask 1-3 related questions. Once answered, repair the affected card fields and continue to the final video prompt without asking the user to restart or re-invoke a skill.

If the user requested cards or an audit only, do not create this handoff.
