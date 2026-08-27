# Source access and cache

Use live production sources for current facts and local data for acceleration, reproducibility, and fallback.

## Read route

1. Resolve the requested project coordinates, required fields, and whether each authoritative source is live-connected or current-local.
2. For a live source, prefer a scoped record query over a full-table export. For a current local source, read only the required sheet, rows, section, or document range when the format supports it.
3. Reuse cache only when source identity, scope, and freshness evidence match.
4. Download attachments only when pixels must be inspected or handed to a media Skill.
5. Compile provenance with every used field.

For Feishu Base, prefer user identity for user-owned production data. Resolve URL or known coordinates, query records, and use the Base attachment command with record id and `file_token`. Follow the active `lark-base` and `lark-shared` command contracts rather than copying stale command syntax into this Skill.

Text records may remain in command output for small requests. Batch reads may use task-local NDJSON. Neither form becomes a persistent cache without explicit authorization and freshness metadata.

## Freshness decision

Treat cache as `cache_validated` only when at least one reliable basis matches the live source:

- source revision or version
- record modified time
- stable record ids plus content hash for the requested fields
- attachment `file_token` plus verified file hash

If the connector exposes no revision or modified time, re-read the requested record range and compare normalized field hashes. Do not re-download an unchanged attachment when its token and verified hash still match.

## Fallback order

```text
current authoritative scoped source: live read or readable current local range, per field precedence
validated scoped cache
newest approved scoped snapshot
unresolved
```

When a fallback is used, record its capture or validation date. `snapshot` and unverified cache are never labeled latest.

## Persistence boundary

Read-only production access authorizes:

- live reads
- task-local NDJSON
- task-local attachment download
- in-memory hash comparison

It does not authorize:

- writing production records
- changing permissions
- replacing persistent cache
- creating or replacing an approved snapshot
- changing the project registry or manifest

Persistent refresh requires a separate checkpoint. Stage new data, verify project id, source scope, record count, shot ids, attachment count, and hashes, then replace only the approved target.

## Failure recovery

| Trigger | First action | If unresolved |
| --- | --- | --- |
| Live authentication fails | Keep identity unchanged and repair the required authorization path. | Use an approved fallback and mark non-live status. |
| Scoped query unavailable | Read the smallest supported batch and filter by stable ids. | Do not download unrelated attachments. |
| Attachment download fails | Retry once with record id and exact file token after checking command usage. | Keep visual facts unresolved. |
| Cache differs from live | Use live for affected fields and mark cache stale. | Do not blend values from both versions. |
| Snapshot hash fails | Reject that snapshot file. | Request another readable source. |
| Current local source is corrupt, password-protected, unsupported, or unreadable | Request a readable export or the exact required rows. | Keep source-owned fields pending; use another source only for fields it independently owns. |
