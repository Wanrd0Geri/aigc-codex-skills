# Shot Card Contract

Use this contract when producing project-backed shot cards or compiling context internally for a final video request. Keep every card source-backed, platform-neutral, and self-contained.

## Status

Every card must declare `schema_version: "1.0"` and one status:

- `validated`: every material field needed by the requested artifact is supported; `未决项` contains no production-changing choice.
- `pending`: a named unresolved choice could change action, performance, blocking, continuity, dialogue, prop state, reference use, or the ending.
- `overloaded`: the locked beats exceed the requested or estimated duration; the beats remain intact for downstream production decisions.

Do not label a card `validated` merely because it is well written. Validation describes source integrity, not prose quality.

## Required Fields

Use these field names verbatim:

| Field | Required content |
| --- | --- |
| `schema_version` | Contract version, currently `1.0`. |
| `状态` | `validated`, `pending`, or `overloaded`. |
| `项目` | Active project id/title and package used. |
| `集/场/镜` | Exact episode, scene, and shot ids in physical source order. |
| `来源映射` | Field-scoped source, version, and conflict resolution; do not use one flat winner for the whole card. |
| `本镜剧情功能` | Source-supported purpose of this shot in the scene. |
| `上一镜承接` | Only the inherited pose, gaze, object, movement, screen relation, emotion, sound, or location needed now. |
| `锁定动作` | Physical actions and action order already fixed by the user or active source. |
| `当前画面事实` | Visible source facts only; never place working interpretation here. |
| `表演意图` | User/source-supported motivation or emotional direction. |
| `可见表演` | Gaze, posture, pause, breath, contact, distance, expression, and vocal behavior that render the intent without adding action. |
| `理解来源` | Source for the intent and visible translation: `user`, `storyboard`, `script`, `project`, or `agent_inference`. |
| `置信度` | `high`, `medium`, or `low`, with a short reason when below high. |
| `对白/声音` | Exact dialogue/narration plus source-supported sound or silence. |
| `资产与参考角色` | Asset state, literal anchor, assigned role, allowed fields, and forbidden fields. |
| `时长` | Source duration when present; otherwise estimate and reason. Never claim frame-exact timing. |
| `下一镜交接` | Only the outgoing state the next shot must inherit. |
| `未决项` | Missing material choices, conflicting sources, or assets that block validation; write `无` when none. |
| `禁止偏移` | Identity, count, location, staging, action, dialogue, reference-role, and continuity failures to prevent. |

## Card Template

```yaml
schema_version: "1.0"
状态: validated
项目: "<project id/title and package>"
集/场/镜: "<exact ids>"
来源映射:
  当前画面事实: "<source id + version>"
  对白/声音: "<source id + version>"
  表演意图: "<user/storyboard/script/project/inference>"
本镜剧情功能: "<source-supported function>"
上一镜承接:
  - "<only required inherited state>"
锁定动作:
  - "<action in locked order>"
当前画面事实:
  - "<visible fact>"
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
  estimate: "<range or 不需估计>"
  basis: "<visible complexity>"
下一镜交接:
  - "<only required outgoing state>"
未决项: 无
禁止偏移:
  - "<specific failure to avoid>"
```

Use only fields relevant to the shot inside nested lists, but do not omit the required top-level fields.

## Source and Interpretation Rules

- Resolve authority per field. A new composition reference may override composition without changing dialogue, identity, or action order.
- Keep `当前画面事实` limited to directly supported visible facts.
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
- Otherwise estimate from visible complexity and label the result as a planning estimate.
- If the duration cannot hold all locked beats, set `状态: overloaded`, list the conflict in `时长` and `未决项`, and preserve the complete beat order.
- Do not simplify, delete, split, merge, or redesign locked action or camera inside the context layer.

## Validation Checklist

Before returning or handing off a card, verify:

- project, episode, scene, shot ids, physical order, exclusions, and source versions are correct
- identity, subject count, location, prop state, locked action order, exact dialogue, and ending state did not drift
- every reference has one state and a narrow assigned role
- facts, interpretation, and unresolved choices are visibly separated
- visible performance does not introduce new production choices
- previous and next continuity contain only necessary state
- `validated`, `pending`, or `overloaded` matches the actual card condition
