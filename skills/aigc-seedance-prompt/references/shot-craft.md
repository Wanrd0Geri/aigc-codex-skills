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
- A one-shot segment that still needs a total-duration budget, audio policy, and stable identity.

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
- Put spoken dialogue in the official braces syntax: `角色说道{台词}`. Use `<音效>` for a discrete sound effect. Use `（音乐）` and `【字幕】` only when the user explicitly overrides this workflow's no-music/no-subtitle policy.
- The opening-overview phrase `无配乐，无字幕。` does not mean silence: keep diegetic speech and necessary action/environment sound when the shot needs them, and do not invent voiceover or dubbing unless the user asks.
- Include subtitles only when the user explicitly asks; otherwise keep them out of the prompt.

If dialogue is requested but the mouth is not visible or the shot is too short for lip sync, adjust framing, reduce dialogue, or state the risk before drafting.
