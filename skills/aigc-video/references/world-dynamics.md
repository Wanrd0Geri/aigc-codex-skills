# Dynamic World Modeling

Use this reference for every final new/reference generation and whenever optimization changes visible motion or physical interaction. Review the physical world around each visible unit, then choose whether valuable coupling, primary action mechanics, or intentional stillness best serves the shot. Review is mandatory; added world motion is conditional, and the `VisibleSetGate` is mandatory even for a simple, object, environment, or previsualization shot.

## Contents

1. Core contract and evidence boundary
2. Scene scan, coupled system, and motion hierarchy
3. Rendering ownership and structure-table cell
4. Format adjustments and final audit

## Core contract

Resolve world dynamics for every affected shot or operation segment:

```text
world_dynamics_review: pending | resolved
world_dynamics_mode: coupled_world | primary_action | intentional_stillness
```

- `coupled_world`: render a useful visible causal exchange between the main action and existing world receivers.
- `primary_action`: render the main action, necessary body mechanics, and necessary prop motion; finish this layer when the action reads clearly.
- `intentional_stillness`: render the stable fields and the sole authorized activity beat.

`pending` leaves the mode unset. A new, reference-generated, rebuilt, extended, bridged, or dynamics-redesigned visible unit becomes `resolved` after one mode is selected. A structure-preserving strict edit that leaves dynamics untouched becomes `resolved` without a mode; its preservation boundary carries the source behavior.

Evidence source and confidence remain in `EvidenceLedger`. Driver, direction, disturbance, contact state, and residual phase remain in `BoundaryState`. Extension and bridge read the inherited seam state, then select a mode for the new segment. A materially required unreadable seam fact keeps the review pending and the stage blocked. Camera movement remains camera behavior.

## Evidence boundary

Infer low-risk physical behavior from existing visible bodies and materials:

- breathing, weight transfer, momentum, settling, and body follow-through
- hair, cloth, loose accessories, carried objects, and flexible parts lagging or rebounding with body motion
- existing foliage, curtains, hanging objects, dust, smoke, fog, water, rain, steam, reflections, shadows, crowds, traffic, or machinery continuing plausible motion
- contact response where a visible subject touches ground, water, vegetation, a door, furniture, fabric, or another existing surface

Do not infer a new weather event, water source, plant, animal, crowd, vehicle, prop, effect, damage event, or story beat. Treat an effect consequence explicitly supplied by the current user or a `design_ready` upstream CombatHandoff as authorized; render only that named consequence and its physically necessary response, not adjacent unstated destruction. A visible tree may support restrained leaf and branch response; it does not authorize falling leaves. A wet surface may support changing reflections under footsteps; it does not authorize new rain. When the source is unreadable, label-only, graphic UI, or silent about a material fact that would change the scene, stay neutral.

## Scene-image dynamics pass

Before planning motion, scan the entire readable scene image across foreground, midground, and background. Inventory every visible motion-capable candidate, even when it will remain inactive:

- ambient media: wind cues in existing receivers, fog, smoke, steam, rain, snow, dust, clouds, heat distortion
- liquids and responsive surfaces: rivers, shallow water, puddles, wet ground, reflections, grass, sand, loose soil, snow, debris
- flexible or suspended materials: hair, clothing, flags, curtains, foliage, ropes, paper, ornaments, hanging props
- optical and background systems: moving or occluded light, shadows, reflections, crowds, traffic, machinery
- combat/VFX receivers: existing air media, particles, cloth, vegetation, water, ground, loose objects, light, shadow, and reflections inside the effect's plausible influence zone

Treat this as a complete inventory, not an instruction to animate everything. Select only candidates that are visible, causally connected, and useful to the shot. A still image may reveal a material and a directional cue, but not necessarily its true motion phase; use gravity, slope, deformation, trails, or displaced receivers as evidence. If exact wind, flow, or effect propagation materially changes the shot and the image does not resolve it, keep it unresolved rather than claiming it was observed.

