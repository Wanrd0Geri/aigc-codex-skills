# Video contracts

Use these contracts silently. They prevent creative stages, language cleanup, and platform rendering from changing one another's facts.

## Contents

1. Task, evidence, reference, and lock ledgers
2. Sparse BoundaryState
3. MotionSpec and stage status

## TaskEnvelope

- `terminal_artifact`: final_video_prompt
- `platform` and `version`, or explicit `platform_neutral`
- `task_kind`: new_text | reference | edit | extend | bridge. Use `reference` whenever an actual start-frame or end-frame asset/anchor is supplied. Use `new_text` only when start or terminal conditions are described in text with no boundary asset; record those conditions in BoundaryState without inventing an asset role.
- `operation`: draft | optimize
- `output_mode`: default | prompt_only | ab
- `expression_request`: default | explicit_vibe
- `project_scope`: optional project/episode/scene/shot ids
- `requested_duration`
- `world_activity`: active | inherited | intentionally_still — resolve on every task; default new/reference generation to active and source operations to inherited
- `structure_review`: not_required | pending | confirmed — task level, aggregated from the per-shot `structure_gate: none | echo | blocking` defined in `SKILL.md`; any blocking shot or materially required unresolved source dynamic makes the task `pending`

For optimization of an existing accepted prompt, strict edit, extension, bridge, observed-result review, and local repair, inherit a source-backed or previously accepted structure as `confirmed` while composition remains preserved. Reopen only the affected shot rows when the operation changes a material structural field; each reopened shot re-enters at the gate its new structure source implies (`echo` for text-specified changes, `blocking` for visual reads).

## EvidenceLedger

For each fact record:

- value
- field
- source: current_user | readable_asset | project_card | storyboard | script | project_default | personal_default | inference
- confidence
- asset state: available_readable | anchor_only | missing

Apply precedence per field, not to a whole document. A newer composition instruction does not erase unrelated current dialogue or identity facts.

When the current user replaces a video, layout, storyboard, image, or other asset, invalidate only facts sourced from the replaced asset whose fields fall within that asset's operational role, boundary scope, or borrowed dimensions. Preserve unrelated current-user and project locks such as identity, exact dialogue, and duration. Mark directly dependent shot fields unresolved until they are rebuilt from the replacement asset. If same-named, similarly named, older, and newer files could be confused, verify the full source identifier or path before reading or reviewing one; a matching base filename is not evidence that it is the intended asset.

## ReferenceMap

For each material record:

- source identifier: keep any supplied platform handle, UUID, or filename internally so the asset cannot be confused with another input
- final material label: default to a plain upload-order label such as `图片1`, `视频1`, or `音频1`; use a literal source identifier only when the current user explicitly requests it for the current output
- asset state
- operational role: reference_input | start_frame_source | end_frame_target | edit_target | extension_source | bridge_predecessor | bridge_successor; record more than one only when the user explicitly combines roles
- for `reference_input` only, one primary borrowed dimension composed from explicitly authorized atomic attributes: identity | appearance | wardrobe | prop | environment | layout | look | lighting | material | silhouette | scale | action | motion | pose | blocking | composition | camera | timing | effect | audio | voice | text | graphic
- any explicitly authorized secondary borrowed dimension
- for `start_frame_source` or `end_frame_target` only, boundary lock scope: selected composition | pose | identity | light | material | visible roster attributes, or `full_frame` when the whole supplied frame is explicitly authoritative
- one semantic label for every identity/appearance reference subject; a user-supplied character name or roster is a semantic mapping, not a borrowed identity dimension unless explicitly authorized
- two or three stable identifying traits only when subject selection is ambiguous and the traits are available from a readable asset or the user/source
- forbidden/unassigned dimensions
- exact text or identity locks, if authorized

An operational role controls task grammar. A boundary scope controls the source opening or requested terminal frame. Borrowed dimensions control which attributes may transfer from a `reference_input`; slash-separated or neighboring taxonomy terms never authorize a whole group. An attribute such as pose, composition, or material may be a borrowed dimension for `reference_input` or a boundary lock for `start_frame_source` / `end_frame_target`; the operational role determines its meaning. Preservation and inherited-state obligations from edit, extension, and bridge sources are not borrowed dimensions. Never assign borrowed dimensions to a boundary input, edit target, extension source, or bridge input merely because the material is present. Unassigned fields stay neutral. Keep the source identifier and final material label distinct so normalization never changes asset identity or order. `forbidden/unassigned dimensions` are internal validation data, not a negative list for the final prompt. For multi-reference generation, always build the responsibility map internally; let the active platform adapter decide whether and how to render it. Use `图片1中[稳定特征]的主体作为[角色名]` only when choosing among multiple visible subjects or combining sources for one identity. Consolidate all borrowed dimensions from the same reference input into one line whenever possible.

Record one intended rendered owner for each fact. The active platform adapter decides the exact heading and omission behavior; this internal contract only prevents duplicate ownership or presentation-only choices.

## LockLedger

