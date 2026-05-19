# Prompt Principles And Director Judgment

Use this reference when a Seedance request needs creative completion, shot design, style handling, continuity judgment, or translation from abstract intent into visible video instructions. The goal is not to add decoration; it is to make the video legible, emotionally effective, and stable for generation.

## Core Judgment

- Identify the segment goal: what the viewer must understand, feel, or see change by the end.
- Decide the viewing priority: the person, object, gesture, spatial change, or emotional turn that should attract attention first.
- Choose the emotional carrier: performance, pause, breath, gaze, contact point, posture, object movement, light state, sound, or spatial distance.
- Keep every shot anchored to visible action and state change. Abstract mood words must become visible or audible cues.
- Prefer the fewest shots and shortest reasonable duration that preserve the idea, starting state, ending state, and long-form handoff.

## Incomplete Information

Default to reasonable creative assumptions and draft. Ask only when the missing answer changes the actual shot design or generation strategy:

- Reference roles are impossible to infer: character, scene, first frame, end frame, style, motion, sound, or edit rhythm.
- Blocking relationships such as left/right, near/far, front/back, primary/secondary, or start/end state affect the action.
- The user explicitly says not to fill gaps without confirmation.
- The request contains a hard contradiction that cannot be resolved by priority.

When a gap matters but does not block the prompt, state the assumption in 1-2 concise bullets and continue.

## Shot Design

Each shot should have:

- one clear visual focus
- one main action
- optional micro-actions only when they strengthen that action
- a visible result or state change
- shot size, angle, camera movement, performance, and spatial relationship that serve the segment goal

## Shot Line And Execution Notes

Write each shot as one practical execution paragraph in natural Chinese prose:

1. Shot lead-in: `镜头N：x秒，景别。` End with a period so the prose body starts cleanly.
2. Composition sentence: write angle, camera position, main camera movement, and visual focus as one complete Chinese sentence with a verb — not as a chain of bare parameter phrases.
3. Execution body: practical, flowing sentences covering what appears first, where subjects or objects start, how they move, how the camera relates to them, what frame-space they cross, what exits or lands, and what visible result remains. Use connectives (`随后`, `紧接着`, `与此同时`, `此时`, `最终`) so beats actually link.

Use this style because Seedance responds better when the shot number, duration, and shot size are explicit and the rest reads like executable shooting instructions a director would speak aloud — not a comma-chained parameter dump and not a rigid template.

Keep it efficient. Natural prose should connect the beats and add verbs, not inflate a simple shot with unnecessary atmosphere or repeated stability language.

Use Chinese-only shot and camera language in the final prompt by default. Do not include English shot abbreviations or English camera terms unless the user explicitly requests bilingual camera labels.

For action, VFX, object, flight, impact, transformation, or creature/character performance shots, include only the controls that reduce ambiguity:

- entry point, passing point, exit point, landing point, or ending pose
- whether the camera is fixed or following, and from which side/height/distance
- movement direction, speed change, pause, impact, rebound, or continuation
- environment reaction such as cloud movement, water displacement, debris fall, light bloom, shadow shift, or mist clearing
- final state that the next shot can inherit

Do not drop composition information, but do not place it on a separate composition-label line. Put the shot size in the structured lead-in (`镜头N：x秒，景别。`), then write the angle, camera position, camera movement, and visual focus as the first complete sentence of the prose body.

Avoid camera contradictions: `固定机位` means the camera holds while the subject moves through frame; `跟随拍摄` means the camera follows a subject or path and should specify whether it follows from above, behind, side, front, or near a specific object/body part.

Use one continuous shot only when continuity, immersion, or uninterrupted performance is the strongest expression. For one-shot prompts, use only `镜头1`, describe the internal action order clearly, and define how the viewing focus transfers.

Use multiple shots when they improve clarity, rhythm, information delivery, or emotional contrast. Do not split shots just to sound cinematic.

## Abstract-To-Visible Translation

Use abstract terms only for planning. In the final prompt, translate them:

| Internal term | Final-prompt translation |
| --- | --- |
| Cinematic | shot size, angle, lens distance, light direction, depth cues, camera speed |
| Premium | restrained composition, clean materials, controlled color, precise motion, readable subject |
| Impactful | scale contrast, low angle, shadow coverage, air pressure, object displacement |
| Tense | held breath, tightened fingers, delayed response, gaze direction, quiet environmental sound |
| Mysterious | partial reveal, backlight, occlusion, distant source, slow movement |
| Realistic | natural proportion, plausible physics, grounded light, material response, believable movement |
| Animated | clear silhouette, stable character design, readable color blocks, rhythmized motion |

If a word cannot be filmed or heard, translate it before placing it in the final prompt.

## Style Handling

- If the user specifies a style, follow it.
- If references imply a style, inherit that style without renaming or changing it.
- If style is unspecified, write neutral execution quality only: clear subject, coherent light, readable action, stable identity, and clean frame.
- Do not invent labels such as `三渲二`, `UE5风格`, `照片级写实`, `cel shading`, or `cinematic` unless the user or references establish them.
- Separate style, material, color tone, and lighting. When inheriting style, do not accidentally change light direction, shadow relationship, or color mood unless requested.

## Continuity

For connected shots or long-form animation segments, preserve:

- character appearance, costume, props, and identifying details
- light direction, color temperature, and scene geography
- facing direction, relative position, movement path, and action handoff
- emotional progression and stable ending state

Define the segment function before drafting: what it carries from the previous segment, what changes inside this segment, and what the next segment can inherit. Leave a clear edit point when the clip is meant to connect into a longer sequence.

## Complex Scene Stability

When the idea includes many subjects, large action, occlusion, similar-looking characters, complex blocking, or compound camera movement, decide whether the difficulty is essential or decorative. If decorative, simplify the concept before writing the prompt.

If the difficulty is essential:

- choose the lead subject and make other subjects context
- place cuts between stable states, not mid-swap
- use fixed camera or one simple movement when possible
- split large position changes into more than one shot

Avoid a single shot that combines large action, complex position swaps, many similar-looking people, occlusion, and compound camera movement.
