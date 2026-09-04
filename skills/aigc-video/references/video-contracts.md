# Video contracts

Use these contracts silently. They prevent creative stages, language cleanup, and platform rendering from changing one another's facts.

## Contents

1. Task, evidence, reference, and lock ledgers
2. SceneSpatialContract
3. ChangeSet and sparse BoundaryState
4. MotionSpec and specialist handoffs
5. Stage status
6. Visible-set/current-frame gate
7. Intent/fact gate
8. Delivery topology and semantic closure
9. Renderability gate
10. State transitions and admission (VIDEO-STATE-01)

## TaskEnvelope

- `terminal_artifact`: final_video_prompt
- `platform` and `version`, or explicit `platform_neutral`
- `task_kind`: new_text | reference | edit | extend | bridge. Use `reference` whenever an actual start-frame or end-frame asset/anchor is supplied. Use `new_text` only when start or terminal conditions are described in text with no boundary asset; record those conditions in BoundaryState without inventing an asset role.
- `operation`: draft | optimize | language_only
- `output_mode`: default | prompt_only | ab
- `expression_request`: default | explicit_vibe
- `project_scope`: optional project/episode/scene/shot ids
- `requested_duration`
- per affected shot, optional `source_shot_id` for internal traceability and a contiguous `prompt_shot_index` beginning at 1 for rendered headings; these identifiers are never interchangeable
- affected units, each with `structure_source`: current_text | visual_asset | inherited | unresolved, `structure_status`: pending | confirmed | source_preserved, `structure_version`, `structure_review_mode`, and `acceptance_ref`; `source_preserved` uses null for the last three fields when no accepted design version exists
- per affected shot or operation segment, `world_dynamics_review`: pending | resolved and, when the unit generates or redesigns visible motion, `world_dynamics_mode`: coupled_world | primary_action | intentional_stillness
- per affected shot or operation segment, `light_composite_applicability`: physical | non_physical and `light_composite_review`: pending | resolved | not_applicable under `VIDEO-LIGHT-01`; preserving operations inherit unchanged source light/integration
- per affected unit when specialist combat design applies, `combat_design_required`, `combat_design_status`: not_started | structure_ready | design_ready, and the exact `combat_structure_version` bound to its CombatHandoff

For `operation: language_only`, inherit only production state that already exists. When an existing prompt has no recorded design or light-review state, leave those fields uninitialized/null rather than inventing confirmation, `source_preserved`, or a craft review. Literal and semantic checks still apply.

### Structure provenance — VIDEO-STRUCTURE-01

Every new/reference-generated, structurally rebuilt, extended, or bridged visible unit starts `pending` with `review_required`. For optimization, strict edit, observed-result review, and repair, inherit only a structure version whose acceptance is explicitly recorded in the current text or project context and whose complete structure field set from `SKILL.md` remains preserved. Readable-source evidence and a supplied geometry asset establish facts; recorded acceptance supplies approval. Reopen affected rows when `change-impact-and-delivery.md` finds a structural dependency.

A first strict edit that preserves every structure field uses `structure_status: source_preserved` instead of inventing confirmation. Its evidence is the identified edit target, exact requested change/interval (or explicit whole-clip scope), and preservation boundary. Reuse ReferenceMap and BoundaryState for those facts; read media only where the requested change or a source-dependent claim requires it. Do not reconstruct hidden geometry merely to approve a color replacement. With no accepted design version, keep `structure_version`, `structure_review_mode`, and `acceptance_ref` null. This state is legal only for `task_kind: edit` and a ChangeSet whose dependency closure changes no structure field. It never grants permission to redesign a source, generate an extension, or bridge two clips. A previously recorded accepted version may remain `confirmed` if preserved.

A blocking-critical pose changes body footprint, crop, occlusion, contact geometry, route, locked opening/action boundary, or endpoint. Expressive posture inside the accepted blocking envelope remains a performance field. Light and world continuity facts remain in their owning ledgers and table context; they increment structure only through a visible structural dependency.

