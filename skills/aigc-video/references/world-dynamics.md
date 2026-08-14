# Dynamic World Modeling

Use this reference for every new/reference generation and whenever optimization changes visible motion or physical interaction. Treat the image as one already-running world, not a foreground subject animated over a static background.

## Core contract

Resolve `world_activity` on every task:

- `active`: build and render a compact living-world chain; default for new/reference generation.
- `inherited`: preserve the source driver's direction, intensity, disturbance, and residual phase; default for edit, extension, and bridge.
- `intentionally_still`: keep secondary motion absent because the user locks stillness or the inspection format would be harmed by it. Record this as a completed decision, not a skipped check.

Build subject-to-world and world-to-subject coupling when visible evidence supports it. Let the world act before the subject enters, respond while the subject moves, and retain a decaying state after the main action ends. Camera movement never counts as world activity.

## Evidence boundary

Infer low-risk physical behavior from existing visible bodies and materials:

- breathing, weight transfer, momentum, settling, and body follow-through
- hair, cloth, loose accessories, carried objects, and flexible parts lagging or rebounding with body motion
- existing foliage, curtains, hanging objects, dust, smoke, fog, water, rain, steam, reflections, shadows, crowds, traffic, or machinery continuing plausible motion
- contact response where a visible subject touches ground, water, vegetation, a door, furniture, fabric, or another existing surface

Do not infer a new weather event, water source, plant, animal, crowd, vehicle, prop, effect, damage event, or story beat. A visible tree may support restrained leaf and branch response; it does not authorize falling leaves. A wet surface may support changing reflections under footsteps; it does not authorize new rain. When the source is unreadable, label-only, graphic UI, or silent about a material fact that would change the scene, stay neutral.

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

## Structure-table review cell

Whenever `SKILL.md` requires a `镜头结构确认` or `镜头结构回显` table, add the exact column `环境动态确认` and summarize the per-shot `world_dynamics_review` there:

- For `planned`, write the low-risk chain from existing visible materials directly.
- For `source_backed` or `inherited`, directly state the source and the driver, direction, phase, disturbance, or residual state being continued.
- For `intentionally_still`, directly name what stays still and the only allowed main motion when useful.
- For `unresolved`, directly name what cannot be read reliably and end with `待确认`.

Keep the exact `环境动态确认` column. Write only the moving world elements and causal relationship as one natural Chinese sentence or at most three semicolon-separated groups: persistent environment; interaction or VFX influence; residual or cross-shot handoff. Omit inactive groups, group related receivers, and never expose the internal review-state label or add a status prefix. Keep it as an approval summary rather than duplicating the complete shot paragraph. Source-backed dynamics must be compared with the corresponding frame or interval; ordinary low-risk planning does not block same-turn delivery. If the user explicitly skips the structure table, resolve the same fields internally without rendering the column.

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

Patch only the failed layer. If the body action is correct but the world is frozen, add the smallest causal receiver chain; if motion is excessive, reduce receivers and amplitude rather than freezing the whole scene.
