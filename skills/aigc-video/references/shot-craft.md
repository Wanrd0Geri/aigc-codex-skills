# Shot Craft: Detail Levels, Camera, Performance, Dialogue

Load this reference when a shot needs performance direction, camera movement design, dialogue/lip-sync handling, visual-specificity compilation, or a decision about how much detail a shot paragraph deserves.

## Contents

1. Shot detail levels
2. Camera movement, framing, and optical result
3. World, screen, camera, and lighting coordinates
4. Conditional visual specificity
5. Performance, cross-shot action, and dialogue

## Shot Detail Levels

Length is decided per shot or action unit, not per whole video. These labels control only detail density after structure review resolves under `SKILL.md`. Never reveal the `simple` / `standard` / `complex` labels in the final prompt.

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

Reject camera contradictions: fixed cannot follow; following names its target and relation. Strict first-person POV sits at the viewpoint character's eyes and cannot show their head, face, or back without reflection. OTS may show partial shoulder/back; a rear two-person view may show both backs; observation is not POV. Surface locked relation/visibility conflicts instead of silently changing views.

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

Visibility roster, offscreen causality, effect-path, and terminal-frame checks consume the core `VisibleSetGate` in `references/video-contracts.md`; load `references/single-segment-quality-control.md` only for its extended complex-shot checks.

When the current visible set contains only environment, a product, an object, or camera motion, use only the relevant material and spatial mechanics. Do not import a human performance template such as center of gravity, gait, breathing, clothing, hair, gaze, or body-part choreography unless a human subject is actually visible and the field is needed.

## Optical Result

Choose optics from the visible purpose rather than decorating every shot with a focal-length number:

- portrait or reaction: protect facial readability and subject separation
- observation or dialogue: preserve readable distance and spatial relation
- environment or choreography: preserve depth, geography, and route
- detail or product: protect surface, edge, label, and focus transition

Describe the result the model must show: camera distance, near/far perspective, background compression or expansion, environment readability, foreground exaggeration, subject separation, and depth-of-field behavior. Preserve an exact focal length, aperture, or FOV only when the user or source locks it; pair it with its visible consequence. Do not invent precise millimeters or optical parameters merely to sound professional.

Use one optical character within a shot. A dolly may change camera distance while preserving that character; a deliberate zoom must state the visible perspective/framing result. A cut may change optics, but the new choice must still agree with the structure-resolved crop, visible envelope, and spatial continuity. Check for accidental lens drift when a modification changes camera position or framing.

## Lighting Direction And Exposure

Treat lighting as world-space geometry, not a mood adjective. When light materially affects readability or continuity, resolve this chain:

`physical source -> world direction -> subject lit and shadow sides -> camera relation -> visible result`

Record only the fields that change the image:

- primary source and location: sun, window, practical lamp, fire, screen, or authorized effect
- world direction and height
- whether the camera sees mainly the lit side, shadow side, rim, silhouette, or mixed planes
- subject exposure and face/eye readability
- background exposure and separation
- important highlight, reflection, translucent, wet, metal, or edge-light receivers
- the neighboring shot state that must remain continuous

Write one compact source-direction-result sentence for a simple stable setup. Add exposure separation, receivers, or cross-shot continuity only for side/back/low-key light, moving or occluded light, reflective/translucent materials, multiple shots in one space, or a lighting-related failure. Do not add a lighting paragraph when the source has no material effect on the requested result.

A camera move or cut changes which lit plane the camera sees; it does not move the sun, window, lamp, or fire. Recalculate the camera-to-light relation after every camera-side change. Keep static source, direction, exposure, and highlight ownership here. Let `world-dynamics.md` own moving-light phase, shadow/reflection motion, occlusion, flicker, receiver response, and residual continuity.

## Visual Specificity Pass

