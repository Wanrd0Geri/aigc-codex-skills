---
name: aigc-script-context
description: Use when turning a script, storyboard, shot list, or long-form AIGC video project such as 临渊行 into shot-level context cards, continuity handoffs, performance notes, and Seedance-ready story context before final video prompt writing.
---

# AIGC Script Context

Use this skill before `aigc-seedance-prompt` when a video prompt needs story knowledge beyond the current shot. Compile source-backed production facts into a compact handoff; do not silently take over directing or final platform-prompt decisions.

## Scope and Ownership

Treat script context as a continuity compiler for already-defined scenes and shots, not a plot summary or a second directing pass.

| Request layer | Owner |
| --- | --- |
| Existing shot ids or storyboard rows -> source facts, performance translation, continuity, prop state, and previous/next handoffs | This skill |
| Script only -> new shot ids, coverage, camera/lens/movement, composition, lighting, blocking, or edit rhythm | `director-master` or another installed directing/storyboard skill |
| Validated card -> final Seedance/Doubao/Dreamina wording, duration compression or splitting, reference syntax, and platform constraints | `aigc-seedance-prompt` |

For a multi-layer request, run the needed layers in that order and return the requested final deliverable. Preserve directing choices already present in the active source, but do not create new ones here. If a required companion skill is unavailable, deliver only this skill's validated context handoff and state which downstream decision remains unresolved.

## Source Authority

Apply this source priority:

First identify the active project or source package. Do not merge sources across projects.

1. Latest user instruction.
2. Newly attached reference images, only within their explicitly assigned semantic roles.
3. Current storyboard or shot list.
4. Current episode script.
5. Project bible, outline, worldbuilding notes, and older summaries.

If sources conflict, keep the higher-priority source and note the conflict briefly. Do not let an old outline overwrite the current storyboard or script.

Current storyboard and script are production truth. Outline and worldbuilding can fill missing context only; they must not override current storyboard, script, exclusions, or latest user instructions.

Project exclusions override raw source rows. If a project package marks a scene, shot, placeholder row, or asset as excluded, skip it even when the original spreadsheet or script still contains it.

Separate source-backed **locked facts** from **working inferences** before building a card. A working inference may bridge a minor omission only when it does not change shot ids, dialogue, action order, camera, lighting, blocking, prop state, or the ending handoff. Label it as an inference and never place it in `当前画面事实` as production truth. If the missing fact requires one of those choices, leave it unresolved and ask or route instead of inventing it.

## 🔴 CHECKPOINT · One Blocking Question

Before building or handing off, stop and ask exactly one concise question only when the answer is required to prevent a materially different production result:

1. The active project is ambiguous.
2. Two active sources at the same priority conflict, and recency, version labels, and project exclusions do not resolve them.
3. A reference image's semantic role is unspecified and could control conflicting layers such as identity/clothing versus space/composition/light.
4. A missing source fact requires a choice between materially different shot actions, dialogue or action order, prop state, subject position, or ending handoff.

If several triggers exist, ask only the first unresolved blocker in that order. Do not stop for a choice already resolved by source priority, version, or exclusion; a user-set duration such as 8 seconds; an optional missing scene reference; or the mere transition between a requested audit/card-only stage and an explicit follow-up final-prompt stage. Continue within the requested stage, label unspecified visual layers, flag overload, and route implementation choices owned by `director-master` or `aigc-seedance-prompt` without adding a confirmation turn.

## Workflow

1. Identify the project and source package. If a matching project package exists in the current workspace, load its project context first. If the requested package is absent, ask for the package, source files, or relevant excerpts instead of assuming project facts.
2. Classify the requested layer with the ownership table. Route new shot design before context compilation; keep an existing shot design unchanged.
3. Locate the requested episode, scene, shot range, and each reference image's semantic role.
4. If no prepared scene context exists, fall back to the project raw-source extraction rules before answering; do not rely on a scene-index summary alone.
5. Separate locked facts, permitted working inferences, and unresolved choices. Build the card from locked facts; label any permitted inference outside `当前画面事实`.
6. Include only what the current shot needs: function, inherited state, visible facts, source-supported performance cues, dialogue, prop state, and next-shot handoff.
7. Record a source duration when present; otherwise estimate by visual complexity and flag overload without redesigning the shot.
8. Validate the card before output or handoff: exact shot ids, identity, action/dialogue order, emotion, prop state, inherited camera relation, and previous/next continuity.
9. When the user asks for a final video prompt, pass the validated card to `aigc-seedance-prompt` and return its final deliverable; do not expose an extra planning stage unless a decision is unresolved.