`structure_status` belongs to the affected unit and, when designed, its current structure version. `structure_review_mode` belongs to the current logical request and affected unit. Recorded confirmation sets `confirmed`; direct authorization removes the review pause for its scoped units and expires with the request. Direct authorization preserves the pending status. Use `SKILL.md` for current-user authorization phrase interpretation and `VIDEO-STATE-01` below for final admission. `source_preserved` describes source inheritance, not a user acceptance event.

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

- source identifier: retain the supplied handle, UUID, or filename to keep asset identity stable
- final material label: apply only `VIDEO-LITERAL-01` in `language-lint.md`; new/substantive platform compilation uses upload-order labels by default, while language-only cleanup retains the existing literal labels
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
- for each structural dimension and scope, `authority_owner`: the single material or current-user/source instruction that owns topology/layout, blocking/route, composition/camera, timing/cuts, or boundary state

An operational role controls task grammar. A boundary scope controls the source opening or requested terminal frame. Borrowed dimensions control which attributes may transfer from a `reference_input`; slash-separated or neighboring taxonomy terms never authorize a whole group. An attribute such as pose, composition, or material may be a borrowed dimension for `reference_input` or a boundary lock for `start_frame_source` / `end_frame_target`; the operational role determines its meaning. A `staging_map` is narrower: it may authorize only the structure-resolved geometry and map scope named in `blocking-diagram.md`. Identity, wardrobe, environment, style, material, lighting, expression, and sound retain their normal owners. Preservation and inherited-state obligations from edit, extension, and bridge sources are not borrowed dimensions. Assign borrowed dimensions only to a `reference_input`; give each other operational role its own contract. Unassigned fields stay neutral. Keep the source identifier and final material label distinct so normalization never changes asset identity or order. `forbidden/unassigned dimensions` are internal validation data, not a negative list for the final prompt. For multi-reference generation, always build the responsibility map internally; let the active platform adapter decide whether and how to render it. Use `图片1中[稳定特征]的主体作为[角色名]` only when choosing among multiple visible subjects or combining sources for one identity. Consolidate all borrowed dimensions from the same reference input into one line whenever possible.

Only one active authority owner may govern a structural dimension inside the same scope. A coarse video may own timing/cuts and camera while an image owns environment appearance, for example, but a scene image must not silently override the video's bridge topology. If two readable sources materially disagree while claiming the same structural dimension, apply an explicit current-user/source priority or leave the field unresolved and ask before compiling the table. Never simulate a priority decision by stacking prompt-side exclusions.

Record one intended rendered owner for each fact. The active platform adapter decides the exact heading and omission behavior; this internal contract only prevents duplicate ownership or presentation-only choices.

## LockLedger

- exact: current-user, source, or project literals and numbers that must not change
- semantic: meaning and relationships that must not drift
- mutable: free expression wording
- unresolved: a decision requiring discussion or a bounded assumption

Creative stages can write only mutable fields. Adapter syntax can wrap exact/semantic fields but cannot reinterpret them.

During new or substantive platform compilation, a shot-internal timestamp written by an earlier model is not automatically exact merely because it appears in a current prompt or because the surrounding structure was accepted. In that compilation path, protect it only when the current user, an authoritative source, or the accepted version specifically records it as a timing lock; otherwise treat it as mutable planning scaffold and let the active adapter replace it with causal phase language. Language-only cleanup preserves every supplied time under `VIDEO-LITERAL-01` and does not enter this normalization pass.

## VisibleSetGate

Run `VisibleSetGate` before compiling or displaying each structure-review row (and before completing an internally compiled directly-authorized unit), then run it again before final rendering for every shot or operation segment. This gate applies regardless of complexity; a structure table is an external fact view and must not contain an unseen region merely because the final prompt has not been written yet.

- `visible_start_set`: subjects, props, landmarks, and environment regions visible at the current opening frame
- `visible_path_set`: only items that enter the frame, remain visible, visibly interact, or are proven by a visible response during the camera path
- `visible_terminal_set`: the requested terminal crop and its visible endpoint
- `offscreen_causal_clue`: the smallest visible entry direction, gaze/body axis, light, impact point, or material response needed to explain an offscreen cause

