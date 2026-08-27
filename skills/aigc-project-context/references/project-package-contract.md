# External project package contract

Project data lives outside the Skill. A registry locates packages; a package identifies live sources, cache, snapshots, derived references, assets, field authority, defaults, and exclusions.

## Registry

Default user-data registry: `%USERPROFILE%\.aigc-projects\registry.yaml` on Windows, or the equivalent home-directory path on another OS. It is not relative to the current repository, Skill directory, or shell working directory.

```yaml
schema_version: "1.0"
projects:
  - id: "project-id"
    title: "Project title"
    aliases: ["alias"]
    package_root: "project-id"
```

Resolve relative `package_root` from the registry directory. A user-supplied absolute package path needs no registry entry. Load at most one package per task.

## Package root

Recommended layout:

```text
project-id/
├─ project.yaml
├─ connectors/       live-source coordinates and field mappings; no secrets
├─ sources/          current readable local scripts, storyboards, briefs, and shot files
├─ cache/            validated acceleration data and downloaded attachments
├─ snapshots/        dated approved immutable source captures
└─ derived/          bibles, indexes, and summaries with provenance
```

`project.yaml` must identify:

- stable project id, title, aliases, and production state
- live sources and their scopes
- current local sources, when the project is file-backed rather than connector-backed
- cache locations and freshness evidence
- approved snapshots and dates
- field-level source precedence
- assets and allowed roles
- defaults and exclusions
- derived references and their provenance

## Live source entry

```yaml
live_sources:
  - id: "current-storyboard"
    type: "feishu_base"
    access_context: "connectors/feishu-base.md"
    scope: "episode/scene range"
    status: "current_live"
    verified_at: "ISO-8601 timestamp"
```

Store resource coordinates and stable field ids when needed. Never store access tokens, refresh tokens, app secrets, device codes, or credentials.

## Current local source entry

```yaml
local_sources:
  - id: "current-script"
    type: "xlsx | docx | markdown | csv | json | other"
    path: "sources/current-script.xlsx"
    scope: "episode/scene range"
    status: "current_local"
    verified_at: "ISO-8601 timestamp"
    sha256: "optional verified content hash"
```

A project may be live-backed, local-file-backed, or hybrid. A readable current local source is first-class evidence; it is not a cache merely because it is local. Its relative path resolves from package root. File existence, filename, modified time, or an old summary alone does not prove readable content.

## Cache entry

```yaml
caches:
  - id: "storyboard-cache"
    path: "cache/storyboard.ndjson"
    source: "current-storyboard"
    scope: "episode/scene range"
    validated_at: "ISO-8601 timestamp"
    freshness_basis: "source revision, record modified time, or content hash"
```

A path alone does not prove freshness. Missing freshness evidence downgrades the cache to snapshot evidence.

## Snapshot entry

```yaml
snapshots:
  - id: "release-2026-08-24"
    root: "snapshots/2026-08-24"
    captured_at: "2026-08-24T00:00:00+08:00"
    scope: "episode/scene range"
    status: "approved_fallback"
```

Every snapshot source records original filename, sheet or document coordinate, scope, and SHA-256 when available. Snapshot date must remain visible whenever it substitutes for live data.

## Validation

- Registry project id, package directory, and `project.id` agree.
- Relative paths resolve from package root and exist.
- Live source, cache, snapshot, and derived references remain distinct.
- Current local sources remain distinct from cache and snapshots, carry scope, and pass a readable-content check before use.
- Every cache names its source and freshness basis.
- Every snapshot names capture date and scope.
- Source authority is field-scoped.
- Every asset declares state, scope, allowed roles, and prohibited roles.
- Defaults fill only unspecified fields.
- Exclusions override matching records or assets.
- Paths, hashes, record ids, and attachment tokens do not prove visible content.

## Missing or partial package

- Missing registry: accept a user-supplied package root; otherwise request it.
- Missing live source: use an approved scoped fallback only when declared.
- Missing live source in a local-file-backed package: use its readable `local_sources`; do not require a connector.
- Missing cache: query live; do not manufacture cache metadata.
- Missing snapshot: live access may still proceed; offline fallback remains unavailable.
- Malformed path or hash mismatch: mark that source unusable until repaired.
- Corrupt, password-protected, unsupported, or unreadable local source: request a readable export or the required rows. Keep fields owned only by that source unresolved; other sources may still provide only the fields they independently own.