Run this hard pass only when the route in `SKILL.md` is active for the affected generation unit: the current user/project asks for enriched or higher-specificity visuals, supplies a visible descriptor bundle, or selects the cinematic 3D CG profile through ordinary language such as `院线级三维渲染CG动画电影`. The user never needs an internal profile token.

Do not activate from the word `电影感` alone during language-only cleanup, for a source edit that must preserve the existing look, or for an unrelated product, UGC, previsualization, graphic, or other style task unless the current request makes visual enrichment material. This pass improves semantic and shot specificity; it does not prove or guarantee higher base image quality.

After structure resolves and before platform rendering:

1. classify each supplied quality/style phrase as an exact lock, concrete visible fact, or empty booster
2. preserve exact locks; translate an empty booster only when the current brief supports concrete facts, otherwise remove it
3. assign each concrete fact to one smallest stable owner, then run `VisibleSetGate` against every crop
4. merge duplicates and resolve true material/light/optics conflicts through the authority order in `SKILL.md`

| Owner | Put here | Keep out |
| --- | --- | --- |
| `主体：` | identity-stable visible surfaces and construction: face/skin, hair, eyes, wardrobe, carried prop material | scene surfaces, camera optics, per-shot light result |
| `场景：` | environment surfaces, vegetation, stable light source/direction, atmosphere, persistent depth cues | portrait-only anatomy, lens/focus commands |
| `风格：` | medium, rendering language, palette, and shared material/texture behavior | local skin pores, one rock face, one-shot focus |
| owning `镜头N` | crop-visible optics, focal plane, depth of field, exposure separation, local light/material response, foreground depth device | invisible detail, repeated global style, another shot's camera state |

Keep only facts the requested crop can show. Iris moisture, skin scattering, hair strands, or lip texture may control a close shot but do not belong in a wide environment shot. A foreground ribbon, sleeve, weapon, branch, or flare is allowed only when that object/effect already exists or is explicitly authorized; this pass cannot invent it merely to create depth.

When the current user/project selects the cinematic 3D CG profile meaning, render `院线级三维渲染的CG动画电影截帧` exactly once in `风格：`. Concrete subject, scene, light, material, and optical facts carry execution. Do not add `正片`, `国漫`, `不是海报`, or `不是游戏宣传图`; the profile implies no regional, period, costume, or palette fact.

| Trigger | First repair | If still unresolved |
| --- | --- | --- |
| prompt contains several empty quality boosters | keep the selected exact profile once and replace only source-supported boosters with visible facts | remove the unsupported boosters rather than invent detail |
| the same material/light/optics fact appears globally and per shot | retain the smallest stable owner and remove duplicates | resolve a true source conflict through `IntentFactGate` |
| requested detail is outside the crop | remove it from that shot or use a supported existing visible receiver | reopen structure only when that detail is a locked result |
| cinematic profile appears in another style/task | remove the leaked profile and restore the active source/user style | ask only when two authoritative styles genuinely conflict |
| a result remains low quality but semantically accurate | preserve the prompt and classify the observed failure through `failure-recovery.md` | do not add a generic quality or negative tail without a discriminating test |

## Performance And Blocking Detail

For performing subjects, scale detail by complexity. Do not reduce performance to labels like `sad`, `happy`, `stares`, or `walks`.

Keep performance detail inside the resolved blocking envelope. Expressive posture, balance, and hand support may change after confirmation while body footprint, crop, occlusion, contact geometry, route, locked opening/action boundary, and endpoint remain stable. A change to any of those structure fields follows `change-impact-and-delivery.md` before enrichment.

- **Simple**: one visible action plus one cue, such as gaze target, hand contact, posture shift, or expression change.
- **Standard**: starting pose, active body part, contact point, movement direction, gaze target, and continuity anchor when useful.
- **Complex**: add action order, eye-line logic, foreground/background blocking, and inherited pose/gaze only when the shot depends on them.

