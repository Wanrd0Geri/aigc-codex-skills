# Director Judgment Rules

Use these rules before drafting or optimizing a Seedance prompt. The goal is not to add decoration; it is to make the video legible, emotionally effective, and stable for generation.

## Core Judgment

- Identify the scene's primary goal: what the viewer must understand or feel by the end of the clip.
- Decide the viewing priority: which person, object, gesture, spatial change, or emotional turn should attract attention first.
- Choose the emotional carrier: performance, pause, breath, gaze, action result, spatial distance, light state, sound, or object movement.
- Keep every shot anchored to visible action and state change. Avoid writing abstract mood without a visible carrier.
- Prefer the shortest reasonable duration and fewest reasonable shots needed to express the scene, while preserving enough starting and ending state for connected segments.

## Incomplete Information

Default to moving forward with reasonable creative assumptions. Ask the user only when:

- Multiple reference images/videos have unclear roles and it is impossible to tell which is the character, scene, first frame, or end frame.
- Left/right, front/back, primary/secondary, or blocking relationships are unclear and directly affect the intended action.
- The user explicitly says not to fill gaps without confirmation.
- The request contains hard contradictions that cannot be safely resolved.

When an issue matters but is not blocking, state it briefly in 1-2 bullets and continue to draft.

## Shot Design

Each shot should have:

- A clear visual focus.
- One main action.
- Optional supporting micro-actions only when they strengthen the main action.
- A visible result or state change.
- Shot size, angle, camera movement, performance, and spatial relationship that serve the scene goal.

Do not stack multiple major camera moves in the same shot. Use a fixed camera when movement does not improve expression.

When the desired director idea creates high generation risk, such as many subjects, large motion, occlusion, complex blocking, or compound camera movement, simplify the shot organization first and preserve only the core expression that matters to the scene.

## One-Shot vs Multi-Shot

Use one continuous shot only when continuity, immersion, or uninterrupted performance is the strongest expression. In a one-shot prompt:

- Use only `镜头1`.
- Describe the action order with clear sequence words such as "先", "随后", "接着", "最后".
- Keep one main action chain.
- Define how the viewing focus transfers during continuous movement.
- Clarify spatial route, character path, foreground/background relationship, and key prop positions.

Use multiple shots when they improve clarity, rhythm, information delivery, or emotional contrast. Do not split shots just to sound cinematic.

## Continuity

Maintain continuity across shots:

- Character appearance, costume, props, and identifying details.
- Light direction, color temperature, and scene geography.
- Character facing direction, relative position, and movement path.
- Emotional progression and action handoff.

Avoid unmotivated jumps, spatial confusion, broken motion lines, or character identity drift.

For animation PVs and long-form animation segments, define the segment function before drafting: what it carries from the previous segment, what changes inside this segment, and what stable ending state the next segment can inherit. Leave a clear edit point when the clip is meant to connect into a longer sequence.

## Complex Scene Stability

For multi-person or high-risk scenes (large action, occlusion, similar-looking subjects, complex blocking), the canonical downgrade procedure lives in `single-segment-quality-control.md` under `Complexity Downgrade`. The director-side decisions to make before applying it:

- Decide which subject the scene is actually about. The other subjects exist as context, not as co-leads.
- Decide whether the difficulty is essential to the scene goal or decorative. If decorative, simplify the concept first; do not try to compensate with prompt engineering.
- Decide where to place the cut: between two stable states, never in the middle of an action swap.

Avoid a single shot that combines large action, complex position swaps, many similar-looking people, occlusion, and compound camera movement.