World existence, persistent topology, and a hidden visual cause do not enter a visual shot clause by themselves. A concrete visual noun is rendered only when it belongs to one of these sets. This gate does not delete authoritative offscreen dialogue, narration, ambience, or sound ownership from the audible plan; record an offscreen person in the visual roster only when their presence changes visible blocking, attention, or causality. For a continuous moving shot that reveals space, an optional `visible_space_progression` records `current visible region -> region revealed by subject/camera movement -> terminal visible region`; omit it for a static shot or when no meaningful reveal occurs. The adapter and final QC consume this contract; they must not replace it with a scene-wide inventory.

## IntentFactGate

This is a human-led second-pass safeguard, not a second director and not a compliance-only pass. The current user's explicit choices and accepted source facts define the intended result. Actively compare their combined meaning across the script, latest complete prompt, readable materials, current MotionSpec, project/context facts, and active platform capability. Do not invent a problem merely because the task is complex; do not silently copy a local instruction whose combined result is materially contradictory or non-executable.

Before compiling or displaying structure facts, and again before final rendering, classify each difference as:

- consistent: continue;
- uniquely inferable without changing the shootable result: resolve internally and record the evidence;
- structural blocker: a missing or unreadable fact means the shot itself cannot be identified, the current visible structure cannot be built reliably, or competing readings would materially change the structure/result; set `stage_status: blocked`, ask before displaying a row, and do not guess;
- pending field: the row remains reliable and only a field such as duration, exact dialogue, identity, or one material relationship is missing; write that cell as `待确认`, include it in the same grouped structure-table question, and block only final rendering until it is resolved;
- result-changing conflict: a direct conflict, evidence-backed suspected typo, or capability mismatch changes the result or makes it non-executable; set `stage_status: blocked` and do not render a partial prompt.

Record the compared facts, whether they can coexist, and their visible or executable consequence internally. A question is justified only when that consequence is material and unresolved. When the combined specification is clear, complete, and consistent, proceed without narrating the check or inventing alternatives. For a blocked request, scan the complete affected unit and ask once with every root conflict, evidence, smallest distinct shootable options, and a recommendation; do not display a structure row or final prompt containing the blocked fact. Current-user priority does not silently overwrite an authoritative readable/confirmed fact when the wording is plausibly mistaken. A suspected typo blocks only when it conflicts with that authoritative fact or makes the result non-executable; a wording-only difference does not trigger a question. Once the user explicitly confirms that the new instruction is an intentional field change, update that field's authority and continue without asking the same conflict again.

## DeliveryTopology

For two or more shots, multiple cut points, or a complete sequence, the default terminal artifact is one unified continuous command/timeline. Separate prompts are an explicit exception for a single shot or a current-user request for separate outputs. Every rendered shot segment must be semantically executable from its own current visible start through its terminal state, including the current subject/asset state, spatial relation, action phase, camera-visible result, and handoff facts needed by that interval. This semantic closure is local state completeness inside the unified command; it does not create independent prompt cards, repeat the global material package, or change delivery topology. Continuity is carried by current-state wording, not by asking the model to consult an earlier paragraph or by restaging a completed onset.

Externalize a control only when it is user-locked, source/project-locked, an active personal default, platform-required, directly conflict-resolving, or supported by an observed generation failure. A speculative failure mode remains internal. On a first attempt, preserve the locked production result while leaving mutable effect detail and secondary physical response open.

Observed failure evidence authorizes a change only to the failed field. Use existing EvidenceLedger and ReferenceMap attributes for the repair; it does not authorize a new visual design axis.

`operation`, `project_scope`, `expression_request`, and `output_mode` are orthogonal to `task_kind`. Never replace `edit`, `extend`, or `bridge` with optimization, project context, Vibe, or A/B.

## RenderabilityGate

Before final delivery, classify every material internal decision in the current MotionSpec:

- `generation_control`: an active, source-backed or authorized decision that materially changes what the model must show, perform, hear, synchronize, preserve, or reach. This includes playable task and feedback logic, a shared relationship change, a performance continuity anchor, an emotional/experiential progression, a selected beat-to-action mapping, camera-visible result, active light/world response, and boundary handoff.
- `metadata_only`: evidence identifiers, confidence, source-shot mapping, stage status, feasibility estimates, rejected alternatives, diagnosis, and validation history. These stay internal unless the current user explicitly requests an audit rather than a generation artifact.

