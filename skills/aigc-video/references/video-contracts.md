# Video contracts

Use these contracts silently. They prevent creative stages, language cleanup, and platform rendering from changing one another's facts.

## Contents

1. Task, evidence, reference, and lock ledgers
2. Sparse BoundaryState
3. MotionSpec and stage status

## TaskEnvelope

- `terminal_artifact`: final_video_prompt
- `platform` and `version`, or explicit `platform_neutral`
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
- operational role: reference_input | start_frame_source | end_frame_target | edit_target | extension_source | bridge_predecessor | bridge_successor; record more than one only when the user explicitly combines roles
- for `reference_input` only, one primary borrowed dimension composed from explicitly authorized atomic attributes: identity | appearance | wardrobe | prop | environment | layout | look | action | motion | camera | timing | effect | audio | voice | text | graphic
- any explicitly authorized secondary borrowed dimension
- for `start_frame_source` or `end_frame_target` only, boundary lock scope: selected composition | pose | identity | light | material | visible roster attributes, or `full_frame` when the whole supplied frame is explicitly authoritative
- one semantic label for every identity/appearance reference subject; a user-supplied character name or roster is a semantic mapping, not a borrowed identity dimension unless explicitly authorized
- two or three stable identifying traits only when subject selection is ambiguous and the traits are available from a readable asset or the user/source
- forbidden/unassigned dimensions
- exact text or identity locks, if authorized

An operational role controls task grammar. A boundary scope controls the source opening or requested terminal frame. Borrowed dimensions control which attributes may transfer from a `reference_input`; slash-separated or neighboring taxonomy terms never authorize a whole group. Preservation and inherited-state obligations from edit, extension, and bridge sources are not borrowed dimensions. Never assign borrowed dimensions to a boundary input, edit target, extension source, or bridge input merely because the anchor is present. Unassigned fields stay neutral. Preserve labels exactly through every stage. `forbidden/unassigned dimensions` are internal validation data, not a negative list for the final prompt. For multi-reference generation, render one compact positive reference summary that gives every identity/appearance subject a semantic name, adds identifying traits only when evidence is available and selection is ambiguous, and names the borrowed dimension of every reference input. The identity-definition sentence itself counts as the selected `identity`, `appearance`, or combined binding only when it explicitly names those authorized attributes; a user-supplied name alone does not. Consolidate all borrowed dimensions from the same reference-input anchor into one binding whenever possible, then use semantic names in the shot body.

## LockLedger

- exact: literals and numbers that must not change
- semantic: meaning and relationships that must not drift
- mutable: free expression wording
- unresolved: a decision requiring discussion or a bounded assumption

Creative stages can write only mutable fields. Adapter syntax can wrap exact/semantic fields but cannot reinterpret them.

Externalize a control only when it is user-locked, source/project-locked, platform-required, directly conflict-resolving, or supported by an observed generation failure. A speculative failure mode remains internal. On a first attempt, preserve the locked production result while leaving mutable effect detail and secondary physical response open.

Observed failure evidence authorizes a change only to the failed field. Use existing EvidenceLedger and ReferenceMap attributes for the repair; it does not authorize a new visual design axis.

`operation`, `project_scope`, `expression_request`, and `output_mode` are orthogonal to `task_kind`. Never replace `edit`, `extend`, or `bridge` with optimization, project context, Vibe, or A/B.

## BoundaryState

Use a BoundaryState for a source opening or ending and for a shot's visible start or terminal frame. It is a sparse boundary delta, not a duplicate shot description. Record only fields that are locked, change at that boundary, or materially affect continuity/composition:

- visible roster: subjects, effects, props, and environment anchors actually in frame
- offscreen causal sources that continue to exist but should not be rendered at this boundary
- subject world relationship plus screen position, scale, or occlusion only when materially fixed
- facing, gaze, pose, contact, and active effect or light state only when the boundary depends on them
- active action identity and phase when the next shot continues the same event rather than starting a new one
- camera framing, action-axis side, or motion vector only when it changes or must carry across the boundary

World presence never implies membership in the visible roster. A terminal BoundaryState is the desired ending image even when no later shot needs a handoff.

## MotionSpec

- goal and viewer priority
- medium/style
- segment start and terminal BoundaryStates
- initiating action
- visual anchor
- emotional vector
- primary performance carrier
- duration
- references and any active source-backed audio, dialogue, or visible text
- shots:
  - purpose
  - sparse visible-start BoundaryState
  - viewer focus and ongoing framing; dominance and scale cue only when material
  - any visible entry or exit not already expressed by the boundaries
  - ongoing camera relation and movement
  - action chain and spatial causality: world axis when material, camera side, screen-entry direction, target or impact point, gaze/body axis, inherited phase when continuing the same event across a cut, and the immediate continuation after a reveal when the reveal is not the endpoint
  - effect outcome when blocking, redirecting, dismantling, absorbing, reflecting, or evading must remain distinct
  - performance carrier
  - space, light, and source-backed sound only when active
  - sparse terminal BoundaryState
  - next handoff: only the subset of the terminal state that a later shot must inherit

For A/B, keep one shared fact-and-lock core in the MotionSpec and record two expression overlays. An overlay may vary only an unlocked or explicitly variant-scoped viewer priority, supported performance carrier, atmosphere wording, or rhythm. Never vary a shared exact or semantic lock; a user instruction that deliberately assigns different values to A and B belongs to the corresponding overlays rather than the shared core.

Externalize the visible roster, visible action chain, and only the causal clues needed to read them. Keep offscreen world continuity and unused boundary fields internal.

Mark project-sourced facts separately from bounded interpretation. Never present an interpretation as a locked project fact.

## Stage status

Each stage resolves internally to:

- `ready`: all required facts exist
- `assumed`: a low-risk default was used
- `warn`: the artifact can be delivered with a known stability tradeoff
- `blocked`: a missing asset or conflicting hard decision prevents a faithful result
