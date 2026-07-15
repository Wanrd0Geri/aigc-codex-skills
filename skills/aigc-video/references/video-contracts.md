# Video contracts

Use these contracts silently. They prevent creative stages, language cleanup, and platform rendering from changing one another's facts.

## TaskEnvelope

- `terminal_artifact`: final platform video prompt
- `platform` and `version`
- `task_kind`: new_text | reference | edit | extend | bridge
- `operation`: draft | optimize
- `output_mode`: default | prompt_only | diagnostic | ab
- `expression_request`: default | explicit_vibe
- `project_scope`: optional project/episode/scene/shot ids
- `requested_duration`

## EvidenceLedger

For each fact record:

- value
- field
- source: current_user | readable_asset | project_card | storyboard | script | project_default | personal_default | inference
- confidence
- asset state: available_readable | anchor_only | missing

Apply precedence per field, not to a whole document. A newer composition instruction does not erase unrelated current dialogue or identity facts.

## ReferenceMap

For each literal anchor record:

- exact label
- asset state
- assigned roles
- forbidden/unassigned roles
- exact text or identity locks, if authorized

Unassigned fields stay neutral. Preserve labels exactly through every stage. `forbidden/unassigned roles` are internal validation data, not a negative list for the final prompt. For multi-reference generation, render one compact positive reference summary and normally mention each anchor once; use semantic names in the shot body.

## LockLedger

- exact: literals and numbers that must not change
- semantic: meaning and relationships that must not drift
- mutable: free expression wording
- unresolved: a decision requiring discussion or a bounded assumption

Creative stages can write only mutable fields. Adapter syntax can wrap exact/semantic fields but cannot reinterpret them.

Externalize a control only when it is user-locked, source/project-locked, platform-required, directly conflict-resolving, or supported by an observed generation failure. A speculative failure mode remains internal. On a first attempt, preserve the locked production result while leaving mutable effect detail and secondary physical response open.

Observed failure evidence authorizes a change only to the failed field. Use existing EvidenceLedger and ReferenceMap attributes for the repair; it does not authorize a new visual design axis.

`operation`, `project_scope`, `expression_request`, and `output_mode` are orthogonal to `task_kind`. Never replace `edit`, `extend`, or `bridge` with optimization, project context, Vibe, or A/B.

## MotionSpec

- goal and viewer priority
- medium/style
- start state and end handoff
- initiating action
- visual anchor
- emotional vector
- primary performance carrier
- duration
- references and any active source-backed audio, dialogue, or visible text
- shots:
  - purpose
  - inherited start state
  - focus and framing
  - camera relation and movement
  - action chain
  - performance carrier
  - space, light, and source-backed sound only when active
  - visible end state

Mark project-sourced facts separately from bounded interpretation. Never present an interpretation as a locked project fact.

## Stage status

Each stage resolves internally to:

- `ready`: all required facts exist
- `assumed`: a low-risk default was used
- `warn`: the artifact can be delivered with a known stability tradeoff
- `blocked`: a missing asset or conflicting hard decision prevents a faithful result