Every `generation_control` must have an explicit natural rendered owner at the smallest valid scope: a global owning heading, one shot or operation segment, or the standing output sentence. A boundary or continuity fact may be restated only where local semantic closure requires both the prior endpoint and the next cut-in; treat that as one paired handoff, not permission for global repetition. A control may be omitted only when it is inactive, immaterial to the produced result, or already represented by the same semantic fact at its smallest valid scope. Never print schema labels or copy the analysis block; compile the decision into observable state, playable task, causal action, audible/synchronization relation, or endpoint. If an active control has no rendered owner, final admission fails. If metadata appears in the executable prompt, language admission fails.

## SceneSpatialContract

Use `SceneSpatialContract[]` only when several shots share one location and stable world topology materially affects continuity. Each contract records:

- `scene_id`, `spatial_version`, applicable shot or operation ranges, and supporting EvidenceLedger references
- source-backed regions, separators, doors, passages, portals, and connectivity
- fixed landmarks, fixed objects, and fixed light-source anchors in world space
- locked relative position, distance, height, floor, and access relationships
- explicitly locked cross-shot subject world relationships

Each consuming shot records `scene_spatial_ref: scene_id@spatial_version`. The contract owns stable world topology only. Shot and BoundaryState continue to own camera, crop, screen position, current visibility, current occlusion, current subject position, path, action axis, camera side, and action phase.

A fixed light-source anchor in `SceneSpatialContract` stores only source identity and world location. `LightCompositeSpec` owns active light authority, static intensity/exposure, and the current visible subject/material/atmosphere response; `shot-craft.md` supplies only the current crop and camera-facing visibility constraints to that result. On/off transitions, moving-light phase, occlusion change, flicker, response delay, and residual timing remain with Shot, BoundaryState, and `world-dynamics.md`; the light-composite pass consumes their current state without redefining its timing.

A single composition frame or Diagram proves only the visible shot geometry it contains. Promote a spatial fact into this contract only when current-user instruction, readable multi-view evidence, an accepted storyboard/project source, or another authoritative source establishes it across shots. Diagram may consume or check a contract; it never writes one.

Compile these facts through the normal structure-review path. Render a stable spatial fact once at the smallest scope shared by all consuming shots; shot paragraphs carry only visible changes and local continuity facts.

## ChangeSet

For any modification, optimization, failure repair, or material workflow transition, record silently in the existing ChangeSet; do not create a second state ledger:

- `event_id`, triggering `source_event`, affected unit ids, literal changed field and source
- `change_scope`: field | shot | sequence | global
- affected shot or operation ids
- invalidated dependencies and first stable unaffected boundaries
- prior/current structure version and status, acceptance evidence reference, and current request-scoped review mode; null design metadata stays null on `source_preserved`
- each touched prior corrective clause as `still_active | supplemented | superseded`, with its field/scope and the evidence for that disposition
- `delivery_scope`: complete_shot | complete_sequence | complete_prompt | complete_operation; `delivery_form`: replacement | standalone and, for a replacement, its complete current parent reference under `VIDEO-DELIVERY-01`
- `changed_fields`, `invalidated_fields`, and `rechecked_fields` at the smallest affected scope
- `delivery_decision`: wait_for_input | wait_for_review | deliver, and `admission_basis`: unresolved | confirmed_version | direct_authorized | source_preserved | language_only; attach the user/source evidence reference that supports it

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

VideoContext 1.2 mapping: preserve `visible_roster`; map `offscreen_causal_sources` to material offscreen presence; refine primary/partial visibility only from source-backed crop; promote `exact_dialogue_sound_text` to boundary state only when explicitly reaching it. Accept a dated `stale_fallback` only through its field-level snapshot or validated-cache provenance and never relabel it live. For a source-operation seam, leave any required phase unbacked by readable media or the current user unresolved. Never infer or re-ask resolved facts.

A terminal BoundaryState is the desired ending image even when no later shot needs a handoff.

## MotionSpec

