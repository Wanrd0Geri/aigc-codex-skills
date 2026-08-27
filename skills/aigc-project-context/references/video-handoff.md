# VideoContext Handoff

Use this contract only when project context is required for a final video prompt. Do not instantiate or display full shot cards first; compile source facts directly into this compact internal envelope and continue with `aigc-video` in the same task.

## Gate

- `validated`: continue.
- `stale_fallback`: continue only with dated snapshot or validated-cache provenance; never call it current or live.
- `overloaded`: pass every locked beat and source duration intact; `aigc-video` owns the feasibility decision.
- `pending`: continue only when the unresolved item cannot change the requested final result. Otherwise discuss it before drafting.

## Envelope

```yaml
artifact: final_video_prompt
project: "<project id/title>"
shot_range: "<exact episode/scene/shot ids>"
context_schema_version: "1.2"
context_status: "validated | overloaded | pending | stale_fallback"
source_authority: "<field-scoped winners and unresolved conflicts>"
provenance:
  - field: "<field>"
    source: "<source id + record/file coordinate>"
    retrieved_at: "<timestamp or snapshot date>"
    freshness: "live | local_current | cache_validated | snapshot"
shots:
  - id: "<exact shot id>"
    start_boundary:
      visible_roster: []
      offscreen_causal_sources: []
      spatial_state: []
      world_state:
        driver: "<source/project-backed environmental or VFX driver>"
        direction: "<source direction>"
        intensity: "<source intensity when material>"
        phase: "<active material or effect phase>"
        disturbance: []
        residual: []
    locked_actions: []
    source_visible_facts: []
    performance_intent: "<source-backed intent or 未指定>"
    visible_performance: []
    terminal_boundary:
      state: "<locked or unlocked>"
      visible_roster: []
      spatial_state: []
      world_state:
        driver: "<source/project-backed environmental or VFX driver>"
        direction: "<source direction>"
        intensity: "<source intensity when material>"
        phase: "<terminal material or effect phase>"
        disturbance: []
        residual: []
    next_handoff: []
    exact_dialogue_sound_text: []
    duration: "<source value or unspecified>"
reference_map:
  - anchor: "<literal anchor or asset id>"
    state: available_readable
    role: "<narrow role>"
    may_control: []
high_cost_locks: []
user_overrides: []
project_defaults: []
open_decisions: []
requested_platform: "<named platform, unspecified, or platform_neutral>"
output_request: "<prompt only, explanation, variants, etc.>"
```

Omit empty optional fields. Populate `world_state` only from the current user, active project/source, or an already accepted boundary; never fill it with downstream motion planning. If a materially required direction, phase, disturbance, or residual is missing or contradictory, keep it unresolved in `open_decisions`. Do not include the full script, complete cards, project bible, `must_not_control` lists, or unrelated neighboring shots.

## Downstream ownership

Treat this envelope as already compiled evidence, locks, references, and boundaries. `aigc-video` maps it directly into MotionSpec without rebuilding the source ledger or asking again about resolved fields. It owns platform or platform-neutral rendering, duration feasibility, shot execution, dialogue/lip-sync syntax when applicable, protected language cleanup, and final formatting.

Preserve exact ids, anchors, identity, count, location, locked action order, dialogue, required silence, prop state, start/terminal boundaries, boundary `world_state`, and next handoff. A next handoff is only a subset of terminal state and may carry the world driver, direction, phase, disturbance, or residual that a later shot must inherit; if the rest of the terminal boundary is unlocked, every non-empty handoff field still remains locked there. `aigc-video` may add low-risk planned responses without overwriting this source-backed state. Keep bounded performance intent from authorizing new plot, props, symbols, lighting, or action.

## Role crosswalk

Normalize card `role` or package `roles` without renaming anchors. Collapse attribute-donor roles into one `reference_input`; map `start_frame` / `end_frame` to `start_frame_source` / `end_frame_target`; preserve edit, extension, and bridge roles. Record combined roles only when explicitly assigned. A role never expands `may_control`.

For `reference_input`, use only these borrowed dimensions: `identity`, `appearance`, `wardrobe`, `prop`, `environment`, `layout`, `look`, `lighting`, `material`, `silhouette`, `scale`, `action`, `motion`, `pose`, `blocking`, `composition`, `camera`, `timing`, `effect`, `audio`, `voice`, `text`, or `graphic`. Normalize only the card-specific aliases `face -> identity`, `age -> appearance`, `clothing -> wardrobe`, and `scene_light -> lighting`.

For boundary roles, copy an existing boundary-scope value; normalize `face -> identity`, `scene_light -> light`, and `age|clothing -> visible_roster_attributes`. Boundary roles receive no borrowed dimensions.

Leave absent, contradictory, or unrecognized values unresolved. Omit `must_not_control` only after every authorized value maps successfully; unlisted dimensions remain unassigned by whitelist semantics.

If uncertainty remains, present the evidence, current reading, alternatives, and recommendation, then ask one combined question. Once answered, repair only the affected envelope fields and continue; do not make the user restart the workflow.
