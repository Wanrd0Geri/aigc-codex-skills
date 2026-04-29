# Efficient Video Prompting

Use this reference to turn vague creative intent into Seedance-readable video prompts. The final prompt should describe what a camera can see or hear, not production shorthand or abstract taste.

## Core Formula

Build the prompt in this order, then merge the information into natural shot descriptions:

1. Creative goal: what the segment must communicate or change.
2. Subject identity: stable clothing, silhouette, prop, face, or position anchors.
3. Reference roles: what each image or video controls.
4. Scene space: location, foreground/background, left/right, near/far, and key object placement.
5. Action chain: one main action per shot and its visible result.
6. Camera language: shot size, angle, and one main camera movement.
7. Emotion carrier: gaze, pause, breath, hand movement, posture, spacing, light, or sound.
8. Light and texture: visible light direction, color temperature, material response, and atmosphere.
9. Sound policy: no music; keep only environment sound, action sound, and necessary diegetic sound.
10. Continuity and stability: identity, props, light, spatial direction, and action handoff.

## Long-Form Segment Workflow

For animation PVs and long-form animation, treat each generated video as a segment in a larger edit:

- Segment function: define whether the clip establishes space, reveals a character, continues an action, transitions locations, escalates emotion, or lands a result.
- Starting state: inherit character position, facing direction, held objects, light state, and emotion from the previous segment when known.
- Segment action: describe the main visible action and the change it creates.
- Ending state: leave a stable posture, gaze direction, object position, or camera endpoint for the next segment.
- Edit handoff: when useful, hold the final state briefly or end on a readable movement direction so the next clip can connect cleanly.

Do not apply short-video hook logic by default. Favor narrative clarity, stable continuity, and clean edit points over constant surprise or rapid escalation.

## Style Handling

Style is not fixed by this skill.

- If the user specifies a style, follow it.
- If reference images or videos imply a style, inherit that style without renaming or changing it.
- If style is unspecified, write neutral execution quality only: clear subject, coherent light, readable action, stable identity, and clean frame.
- Do not invent style labels such as 2D animation, cel shading, photorealism, Unreal Engine, or three-render-two unless the user or references clearly establish them.
- Separate style, material, color tone, and lighting. When inheriting or changing style, keep the original light direction, shadow relationship, and color mood unless the user explicitly asks to change them.
- For stylized 3D, CGI, or other high-material-detail looks, describe material response and lighting behavior separately, so style transfer does not accidentally over-saturate the frame or flatten the original atmosphere.

## Abstract-To-Visible Translation

Use abstract terms only for internal planning. In the final prompt, translate them into visible or audible details:

| Internal term | Final-prompt translation |
| --- | --- |
| Cinematic | shot size, camera angle, lens distance, light direction, depth cues, camera speed |
| Premium | restrained composition, clean materials, controlled color, precise motion, readable subject |
| Impactful | scale contrast, low angle, shadow coverage, air pressure, object displacement |
| Tense | held breath, tightened fingers, delayed response, gaze direction, quiet environmental sound |
| Mysterious | partial reveal, backlight, occlusion, distant source, slow movement |
| Realistic | natural proportion, plausible physics, grounded light, material detail, believable movement |
| Animated | clear silhouette, stable character design, readable color blocks, rhythmized motion |

If a word cannot be filmed or heard, translate it before placing it in the final prompt.

## Efficient Writing Rules

- Write visible subject, action, space, camera, light, sound, and result.
- Keep one main action and one main camera movement per shot.
- Prefer concrete verbs and visible state changes over adjectives.
- Use reference labels with semantic roles, such as `@图1（Image 1，UFO外形参考）`.
- Keep sound sparse and diegetic: wind, footsteps, metal vibration, breath, rain, distant machinery, or similar scene sounds.
- Use positive stability language: "主体识别稳定", "动作承接清楚", "空间关系清晰", "服装与道具保持连续".
- Keep final prompts free of internal explanation, rule names, and vague production shorthand.
