# Project Package Contract

Read this reference only when the user names a project, supplies a project package, or the controlled workspace clearly contains the active project. A package is project data, not a second copy of this skill.

## Package Goals

A usable package identifies:

- the active project and package root
- current production sources and their versions/scopes
- field-scoped source precedence
- asset states and permitted roles
- project defaults
- exclusions
- prepared context locations and raw-source fallback locations

Resolve relative paths from the package root. Never scan or merge another project to fill a gap.

## Recommended `project.yaml`

```yaml
schema_version: "1.0"
project:
  id: "<stable-id>"
  title: "<human title>"

sources:
  - id: current-storyboard
    type: storyboard
    path: "sources/storyboard.xlsx"
    version: "<date/tag>"
    scope: "<episode/scene range>"
    status: current
  - id: current-script
    type: script
    path: "sources/script.pdf"
    version: "<date/tag>"
    scope: "<episode/scene range>"
    status: current

source_precedence:
  composition: [current_user, assigned_current_asset, current-storyboard, current-script]
  action: [current_user, current-storyboard, current-script]
  dialogue: [current_user, current-script, current-storyboard]
  identity: [current_user, assigned_current_asset, character-registry, current-script]

assets:
  - id: character-lead
    path: "assets/characters/lead.png"
    state: available_readable
    roles: [character_identity, clothing]
    scope: "<character/version>"
    must_not_control: [scene_light, environment, camera, composition]

defaults:
  medium: "<project medium>"
  audio: "<project audio default>"
  visible_text: "<project visible-text default>"

exclusions:
  - scope: "<scene/shot/asset>"
    reason: "<why excluded>"

context:
  prepared: "projects/<id>/contexts"
  raw_storyboard: "sources/storyboard.xlsx"
  raw_script: "sources/script.pdf"
```

Equivalent Markdown or JSON packages are acceptable when they contain the same semantics. Do not require conversion merely for formatting.

## Validation Rules

- `schema_version`, project identity, and package root must be knowable.
- Every source must have a type, location, scope, and current/older status.
- Source priority must be field-scoped. A single global winner is insufficient when dialogue, composition, identity, and action come from different sources.
- Every asset must declare `available_readable`, `anchor_only`, or `missing`, plus allowed roles. An unassigned asset controls nothing.
- Exclusions override matching raw rows or assets.
- Defaults fill unspecified fields only. They cannot override the current user, assigned current assets, or current production sources.
- Paths or anchors do not prove visible content. Inspect readable assets before recording visual facts.

## Loading Strategy

Load only what the requested shot range needs:

1. project identity, exclusions, and relevant source/asset registry entries
2. prepared context for the requested range when sufficient
3. otherwise requested storyboard rows, one useful boundary row on each side, the matching script scene, and relevant assets
4. outline or worldbuilding only for missing motivation/context that does not override production truth

Do not load every episode, asset, or lore file by default.

## Missing or Partial Packages

- If project identity is ambiguous, present likely candidates and ask the user to select one.
- If a required source path is missing, name the missing layer and mark affected card fields pending.
- If prepared context is thin, use raw-source fallback rather than a scene-index summary alone.
- If no manifest exists but the active package is clear, build a temporary in-memory registry from supplied sources; do not invent absent versions, roles, or defaults.
- Keep project-specific style, naming, and exclusions in the package rather than hardcoding them into the generic skill.
