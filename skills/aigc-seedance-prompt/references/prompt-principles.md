# Prompt Principles And Director Judgment

Use this reference when a Seedance request needs creative completion, shot design, style handling, continuity judgment, or translation from abstract intent into visible video instructions. The goal is not to add decoration; it is to make the video legible, emotionally effective, and stable for generation.

## Contents

1. Core judgment and incomplete information
2. Shot design and execution notes
3. Abstract-to-visible and natural language
4. Style and medium handling
5. Continuity and complex-scene stability

## Core Judgment

- Identify the segment goal: what the viewer must understand, feel, or see change during the segment.
- For ordinary pure text-to-video requests, keep the Vibe-first expressive core before execution detail: story moment, emotional direction, visual anchor, action/state, local tone, and video theme.
- Decide the viewing priority: the person, object, gesture, spatial change, or emotional turn that should attract attention first.
- Choose the emotional carrier: performance, pause, breath, gaze, contact point, posture, object movement, light state, sound, or spatial distance.
- Keep every shot anchored to visible action, spatial logic, and any continuity detail that matters. Abstract mood words must become visible or audible cues.
- Prefer the fewest shots and shortest reasonable duration that preserve the idea, starting state, and long-form handoff when the clip is part of a connected sequence.

## Incomplete Information

Default to reasonable creative assumptions and draft. Ask only when the missing answer changes the actual shot design or generation strategy:

- Reference roles are impossible to infer: character, scene, first frame, end frame, style, motion, sound, or edit rhythm.
- Blocking relationships such as left/right, near/far, front/back, primary/secondary, start state, or required handoff anchor affect the action.
- The user explicitly says not to fill gaps without confirmation.
- The request contains a hard contradiction that cannot be resolved by priority.

When a gap matters but does not block the prompt, state the assumption in 1-2 concise bullets and continue.

## Shot Design

Each shot should have:

- one clear visual focus
- one main action
- optional micro-actions only when they strengthen that action
- a visible action or state change when it helps the shot read
- shot size, angle, camera movement, performance, and spatial relationship that serve the segment goal

## Shot Line And Execution Notes

Write each shot as one practical execution paragraph in natural Chinese prose:

1. Shot lead-in: `镜头N：景别。` End with a period so the prose body starts cleanly. State total duration once in the overview; do not assign exact seconds to every generated shot by default.
2. Composition sentence: write angle, camera position, main camera movement, and visual focus as one complete Chinese sentence with a verb — not as a chain of bare parameter phrases.
3. Execution body: practical, flowing sentences covering what appears first, where subjects or objects start, how they move, how the camera relates to them, what frame-space they cross, what exits or lands, and what a later shot needs to inherit. Use connectives (`随后`, `紧接着`, `与此同时`, `此时`) only when they make beats actually link; use `最终` only when a concrete endpoint matters.

Use this style because Seedance benefits from clear shot order and shot size while the rest reads like executable shooting instructions a director would speak aloud — not a comma-chained parameter dump and not a rigid template. The official Seedance 2.0 guide warns that precise time ranges such as `0-3秒` are unstable; express generated timing through event order or `前段 / 中段 / 后段`, except for targeted source-video edits or an explicit timing-critical request.

Keep it efficient. Natural prose should connect the beats and add verbs, not inflate a simple shot with unnecessary atmosphere or repeated stability language.

Use Chinese-only shot and camera language in the final prompt by default. Do not include English shot abbreviations or English camera terms unless the user explicitly requests bilingual camera labels.

For action, VFX, object, flight, impact, transformation, or creature/character performance shots, include only the controls that reduce ambiguity:

- entry point, passing point, exit point, landing point, or ending pose
- whether the camera is fixed or following, and from which side/height/distance
- movement direction, speed change, pause, impact, rebound, or continuation
- environment reaction such as cloud movement, water displacement, debris fall, light bloom, shadow shift, or mist clearing
- posture, gaze, object position, movement direction, or light state only when the next shot must inherit it

Do not drop composition information, but do not place it on a separate composition-label line. Put the shot size in the structured lead-in (`镜头N：景别。`), then write the angle, camera position, camera movement, and visual focus as the first complete sentence of the prose body.

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

## Natural Prompt Language

Natural prompt language is a quality-control pass, not a request to make the wording longer. The final text should sound like a director describing a shot that can be filmed, animated, or edited. The cross-skill standard lives in `aigc-natural-language-prompt`; this reference applies that standard to Seedance prompts.

