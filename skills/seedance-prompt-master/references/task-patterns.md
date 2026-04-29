# Task Patterns

Use this reference when a request matches a specific video format. These patterns are not mandatory templates; they are compact checks for what each format usually needs.

## Six-Dimension Scan

For vague or mixed requests, silently scan six dimensions before drafting:

1. Input: image, video, audio, or text references and their roles.
2. Content: subject, environment, action, emotion carrier, and visible result.
3. Style: only user-provided or reference-established style, plus visible light, color, texture, or material behavior.
4. Camera: shot size, angle, one main movement, and camera rule such as one-take or fixed frame.
5. Structure: timing, shot order, transition, ending state, and segment handoff.
6. Edit: what changes, what stays unchanged, and which reference controls the edit.

Use only dimensions that reduce ambiguity. Do not force all six into a simple prompt.

## Product Or E-Commerce

Prioritize product identity, material, use case, and final readable product frame.

- Assign references: product appearance, logo, packaging, use scene, hand interaction, or edit rhythm.
- Keep the product size and silhouette stable before adding motion.
- Use macro detail only when material or function matters.
- End on a clean product state: assembled, held, used, opened, poured, placed, or hero-framed.
- Avoid unsupported brand claims, fake UI parameters, and decorative transformations that hide the product.

## UGC Or Smartphone Realism

Prioritize casual framing, natural imperfection, and believable sound.

- Use handheld, eye-level, selfie, or phone-recorded perspective only when it supports the request.
- Keep actions small and continuous: talking, showing a product, turning the camera, walking, reacting.
- Use natural room tone, street noise, hand movement, autofocus shifts, or exposure changes when useful.
- Avoid overproduced commercial lighting unless the user asks for polished advertising.

## Creative VFX Or Transformation

Prioritize transformation logic and visible stages.

- Define the source state, trigger, transformation path, and final state.
- Name material behavior: liquid, particles, smoke, glass, metal, cloth, fire, light, ink, dust, or mechanical parts.
- Keep one main transformation per shot unless the request is explicitly complex.
- For ambitious effects, split into setup, trigger, transformation, and aftermath.
- Preserve readable subject identity before and after the effect.

## Dialogue Drama Or Short Series

Prioritize emotional turn, performance carrier, and readable blocking.

- State who speaks, where they are, and what visible reaction follows each line.
- Keep dialogue short enough for the segment duration.
- Use gaze, pause, breath, hand tension, posture, or object handling as the emotion carrier.
- Avoid long backstory. Show the emotional beat inside the clip.
- If using subtitles, include them only when the user explicitly asks.

## Music Beat Sync

Prioritize beat ownership and action timing.

- Assign `@音频1` or `@视频1` as rhythm, beat, BGM, or edit-reference role.
- Map major visual changes to beats: entrance, cut, gesture, impact, reveal, transition, or final pose.
- Keep the number of beat events realistic for the duration.
- If the user does not ask for music, do not add BGM by default; use environmental and action sounds.

## One-Take

Prioritize route, focus transfer, and no hard cuts.

- Say it is one continuous shot only when continuity is central.
- Define starting frame, subject route, camera path, focus transfer, and ending frame.
- Use occlusion or foreground wipe only as a visible transition, not as a hidden hard cut.
- Avoid stacking unrelated locations unless the path between them is visible and physically plausible.

## Educational Visualization

Prioritize clarity, cause-effect, and readable states.

- Define the thing being explained and the visible before/after change.
- Use simplified symbolic visualization when microscopic, medical, mechanical, or abstract processes are involved.
- Keep labels, diagrams, subtitles, or narration out unless the user explicitly requests them.
- End on a clear comparison or stable explanatory frame.

## Multi-Video Fusion Or Bridge

Prioritize inheritance and transition logic.

- Assign each video a role: source clip, camera reference, action reference, style reference, end frame, or next-state target.
- Continue from the previous clip's ending posture, movement direction, light state, and camera momentum.
- Write the transition as visible action, material, camera movement, or matching shape/color, not as "connect to next".
- Preserve identity, lighting, and spatial direction unless the user asks for a deliberate change.
