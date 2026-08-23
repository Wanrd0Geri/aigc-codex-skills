# Video contracts

Use these contracts silently. They prevent creative stages, language cleanup, and platform rendering from changing one another's facts.

## Contents

1. Task, evidence, reference, and lock ledgers
2. SceneSpatialContract
3. ChangeSet and sparse BoundaryState
4. MotionSpec and stage status

## TaskEnvelope

- `terminal_artifact`: final_video_prompt
- `platform` and `version`, or explicit `platform_neutral`
- `task_kind`: new_text | reference | edit | extend | bridge. Use `reference` whenever an actual start-frame or end-frame asset/anchor is supplied. Use `new_text` only when start or terminal conditions are described in text with no boundary asset; record those conditions in BoundaryState without inventing an asset role.
- `operation`: draft | optimize
- `output_mode`: default | prompt_only | ab
- `expression_request`: default | explicit_vibe
- `project_scope`: optional project/episode/scene/shot ids
- `requested_duration`
- affected units, each with `structure_source`: current_text | visual_asset | inherited | unresolved, `structure_status`: pending | confirmed, an incrementing `structure_version`, and current-request `structure_review_mode`: review_required | direct_authorized
- per affected shot or operation segment, `world_dynamics_review`: pending | resolved and, when the unit generates or redesigns visible motion, `world_dynamics_mode`: coupled_world | primary_action | intentional_stillness

Every new/reference-generated, structurally rebuilt, extended, or bridged visible unit starts `pending` with `review_required`. For optimization, strict edit, observed-result review, and repair, inherit only a structure version whose acceptance is explicitly recorded in the current text or project context while composition and endpoints remain preserved. Readable-source evidence and a supplied geometry asset establish facts; recorded acceptance supplies approval. Reopen affected rows when `change-impact-and-delivery.md` finds a structural dependency.

A blocking-critical pose changes body footprint, crop, occlusion, contact geometry, route, locked opening/action boundary, or endpoint. Expressive posture inside the accepted blocking envelope remains a performance field. Light and world continuity facts remain in their owning ledgers and table context; they increment structure only through a visible structural dependency.

`structure_status` belongs to the structure version. `structure_review_mode` belongs to the current logical request and affected unit. Recorded confirmation sets `confirmed`; direct authorization removes the review pause for its scoped units and expires with the request. Direct authorization preserves the pending status. Use the delivery gate in `SKILL.md` as the single owner of phrase interpretation and final admission.

## EvidenceLedger

For each fact record:

- value
- field
- source: current_user | readable_asset | project_card | storyboard | script | project_default | personal_default | inference
- confidence
- asset state: available_readable | anchor_only | missing

Apply precedence per field, not to a whole document. A newer composition instruction does not erase unrelated current dialogue or identity facts.

For source-video operations, a readable boundary controls existing visible state over old prompts, storyboards, or project cards. When unavailable or unreadable, a complete current-user BoundaryState substitutes; only required fields absent from both remain unresolved. Current requested new-segment changes or strict edits stay authoritative; older text fills only nonconflicting unresolved identity, context, relationship, or sound.

When the current user replaces a video, layout, storyboard, image, or other asset, invalidate only facts sourced from the replaced asset whose fields fall within that asset's operational role, boundary scope, or borrowed dimensions. Preserve unrelated current-user and project locks such as identity, exact dialogue, and duration. Mark directly dependent shot fields unresolved until they are rebuilt from the replacement asset. If same-named, similarly named, older, and newer files could be confused, verify the full source identifier or path before reading or reviewing one; a matching base filename is not evidence that it is the intended asset.

## ReferenceMap

For each material record:

- source identifier: keep any supplied platform handle, UUID, or filename internally so the asset cannot be confused with another input
- final material label: default to a plain upload-order label such as `图片1`, `视频1`, or `音频1`; use a literal source identifier only when the current user explicitly requests it for the current output
- asset state
- operational role: reference_input | staging_map | start_frame_source | end_frame_target | edit_target | extension_source | bridge_predecessor | bridge_successor; record more than one only when the user explicitly combines roles
- for `staging_map` only, `map_scope`: composition | route; one active version may exist per scope and owning shot
- for `reference_input` only, one primary borrowed dimension composed from explicitly authorized atomic attributes: identity | appearance | wardrobe | prop | environment | layout | look | lighting | material | silhouette | scale | action | motion | pose | blocking | composition | camera | timing | effect | audio | voice | text | graphic
- any explicitly authorized secondary borrowed dimension
- for `start_frame_source` or `end_frame_target` only, boundary lock scope: selected composition | pose | identity | light | material | visible roster attributes, or `full_frame` when the whole supplied frame is explicitly authoritative
- one semantic label for every identity/appearance reference subject; a user-supplied character name or roster is a semantic mapping, not a borrowed identity dimension unless explicitly authorized
- two or three stable identifying traits only when subject selection is ambiguous and the traits are available from a readable asset or the user/source
- forbidden/unassigned dimensions
- exact text or identity locks, if authorized