- exact: literals and numbers that must not change
- semantic: meaning and relationships that must not drift
- mutable: free expression wording
- unresolved: a decision requiring discussion or a bounded assumption

Creative stages can write only mutable fields. Adapter syntax can wrap exact/semantic fields but cannot reinterpret them.

Externalize a control only when it is user-locked, source/project-locked, an active personal default, platform-required, directly conflict-resolving, or supported by an observed generation failure. A speculative failure mode remains internal. On a first attempt, preserve the locked production result while leaving mutable effect detail and secondary physical response open.

Observed failure evidence authorizes a change only to the failed field. Use existing EvidenceLedger and ReferenceMap attributes for the repair; it does not authorize a new visual design axis.

`operation`, `project_scope`, `expression_request`, and `output_mode` are orthogonal to `task_kind`. Never replace `edit`, `extend`, or `bridge` with optimization, project context, Vibe, or A/B.

## BoundaryState

Use a BoundaryState for a source opening or ending and for a shot's visible start or terminal frame. It is a sparse boundary delta, not a duplicate shot description. Record only fields that are locked, change at that boundary, or materially affect continuity/composition:

- visible roster: subjects, effects, props, and environment anchors actually in frame
- offscreen causal sources that continue to exist but should not be rendered at this boundary
- subject world relationship plus screen position, scale, or occlusion only when materially fixed
- facing, gaze, pose, contact, and active effect or light state only when the boundary depends on them
- active action identity and phase when the next shot continues the same event rather than starting a new one
- active world driver, direction, contact disturbance, and residual phase only when the boundary depends on them
- camera framing, action-axis side, or motion vector only when it changes or must carry across the boundary

World presence never implies membership in the visible roster. A terminal BoundaryState is the desired ending image even when no later shot needs a handoff.

## MotionSpec

- goal and one viewer priority, rendered as `画面重心` only when the prompt needs it
- medium/style
- segment start and terminal BoundaryStates
- initiating action
- visual anchor
- emotional vector
- primary performance carrier
- dynamic-world layer: `world_activity`, primary physical driver, visible receivers, subject-to-world and world-to-subject coupling, material-specific delay/amplitude/damping, depth propagation, and only the residual states that must persist
- total duration and continuous, non-overlapping time ranges that start at zero and end exactly at total duration; for the explicit unreadable-cut coarse-white-model exception, preserve source order and cuts and render ordered shots without invented time ranges
- references and any active source-backed audio, dialogue, or visible text
- shots:
  - purpose
  - `world_dynamics_review`: planned | source_backed | inherited | intentionally_still | unresolved — use this only to decide the content and blocking state of `环境动态确认`; never render the enum value or a Chinese status prefix
  - sparse visible-start BoundaryState
  - shot size, angle, and camera mode
  - current visible state and material spatial relationship
  - any visible entry or exit not already expressed by the boundaries
  - action, performance, exact dialogue, and causal response
  - main camera movement and its visible result
  - viewer focus / `画面重心` only when several visible elements compete; dominance and scale cue only when material
  - action chain and spatial causality: world axis when material, camera side, screen-entry direction, target or impact point, gaze/body axis, inherited phase when continuing the same event across a cut, and the immediate continuation after a reveal when the reveal is not the endpoint
  - effect outcome when blocking, redirecting, dismantling, absorbing, reflecting, or evading must remain distinct
  - performance carrier
  - local living-world chain: inherited or current driver -> visible body/attached/contact/ambient/surface/background response -> residual state, only when active and supported
  - space, light, and source-backed sound only when active
  - sparse terminal BoundaryState
  - next handoff: only the subset of the terminal state that a later shot must inherit

For A/B, keep one shared fact-and-lock core in the MotionSpec and record two variant overlays. Without explicit per-variant instructions, vary only unlocked viewer priority, supported performance carrier, atmosphere wording, or rhythm. Keep the established world driver, direction, and material system shared unless the user explicitly makes world behavior the comparison variable. If the current user deliberately assigns different A/B values to another field such as camera, composition, wardrobe, or action, place only that named field in the corresponding overlays; it is variant-scoped rather than shared. Never vary any exact or semantic field that the user/source/project leaves shared. For A/B structure review, deliver one table built from the shared core; only a field deliberately placed in a variant overlay carries two labeled A/B values in its row — never two full parallel tables.

Externalize the visible roster, visible action chain, and the minimum dynamic-world clues needed to make the shot physically continuous. When a structure table is active, expose the governing driver/direction, selected visible response or contact, and residual/handoff state once under `环境动态确认`; do not duplicate the full shot paragraph there. Keep offscreen world continuity, unused receivers, and unused boundary fields internal.

Mark project-sourced facts separately from bounded interpretation. Never present an interpretation as a locked project fact.

## Stage status

Each stage resolves internally to:

- `ready`: all required facts exist
- `assumed`: a low-risk default was used
- `warn`: the artifact can be delivered with a known stability tradeoff
- `blocked`: a missing asset or conflicting hard decision prevents a faithful result
