# Observed Video Failure Recovery

Load this file only when the user supplies an observed failed/unstable Seedance-family result, paired results, or another concrete prior-result error. Also load `change-impact-and-delivery.md`: this file diagnoses the smallest cause, while that file owns propagation, structure reopening, recompilation, and delivery scope. Do not preload these controls on a first attempt or generalize its heuristics to other video models. Provider guidance in this file follows the source and version recorded in `seedance-2-rules.md`.

## Generated-result review order

1. Compare requested and actual shot count, order, and cut points. Treat automated scene detection as an aid and manually verify cuts with similar color or lighting before concluding that a shot is missing.
2. Sample representative opening, action, and terminal frames for each shot. Compare framing and crop, visible roster and occlusion, camera and screen direction, action endpoint, cross-shot performance invariants, and any active exact dialogue or text.
3. Pass the observed mismatches to the attribution rules below. Recommend regenerating and replacing only one shot only when the user's workflow supports shot-level replacement; otherwise use a controlled rerun.

## FailureCase and recovery action

Record each failed shot or operation segment separately:

- observed mismatch and affected unit
- compared prompts, assets, settings, and outcomes
- `attribution_status`: unresolved | resolved
- smallest supported cause when resolved
- `next_action`, assigned only after attribution resolves

Allowed next actions:

- `controlled_rerun`: identical inputs need one comparison with a new evidence-backed hypothesis and explicit discriminating criterion
- `prompt_repair`: one prompt field aligns with the visible failure
- `asset_repair`: material content, responsibility, version, readability, or role isolation caused the failure
- `structural_replan`: evidenced locked load exceeds the current duration, one-shot capacity, or both; the resolved remedy changes duration, shot structure, or both
- `workflow_fallback`: a provider hard limit or controlled comparison establishes a current workflow capability boundary

When several causes remain plausible, keep attribution unresolved, set `stage_status: blocked`, and request the missing comparison. Different failed units may resolve to different actions.

An identical-input paired success and failure may resolve the comparison class to `generation_variance` after prompt, asset, and setting deltas are excluded. This supports `controlled_rerun` without claiming a more specific mechanism.

## Attribution before editing

1. Compare the nearest successful and failed prompts, assets, settings, and visible outcomes.
2. If exactly one changed prompt field aligns with the visible failure, resolve attribution to that field and select `prompt_repair`.
3. If a material's content, role, version, readability, or visual contamination aligns with the failure, resolve attribution to that material and select `asset_repair`.
4. If a paired success and failure have identical prompts, assets, and settings, resolve the comparison class to `generation_variance`. Select `controlled_rerun` only when the next run tests a new evidence-backed hypothesis with an explicit discriminating criterion. Preserve every prompt field.
5. When the same inputs and hypothesis produce another result that fails the declared discriminating criterion, end that rerun path and re-open attribution. The declared criterion defines recurrence across visually different failed results.
6. Select `structural_replan` when evidence shows that the current duration or one-shot execution cannot carry the locked time, space, subject count, action load, or camera load. Repeated failure triggers attribution review; resolved overload enters the classification below.
7. Select `workflow_fallback` only from a current provider hard limit or a controlled comparison that isolates the workflow boundary.
8. Treat one correlation as one case-specific hypothesis.

Every prompt repair or controlled rerun tests one fresh evidence-backed hypothesis. When no fresh hypothesis exists, end wording changes and re-open attribution.

## Structural replan classification

For an observed failure whose resolved next action is `structural_replan`, classify total-time capacity and one-shot capacity independently for every affected unit:

1. Establish total-time evidence from exact dialogue speaking time, indivisible action phases, user or source timing, and controlled duration comparisons. Treat the feasibility estimates in `single-segment-quality-control.md` as planning ranges; timestamps remain source-backed or unresolved.
2. Resolve `duration_overload` when the locked beats exceed the available duration while the current shot structure remains viable. Preserve shot count, continuous-take form, beat content, order, and endpoints; the supported remedy is the smallest evidenced duration change.
3. Resolve `one_shot_overload` when total time is sufficient while the combined subject, path, occlusion, action, or camera continuity exceeds one readable shot. Preserve total duration, beat content, order, and endpoints; the supported remedy is the successful controlled split when available, otherwise group compatible beats at source-backed action-phase boundaries and identify the feasible plan with the fewest shots.
4. Resolve `mixed_overload` when both capacities are exceeded. The supported remedy combines the smallest evidenced duration change with the fewest-shot feasible phase split and names the duration, shot-count, and continuous-take locks it changes.
5. Keep the overload subtype unresolved when required timing or phase-order evidence is missing. Preserve every independently supported finding, mark only unsupported fields `待确认`, and set `stage_status: blocked`. When controlled comparisons can distinguish the remaining subtypes, state the smallest independent comparison set, recommend that set, name the temporary lock changed by each comparison, and ask one grouped authorization. Request the latest complete affected unit plus the missing dialogue, timing, or phase-order evidence in the same round.