## Output Modes

- **Context card only**: when the user asks for source-backed cards, existing-shot context, continuity extraction, or production handoff.
- **Handoff to Seedance**: when the user asks for a Seedance/Doubao/Dreamina prompt. Produce a compact card first internally, then draft using `aigc-seedance-prompt` rules.
- **Continuity audit**: when the user asks whether a prompt matches the script/storyboard. Compare against source priority and report mismatches; rewrite only when separately requested.

## Duration Heuristic

Use this when the storyboard has no per-shot duration:

- Simple object, still reaction, or one clean action: 4-6 seconds.
- Standard acting beat, dialogue beat, or one subject movement: 6-10 seconds.
- Complex blocking, multiple subjects, reveal, VFX, or strong camera move: 10-15 seconds.
- If the estimate exceeds 15 seconds or a user-set duration cannot hold the locked beats, mark the card as overloaded and preserve story function, action order, and dialogue. Do not split, delete beats, or redesign camera here; pass the intact card and duration constraint to `aigc-seedance-prompt` for that decision.

Do not write frame rate, resolution, aspect ratio, or platform settings inside the prompt body unless the user explicitly asks.

## Shot Context Card

Read `references/shot-card-contract.md` before building any card and use its field names and meanings verbatim; it is the single source of truth for the card schema. This file remains authoritative for workflow and cross-skill ownership. Downstream mapping in `aigc-seedance-prompt` depends on the contract names.

Translate source-stated performance beyond labels such as `愤怒`, `震惊`, or `害怕` into visible gaze, posture, pause, breath, contact, and expression cues. Do not let performance translation introduce a new action, blocking choice, prop state, camera instruction, or endpoint.

## References

- Read `references/shot-card-contract.md` when building shot cards or duration estimates.
- Read `references/seedance-handoff.md` when the next step is a Seedance 2.0 prompt.
- Known project package: for `临渊行`, read the matching local project package only when it exists in the current workspace. Otherwise ask for the project package or source files.

## Failure Recovery

| Trigger | First action | Still unresolved |
| --- | --- | --- |
| Project ambiguous or package absent | Run the checkpoint; load only the selected package. | Ask for its name/path or source excerpts; return no project facts until supplied. |
| Scene context missing or thin | Use its extraction reference; pull requested storyboard rows in physical order, one boundary row on each side, the matching script scene, and exclusions. | If no reference exists, pull those four layers directly; list missing layers and mark affected cards pending. |
| Duplicate, blank, or gapped shot ids | Keep physical row order; suffix duplicates `a/b`; fold blank-id dialogue/actions into the surrounding requested range; preserve numeric gaps. | Ask for raw rows if order is unreadable; never collapse duplicates, create blank-id cards, or invent gap ids. |
| Source, exclusion, or reference-role conflict | Apply source authority and the role whitelist; an explicit exclusion wins over its raw row. | Run the one-question checkpoint; if unanswered, return a conflict audit only. |
| Required visual missing or row non-executable | Label the visual layer unspecified or the row pending; keep source facts only. | Route new design to a directing skill; if unavailable, deliver a source/continuity brief and stop. |
| Final-prompt handoff fails | Retry with the validated card and current-shot facts only. | If the specialist is unavailable, deliver the card, name the unresolved decision, and never improvise platform format. |

## Avoid

- Do not merge storyboard, script, outline, character assets, or exclusions across different projects.
- Do not let outline/worldbuilding overwrite current storyboard rows, current script beats, latest user instructions, or explicit exclusions.
- Do not skip raw-source fallback when the prepared scene context is missing or too thin.
- Do not treat white-background character sheets as final scene lighting, color, camera angle, or environment reference.
- Do not present a working inference as a locked source fact.
- Do not create shot ids, camera, lighting, composition, blocking, or edit choices that the active source does not contain.
- Do not make duration compression, shot splitting, beat deletion, or final platform-format decisions inside the context layer.
- Do not turn a context card into a final Seedance prompt unless the user asks for final video prompt writing.
- Do not include full plot recap, lore explanation, or every neighboring shot when the current shot only needs locked facts and continuity anchors.