- goal and one viewer priority per shot, rendered as `画面重心`
- medium/style
- segment start and terminal BoundaryStates
- initiating action
- visual anchor
- source-backed emotional/experiential direction when it materially changes the result; map it to an observable starting state, any supported change, and endpoint instead of retaining an internal adjective
- primary performance carrier
- applicable `SceneSpatialContract[]` and per-shot `scene_spatial_ref`
- per-shot or per-operation world-dynamics review and mode; primary physical driver, necessary body mechanics, selected receivers, coupling, stability lock, and residual state only when that mode calls for them
- per-shot or per-operation light/composite applicability and review; physical imagery uses the minimum source-response-integration chain, explicit non-physical imagery uses only existing graphic/black-frame continuity under `VIDEO-LIGHT-01`
- total duration and continuous, non-overlapping shot-heading ranges when the current user/source supplies them or the active adapter requires them; when ranges are active, start at zero and end exactly at total duration, keep only current-user/source-locked shot-internal timing as a separate exact fact, and never derive adjacent subdivisions; for the explicit unreadable-cut coarse-white-model exception, preserve source order and cuts and render ordered shots without invented time ranges
- references and a complete per-shot audible plan: exact dialogue/narration, visible-action foley, active ambience, or explicit no-new-event/silence; source-operation boundaries may additionally preserve already embedded music/subtitles, while new/reference generation keeps them inactive under the standing lock
- shots:
  - `structure_source`: current_text | visual_asset | inherited | unresolved
  - optional internal `source_shot_id`
  - rendered `prompt_shot_index`, contiguous from 1 in the current sequence
  - `structure_status`: pending | confirmed | source_preserved
  - `structure_version`, `acceptance_ref`, and current-request `structure_review_mode` under `VIDEO-STRUCTURE-01`; null when the preserving source edit has no accepted design version
  - purpose
  - `scene_spatial_ref` when the shot consumes a stable cross-shot topology
  - `world_dynamics_review`: pending | resolved
  - `world_dynamics_mode`: coupled_world | primary_action | intentional_stillness when the shot generates or redesigns visible motion; a dynamics-preserving strict edit may leave it unset
  - `light_composite_applicability` and `light_composite_review` under `VIDEO-LIGHT-01`; a preserving strict edit may inherit unchanged source integration
  - sparse visible-start BoundaryState
  - `VisibleSetGate` for the current start, visible path, and terminal frame
  - shot size, angle, and camera relation, including viewpoint owner when POV applies
  - current visible state, material offscreen presence, and spatial relationship
  - any visible entry or exit not already expressed by the boundaries
  - action, performance, and causal response; exact dialogue/narration belongs to the sound plan below
  - main camera movement and its visible result
  - one viewer focus / `画面重心` for the current crop; focal-plane/depth-of-field state, focus shift, and scale cue when material
  - action chain and spatial causality: action axis when material, camera side, screen-entry direction, target or impact point, gaze/body axis, inherited phase when continuing the same event across a cut, and the immediate continuation after a reveal when the reveal is not the endpoint
  - optional `visible_space_progression`: current visible region -> region revealed by the subject/camera path -> terminal visible region, only when a continuous move materially reveals space
  - effect outcome when blocking, redirecting, dismantling, absorbing, reflecting, or evading must remain distinct
  - performance carrier
  - optional `ActingTask` for a materially acting-driven dialogue, reaction, or close shot; its playable task must be rendered with visible execution rather than kept as internal-only analysis
  - `performance_continuity_anchor` only when relation, attention, intensity, or decision state must remain stable across a cut; when it controls the next performance, render that inherited state at the next shot's cut-in
  - local world layer selected by mode: coupled causal chain, primary action mechanics, or stable fields plus the sole activity beat
  - complete per-shot sound plan: exact dialogue/narration owner, `speech_visibility`: on_screen | off_screen | voiceover and separate `lip_sync_required` when speech exists, causal foley, active ambience, or explicit no-new-event/silence; only a source-operation seam may preserve already embedded music/subtitles
  - current `LightCompositeSpec`: its applicability, minimum applicable relation, and only continuity state that changes the result; do not populate physical fields for non-physical imagery
  - sparse terminal BoundaryState
  - next handoff: only the subset of the terminal state that a later shot must inherit