An operational role controls task grammar. A boundary scope controls the source opening or requested terminal frame. Borrowed dimensions control which attributes may transfer from a `reference_input`; slash-separated or neighboring taxonomy terms never authorize a whole group. An attribute such as pose, composition, or material may be a borrowed dimension for `reference_input` or a boundary lock for `start_frame_source` / `end_frame_target`; the operational role determines its meaning. A `staging_map` is narrower: it may authorize only the structure-resolved geometry and map scope named in `blocking-diagram.md`. Identity, wardrobe, environment, style, material, lighting, expression, and sound retain their normal owners. Preservation and inherited-state obligations from edit, extension, and bridge sources are not borrowed dimensions. Assign borrowed dimensions only to a `reference_input`; give each other operational role its own contract. Unassigned fields stay neutral. Keep the source identifier and final material label distinct so normalization never changes asset identity or order. `forbidden/unassigned dimensions` are internal validation data, not a negative list for the final prompt. For multi-reference generation, always build the responsibility map internally; let the active platform adapter decide whether and how to render it. Use `图片1中[稳定特征]的主体作为[角色名]` only when choosing among multiple visible subjects or combining sources for one identity. Consolidate all borrowed dimensions from the same reference input into one line whenever possible.

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

## SceneSpatialContract

Use `SceneSpatialContract[]` only when several shots share one location and stable world topology materially affects continuity. Each contract records:

- `scene_id`, `spatial_version`, applicable shot or operation ranges, and supporting EvidenceLedger references
- source-backed regions, separators, doors, passages, portals, and connectivity
- fixed landmarks, fixed objects, and fixed light-source anchors in world space
- locked relative position, distance, height, floor, and access relationships
- explicitly locked cross-shot subject world relationships

Each consuming shot records `scene_spatial_ref: scene_id@spatial_version`. The contract owns stable world topology only. Shot and BoundaryState continue to own camera, crop, screen position, current visibility, current occlusion, current subject position, path, action axis, camera side, and action phase.

A fixed light-source anchor stores only source identity and world location. On/off state, intensity, flicker, exposure, moving-light phase, and visible receiver response remain with Shot, BoundaryState, `shot-craft.md`, and `world-dynamics.md`.

A single composition frame or Diagram proves only the visible shot geometry it contains. Promote a spatial fact into this contract only when current-user instruction, readable multi-view evidence, an accepted storyboard/project source, or another authoritative source establishes it across shots. Diagram may consume or check a contract; it never writes one.

Compile these facts through the normal structure-review path. Render a stable spatial fact once at the smallest scope shared by all consuming shots; shot paragraphs carry only visible changes and local continuity facts.

## ChangeSet

For any modification, optimization, or failure repair, record silently:

- literal changed field and source
- `change_scope`: field | shot | sequence | global
- affected shot or operation ids
- invalidated dependencies and first stable unaffected boundaries
- structure versions that remain confirmed or increment and return to pending, plus the current request's review mode for each affected unit
- `delivery_scope`: complete_shot | complete_sequence | complete_prompt | complete_operation

Use `change-impact-and-delivery.md` as the single owner of propagation and delivery scope. This contract records the result; it does not create a second dependency map.

## BoundaryState

Use a BoundaryState for a source opening or ending and for a shot's visible start or terminal frame. It is a sparse boundary delta, not a duplicate shot description. Record only fields that are locked, change at that boundary, or materially affect continuity/composition:

- visible roster, with primary or partial visibility only when materially fixed, plus any material offscreen presence
- subject world relationship plus screen position, scale, or occlusion only when materially fixed
- facing, gaze, pose, contact, and active effect or light state only when the boundary depends on them
- active action identity and phase when the next shot continues the same event rather than starting a new one
- active world driver, direction, contact disturbance, and residual phase only when the boundary depends on them
- seam-active source-backed sound/text—dialogue, narration/voice, ambience/SFX/music, subtitle/visible text, or locked silence—with locked owner/content/position and current phase; never restart completed elements
- camera framing, relation, viewpoint owner when POV applies, action-axis side, or motion vector only when it changes or must carry across the boundary

