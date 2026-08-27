---
name: aigc-project-context
description: Resolve current production sources for a named AIGC project, episode, scene, or shot range and compile source-backed ImageContext, VideoContext, shot cards, or continuity audits. Use when project coordinates, live production data, cross-shot continuity, reference ownership, or source conflicts matter. This skill owns project-source access and field-level authority, not final image or video prompts. Do not invoke for unrelated standalone media requests.
---

# AIGC Project Context

Turn the smallest current project-source slice into a validated context envelope. Keep project data outside the Skill so workflow updates cannot overwrite production sources.

## Ownership

- Own: project resolution, live/source access, freshness, field-level authority, source conflicts, reference roles, continuity, and context handoffs.
- Do not own: directing new coverage, changing plot or blocking, editing project sources, or rendering final media prompts.
- Final project-backed image edit: compile `ImageContext`, then continue with `aigc-image` in the same task.
- Final project-backed video prompt: compile `VideoContext`, then continue with `aigc-video` in the same task.
- Cards or audit requested: deliver that artifact and stop.

## 1. Resolve project and terminal artifact

Identify project, package root, episode, scene, shot range, requested artifact, and current source scope. Use this order:

1. current user-supplied package or registry path
2. configured external project registry
3. user-home data registry `%USERPROFILE%\.aigc-projects\registry.yaml` on Windows, or the equivalent home-directory path on another OS

Read [references/project-package-contract.md](references/project-package-contract.md) before loading a package. Load at most one project package. Never scan another project to fill a gap.

Choose one artifact:

- `ImageContext`: project facts and reference roles needed by one image edit.
- `VideoContext`: project facts, boundaries, continuity, performance intent, and references needed by one final video request.
- `shot cards`: user-visible source-backed cards for the requested range.
- `continuity audit`: mismatches between a supplied artifact and current project facts.

Do not load project context for an unrelated standalone image or video request merely because a package exists.

🔴 **CHECKPOINT · 🛑 STOP** when project identity, active package, or requested shot range has two materially different matches. Show the candidates and ask one choice. Return no mixed-project context.

## 2. Resolve source access and freshness

Read [references/source-access-and-cache.md](references/source-access-and-cache.md) when a package declares a live source, current local source, cache, or snapshot.

For every field used, record:

- source id and source type
- record, row, asset, or file coordinate
- retrieval or snapshot time
- freshness: `live`, `local_current`, `cache_validated`, `snapshot`, or `unresolved`
- exact or semantic authority

Default performance route:

1. Query only the requested records, useful boundary records, and required fields from a live source, or read the smallest useful range from a current local source.
2. Reuse a validated cache entry when its source identity and freshness evidence still match.
3. Download an attachment only when its pixels are needed for a visual claim or final reference role.
4. If live access fails, use the newest scoped approved snapshot and label its date and non-live status.
5. If neither current data nor a usable fallback exists, mark affected fields unresolved.

Text records do not require a permanent XLSX or Markdown export. Batch NDJSON and downloaded attachments belong in task-local scratch or the external package cache, never inside this Skill.

🔴 **CHECKPOINT · 🛑 STOP** before writing to a live source, refreshing a persistent cache, replacing an approved snapshot, or changing project registry/package data. Read access and task-local scratch do not authorize persistent updates.

## 3. Resolve authority per field

Default priority:

1. current user instruction
2. current readable asset, only for its assigned attributes
3. current live production record or readable current local source, resolved by the package's field precedence
4. current approved project snapshot
5. current script or storyboard not already represented above
6. derived project references
7. bounded agent interpretation

The project manifest may override this order per field. Apply priority separately to identity, composition, action, dialogue, timing, lighting, environment, continuity, and reference roles. A new composition source does not erase unrelated dialogue or identity.

Separate:

- `source fact`: directly supported by the selected source
- `working interpretation`: bounded reading that adds no production event
- `unresolved`: missing or conflicting choice that changes the result

Never put interpretation inside locked visible facts.

## 4. Load the smallest useful slice

Load only:

- requested records in physical order
- one useful boundary record on each side when continuity needs it
- matching script or storyboard fields not supplied by the live record
- referenced assets whose assigned roles matter
- applicable exclusions and project defaults

Preserve duplicate ids with suffixes, blank-id continuation rows, physical order, and numeric gaps. Do not load a full episode, project bible, asset library, or old snapshot when the requested range does not need it.

