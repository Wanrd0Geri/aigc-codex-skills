# Dynamic World Modeling

Use this reference for every new/reference generation and whenever optimization changes visible motion or physical interaction. Treat the image as one already-running world, not a foreground subject animated over a static background.

## Contents

1. Core contract and evidence boundary
2. Scene scan, coupled system, and motion hierarchy
3. Rendering ownership and structure-table cell
4. Format adjustments and final audit

## Core contract

Resolve `world_activity` on every task:

- `active`: build and render a compact living-world chain; default for new/reference generation.
- `inherited`: preserve the source driver's direction, intensity, disturbance, and residual phase; default for edit, extension, and bridge.
- `intentionally_still`: keep secondary motion absent because the user locks stillness or the inspection format would be harmed by it. Record this as a completed decision, not a skipped check.

Keep this task-level mode separate from per-shot `world_dynamics_review`: `planned | source_backed | inherited | intentionally_still | unresolved` records evidence state. It never replaces `structure_status`. An active task may contain planned and source-backed shots; `planned` needs no separate dynamics question, while a materially required unreadable source-backed or inherited state remains `unresolved` inside the universal structure-confirmation row.

Build subject-to-world and world-to-subject coupling when visible evidence supports it. Let the world act before the subject enters, respond while the subject moves, and retain a decaying state after the main action ends. Camera movement never counts as world activity.

## Evidence boundary

Infer low-risk physical behavior from existing visible bodies and materials:

- breathing, weight transfer, momentum, settling, and body follow-through
- hair, cloth, loose accessories, carried objects, and flexible parts lagging or rebounding with body motion
- existing foliage, curtains, hanging objects, dust, smoke, fog, water, rain, steam, reflections, shadows, crowds, traffic, or machinery continuing plausible motion
- contact response where a visible subject touches ground, water, vegetation, a door, furniture, fabric, or another existing surface

Do not infer a new weather event, water source, plant, animal, crowd, vehicle, prop, effect, damage event, or story beat. Treat an effect consequence explicitly supplied by the current user or an upstream `aigc-vfx-combat` design card as authorized; render only that named consequence and its physically necessary response, not adjacent unstated destruction. A visible tree may support restrained leaf and branch response; it does not authorize falling leaves. A wet surface may support changing reflections under footsteps; it does not authorize new rain. When the source is unreadable, label-only, graphic UI, or silent about a material fact that would change the scene, stay neutral.

## Scene-image dynamics pass

Before planning motion, scan the entire readable scene image across foreground, midground, and background. Inventory every visible motion-capable candidate, even when it will remain inactive:

- ambient media: wind cues in existing receivers, fog, smoke, steam, rain, snow, dust, clouds, heat distortion
- liquids and responsive surfaces: rivers, shallow water, puddles, wet ground, reflections, grass, sand, loose soil, snow, debris
- flexible or suspended materials: hair, clothing, flags, curtains, foliage, ropes, paper, ornaments, hanging props
- optical and background systems: moving or occluded light, shadows, reflections, crowds, traffic, machinery
- combat/VFX receivers: existing air media, particles, cloth, vegetation, water, ground, loose objects, light, shadow, and reflections inside the effect's plausible influence zone

Treat this as a complete inventory, not an instruction to animate everything. Select only candidates that are visible, causally connected, and useful to the shot. A still image may reveal a material and a directional cue, but not necessarily its true motion phase; use gravity, slope, deformation, trails, or displaced receivers as evidence. If exact wind, flow, or effect propagation materially changes the shot and the image does not resolve it, keep it unresolved rather than claiming it was observed.

## Build one coupled system

1. Organize all source-backed persistent motion into one readable baseline system. Identify one dominant environmental driver, such as wind, gravity, water flow, rainfall, heat, machinery, vehicle passage, or moving/occluded light, while keeping other real independent flows quieter and subordinate. When an authorized combat/VFX event occurs, add at most one dominant transient driver.
2. Select only visible receivers that clarify the same world: body, attached materials, contact zone, ambient medium, responsive surface, or background system.
3. Write one causal chain in visible order: pre-existing state -> driver or contact -> material-specific response -> residual or handoff.
4. Keep direction coherent. Let depth, attachment, mass, stiffness, drag, and distance change amplitude and delay.
5. Let contact work both ways. The world may move clothing or hair; the subject may displace water, compress grass, disturb dust, shift a reflection, or set a hanging object moving.
6. Carry only material state across cuts: wind/flow direction, wetness, smoke or fog drift, branch/cloth phase, spreading ripples, disturbed dust, moving shadow, or mechanical cycle.

When combat or VFX adds the dominant transient driver, preserve the existing baseline system underneath it. Model the event as source -> propagation through space -> reachable material responses -> dissipation/residual. Respect distance, occlusion, surface orientation, mass, stiffness, fluid behavior, and delay: nearby loose cloth may snap first, fog may split then curl back, water may shear and spread, heavier branches may respond later, and distant systems may barely move. Do not add a second competing event driver or make every receiver react at once or with the same amplitude.