- Prefer complete visual sentences over parameter chains. A useful sentence usually contains subject, action, space, camera relationship, and only the continuity detail needed for this shot.
- Turn abstract adjectives into carriers the viewer can notice: posture, distance, contact, gaze, light direction, shadow coverage, material response, environment reaction, sound, or timing.
- Describe only current-shot visible/audible details or facts already established by previous shots. Do not invent a source such as wind, light, sound, or movement direction if the source is not visible or previously established.
- For cuts, state the new frame relationship when needed: what previous view it comes from, where the camera now is, and which objects or subjects remain visible.
- Keep only the specific detail that changes generation behavior. Remove generic boosters such as `cinematic`, `premium`, `masterpiece`, `high quality`, `ultra detailed`, `氛围感`, `高级感`, and `质感拉满` unless translated into visible choices.
- Avoid over-smoothing the language into ad copy. The prompt can be elegant, but it must remain operational: what enters frame, what moves, what the camera does, what changes, and what the next shot needs to keep.
- If two clauses only repeat the same mood, keep the stronger visible one and delete the weaker decorative one.

## Seedance Logic Scan

Before final output, apply this scan while preserving Seedance-specific duration, reference mapping, and shot-bridge rules:

- Each sentence should name a visible subject and a real verb. Replace noun piles such as `中景、冷色、孤独、电影感` with filmed relationships such as `中景固定拍摄，人物独自站在冷白路灯下，身后的街道空旷`.
- Keep cause and sequence readable. Use `先`, `随后`, `此时`, or `最终` only when they clarify action order; do not add connectors as decoration.
- Use adjectives only after the concrete carrier is clear. `压抑` should become tight spacing, low ceiling, held breath, blocked doorway, heavy shadow, or another visible/audible cue.
- Do not invent an off-screen source or cause. If the source is not visible in the current shot or clearly established by a previous shot, write only the visible result, such as `额前碎发被轻轻吹开`.
- When a shot cuts from a previous view, state the current frame relationship only when it prevents confusion, such as `从上一镜头的远景切到桌前右侧中近景`.
- Remove prompt-flavored filler before output: `高质量`, `大师级`, `极致细节`, `电影质感`, `氛围拉满`, `高级感`. If the idea matters, translate it into camera, light, blocking, material, sound, or movement.
- Remove AI-flavored structure before output: "不只是...更是...", rule-of-three padding, generic conclusions, decorative `最终`, and any sentence that explains creative intent instead of controlling the visible shot.
- Do not write a closing state merely to make the prompt feel complete. Add a continuity anchor only when it prevents confusion in the next shot or connected segment.
- Check that the shot can be acted or animated. If a phrase cannot be seen, heard, performed, lit, framed, or timed, rewrite it before placing it in the final code block.

## Style Handling

- If the user specifies a style, follow it.
- If references imply a style, inherit that style without renaming or changing it.
- If style is unspecified, write neutral execution quality only: clear subject, coherent light, readable action, stable identity, and clean frame.
- Do not invent labels such as `三渲二`, `UE5风格`, `照片级写实`, `cel shading`, or `cinematic` unless the user or references establish them.
- Separate style, material, color tone, and lighting. When inheriting style, do not accidentally change light direction, shadow relationship, or color mood unless requested.

## Medium Vocabulary Branch

Identify the intended medium before choosing prompt vocabulary. Do not let live-action cinematography language override a non-photoreal target.

- **Live-action photoreal**: use grounded lighting, exposure, lens distance, atmosphere, and material response terms when they help.
- **2D animation / illustration**: prioritize clean silhouette, line/design consistency, readable color blocks, stable character shape, and rhythmized pose changes. Avoid film grain, IRE values, film-stock names, and photoreal skin/material language unless the user asks for them.
- **Stylized 3D / game cinematic**: prioritize stable model identity, readable staging, clean material hierarchy, soft but controlled lighting, natural ear/tail/cloth/hair motion, and clear action timing. Use engine or game-cutscene style terms only as global constraints; shot bodies still need concrete actions and spatial relationships.
- **Product / object render**: prioritize shape accuracy, logo/mark preservation, material response, contact shadows, reflection control, and camera-object relationship.

If the user's references imply a medium, inherit that medium without renaming it. If style is unspecified, keep the prompt neutral and execution-focused.

## Continuity

For connected shots or long-form animation segments, preserve:

- character appearance, costume, props, and identifying details
- light direction, color temperature, and scene geography
- facing direction, relative position, movement path, and action handoff
- emotional progression and only the stable handoff details needed for connected segments

Define the segment function before drafting: what it carries from the previous segment, what changes inside this segment, and what the next segment can inherit. Leave a clear edit point when the clip is meant to connect into a longer sequence.

## Complex Scene Stability

When the idea includes many subjects, large action, occlusion, similar-looking characters, complex blocking, or compound camera movement, decide whether the difficulty is essential or decorative. If decorative, simplify the concept before writing the prompt.

If the difficulty is essential:

- choose the lead subject and make other subjects context
- place cuts between stable states, not mid-swap
- use fixed camera or one simple movement when possible
- split large position changes into more than one shot

Avoid a single shot that combines large action, complex position swaps, many similar-looking people, occlusion, and compound camera movement.
