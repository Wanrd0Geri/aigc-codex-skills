# Project Package Contract

Read this reference only when the user names a project, supplies a project package, or the controlled workspace clearly contains the active project. A package is project data, not a second copy of this skill.

## Registry and Package Root

This section governs packages stored with this skill. `projects/README.md` is the skill-level registry for those packages: it maps project names and aliases to a package directory, and it is the first thing to check when the user names a project. Consult it before opening a stored package. A package the user supplies directly needs no registry entry.

Each stored package root is `projects/<id>/`, where `<id>` matches `project.id` in that package's manifest. The registry lists one row per stored package root.

Every relative path inside `project.yaml` resolves from that package root, never from the skill root and never from the registry. A manifest at `projects/linyuanxing/project.yaml` writing `contexts/EP01-storyboard.md` means `projects/linyuanxing/contexts/EP01-storyboard.md`. Do not repeat the `projects/<id>/` prefix inside the manifest.

Load at most one package per task. Never scan or merge another project to fill a gap.

A package supplied directly by the user, outside `projects/`, still follows this contract: its package root is whatever directory holds its `project.yaml`.

## Package Goals

A usable package identifies:

- the active project and package root
- current production sources and their versions/scopes
- field-scoped source precedence
- asset states and permitted roles
- project defaults
- exclusions
- prepared context locations and raw-source fallback locations

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
    # optional extensions
    readable_context: "contexts/storyboard.md"
    original_filename: "<name the file had when supplied>"
    sheet: "<worksheet name>"
    data_range: "<used range, e.g. A1:I412>"
    raw_dimension: "<reported range when wider than data_range>"
    sha256: "<uppercase hex digest of the archived file>"
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
  prepared: "contexts"
  raw_storyboard: "sources"
  raw_script: "sources/script.pdf"
  bible: "contexts/series-bible.md"
```

Equivalent Markdown or JSON packages are acceptable when they contain the same semantics. Do not require conversion merely for formatting.

## Paths and Optional Extensions

`sources[].path` is the authoritative location of one concrete source file. It always points at a file, never a directory, and it is what a source-authority or re-verification question resolves to.

`context` fields are navigation hints and may point to either a directory or a file. `prepared: "contexts"` and `raw_storyboard: "sources"` name where to look; `raw_script: "sources/script.pdf"` names one file directly. Both forms are valid, and a `context` entry never overrides `sources[].path`.

These keys are optional extensions. A package without them is still valid, and their absence is not a defect to report:

- `context.bible` — a derived, package-wide reference such as a series bible. It is derived material, not a raw source; when it conflicts with a production source, the source wins.
- `sources[].readable_context` — a prepared, directly readable conversion of that source.
- `sources[].original_filename`, `sheet`, `data_range`, `raw_dimension`, `sha256` — source-verification fields.

When a package archives an `.xlsx` source, record `sha256`, `original_filename`, `sheet`, and `data_range` for it. The digest detects a source that changed after conversion, the original filename preserves provenance across a rename, and the sheet plus range let a reader reach the same cells without guessing. Add `raw_dimension` when the workbook reports a wider range than it uses, so trailing empty columns are expected rather than treated as data.

## Validation Rules

- `schema_version`, project identity, and package root must be knowable.
- For a package stored with this skill, the registry entry, the package directory name, and `project.id` must agree. A user-supplied external package is exempt: it needs no registry entry, and its directory name need not match `project.id`.
- Every relative path must resolve from the package root and must exist. A manifest path that repeats the `projects/<id>/` prefix is malformed.
- Every source must have a type, location, scope, and current/older status.
- Source priority must be field-scoped. A single global winner is insufficient when dialogue, composition, identity, and action come from different sources.
- Every asset must declare `available_readable`, `anchor_only`, or `missing`, plus allowed roles. An unassigned asset controls nothing.
- Exclusions override matching raw rows or assets.
- Defaults fill unspecified fields only. They cannot override the current user, assigned current assets, or current production sources.
- Paths or anchors do not prove visible content. Inspect readable assets before recording visual facts.
- When an archived `.xlsx` source carries no `sha256`, drift between it and its prepared context cannot be verified; with no `sheet` or `data_range`, the cells behind a fact cannot be located again. Say so instead of assuming the conversion still matches the workbook.
- When an archived `.xlsx` source carries no `original_filename`, the provenance chain back to the file the user supplied is incomplete. Say so instead of treating the archived name as the supplied name.

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