For A/B, keep one shared fact-and-lock core in the MotionSpec and record two variant overlays. Without explicit per-variant instructions, vary only unlocked viewer priority, supported performance carrier, atmosphere wording, or rhythm. Keep the established world driver, direction, material system, spatial contract, and resolved dynamics mode shared unless the user explicitly makes one of them the comparison variable. If the current user deliberately assigns different A/B values to another field such as camera, composition, wardrobe, or action, place only that named field in the corresponding overlays; it is variant-scoped rather than shared. Never vary any exact or semantic field that the user/source/project leaves shared. For A/B structure review, deliver one table built from the shared core; only a field deliberately placed in a variant overlay carries two labeled A/B values in its row — never two full parallel tables.

Externalize the visible roster, visible action chain, viewer priority, complete per-shot sound plan, and the smallest spatial, light-composite, or dynamic-world clues needed for physical continuity. When a review-required structure version is pending, follow the compact columns in `SKILL.md`; keep detailed optics, unused receivers, offscreen world continuity, production methods, and unused boundary fields internal until review resolves.

Mark project-sourced facts separately from bounded interpretation. Never present an interpretation as a locked project fact.

## CombatHandoff

Use one internal handoff for each combat-required unit; never attach it to unrelated tasks. Combat owns the action and director design; video owns canonical review, MotionSpec integration and final grammar.

- `structure_ready`: source locks, geometry/envelope, action/FightBeat order, contact/result, terminal boundary and a minimal DirectorDraft are ready for the canonical gate; not final rendering.
- `design_ready`: the current structure and dependencies also have complete mechanics, direction refinement, applicable VFX, sound cues, material StateRelay, feasibility and scoped text audit. Missing render evidence cannot establish or prevent this text-design status.

Record only applicable fields:

- affected unit/shot ids and exact `structure_version`; source/user locks and reference roles;
- accepted FightStory when applicable, combat/spectacle objective, geometry/envelope, initiative, atomic FightBeats, contact/force/recovery ledger and terminal boundary;
- spectacle source, trigger, route, visible result and ending when applicable;
- `DirectorDraft`: per-shot purpose, framing/crop, camera relation or move with carrier/path/end anchor, viewer priority and material focus/depth, blocking dependencies, causal cut and next cut-in;
- refined direction with CompositionProof, dynamic clarity and reference/post roles; body/weapon mechanics, optional authorized VFX, sound cues and feasibility;
- `StateRelay`: from/to shot ids and both current structure versions, material terminal -> visible bridge/unchanged carry -> next opening, and source/dependency owners for body/contact, motion/phase, world/support, weapon, form/VFX and opponent/environment state;
- scoped `CombatAudit`: applicable textual checks, status, evidence, impact, repair closure and responsible layer. Keep render-only results separate; required unresolved facts or textual conflicts cannot enter `design_ready`.

DirectorDraft supplies combat selections to the existing table: framing/camera -> `构图与机位`; viewer priority/focus -> `画面重心`; blocking/visibility -> `人物与空间`; causal action and endpoint -> `动作与终点`. Video checks its current visibility, performance, sound and light/composite owners without choosing a second combat camera design. Detailed performance/VFX/clarity refinement follows the resolved gate and preserves these structure fields; a necessary structural change reopens only its affected units.

The canonical gate owns phrase interpretation. `review_required` returns the table with `structure_ready` and stops; `direct_authorized` keeps structure pending and internal, then immediately finishes combat design; `confirmed` resumes or retains design for that accepted version. No audit introduces another user checkpoint.

Map StateRelay into existing MotionSpec owners rather than a parallel timeline: previous terminal -> sparse terminal BoundaryState; next opening -> sparse visible-start BoundaryState; visible bridge -> owning shot's causal action process; material state to inherit -> next handoff and that next shot's current wording. Body/weapon contact, action phase, world support and form/residue must survive this mapping whenever they affect execution. Keep owner identity distinct from touch or grip changes. Do not print relay/audit/version metadata in the final prompt, and do not use “同上一镜” as an executable state.

After a tracked fact or dependency changes, use `change-impact-and-delivery.md`: invalidate only affected cached mechanics, direction, VFX, relay and audit; recompute across dependent boundaries until stable. Increment only structures actually changed, return their handoffs to `structure_ready`, and rebind rows to both current endpoint versions after review resolves. For nonstructural changes, retain confirmation but clear stale `design_ready` until affected checks finish. A version match is necessary, not sufficient, for reusing dependent content.