VideoContext 1.1 mapping: preserve `visible_roster`; map `offscreen_causal_sources` to material offscreen presence; refine primary/partial visibility only from source-backed crop; promote `exact_dialogue_sound_text` to boundary state only when explicitly reaching it. For a source-operation seam, leave any required phase unbacked by readable media or the current user unresolved. Never infer or re-ask resolved facts.

A terminal BoundaryState is the desired ending image even when no later shot needs a handoff.

## MotionSpec

- goal and one viewer priority, rendered as `画面重心` only when the prompt needs it
- medium/style
- segment start and terminal BoundaryStates
- initiating action
- visual anchor
- emotional vector
- primary performance carrier
- applicable `SceneSpatialContract[]` and per-shot `scene_spatial_ref`
- per-shot or per-operation world-dynamics review and mode; primary physical driver, necessary body mechanics, selected receivers, coupling, stability lock, and residual state only when that mode calls for them
- total duration and continuous, non-overlapping time ranges that start at zero and end exactly at total duration; for the explicit unreadable-cut coarse-white-model exception, preserve source order and cuts and render ordered shots without invented time ranges
- references and any active source-backed audio, dialogue, or visible text with its boundary phase
- shots:
  - `structure_source`: current_text | visual_asset | inherited | unresolved
  - `structure_status`: pending | confirmed
  - `structure_version`
  - current-request `structure_review_mode`: review_required | direct_authorized
  - purpose
  - `scene_spatial_ref` when the shot consumes a stable cross-shot topology
  - `world_dynamics_review`: pending | resolved
  - `world_dynamics_mode`: coupled_world | primary_action | intentional_stillness when the shot generates or redesigns visible motion; a dynamics-preserving strict edit may leave it unset
  - sparse visible-start BoundaryState
  - shot size, angle, and camera relation, including viewpoint owner when POV applies
  - current visible state, material offscreen presence, and spatial relationship
  - any visible entry or exit not already expressed by the boundaries
  - action, performance, exact dialogue, and causal response
  - main camera movement and its visible result
  - viewer focus / `画面重心` only when several visible elements compete; dominance and scale cue only when material
  - action chain and spatial causality: action axis when material, camera side, screen-entry direction, target or impact point, gaze/body axis, inherited phase when continuing the same event across a cut, and the immediate continuation after a reveal when the reveal is not the endpoint
  - effect outcome when blocking, redirecting, dismantling, absorbing, reflecting, or evading must remain distinct
  - performance carrier
  - local world layer selected by mode: coupled causal chain, primary action mechanics, or stable fields plus the sole activity beat
  - space, light, and source-backed sound only when active
  - sparse terminal BoundaryState
  - next handoff: only the subset of the terminal state that a later shot must inherit

For A/B, keep one shared fact-and-lock core in the MotionSpec and record two variant overlays. Without explicit per-variant instructions, vary only unlocked viewer priority, supported performance carrier, atmosphere wording, or rhythm. Keep the established world driver, direction, material system, spatial contract, and resolved dynamics mode shared unless the user explicitly makes one of them the comparison variable. If the current user deliberately assigns different A/B values to another field such as camera, composition, wardrobe, or action, place only that named field in the corresponding overlays; it is variant-scoped rather than shared. Never vary any exact or semantic field that the user/source/project leaves shared. For A/B structure review, deliver one table built from the shared core; only a field deliberately placed in a variant overlay carries two labeled A/B values in its row — never two full parallel tables.

Externalize the visible roster, visible action chain, and only the spatial, light, or dynamic-world clues needed for physical continuity. When a review-required structure version is pending, follow the compact columns in `SKILL.md`; keep detailed optics, lighting, receiver chains, offscreen world continuity, unused receivers, and unused boundary fields internal until review resolves.

Mark project-sourced facts separately from bounded interpretation. Never present an interpretation as a locked project fact.

## Stage status

Each stage resolves internally to:

- `ready`: all required facts exist
- `assumed`: a low-risk default was used
- `warn`: the artifact can be delivered with a known stability tradeoff
- `blocked`: a missing asset or conflicting hard decision prevents a faithful result
