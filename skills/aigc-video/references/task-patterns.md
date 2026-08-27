# Task Patterns

Use this reference when a request matches a specific video format. These patterns are not mandatory templates; they are compact checks for what each format usually needs.

## Contents

1. Six-dimension scan
2. Product, UGC, VFX, and dialogue
3. Visible text and audio rhythm
4. One-take, educational, and bridge patterns
5. Large apparition and effect confrontation
6. 预演

## Six-Dimension Scan

For vague or mixed requests, silently scan six dimensions before drafting:

1. Input: image, video, audio, or text assets; record each operational role first, then any borrowed dimensions for a `reference_input`.
2. Content: subject, environment, action, emotion carrier, visible change or continuity anchor, and the resolved world-dynamics mode for each affected unit.
3. Style: only user-provided or reference-established style, plus visible light, color, texture, or material behavior.
4. Camera: shot size, angle, one main movement, and camera rule such as one-take or fixed frame.
5. Structure: timing, shot order, transition, and only the segment handoff details that matter.
6. Edit: what changes, what stays unchanged, which asset is the `edit_target`, and whether a separate `reference_input` supplies a replacement dimension.

Use only dimensions that reduce ambiguity. Do not force all six into a simple prompt.

## Product Or E-Commerce

Prioritize product identity, material, use case, and final readable product frame.

- Assign each product reference input only the needed canonical borrowed dimension: product `appearance`; logo or packaging `graphic` / `text` / `layout`; use scene `environment`; hand interaction `action`; edit rhythm `timing`.
- Keep the product size and silhouette stable before adding motion.
- Use macro detail only when material or function matters.
- Use `primary_action` for clean product operation and silhouette. Select `coupled_world` only when supported hand contact, liquid, condensation, reflection, flexible packaging, turntable inertia, or surface response improves product readability.
- End on a clean product state: assembled, held, used, opened, poured, placed, or hero-framed.
- Avoid unsupported brand claims, fake UI parameters, and decorative transformations that hide the product.

## UGC Or Smartphone Realism

Prioritize casual framing, natural imperfection, and source-backed sound.

- Use handheld, eye-level, selfie, or phone-recorded perspective only when it supports the request.
- Keep actions small and continuous: talking, showing a product, turning the camera, walking, reacting.
- Use `primary_action` when casual body and camera behavior already reads clearly. Select `coupled_world` when clothing, carried objects, nearby flexible materials, autofocus, or exposure response materially improves the same recording beat.
- Preserve natural room tone or street noise only when the user, active source, or project supplies or requests it. Use hand movement, autofocus shifts, or exposure changes when they support the requested realism.
- Avoid overproduced commercial lighting unless the user asks for polished advertising.

## Creative VFX Or Transformation

Use this section for simple non-combat effects that do not require new specialist design, or to render an already `design_ready` CombatHandoff. When `aigc-vfx-combat` owns the effect design, preserve its form, route, result, presentation, and authorized consequences instead of designing a second version here.

Prioritize transformation logic and visible stages.

- Define the source state, trigger, transformation path, and final state.
- Name material behavior: liquid, particles, smoke, glass, metal, cloth, fire, light, ink, dust, or mechanical parts.
- When `coupled_world` is selected, connect the effect to only the necessary existing cloth, dust, water, foliage, reflection, shadow, pressure, heat, or light receiver and preserve the residual state after the effect beat.
- Keep one main transformation per shot unless the request is explicitly complex.
- Split an ambitious effect into setup, trigger, transformation, and aftermath when feasibility or observed-result evidence shows that locked timing and action load exceed one shot.
- Preserve readable subject identity before and after the effect.

## Large Apparition And Effect Confrontation

Use this pattern only when a shot depends on a large summoned, projected, or assembled figure and a readable attack-response chain. It is not a default fantasy template.

When the confrontation still needs initiative, contact, terminal behavior, or specialist VFX design, route through `aigc-vfx-combat` first. This section then compiles the resolved handoff into the final video grammar.

- Decide whether the figure must be fully mapped in space or mainly felt as larger than the frame. Use a complete view for geography or choreography; use partial framing, depth, occlusion, or frame overflow when impact is the priority.
- If the figure should assemble at full scale, define the final spatial envelope and let material resolve in separated regions. If literal growth is intended, preserve the scale change instead.
- Connect assembly to one immediate action unless the reveal itself is the intended endpoint. Keep the camera related to one active carrier rather than stacking movements.
- Give an attack only the route needed to read origin, direction, and target. Add environmental waypoints only when they visibly interact.
- Distinguish the response by its terminal behavior: stopped, redirected, dismantled, absorbed, reflected, or evaded. Do not substitute a visually adjacent mechanism merely because it is easier to describe.
- In a short segment, protect the causal chain and final performance beat before decorative effect stages. A fast insert may compress travel, but it should not obscure who initiated the attack or how it ended.

## Dialogue Drama Or Short Series

Prioritize emotional turn, performance carrier, and readable blocking.

- State who speaks, where they are, and what visible reaction follows each line.
- Preserve each exact spoken line and use the active platform adapter for its final punctuation. Keep the dialogue language consistent except for proper nouns.
- Keep dialogue short enough for the segment duration.
- Use gaze, pause, breath, hand tension, posture, or object handling as the emotion carrier.
- Select `coupled_world` when one visible hair, clothing, held-object, nearby-atmosphere, or contact-surface response reinforces the performance beat; otherwise keep `primary_action`.
- Avoid long backstory. Show the emotional beat inside the clip.
- Apply the active platform adapter's subtitle rule; keep the exact spoken line in audio and make the speaker's mouth visible when lip sync matters.

## Visible Text, Subtitle, Or Logo

Use only when the current user instruction or active project requests visible text or overrides the no-subtitle default.