For performance interpretation, keep separate:

- locked action
- source-backed performance intent
- restrained visible performance
- interpretation source
- confidence

Visible performance may clarify how an existing action is played. It cannot introduce a new action, prop, blocking choice, camera instruction, flashback, symbol, or endpoint.

When sparse evidence permits materially different performance readings, cite the exact source gap, state the current bounded reading, contrast the viable alternatives, recommend one, and ask one focused choice before locking it. When 2–3 related creative or equal-priority source conflicts belong to the same decision, present their evidence and recommendations together and ask them in one grouped turn; do not serialize micro-questions or promote any option to source fact before the answer.

## 5. Compile the requested envelope

### ImageContext

Read [references/image-handoff.md](references/image-handoff.md). Include only project facts that constrain the image edit: base-image role, identity/wardrobe locks, scene facts, composition and depth evidence, protected lighting/color/material state, exact text, editable properties, reference-role whitelist, exclusions, provenance, and unresolved decisions.

Do not turn a white-background character sheet into scene lighting, composition, or environment control. Do not authorize generation or redesign beyond the user's requested edit.

### VideoContext

Read [references/video-handoff.md](references/video-handoff.md). Preserve exact ids, action/dialogue order, start and terminal boundaries, world-state continuity, performance intent, reference roles, duration source, and only the terminal subset required by the next handoff.

`context_status: validated` proves source integrity, not acceptance of a video structure version. Let `aigc-video` own structure review, feasibility, platform grammar, and final rendering.

### Shot cards

Read [references/shot-card-contract.md](references/shot-card-contract.md). Build full cards only when requested. Record source duration when present; otherwise use `未提供`. A source-free planning estimate cannot create an overload verdict.

### Continuity audit

Compare the supplied prompt, plan, image-edit contract, or result against current authoritative fields. List exact mismatches, stale-source risks, and unresolved decisions. Rewrite only when requested.

## 6. Validate and hand off

Before delivery, verify:

- project, package root, source scope, and shot ids are exact
- freshness and fallback status are explicit
- every field has one authority winner or remains unresolved
- every asset controls only assigned attributes
- exact dialogue, text, timing, identity, count, action order, prop state, and boundaries survive
- no full source export or unrelated project material enters the handoff
- final prompt ownership stays with `aigc-image` or `aigc-video`

When the requested final artifact is ready to continue, hand off internally in the same task. Do not ask the user to invoke another Skill and do not display an internal envelope unless requested.

## Failure recovery

| Trigger | First action | If unresolved |
| --- | --- | --- |
| Project or package ambiguous | Present exact candidates and request one choice. | Return no mixed facts. |
| Live source unavailable | Try a validated scoped cache, then newest approved snapshot. | Mark affected fields unresolved and request the missing source. |
| Cache freshness cannot be proven | Re-read the target live records. | Treat cache as snapshot evidence, never current truth. |
| Required attachment unreadable | Re-download by record id and file token, then inspect it. | Keep visual fields unresolved; text fields may still proceed independently. |
| Current local source corrupt, password-protected, unsupported, or unreadable | Request a readable export or the exact required rows. | Keep only that source's owned fields pending; preserve independently supported fields. |
| Equal-priority fields conflict | Show both values, recommend one, and ask once. | Keep affected fields pending. |
| Snapshot is older than requested state | State snapshot date and limitation. | Do not label it latest or validated-live. |
| Persistent refresh requested | Stage live data outside the active package and verify scope, counts, ids, and hashes. | Stop before replacing registry, cache, snapshot, or project data. |
| Final envelope lacks a required field | Repair only that field from current sources. | Name the blocking production decision; do not rebuild unrelated context. |

## Avoid

- Do not store project source files, production attachments, caches, or snapshots inside this Skill.
- Do not download an entire table when a scoped record query can answer the task.
- Do not treat a cache or dated snapshot as current live data without freshness evidence.
- Do not write to Feishu or another live source from read authorization.
- Do not merge projects, source versions, or asset roles.
- Do not let a derived bible or old summary overwrite current production records.
- Do not infer pixels from filenames, paths, hashes, or attachment metadata.
- Do not emit full cards before a final image/video handoff unless the user requests cards.
- Do not redesign camera, lighting, blocking, dialogue, plot, or final media syntax in the context layer.