Filter supported remedies through the authority order in `SKILL.md` before selection. Explicit current-user permission activates its named duration, shot-count, continuous-take, or beat change. Every other user or source lock remains fixed. When every executable remedy changes a fixed lock, set `stage_status: blocked`, present the smallest distinct shootable options, name the lock each changes, recommend one, and ask one grouped choice.

Rank authorized executable remedies by the number of user or source locks preserved, then by the number of shots. Record the complete changed-field set supplied by the evidence and permission, including duration, time ranges, shot count, continuous-take form, camera strategy, and action allocation whenever each differs. A duration-only remedy changes duration. A split remedy changes the evidenced structural fields. A combined remedy changes its complete named set. Pass the selected remedy and changed fields to `change-impact-and-delivery.md`; that reference owns propagation, structure reopening, recompilation, and delivery scope under the current `structure_review_mode`.

Build each replan from the latest complete affected unit and the successful controlled comparison. An explicit source statement or visible controlled-comparison result supplies each participant-visibility, screen-order, depth, position, occlusion, path, handoff, prop, endpoint, and camera-geometry value. Action order supplies sequence; a named final roster supplies final visibility. Carry every supplied value forward. Mark every remaining spatial field `待确认`.

Apply the selected remedy through `change-impact-and-delivery.md` after its required source is present. While the latest complete affected unit is unavailable, keep `stage_status: blocked`. Under `review_required`, place supplied values and `待确认` fields in the compact affected structure rows, then request that unit, the missing fields, and structure confirmation together. Under `direct_authorized`, keep those rows internal, request only that unit and the missing evidence together, and proceed when the required evidence resolves.

Use only attributes already authorized by the user, source, project, or borrowed reference dimension. Do not introduce a new material system, symbol language, geometry, prop, action, camera choice, or style axis to make a correction distinct.

Treat the observed error and correction discussion as diagnosis evidence, not as content for Seedance. After identifying the smallest repair, rewrite that field as a standalone current visible state, action, spatial relationship, or endpoint that remains intelligible without the prior prompt or failed result. Express the intended current result directly. Retain a short local negative only when the target cannot be resolved positively and the active rules authorize it.

## Provider-documented checks are hypotheses

Use provider guidance only to form the next diagnostic hypothesis after a matching visible failure. It is neither a first-attempt checklist nor a universal Seedance rule, and it does not authorize a prompt change when the attribution rules above do not.

- If subjects, scenery, styles, or effects inherit from the wrong asset, audit the ReferenceMap first. Restore each anchor's operational role, then give each reference input one narrow primary borrowed dimension, name that dimension in the reference paragraph, and remove only an unused or conflicting reference from the next controlled comparison.
- If one action is visibly vague, discontinuous, or anatomically confused, test a local rewrite of only that action field using the active body part, direction or contact point, supported speed/amplitude/force, transition, and visible endpoint. Preserve the scene's established movement scale.
- If a specific effect shape or animation logic is wrong and a suitable user-provided or authorized reference video exists, test assigning that video only to the failed effect dimension instead of adding more descriptive prose.
- If repeated extension visibly degrades identity or image quality, test fewer extension passes. Test a fresh high-quality identity anchor only after the user supplies a literal anchor or readable asset. Permission to obtain or create one authorizes that separate asset step but does not make the asset available; re-run the evidence gate before referencing it. Do not turn this into a blanket ban on extension.
- If a crowded reference produces missing, duplicated, or merged people, test staged grouping or intermediate group images. Treat the provider's reported crowd threshold as version-specific evidence, not a permanent prompt limit.
- If visible text, pronunciation, voice match, or end-of-clip audio fails, isolate that field and use the smallest matching provider suggestion. Keep exact user-supplied text and dialogue locked unless the user approves a phonetic substitute.

## Local recovery map

