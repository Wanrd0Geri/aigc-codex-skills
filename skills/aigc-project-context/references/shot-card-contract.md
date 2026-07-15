# Shot Card Contract

Use this contract for user-requested project-backed shot cards or card audits. For a final video request, compile `references/video-handoff.md` directly instead of instantiating full cards. Keep every delivered card source-backed, platform-neutral, and self-contained.

## Contents

1. Status and required fields
2. Card template
3. Source, asset, and interpretation rules
4. Duration and validation

## Status

Every card must declare `schema_version: "1.1"` and one status:

- `validated`: every material field needed by the requested artifact is supported; `未决项` contains no production-changing choice.
- `pending`: a named unresolved choice could change action, performance, blocking, continuity, dialogue, prop state, reference use, or the ending.
- `overloaded`: the locked beats demonstrably exceed a user/source-locked duration; the beats remain intact for downstream production decisions. A source-free planning estimate cannot create this status.

Do not label a card `validated` merely because it is well written. Validation describes source integrity, not prose quality.

## Required Fields

Use these field names verbatim:

| Field | Required content |
| --- | --- |
| `schema_version` | Contract version, currently `1.1`. |
| `状态` | `validated`, `pending`, or `overloaded`. |
| `项目` | Active project id/title and package used. |
| `集/场/镜` | Exact episode, scene, and shot ids in physical source order. |
| `来源映射` | Field-scoped source, version, and conflict resolution; do not use one flat winner for the whole card. |
| `本镜剧情功能` | Source-supported purpose of this shot in the scene. |
| `本镜起始边界` | Sparse source-locked opening state: visible roster, offscreen causal source when material, world/screen relation, pose/gaze/effect/light, and camera axis only when needed. |
| `锁定动作` | Physical actions and action order already fixed by the user or active source. |
| `当前画面事实` | Visible source facts only; never place working interpretation here. |
| `本镜终态` | Sparse source/user-locked terminal visible state plus `state: locked/unlocked`; unlocked lets video production choose it. |
| `表演意图` | User/source-supported motivation or emotional direction. |
| `可见表演` | Gaze, posture, pause, breath, contact, distance, expression, and vocal behavior that render the intent without adding action. |
| `理解来源` | Source for the intent and visible translation: `user`, `storyboard`, `script`, `project`, or `agent_inference`. |
| `置信度` | `high`, `medium`, or `low`, with a short reason when below high. |
| `对白/声音` | Exact dialogue/narration plus source-supported sound or silence. |
| `资产与参考角色` | Asset state, literal anchor, assigned role, allowed fields, and forbidden fields. |
| `时长` | Source duration when present; otherwise `未提供`, plus an optional card-only planning range when the user asks. |
| `下一镜交接` | Only the subset of `本镜终态` the next shot must inherit. |
| `未决项` | Missing material choices, conflicting sources, or assets that block validation; write `无` when none. |
| `高成本锁` | Positive identity, count, location, action, dialogue, reference-role, or continuity invariants whose drift would be costly. |

## Card Template

```yaml
schema_version: "1.1"
状态: validated
项目: "<project id/title and package>"
集/场/镜: "<exact ids>"
来源映射:
  当前画面事实: "<source id + version>"
  本镜起始边界: "<source id + version>"
  本镜终态: "<source id + version or 未锁定>"
  对白/声音: "<source id + version>"
  表演意图: "<user/storyboard/script/project/inference>"
本镜剧情功能: "<source-supported function>"
本镜起始边界:
  visible_roster: ["<subjects/effects/props actually visible>"]
  offscreen_causal_sources: ["<only when materially active>"]
  spatial_state: ["<only relevant world/screen relation, pose, light, or camera axis>"]
锁定动作:
  - "<action in locked order>"
当前画面事实:
  - "<visible fact>"
本镜终态:
  state: "<locked or unlocked>"
  visible_roster: ["<locked terminal visible subjects/effects/props>"]
  spatial_state: ["<only locked terminal position, pose, effect, light, or camera state>"]
表演意图: "<motivation or emotional direction>"
可见表演:
  - "<visible performance carrier>"
理解来源:
  表演意图: script
  可见表演: agent_inference
置信度: high
对白/声音:
  对白: "<exact text or 无>"
  声音: "<supported sound/silence or 未指定>"
资产与参考角色:
  - anchor: "<literal anchor or asset id>"
    state: available_readable
    role: character_identity
    may_control: [face, age, clothing]
    must_not_control: [scene_light, composition, camera]
时长:
  source_duration: "<value or 未提供>"
  source_complexity: "<simple / standard / complex>"
  planning_range: "<card-only estimate requested by user or 不估计>"
下一镜交接:
  - "<only required subset of 本镜终态>"
未决项: 无
高成本锁:
  - "<positive invariant to preserve>"
```

Use only fields relevant to the shot inside nested lists, but do not omit the required top-level fields.

## Source and Interpretation Rules

- Resolve authority per field. A new composition reference may override composition without changing dialogue, identity, or action order.
- Keep `当前画面事实` limited to directly supported visible facts.
- Keep `本镜起始边界` and `本镜终态` sparse. Do not copy the entire shot description into both boundaries.
- `本镜终态.state: unlocked` is valid when the source leaves the ending open and the downstream video workflow may choose it; this alone does not make the card pending.
- Put bounded interpretation in `表演意图`, `可见表演`, and `理解来源`; never disguise it as source truth.
- If two meaningful readings remain, state the evidence, current reading, alternatives, and recommendation before asking 1-3 related questions.
- A visible-performance translation may refine how a locked action is played. It may not add a new action, prop, blocking choice, camera instruction, flashback, symbol, or endpoint.

## Asset States and Roles

Use one state for every referenced asset:

- `available_readable`: the asset is present and can be inspected; visible facts may be used only within its assigned role.
- `anchor_only`: the literal anchor can be passed downstream, but its unseen contents cannot be described as fact.
- `missing`: the asset is required but unavailable; name the affected field in `未决项`.

Keep literal anchors unchanged. Unassigned references control nothing. White-background character sheets may control identity, clothing, age, silhouette, or distinguishing traits; they do not control scene lighting, color, environment, camera, or composition unless explicitly assigned.

## Duration Handling

- Record source duration exactly when present.
- When absent, record `source_complexity`; estimate a broad planning range only for card output when the user asks for one.
- Set `状态: overloaded` only when a user/source-locked duration conflicts with locked beats. For final-video handoff, leave source-free feasibility to `aigc-video`.
- Do not simplify, delete, split, merge, or redesign locked action or camera inside the context layer.

## Validation Checklist

Before returning or handing off a card, verify:

- project, episode, scene, shot ids, physical order, exclusions, and source versions are correct
- identity, subject count, location, prop state, locked action order, exact dialogue, sparse start boundary, and terminal state did not drift
- every reference has one state and a narrow assigned role
- facts, interpretation, and unresolved choices are visibly separated
- visible performance does not introduce new production choices
- `下一镜交接` is a true subset of `本镜终态` and both contain only necessary state
- when `本镜终态` is otherwise unlocked, every non-empty `下一镜交接` field still appears as a locked terminal subset
- `validated`, `pending`, or `overloaded` matches the actual card condition