Choose one primary visible performance carrier in this order: body/contact -> gaze/attention -> breath/pause -> expression change -> distance/object handling. Add at most one or two supporting changes when they make the beat clearer. When several blocking details are necessary, write them in causal order: body/contact -> gaze/attention -> breath/pause or expression transition -> movement endpoint -> continuity handoff.

For close, reaction, and dialogue shots, first compare the script beat, established relationship, current action phase, neighboring performance state, and crop. Preserve their meaning and intensity; then choose only the visible cue or cues needed to make the beat readable. When `collaboration-and-performance.md` supplies an `ActingTask`, attach those cues to the rendered playable task; never replace the task with gestures or keep it only in hidden analysis. A word such as `沉默`、`判断`、`警觉`、`没有惊慌` may summarize intent internally, but the rendered performance should make the intended difference observable when the crop and scene require it. Do not force every shot through a trigger/tactic/carrier/endpoint formula, and do not expand one intention into a facial, gaze, breath, and finger checklist.

For a material change, verify that the chosen carrier reads differently at the start and endpoint in the actual crop. Do not ask one unchanged cue to carry both states, such as `皱眉 -> 更深地皱眉`, when the intended turn is loss, relief, recognition, or withdrawal. Let the trigger cause one observable attention, head/shoulder, posture, distance, contact, or expression change, then keep the reached state through the cut instead of returning to the opening mask.

When the character is silent and no gasp, breath sound, or vocalization is source-backed, do not use opening the mouth as a generic emotion carrier. Prefer a change in gaze target, focus duration, head or shoulder set, lip-line tension, jaw tension, posture, distance, or object contact. Mouth opening belongs only to visible speech, an authorized vocal/breath event, or a physical action that requires it.

Apply the resolved world-dynamics mode. `coupled_world` may propagate body acceleration and contact into supported hair, clothing, accessories, carried props, surfaces, or media with material-appropriate lag and damping. `primary_action` keeps only the body and prop mechanics needed to read the acting beat. `intentional_stillness` preserves the stable fields and sole activity. Use `references/world-dynamics.md` for evidence and continuity.

When prop handling is the main action, define the visible active hand, contact, necessary support or counterbalance, transition, and endpoint. Mention the supporting hand only when it is inside the crop and leaving it undefined would make the pose or action materially ambiguous.

When non-contact is a material lock, make the visible separation part of the terminal geometry rather than describing only an approach toward the target. State where the active hand, body, or prop visibly stops relative to an existing reference, then hold or withdraw it; do not rely on repeated `不接触` wording to counteract an otherwise contact-completing action. If the requested near-gap is too small for the resolved crop to verify, surface the smallest framing, isolated-shot, or boundary-asset choice instead of pretending the text alone guarantees that distance.

When gaze is narratively material, name the visible target. If the target is off the camera axis, the head or eyes could plausibly remain forward, or an observed result missed the target, use the smallest sufficient orientation chain: torso relation -> head turn -> nose/chin direction -> eye direction -> target. Omit links already made unambiguous by the framing.

## Cross-Shot Action Phase

When a cut changes the view of one continuing event, carry the terminal action identity and phase into the next shot. Start the new shot from what is already happening and advance it; do not restage the onset merely because the camera angle changed.

The inherited visible state is more important than any continuity label: an already-open door stays open, an already-emitted beam remains connected, and a subject already passing another person does not approach and pass them again. In the final unified timeline, write those as current facts (`门已打开`、`光束已与目标相连`、`主体正在越过对方`) rather than `同上一镜`、`继续刚才` or `承接上一镜`; relative labels may remain internal only.

Carry world-facing and world position across a cut unless a visible turn or reposition occurs before that boundary. A new camera side may reveal a face or reverse screen order, but it does not authorize the subjects to rotate toward each other. Solve face visibility by placing the camera around the preserved blocking; if the requested face view cannot coexist with the locked facing or axis, reopen the affected structure instead of silently changing the performance geometry.

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