Compile the final prompt without inventing a second attack-response chain or changing hit, block, evade, deflect, absorb, reflect, dismantle or terminal behavior. Return upstream conflicts to their smallest owning closure; never silently change choreography to make compilation easier. Video retains duration, timestamps, material labels, locks, sound grammar, platform syntax, world/light integration and complete delivery.

## State transitions and admission — VIDEO-STATE-01

Use the current MotionSpec and its latest ChangeSet to decide; status words without evidence are not approval. Only material transitions need a record. Keep this trace internal unless an audit is requested.

| Trigger | State and invalidation | Next action |
| --- | --- | --- |
| New generated unit, extension, bridge, or structural source edit | `pending`, version 1 or next affected version, scoped review mode; unset old acceptance for the changed version | Resolve required facts and structural feasibility, then review or directly compile |
| Explicit acceptance of the displayed current version | `confirmed`, unchanged version, `acceptance_ref` points to that user/project acceptance | Continue unfinished detail passes |
| Current request explicitly skips structure review | Keep `pending`; set scoped `direct_authorized`; no acceptance record | Continue once remaining requirements resolve |
| First source edit with no structural change | `source_preserved`, null version/review mode/acceptance; evidence from `VIDEO-STRUCTURE-01` | Render complete operation after its impact checks |
| Non-structural detail change | Preserve confirmed/source-preserved state; invalidate only touched world/light/sound/performance and required combat/relay dependencies | Recheck those fields, then deliver |
| Structural dependency changes after confirmation or source preservation | Increment affected design version (null becomes 1), set `pending`; invalidate dependent Diagram and combat design readiness | Rebuild affected structure under the current request's review mode |
| Pure language repair | Preserve all production state and literal locks; no new structure/version | Validate protected differences and deliver complete existing artifact |
| Delivery, cancellation, or replacement of the logical request | Expire only that request's direct authorization | A new request receives its own mode; recorded acceptance is retained only for the same version |

Before delivery, the latest ChangeSet must account for every invalidated field as rechecked or still unresolved. A detailed performance, light, or combat pass may write only within its accepted structure envelope. If it needs a structural change, return that change through the existing impact closure; it cannot silently retain the old confirmation or `design_ready`. Preserve unrelated accepted units. A confirmation reply resumes the pending stage; it never supplies missing source facts or skips an unfinished specialist phase.

Admission order:

1. Complete all internally resolvable checks. An unfinished internal pass is work to resume, not a reason to ask the user. A structural blocker or result-changing conflict under IntentFactGate gives `wait_for_input` / `unresolved`; display neither a guessed row nor a partial final prompt.
2. A review-required pending designed unit with reliable structure gives `wait_for_review`; display the reliable current rows and one grouped request. An unresolved non-structural field, including a material light/boundary fact, may share this round as `待确认` only when IntentFactGate says the row is reliable.
3. Before final rendering, every required fact, applicable world/light review, invalidated dependency, and specialist phase must be resolved. If required input is still missing after available internal work, give `wait_for_input` / `unresolved`; do not render a partial final artifact. Otherwise admit each unit from one evidenced basis: current `confirmed_version`, scoped `direct_authorized`, strict-edit `source_preserved`, or protected `language_only`. Combat design must be `design_ready` for that exact version when required, with valid dependencies and mapped StateRelay boundaries under the CombatHandoff contract above. `not_applicable` light is legal only for explicit non-physical imagery. Language-only and untouched source fields do not acquire new craft reviews merely to pass admission.
4. Check complete-unit delivery under `VIDEO-DELIVERY-01` and render. `stage_status` may be ready, assumed, or evidence-backed warn under `VIDEO-WARN-01`; it cannot override any earlier failed gate.

## Stage status

Each stage resolves internally to:

- `ready`: all required facts exist
- `assumed`: a low-risk default was used
- `warn`: an executable, evidence-backed tradeoff meeting the sole `VIDEO-WARN-01` threshold in `SKILL.md`; recommendation/count alone does not set it
- `blocked`: a missing asset or conflicting hard decision prevents a faithful result
