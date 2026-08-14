# Observed Video Failure Recovery

Load this file only when the user supplies an observed failed/unstable Seedance-family result, paired results, or another concrete prior-result error. Do not preload these controls on a first attempt or generalize its heuristics to other video models. Provider guidance in this file follows the source and version recorded in `seedance-2-rules.md`.

## Generated-result review order

1. Compare requested and actual shot count, order, and cut points. Treat automated scene detection as an aid and manually verify cuts with similar color or lighting before concluding that a shot is missing.
2. Sample representative opening, action, and terminal frames for each shot. Compare framing and crop, visible roster and occlusion, camera and screen direction, action endpoint, cross-shot performance invariants, and any active exact dialogue or text.
3. Pass the observed mismatches to the attribution rules below. Recommend regenerating and replacing only one shot only when the user's workflow supports shot-level replacement; otherwise use a controlled rerun.

## Attribution before editing

1. Compare the nearest successful and failed prompts, assets, settings, and visible outcomes.
2. If exactly one changed prompt span aligns with the visible failure, treat it as the smallest plausible cause and patch only that span.
3. If several changed spans remain plausible, state the ambiguity and request the missing comparison or user choice.
4. If prompt delta is zero, do not release or change any prompt field. Mark the cause as unassigned generation variance and request a controlled rerun or more paired samples.
5. A single correlation does not become a universal platform rule.

Use only attributes already authorized by the user, source, project, or borrowed reference dimension. Do not introduce a new material system, symbol language, geometry, prop, action, camera choice, or style axis to make a correction distinct.

Treat the observed error and correction discussion as diagnosis evidence, not as content for Seedance. After identifying the smallest repair, rewrite that field as a standalone current visible state, action, spatial relationship, or endpoint that remains intelligible without the prior prompt or failed result. Do not automatically carry phrases such as `上一版`、`这次`、`不要再`、`重新生成` or the unwanted failed object/action into the delivered prompt; retain a short local negative only when the target cannot be resolved positively and the active rules authorize it.

## Provider-documented checks are hypotheses

Use provider guidance only to form the next diagnostic hypothesis after a matching visible failure. It is neither a first-attempt checklist nor a universal Seedance rule, and it does not authorize a prompt change when the attribution rules above do not.

- If subjects, scenery, styles, or effects inherit from the wrong asset, audit the ReferenceMap first. Restore each anchor's operational role, then give each reference input one narrow primary borrowed dimension, name that dimension in the reference paragraph, and remove only an unused or conflicting reference from the next controlled comparison.
- If one action is visibly vague, discontinuous, or anatomically confused, test a local rewrite of only that action span using the active body part, direction or contact point, supported speed/amplitude/force, transition, and visible endpoint. Do not globally convert the scene to slow or small movement.
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
| Duration is overloaded | Simplify mutable camera and connective detail first | Delete or reorder locked actions/dialogue |
| Unexpected text/logo/watermark appears | Remove unnecessary source text or add one local observed-failure constraint | Add a generic negative tail |
| Audio drifts | Restore only user/source/project-supplied audio, dialogue, or silence | Add an audio policy paragraph |
| Prompt is generally unstable but no field is attributable | Hold the prompt and run a controlled comparison | Tighten every field at once |
| A giant subject is repeatedly converted into a full wide scale tableau | If the intended priority is impact rather than full-body geography, replace the complete-subject comparison with one or two visible scale cues such as frame overflow, near-field perspective, occlusion, or a partial secondary figure at the edge | Treat wide framing as universally wrong; preserve it when full anatomy, spatial geography, or a requested group endpoint matters |
| Two subjects repeatedly receive equal visual weight although one should dominate | Keep one viewer priority, express it once as `画面重心`, and reduce the other subject to the minimum visible relationship needed for scale, causality, or continuity | Remove a locked subject, invent an exact screen percentage, or assume every two-subject frame needs unequal weight |
| A summoned or transformed figure reads as a small object enlarging | If scale-up was not intended, establish the final spatial envelope first and describe material arriving into multiple separated regions of that envelope | Ban all growth shots; scaling remains valid when it is the intended transformation |
| A revealed figure freezes after formation or resembles a held reference pose | Narrow any over-broad pose/composition borrowed dimension, then connect formation directly to the next visible action and keep one motion carrier active through the reveal | Add several unrelated camera moves or assume every pause comes from the prompt without a controlled comparison |
| An effect meant to be dismantled is redirected, deflected, or carried away | Replace the ambiguous interaction span with a visible loss-of-structure chain and an in-place terminal state, while preserving the authorized material design | Add repeated negations, change the whole effect system, or erase an explicitly requested deflection outcome |
| A requested tight shot repeatedly widens to include lower body or complete scenery | Remove only mutable visible-body or landmark requirements that exceed the intended crop, then state one observable crop boundary | Repeat `紧近景`, add a generic exclusion tail, or remove a locked interaction or group endpoint |
| An important off-axis gaze reads as looking straight ahead | Replace the abstract gaze phrase with the smallest sufficient head/face/eye orientation and a visible target | Freeze the whole body, prescribe unnecessary eye micro-motion, or rewrite unrelated performance |
| The subject moves but clothing, hair, props, contact surfaces, and visible background remain frozen | Keep the correct main action and add the smallest shared driver -> one attached or contact response -> residual chain supported by existing visible materials | Append a generic list of wind, leaves, water, fog, dust, and reflections or rewrite the whole shot |
| Clothing, foliage, water, fog, and background all sway together like one layer | Restore one driver, then separate receiver timing by attachment, mass, stiffness, drag, depth, and damping | Freeze the environment, randomize every element, or prescribe frame-by-frame motion |
| Wind, flow, smoke, ripple, or moving-light direction resets or reverses at a cut | Inherit the previous boundary's direction and active phase, then advance or decay it in the new view | Restart the driver because the camera angle changed or restage the completed disturbance |
| Secondary world motion overwhelms the subject or makes the frame chaotic | Keep the main action as primary, reduce the receiver count and amplitude, and retain only one useful ambient/contact/residual chain | Remove all physical response or add a global `环境稳定` prohibition |
| A strict replacement introduces new wind, water, particles, or background movement | Remove the injected dynamic axis and inherit the source video's existing world state while keeping the requested replacement | Recast the operation as reference generation or change unrelated source motion |

Return a clean standalone local replacement sentence or field and name the exact shot, time range, sentence, or field that it replaces. If the user cannot locate the anchor or explicitly requests the complete affected shot, return that complete shot only. Never solve a local failure by rewriting unaffected shots or the whole prompt.
