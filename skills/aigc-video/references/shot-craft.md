# Shot Craft: Detail Levels, Camera, Performance, Dialogue

Load this reference when a shot needs performance direction, camera movement design, dialogue/lip-sync handling, or when deciding how much detail a shot paragraph deserves.

## Contents

1. Shot detail levels
2. Camera movement and framing
3. World, screen, and camera coordinates
4. Performance, cross-shot action, and dialogue

## Shot Detail Levels

Length is decided per shot or action unit, not per whole video. Never reveal the `simple` / `standard` / `complex` labels in the final prompt.

### Simple Shot

Use one short Chinese sentence when the subject, action, and continuity are obvious:

- One clear subject or one clear edit.
- One main action with no layered blocking.
- Little risk of confusing asset operational roles, borrowed-dimension assignments, spatial relationships, or emotional intent.
- Atmosphere, light, sound, and camera do not change the user's meaning.

Write only the needed subject, action, and essential continuity. Do not add extra camera, lighting, mood, material, sound, or stability language just to make the shot look professional.

### Standard Shot

Use one to two compact Chinese sentences when the shot needs moderate control:

- A clear subject plus atmosphere, space, expression, prop, or one active reference-input borrowed dimension.
- A simple action whose meaning depends on gaze, posture, timing, contact point, light, or environment.
- A one-shot segment that still needs a total-duration budget, stable identity, and any active dialogue or audio constraint.

For any performing subject, write the key body part, gaze target, contact point, or expression change that makes the performance readable. Mention only details that reduce ambiguity, improve generation reliability, or make the acting beat visible.

### Complex Shot

Expand only when detail prevents likely misunderstanding:

- Multiple subjects, layered actions, or action handoffs.
- Foreground/midground/background relationships, occlusion, entrances/exits, or position changes.
- Camera movement, reveal order, transition logic, or continuity across shots matters.
- Reference assets have overlapping assignments or could be mapped incorrectly.
- The user is choosing between a conservative stable result and a more ambitious visual effect.

Write clear subject, space, action order, camera behavior, and the continuity anchor that prevents likely misunderstanding. Keep the detail purposeful; do not pad with generic quality terms.

## Camera Movement Detail

Camera movement detail scales by shot complexity:

- **Simple shots**: omit camera movement unless it is central to the request. Use `固定机位` when stillness improves stability, symmetry, or quiet atmosphere.
- **Standard shots**: write one main camera movement and its purpose, such as `缓慢推近` for expression or object detail, `横向移动` for spatial reveal, or `跟随拍摄` for a clear subject path.
- **Complex shots**: specify the starting frame, subject relationship, movement path, reveal order, and next-shot anchor only when these details are needed to prevent confusion.

Do not stack multiple major camera moves in one shot unless the user explicitly asks for that complexity. Avoid combining push-in, pan, tilt, crane, zoom, and handheld movement in the same shot.

Avoid contradictions: if the camera is `固定机位`, the subject may cross frame, but the camera should not also follow. If the camera follows a subject, object, or energy trail, write `跟随拍摄` and specify the following relationship.

Apply the shot sentence order from the active platform adapter; this reference does not redefine it. Use the camera guidance below only to express a camera choice that survived that order.

## Framing And Visible Envelope

Before choosing a shot size, treat every body part, prop, subject, and landmark required in the same frame as one minimum visible envelope. The framing must contain that envelope. If it cannot, remove only mutable visibility detail, use a visible reframing when camera movement is allowed, or surface the hard-lock conflict.

- Establish one viewer priority and intended crop before adding contextual visibility. Render it as `画面重心` only when several visible elements would otherwise compete.
- For a tight shot, use observable boundaries such as what the upper and lower frame edges cut, which body parts dominate, and which environment elements remain partial or out of focus.
- Keep world-continuity details internal when they do not need to appear in this shot. Do not ask a chest-up frame to also show feet, a floor contact point, and a complete doorway merely to prove where the subject stands.
- If two locked requirements need incompatible visible envelopes at the same boundary, state the conflict and recommend which framing purpose to protect. Do not repeat `紧近景` or add a negative list as a substitute for resolving it. Do not invent a reframing move when the camera or framing is locked.

