---
name: aigc-project-context
description: Use when a script, storyboard, shot list, project package, episode/scene/shot range, or long-form AIGC production must be compiled into validated shot cards, source-backed performance understanding, reference-role mapping, continuity handoffs, missing-asset status, or a continuity audit. This skill owns context artifacts, not the final video-platform prompt; when the user requests the final video prompt, apply this contract internally and let aigc-video deliver the result in the same task.
---

# AIGC Project Context

Compile production sources into compact, validated shot-level context. Preserve existing directing choices. Do not redesign coverage, camera, lighting, blocking, edit rhythm, dialogue, or plot unless the user explicitly asks for a directing or writing change.

## Ownership

- Own: source extraction, source conflicts, shot cards, performance interpretation, asset/reference mapping, continuity, and audits.
- Do not own: new shot design or the final platform prompt.
- When the user asks only for cards or an audit, stop at that artifact.
- When the user asks for a final video prompt, compile the validated card internally and continue with `aigc-video` in the same task. Do not make the user initiate another workflow.

## 1. Identify the active project

Locate the selected project package, episode, scene, shot range, and active source versions. Never merge sources, assets, defaults, or exclusions across projects.

If the project is ambiguous, show the likely candidates and ask the user to choose. If the package is unavailable, request the project package, source files, or relevant excerpts instead of inventing project facts.

Load a project profile only when the user names the project or the current controlled workspace clearly contains that project. Do not scan project files for an unrelated standalone image or video request.

Read `references/project-package-contract.md` when a project package or `project.yaml` is available.

## 2. Resolve source authority per field

Default source priority:

1. current user instruction
2. current readable assets, only for assigned roles
3. current storyboard or shot list
4. current episode script
5. project bible, outline, worldbuilding, and older summaries
6. bounded agent inference

Project exclusions override raw rows. Current storyboard/script override an old outline. Apply precedence per field: a new composition reference does not erase unrelated dialogue or character identity.

Separate:

- `source fact`: directly supported by the active source
- `working interpretation`: a bounded reading that connects facts without changing production choices
- `unresolved`: a missing choice that would materially change action, performance, blocking, continuity, dialogue, prop state, or ending

Never place a working interpretation inside the card's locked visible facts.

## 3. Communicate as a creative collaborator

The user prefers active dialogue. When sources support more than one meaningful interpretation:

1. cite the relevant source evidence
2. state your current reading
3. explain how the alternatives change performance or production
4. recommend one direction
5. ask 1-3 related questions together

Examples of meaningful uncertainty: nostalgia versus vigilance, whether a pause is avoidance or recognition, conflicting reference roles, two valid end states, or equal-priority source conflict.

Do not ask about choices already resolved by source version, priority, or exclusion. Decide formatting, platform-neutral card wording, ordinary duration estimation, and other non-material details yourself.

## 4. Extract only the needed context

Locate the requested rows in physical order and include only the boundary context needed to understand inherited and outgoing state.

If a prepared scene context is absent or thin, fall back to:

- requested storyboard rows
- one useful boundary row on each side
- matching script scene
- project exclusions and current asset registry

Do not rely on a scene-index summary alone. Preserve duplicate ids with suffixes, retain physical order, fold blank-id dialogue/actions into the appropriate surrounding range, and preserve numeric gaps.

## 5. Translate performance without inventing action

Keep these fields separate:

- `locked action`: what the source says physically happens
- `performance intent`: user/source-supported motivation or emotional direction
- `visible performance`: gaze, posture, pause, breath, contact, distance, or expression cues that render the intent
- `interpretation source`: user | storyboard | script | project | agent_inference
- `confidence`

Performance translation may clarify how an existing action is played. It cannot introduce a new action, prop state, blocking choice, camera instruction, flashback, symbol, or endpoint.

## 6. Build and validate the card

Read `references/shot-card-contract.md` and use its field names. A card must identify its `schema_version` and status:

- `validated`: all facts needed for the requested artifact are supported
- `pending`: a named unresolved item remains
- `overloaded`: locked beats exceed the current duration budget but have not been redesigned

Estimate duration only when no source duration exists:

- still reaction or one clean action: roughly 4-6 seconds
- standard acting or dialogue beat: roughly 6-10 seconds
- complex blocking, multiple subjects, reveal, VFX, or strong camera move: roughly 10-15 seconds

These are planning estimates, not platform timing guarantees. If a locked sequence exceeds the budget, mark it overloaded and pass it intact to video production. Do not delete, split, or redesign beats inside this skill.

Validate exact shot ids, identity, action/dialogue order, prop state, inherited camera/screen relation, performance source, and previous/next continuity.

## Output modes

- `shot cards`: source-backed cards for the requested range.
- `continuity audit`: compare a prompt or plan against active sources and list mismatches; rewrite only when requested.
- `final video request`: read `references/video-handoff.md`, compile cards silently, then let `aigc-video` deliver the final platform prompt.

For card-only output, include unresolved items and missing assets without appending a final video prompt.

## Failure recovery

| Trigger | First action | If unresolved |
| --- | --- | --- |
| Project/package ambiguous | Present the likely project interpretation and ask. | Return no mixed project facts. |
| Equal-priority sources conflict | Explain both readings and recommend one. | Mark affected fields pending until the user decides. |
| Reference role unclear | Offer the safest mapping and its consequences. | Keep the reference unassigned. |
| Scene context missing | Use raw-source fallback. | List missing layers and mark affected facts pending. |
| Required production choice absent | Separate facts from interpretation and discuss it. | Route new directing choices to an appropriate directing workflow. |
| Final video handoff lacks a validated card | Repair only missing card fields. | Deliver the card and name the unresolved final decision. |

## Avoid

- Do not merge project sources or assets across projects.
- Do not let outlines or older summaries overwrite current production sources.
- Do not present an inference as a source fact.
- Do not create shot ids, camera, lighting, composition, blocking, dialogue, or edit choices absent from the active source.
- Do not treat white-background character sheets as final scene lighting, color, camera, or environment references.
- Do not turn every context request into a plot recap.
- Do not stop at a handoff note when the user requested a final video prompt and the card can be validated.
