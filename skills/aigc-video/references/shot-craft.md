# Shot Craft: Detail Levels, Camera, Performance, Dialogue

Load this reference when a shot needs performance direction, camera movement design, dialogue/lip-sync handling, or when deciding how much detail a shot paragraph deserves.

## Shot Detail Levels

Length is decided per shot or action unit, not per whole video. Never reveal the `simple` / `standard` / `complex` labels in the final prompt.

### Simple Shot

Use one short Chinese sentence when the subject, action, and continuity are obvious:

- One clear subject or one clear edit.
- One main action with no layered blocking.
- Little risk of confusing reference roles, spatial relationships, or emotional intent.
- Atmosphere, light, sound, and camera do not change the user's meaning.

Write only the needed subject, action, and essential continuity. Do not add extra camera, lighting, mood, material, sound, or stability language just to make the shot look professional.

### Standard Shot

Use one to two compact Chinese sentences when the shot needs moderate control:

- A clear subject plus atmosphere, space, expression, prop, or reference-image role.
- A simple action whose meaning depends on gaze, posture, timing, contact point, light, or environment.
- A one-shot segment that still needs a total-duration budget, stable identity, and any active dialogue or audio constraint.

For any performing subject, write the key body part, gaze target, contact point, or expression change that makes the performance readable. Mention only details that reduce ambiguity, improve generation reliability, or make the acting beat visible.

### Complex Shot

Expand only when detail prevents likely misunderstanding:

- Multiple subjects, layered actions, or action handoffs.
- Foreground/midground/background relationships, occlusion, entrances/exits, or position changes.
- Camera movement, reveal order, transition logic, or continuity across shots matters.
- Reference assets have overlapping roles or could be mapped incorrectly.
- The user is choosing between a conservative stable result and a more ambitious visual effect.

Write clear subject, space, action order, camera behavior, and the continuity anchor that prevents likely misunderstanding. Keep the detail purposeful; do not pad with generic quality terms.

## Camera Movement Detail

Camera movement detail scales by shot complexity:

- **Simple shots**: omit camera movement unless it is central to the request. Use `固定机位` when stillness improves stability, symmetry, or quiet atmosphere.
- **Standard shots**: write one main camera movement and its purpose, such as `缓慢推近` for expression or object detail, `横向移动` for spatial reveal, or `跟随拍摄` for a clear subject path.
- **Complex shots**: specify the starting frame, subject relationship, movement path, reveal order, and next-shot anchor only when these details are needed to prevent confusion.

Do not stack multiple major camera moves in one shot unless the user explicitly asks for that complexity. Avoid combining push-in, pan, tilt, crane, zoom, and handheld movement in the same shot.

Avoid contradictions: if the camera is `固定机位`, the subject may cross frame, but the camera should not also follow. If the camera follows a subject, object, or energy trail, write `跟随拍摄` and specify the following relationship.

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

Priority order: body/contact -> gaze/attention -> expression transition -> movement endpoint -> continuity handoff.

## Dialogue And Lip Sync

When the user requests dialogue, speech, lip sync, or visible mouth movement:

- State who speaks, the exact spoken line, and whether the mouth is visible in the frame.
- Keep dialogue short enough for the duration. For 15 seconds or less, prefer one or two short lines.
- Give the speaking subject enough stable face time; avoid hiding the mouth behind fast camera motion, back view, heavy occlusion, or a cutaway.
- For Seedance-family output, put spoken dialogue in braces: `角色说道{台词}`; use `<音效>`、`（音乐）` and `【字幕】` only when active. For platform-neutral output, preserve the exact line and ownership in ordinary natural language without platform markers.
- The personal no-music/no-subtitle default prevents additions but does not require an opening policy phrase. Keep user/source/project-supplied dialogue and sound; otherwise do not invent ambience, action sound, voiceover, or dubbing. If the user asks for no sound description, omit all optional audio wording.
- Include subtitles only when the current user instruction or active project requires them; otherwise keep them out of the prompt.

If dialogue is requested but the mouth is not visible or the shot is too short for lip sync, state the conflict and recommend a framing or duration change. Do not reduce exact dialogue or alter locked framing without the user's approval.