## Motion hierarchy

Keep one readable hierarchy instead of making everything equally active:

| Level | Typical carriers | Rule |
| --- | --- | --- |
| Primary | main body action, vehicle, attack, transformation, product operation | Preserve the viewer priority and action timing. |
| Secondary | hair, clothing, accessories, held props, body recoil and settling | Derive from primary motion, attachment, gravity, or the shared ambient driver. |
| Contact | water, ground, grass, doors, furniture, dust, nearby loose objects | Show the smallest reaction that proves physical contact. |
| Ambient | wind, rain, fog, smoke, steam, flowing water, moving light | Establish the persistent driver and do not restart it at each shot. |
| Background | foliage, curtains, crowds, traffic, machinery, clouds, reflections | Keep lower in prominence unless the environment is the subject. |

Vary response rather than writing synchronized motion: light fabric reacts sooner and travels farther than heavy cloth; hair tips move more than roots; nearby leaves respond more clearly than a distant canopy; water ripples spread after a foot leaves; a rigid prop may transmit vibration without bending.

## Rendering ownership

- Put persistent driver, direction, intensity, and background response baseline in `场景：` for Seedance generation.
- Put local body/cloth/prop/environment coupling, contact response, visible material change, and residual state in the owning `情节：` shot.
- Use the same ownership in platform-neutral prose without Seedance headings.
- Do not add a `世界动态：`, `环境动态：`, or generic control section.
- Render one compact causal sentence, not a catalog of moving objects. Repeat only a changed or continuity-critical state.

For a normal motion-bearing clip, include at least one supported living-world cue in the final prompt and, when visible contact exists, at least one two-way subject-world interaction across the clip. Treat these as quality targets rather than quotas: a one-second insert, tight face crop, explicit freeze, clean UI recording, composition-only previsualization, or stable product hero frame may legitimately carry less.

## Structure-table input

The universal table in `SKILL.md` owns its columns. Supply only continuity-critical content to `光线与环境连续性` before confirmation:

- `source_backed` or `inherited`: the source plus only a direction, active phase, disturbance, or residual state whose preservation changes the shot.
- `intentionally_still`: the explicit stillness lock and the only allowed main motion when useful.
- `unresolved`: the unreadable required fact followed by `待确认`.
- `planned`: use `—` unless a cross-shot world fact is already locked. Do not design the full receiver chain before structure is confirmed.

Examples: `继承视频1右向左风向，水面余波保持当前相位。` / `背景与灯光保持静止，仅腕表匀速转动。` / `视频中的风向无法可靠辨认，待确认。`

After confirmation, build the complete dynamic-world layer internally and render it through the normal ownership rules. Never expose review-state labels or duplicate the full shot paragraph inside the table.

## Format adjustments

- Dialogue: keep body performance primary; use breathing, clothing settle, a nearby environmental response, or persistent ambience only when visible and useful.
- Product: protect silhouette, label, and hero readability; use restrained turntable inertia, liquid/material behavior, condensation, reflection, hand contact, or surface response only when supported.
- VFX/combat: let impact, heat, pressure, light, particles, cloth, dust, water, or vegetation respond only when the requested effect could visibly cause it; keep the effect outcome and subject action dominant.
- VFX/combat table and prompt: preserve the baseline fog, water, wind, weather, or mechanical flow; then state the effect-caused disturbance, propagation order, material-specific response, and residual that survives the impact.
- Pure environment: use the environment itself as the primary system; define driver, propagation through depth, material differences, and residual state.
- One-take: maintain the same driver and accumulating disturbances along the route instead of resetting the world when framing changes.
- Previsualization/white model: downscope secondary and ambient motion to the minimum needed to prevent dead poses; omit it when it would obscure the structure being inspected.
- Strict edit: do not inject new world motion into an unrelated replacement. Preserve source dynamics unless the edit target is the dynamic behavior itself.
- Extension/bridge: inherit the boundary phase before introducing any authorized change; converge on the successor's opening world state for a bridge.

## Final audit

- Does the world have a driver other than the camera?
- Do body, clothing, hair, props, surfaces, atmosphere, foliage, water, light, and background respond only when present and visible?
- Does one cause connect the selected responses?
- Was the complete readable scene scanned before selecting the active subset?
- Do material, depth, mass, attachment, delay, amplitude, and damping differ plausibly?
- Does visible contact create an observable reaction or resistance?
- When combat/VFX is present, do baseline natural motion and the transient effect influence coexist without resetting one another?
- Does some motion pre-exist the main action or continue after it instead of starting and stopping in unison?
- Do cuts inherit direction, phase, disturbance, and residual state when the same event continues?
- Does the main action remain dominant, with no unsupported object, weather, event, or synchronized whole-frame motion added?

Repair only the failed layer internally. If the body action is correct but the world is frozen, add the smallest causal receiver chain; if motion is excessive, reduce receivers and amplitude rather than freezing the whole scene. Then follow `change-impact-and-delivery.md` and return the complete affected shot or wider affected unit, never only the repaired sentence.