## World, Screen, And Camera Coordinates

Write each shot as an objective account of what the camera can observe from its visible start through its terminal frame. Keep world position and screen position distinct:

- With a fixed camera, a moving subject normally changes screen position; state the visible route when it matters.
- With a tracking camera, the subject may remain at a stable screen position while changing world position; state the camera-subject relationship.
- With an orbit or side change, preserve the established side of the action axis unless a visible, deliberate axis crossing is required. Translate the same world action into the correct new screen direction after a crossing.

Visibility roster, offscreen causality, effect-path, and terminal-frame checks belong to `references/single-segment-quality-control.md`; do not restate them here.

## Performance And Blocking Detail

For performing subjects, scale detail by complexity. Do not reduce performance to labels like `sad`, `happy`, `stares`, or `walks`.

- **Simple**: one visible action plus one cue, such as gaze target, hand contact, posture shift, or expression change.
- **Standard**: starting pose, active body part, contact point, movement direction, gaze target, and continuity anchor when useful.
- **Complex**: add action order, eye-line logic, foreground/background blocking, and inherited pose/gaze only when the shot depends on them.

Choose one primary visible performance carrier in this order: body/contact -> gaze/attention -> breath/pause -> expression change -> distance/object handling -> environmental or sound response. Add at most one or two supporting changes when they make the beat clearer. When several blocking details are necessary, write them in causal order: body/contact -> gaze/attention -> breath/pause or expression transition -> movement endpoint -> continuity handoff.

When prop handling is the main action, define the visible active hand, contact, necessary support or counterbalance, transition, and endpoint. Mention the supporting hand only when it is inside the crop and leaving it undefined would make the pose or action materially ambiguous.

When gaze is narratively material, name the visible target. If the target is off the camera axis, the head or eyes could plausibly remain forward, or an observed result missed the target, use the smallest sufficient orientation chain: torso relation -> head turn -> nose/chin direction -> eye direction -> target. Omit links already made unambiguous by the framing.

## Cross-Shot Action Phase

When a cut changes the view of one continuing event, carry the terminal action identity and phase into the next shot. Start the new shot from what is already happening and advance it; do not restage the onset merely because the camera angle changed.

Use wording such as `承接上一镜同一次发射动作` only when it resolves a real ambiguity. The inherited visible state is more important than the phrase itself: an already-open door stays open, an already-emitted beam remains connected, and a subject already passing another person does not approach and pass them again.

## Dialogue And Lip Sync

When the user requests dialogue, speech, lip sync, or visible mouth movement:

- State who speaks, the exact spoken line, and whether the mouth is visible in the frame.
- For visible multi-character dialogue, establish the attention handoff: speaker -> addressed listener -> only the materially affected visible reaction. Use at most one necessary listener response per main dialogue beat unless the source locks more. Do not make every visible character react at once or stare toward the same direction throughout unless the source explicitly requires it.
- Fit dialogue to the actual speaking time, natural delivery speed, pauses, reactions, and stable visible-mouth time. A short clip may contain several brief lines when the timeline genuinely gives them room; a long sentence may already overload one short shot.
- Give the speaking subject enough stable face time; avoid hiding the mouth behind fast camera motion, back view, heavy occlusion, or a cutaway.
- For Seedance-family output, use the active Seedance adapter for dialogue and sound placement. For platform-neutral output, preserve the exact line and ownership in ordinary natural language.
- Apply audio and visible-text rendering rules from the active platform adapter; this craft reference does not redefine them.
- Write subtitle content only when the current user, active project/source, or an explicitly authorized text reference requires it. An adapter's trailing `不添加字幕` sentence is a negative default, not subtitle content.

If dialogue is requested but the mouth is not visible or the shot is too short for lip sync, state the conflict and recommend a framing or duration change. Do not reduce exact dialogue or alter locked framing without the user's approval.