| Observed failure | Smallest repair | Do not do |
| --- | --- | --- |
| Offscreen subject or landmark is pulled into the terminal frame | Remove the continuity-only mention and keep the minimum visible causal clue; state the requested terminal roster once | Add a subject blacklist or rewrite every shot |
| Scenery becomes an unintended action waypoint | Reduce the route to origin/entry, direction, and target | Delete scenery that visibly contacts, is crossed, damaged, avoided, or deliberately used |
| Energy/smoke/light becomes a physical entity | Change only material state and agency; preserve authorized silhouette, scale, position, action, and source attachment | Stack `无实体 / 仅呈现 / 并非人物`, flatten the design, or invent runes/anatomy/new emitters |
| Operational role or borrowed dimension leaks | Restore the operational role, then the affected borrowed dimension | Print the full internal forbidden-dimension map |
| Edit or extension is treated as reference generation | Restore direct source grammar for the base operation | Rewrite the whole task as `参考视频` |
| Camera instructions conflict | Preserve the locked camera and remove only the conflicting mutable move | Add several replacement moves |
| Duration or one-shot capacity is overloaded | Simplify mutable camera and connective detail, then apply the structural-replan classification to select a duration-only, split, combined, or evidence-pending remedy and propagate its exact closure | Delete or reorder locked actions/dialogue |
| Unexpected text/logo/watermark appears | Remove unnecessary source text or add one local observed-failure constraint | Add a generic negative tail |
| Audio drifts | Restore only user/source/project-supplied audio, dialogue, or silence | Add an audio policy paragraph |
| Prompt is generally unstable but no field is attributable | Preserve the prompt and run one controlled comparison for a new hypothesis and discriminating criterion | Tighten every field at once |
| A giant subject is repeatedly converted into a full wide scale tableau | If the intended priority is impact rather than full-body geography, replace the complete-subject comparison with one or two visible scale cues such as frame overflow, near-field perspective, occlusion, or a partial secondary figure at the edge | Treat wide framing as universally wrong; preserve it when full anatomy, spatial geography, or a requested group endpoint matters |
| Two subjects repeatedly receive equal visual weight although one should dominate | Keep one viewer priority, express it once as `画面重心`, and reduce the other subject to the minimum visible relationship needed for scale, causality, or continuity | Remove a locked subject, invent an exact screen percentage, or assume every two-subject frame needs unequal weight |
| A summoned or transformed figure reads as a small object enlarging | If scale-up was not intended, establish the final spatial envelope first and describe material arriving into multiple separated regions of that envelope | Ban all growth shots; scaling remains valid when it is the intended transformation |
| A revealed figure freezes after formation or resembles a held reference pose | Narrow any over-broad pose/composition borrowed dimension, then connect formation directly to the next visible action and keep one motion carrier active through the reveal | Add several unrelated camera moves or assume every pause comes from the prompt without a controlled comparison |
| An effect meant to be dismantled is redirected, deflected, or carried away | Replace the ambiguous interaction span with a visible loss-of-structure chain and an in-place terminal state, while preserving the authorized material design | Add repeated negations, change the whole effect system, or erase an explicitly requested deflection outcome |
| A requested tight shot repeatedly widens to include lower body or complete scenery | Remove only mutable visible-body or landmark requirements that exceed the intended crop, then state one observable crop boundary | Repeat `紧近景`, add a generic exclusion tail, or remove a locked interaction or group endpoint |
| An important off-axis gaze reads as looking straight ahead | Replace the abstract gaze phrase with the smallest sufficient head/face/eye orientation and a visible target | Freeze the whole body, prescribe unnecessary eye micro-motion, or rewrite unrelated performance |
| A `coupled_world` result leaves every selected receiver frozen | Keep the correct main action and restore the smallest supported driver -> attached/contact response -> residual chain | Append a generic motion list or rewrite the whole shot |
| Clothing, foliage, water, fog, and background all sway together like one layer | Restore one driver, then separate receiver timing by attachment, mass, stiffness, drag, depth, and damping | Freeze the environment, randomize every element, or prescribe frame-by-frame motion |
| Wind, flow, smoke, ripple, or moving-light direction resets or reverses at a cut | Inherit the previous boundary's direction and active phase, then advance or decay it in the new view | Restart the driver because the camera angle changed or restage the completed disturbance |
| Secondary world motion overwhelms the subject or makes the frame chaotic | Re-review the mode; reduce the receiver chain or select `primary_action` when auxiliary motion adds no visible value | Remove all physical response or add a global `环境稳定` prohibition |
| A strict replacement introduces new wind, water, particles, or background movement | Remove the injected dynamic axis and inherit the source video's existing world state while keeping the requested replacement | Recast the operation as reference generation or change unrelated source motion |

Execute the resolved next action, then propagate its dependencies through `change-impact-and-delivery.md`. Return at least the complete affected shot, the complete affected sequence for a shared handoff, the complete prompt for a global change, or the complete operation command for edit, extension, and bridge. Deliver the smallest complete executable scope. Request the latest complete affected unit when it is unavailable.