Intersect the candidate inventory with the shot's `VisibleSetGate` before compiling a structure row and again before rendering. Any region or medium that exists in the world but is outside the current crop is not a shot fact; it enters the shot only at the interval where the camera or subject visibly reveals it, and only with the visible carrier supported there.

## Build one coupled system

Use this section for `coupled_world`. Preserve every authoritative independent persistent driver that materially affects the shot, such as a valley wind and stream flow. Establish one dominant driver per causal chain; keep quieter independent systems distinct. When an authorized combat/VFX event occurs, add at most one dominant transient driver.

1. Organize source-backed persistent motion into readable baseline systems.
2. Select only visible receivers that clarify the same world: body, attached materials, contact zone, ambient medium, responsive surface, or background system.
3. Write one causal chain in visible order: pre-existing state -> driver or contact -> material-specific response -> residual or handoff.
4. Keep direction coherent. Let depth, attachment, mass, stiffness, drag, and distance change amplitude and delay.
5. Let contact work both ways. The world may move clothing or hair; the subject may displace water, compress grass, disturb dust, shift a reflection, or set a hanging object moving.
6. Carry only material state across cuts: wind/flow direction, wetness, smoke or fog drift, branch/cloth phase, spreading ripples, disturbed dust, moving shadow, or mechanical cycle.

For a continuous moving shot that materially reveals space, record and render a light `visible space progression`: current visible region -> region revealed by the subject or camera path -> terminal visible region. Keep each region limited to its current visible set; omit this progression for a static shot or when movement does not reveal a meaningful new area.

When combat or VFX adds the dominant transient driver, preserve the existing baseline system underneath it. Model the event as source -> propagation through space -> reachable material responses -> dissipation/residual. Respect distance, occlusion, surface orientation, mass, stiffness, fluid behavior, and delay: nearby loose cloth may snap first, fog may split then curl back, water may shear and spread, heavier branches may respond later, and distant systems may barely move. Do not add a second competing event driver or make every receiver react at once or with the same amplitude.

## Motion hierarchy

For `coupled_world`, keep one readable hierarchy instead of making everything equally active. For `primary_action`, use only the primary level plus necessary attached or contact mechanics. For `intentional_stillness`, protect the stable fields and one activity beat.

| Level | Typical carriers | Rule |
| --- | --- | --- |
| Primary | main body action, vehicle, attack, transformation, product operation | Preserve the viewer priority and action timing. |
| Secondary | hair, clothing, accessories, held props, body recoil and settling | Derive from primary motion, attachment, gravity, or the shared ambient driver. |
| Contact | water, ground, grass, doors, furniture, dust, nearby loose objects | Show the smallest reaction that proves physical contact. |
| Ambient | wind, rain, fog, smoke, steam, flowing water, moving light | Establish the persistent driver and do not restart it at each shot. |
| Background | foliage, curtains, crowds, traffic, machinery, clouds, reflections | Keep lower in prominence unless the environment is the subject. |

Vary response rather than writing synchronized motion: light fabric reacts sooner and travels farther than heavy cloth; hair tips move more than roots; nearby leaves respond more clearly than a distant canopy; water ripples spread after a foot leaves; a rigid prop may transmit vibration without bending.

## Rendering ownership

Evaluate each driver independently:

- When one non-light physical driver remains active and useful across every shot in the complete Seedance generation command, place its direction, intensity, and background baseline once in `场景：`.
- When a driver serves only some shots, changes direction or state, or belongs to a sequence containing `primary_action` or `intentional_stillness`, place it only in the owning `情节：` shots.
- Put local body, cloth, prop, environment, contact, material change, and residual response in the owning `情节：` shot.
- For moving, flickering, switched, or occluded light, render only its phase, transition, response delay, and residual timing here. Pass that current state to `LightCompositeSpec`, which alone renders source authority, subject/material receivers, shadows/reflections, and camera-visible exposure; do not write a second light-receiver chain.
- Use the same ownership in platform-neutral prose without Seedance headings.
- Operation commands use their own grammar and include only dynamics needed at the seam or inside the requested change.