- Write visible text as: exact content + appearance timing + frame position + appearance method + color/style when needed.
- Label requested subtitle text in ordinary Chinese and state that it follows the spoken rhythm.
- Prefer common characters; avoid rare characters and special symbols.
- For an exact logo, font, or layout, assign a dedicated image reference with the narrow `graphic`, `text`, or `layout` borrowed dimension instead of relying on description alone.
- Keep visible text separate from dialogue. Use ordinary quotation marks for dialogue; write discrete sound effects, music, and subtitles in natural Chinese only when active.

## Audio Beat And Rhythm Reference

Prioritize beat ownership and action timing.

- When `音频1` or `视频1` is a reference input, map rhythm, beat, or speech pace to `timing`, vocal timbre to `voice`, and a sound effect to `audio`. Use the final material label chosen by the active adapter. Keep an edit target's operational role separate and use direct edit grammar.
- Map major visual changes to beats: entrance, cut, gesture, impact, reveal, transition, or final pose.
- When that beat map materially controls the result, render the selected event-to-beat relation in the owning shot or operation sentence; do not leave the mapping only in analysis or expose an internal timing field. Bind the material once, then name only the relevant strong beat, rhythm change, speech turn, or sound cue where the visual event responds.
- Keep that beat map causal unless the current user or authoritative source supplies exact internal timing; do not convert rhythm analysis into invented shot-body second ranges.
- Keep the number of beat events realistic for the duration.
- When a music-bearing reference is assigned only to rhythm, do not leak its song, lyrics, or BGM into the clip. If the user or project explicitly authorizes its music as an audio dimension, preserve that audio assignment and the exact requested constraints.

## 预演

Use this pattern when the user wants a low-cost multi-shot generation to inspect composition, camera position or direction, framing, blocking, crop, screen direction, foreground/background placement, or occlusion rather than to judge the complete performance.

预演 uses the structure-review rule in `SKILL.md`. Review-required shots display the canonical table; explicitly direct-authorized shots compile the same setup internally. The previsualization verifies execution.

- Preserve any user-supplied shot count and order, reference roles, camera relationships, framing, visible roster, subject positions, foreground/background layers, and occlusion needed for the inspection. Do not assume five shots, cap a larger shot list, or merge shots merely to fit a default preview template.
- A final Seedance 2.5 previsualization prompt uses the active adapter's canonical timeline. If total duration is missing, ask for it — except when a coarse white-model video supplies the whole clip's timing and cuts; then inherit them per the duration rule in `SKILL.md` without asking. Once supplied or inherited, do not delete or combine locked shots to make the allocation easier.
- Select one representative settled or mid-action state for each shot. Establish that state at cut-in instead of spending the short shot entering, starting, stopping, turning, or completing a full dialogue/action cycle, unless that transition is itself the inspection target.
- Default each shot to `primary_action`: one readable state plus only the body or prop mechanics needed for that state. Use `intentional_stillness` when stability is the inspection target. When hard cuts show the same ongoing event, inherit its current phase rather than restarting it from a new angle.
- Downscope dialogue, lip sync, travel phases, environmental motion, secondary effects, and connective performance when they do not affect the requested inspection; preserve any field the user explicitly keeps.
- Treat `预演` as the conversation-level production intent. In the delivered platform prompt, describe only the current visible states and inspection-critical relationships; do not explain that the clip is a preview, test, debug pass, or correction of a previous result.
- If `预演` could mean composition inspection or motion/timing inspection and that choice would materially change the selected states, ask one grouped clarification question before drafting.

## One-Take

Prioritize route, focus transfer, and no hard cuts.

- Say it is one continuous shot only when continuity is central.
- Define starting frame, subject route, camera path, focus transfer, and ending frame.
- When source evidence or `coupled_world` establishes an ambient driver, carry its direction, phase, and accumulated contact disturbances along the route as framing changes.
- Use occlusion or foreground wipe only as a visible transition, not as a hidden hard cut.
- Avoid stacking unrelated locations unless the path between them is visible and physically plausible.

## Educational Visualization

Prioritize clarity, cause-effect, and readable states.

- Define the thing being explained and the visible before/after change.
- Use simplified symbolic visualization when microscopic, medical, mechanical, or abstract processes are involved.
- Keep labels, diagrams, subtitles, or narration out unless the current user instruction or active project requires them.
- End on a clear comparison or stable explanatory frame.

## Multi-Video Fusion Or Bridge

Prioritize inheritance and transition logic.

- Record each video's operational role first. A true bridge uses `bridge_predecessor` and `bridge_successor`; a non-bridge video that supplies `camera`, `action` / `motion`, `look`, or `timing` is a `reference_input` with that separate borrowed dimension. Never use a borrowed dimension as an operational-role name.
- For a true bridge/track-completion task, address the two sources directly in order: `视频1，[可见过渡]，接视频2`; use plain upload-order labels by default and do not describe either source as an ordinary reference video.
- Start from the previous clip's ending visible state and converge on the next clip's opening visible state; do not protect only the first boundary.
- Treat the generated transition as a new visible segment. Resolve structure review for its camera/framing, visible roster, spatial route, action, and endpoint before rendering the complete bridge command; inherited source boundaries remain locked.
- Write the transition as visible action, material, camera movement, or matching shape/color, not as "connect to next".
- Preserve identity, lighting, and spatial direction unless the user asks for a deliberate change.
- Record a start-frame image as `start_frame_source` and an end-frame image as `end_frame_target`. Assign only the authorized boundary lock scope—selected composition, pose, identity, light, material, or visible-roster attributes, or `full_frame` when the whole frame is explicitly authoritative. These are boundary roles, not borrowed dimensions; do not recast either image as `reference_input` unless the user explicitly assigns that additional role.