Render one compact causal sentence for `coupled_world`. Render only the primary action mechanics for `primary_action`. State the stable result and sole activity for `intentional_stillness`. Repeat a driver only when its state changes or continuity requires it.

When the current user explicitly asks for a flowing world, environmental dynamics, or a list of environmental motion, the selected visible carriers and any needed `visible space progression` must appear in the final shot prose. Resolving `world_dynamics_review` internally without rendering the selected result is a failed gate. Keep the response causal and evidence-backed; do not satisfy the request with a generic motion suffix.

## Structure-table input

The table in `SKILL.md` owns its columns. `VIDEO-LIGHT-01` in `lighting-compositing.md` supplies the applicable physical-light or non-physical graphic/black-frame continuity to `光影、合成与环境连续性`; world dynamics may add only continuity-critical motion content to the same cell:

- For source-backed or inherited continuity, write the source plus only a direction, active phase, disturbance, or residual state whose preservation changes the shot.
- For `intentional_stillness`, write the explicit stable fields and sole activity beat when useful.
- For a materially required unreadable fact, write that fact followed by `待确认` and keep the review pending.
- Do not replace applicable light/composite continuity with `—` or invent physical receivers for explicitly non-physical imagery. When no cross-shot world-motion fact is locked, add no world-motion clause. Keep mode selection and the detailed dynamic receiver chain internal until structure review resolves.

Examples: `继承视频1右向左风向，水面余波保持当前相位。` / `背景与灯光保持静止，仅腕表匀速转动。` / `视频中的风向无法可靠辨认，待确认。`

After structure review resolves, complete the selected mode internally and render it through the normal ownership rules. Never expose review-state labels or duplicate the full shot paragraph inside the table.

## Format adjustments

- Dialogue: choose `primary_action` when body performance alone carries the beat; choose `coupled_world` when one visible nearby response improves the same beat.
- Product: use `primary_action` for clean silhouette and operation; choose `coupled_world` only for supported material, liquid, reflection, hand-contact, or surface behavior that improves product readability.
- VFX/combat: choose `coupled_world` when reachable existing receivers clarify impact, heat, pressure, or light; keep the effect outcome and subject action dominant.
- VFX/combat with `coupled_world`: preserve any authoritative baseline fog, water, wind, weather, or mechanical flow; then state the effect-caused disturbance, propagation order, material-specific response, and residual that survives the impact.
- Pure environment: normally use `coupled_world`; define existing driver, propagation through depth, material differences, and residual state.
- One-take: when `coupled_world` applies, maintain drivers and accumulating disturbances along the route as framing changes.
- Previsualization/white model: normally use `primary_action`; use `intentional_stillness` when stability is the inspection target.
- Flat graphics/screen recordings: animate only the authorized graphic/UI change; use `primary_action` for that change or `intentional_stillness` for a held screen/black frame, without adding physical world receivers.
- Strict edit: resolve without a mode when the operation preserves source dynamics. A dynamics edit returns the review to pending and selects a new mode.
- Extension/bridge: inherit the boundary phase, select the new segment's mode, and converge on the successor's opening world state for a bridge.

## Final audit

- Every affected unit's review is resolved.
- Every visible-motion generation or redesign unit has one mode; a dynamics-preserving strict edit carries the source state without a mode.
- `coupled_world` has one readable cause per chain, present visible receivers, plausible material differences, and coherent direction, phase, disturbance, and residual continuity.
- `primary_action` contains the mechanics needed to read the action and ends before auxiliary world detail competes.
- `intentional_stillness` states stable fields and one authorized activity beat.
- Each driver occupies the smallest correct rendered scope.
- The complete readable scene was scanned before mode and receiver selection.
- Existing baseline motion and an authorized transient VFX event keep their distinct phases.
- The main action remains dominant and every added fact stays inside the evidence boundary.

Repair only the failed layer internally. A frozen result with `coupled_world` adds the smallest missing causal chain. Excessive response may change the mode to `primary_action` when auxiliary motion adds no visible value. Then follow `change-impact-and-delivery.md` and return the complete affected unit.
