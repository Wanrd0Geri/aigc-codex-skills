# Single-Segment Quality Control

Use this reference for complex subjects, blocking, occlusion, overloaded action, offscreen causality, terminal composition, or continuity-sensitive Seedance-family prompts.

## Quality order

Check only what the shot needs, in this order:

1. stable identity and intended visible roster
2. one readable main action per shot
3. material spatial relationships
4. one main camera strategy
5. one supported performance carrier when active
6. required terminal image
7. only the terminal subset a later shot must inherit

Fix a missing high-priority field before adding style, atmosphere, or effect detail.

## Complexity and duration

Simplify only mutable execution fields:

- prefer one camera movement; fixed camera is useful only when it serves the shot
- define subject positions or routes when multiple people, occlusion, or crossings would otherwise be ambiguous
- reduce active subjects only when subject count is not locked
- make one action readable before another begins when overlap would confuse the result

Use these as internal feasibility estimates before allocating the required timeline:

- one action beat: about 2-3 seconds
- one camera move plus one action: about 3-4 seconds
- one expression/attention change: about 1-2 seconds
- one contact and reaction: about 2-3 seconds
- one multi-character handoff: about 3-5 seconds

A roughly one-second fast insert can carry one instantaneous beat, such as an eye activation, hand contact, launch, impact, or reaction. A fast-cut sequence may distribute one causal chain across several inserts, but each insert should not contain its own setup, development, and result. Count described action phases, not just numbered shots.

If the duration cannot hold locked beats, simplify mutable camera and description first, then recommend extending or splitting. Never delete, merge, or reorder locked beats. For Seedance 2.5 new/reference generation with a known total duration, allocate exact continuous ranges; if total duration is unknown, ask rather than inventing it.

## Persistent scene topology

Use this only when multiple shots share a location and depend on persistent blocking, separation, occlusion, or a repeated camera setup. Establish the source-backed regions, separators, relative distance, eyeline height, and any locked screen side or camera relation before drafting. Externalize each cross-shot spatial invariant once; shot paragraphs carry only material changes and any local fact needed to preserve the intended visible roster or occlusion. Do not infer permanent left/right placement or distance from fixed camera or shot count alone.

## Visibility, path, and terminal audit

Scan each shot silently:

1. Separate world existence from intended shot visibility.
2. At each material start or terminal boundary, compare the intended crop with the minimum visible envelope implied by every body part, prop, subject, and landmark requested in that frame. Remove only mutable visibility details that exceed the crop; preserve any explicitly locked group view, full-body view, interaction point, or landmark. A supported camera move may transition between different envelopes.
3. In non-quoted visual instruction prose, keep a concrete scene noun only when it is visible, visibly interacting, or needed to establish the visible environment. Exclude protected dialogue, narration, lyrics, visible text, and literal `@...` anchors from this audit.
4. Describe a moving subject or effect with only the material route: origin or screen entry -> direction -> target. Keep an intermediate building, doorway, vehicle, or prop when the action visibly contacts, crosses, damages, avoids, or deliberately uses it; otherwise do not promote scenery into a waypoint.
5. Preserve an offscreen cause with the minimum visible clue needed to read the action, such as screen-entry direction, gaze/body axis, directional light, environmental response, or impact point.
6. When terminal composition matters, let the final clause or sentence state the visible endpoint. Do not append a world-continuity summary after it.
7. Preserve every explicitly requested opponent, landmark, group frame, interaction, or final standoff. This audit removes unintended visibility; it never creates a universal one-subject or landmark-free rule.

## Visual dominance, scale, and reveal continuity

Use these checks only when hierarchy, unusual scale, transformation, or a reveal materially affects the shot:

1. Keep one viewer priority. Render it as `画面重心` only when several visible elements compete. A secondary subject may remain visible for causality, continuity, or scale without receiving an independent portrait treatment.
2. Choose scale cues by shot purpose. Frame overflow, near-field perspective, occlusion, parallax, and a limited familiar-size cue can suggest a subject larger than the frame; a wide or complete view remains appropriate when geography, full anatomy, choreography, or the requested endpoint needs it.
3. Prefer observable framing language to unsupported composition arithmetic. Preserve exact percentages when the user or source locks them; otherwise state what crosses the frame edge, what remains partial, and which depth relationship changes.
4. If a formation should appear at its final scale rather than grow, establish its final spatial envelope and let material resolve across multiple separated regions. Use small-to-large scaling when growth itself is the intended event.
5. Treat a reveal as an action boundary, not automatically an endpoint. Unless the held reveal is intentional, state the next immediate change—gaze activation, weight shift, limb action, material discharge, or another authorized beat—and keep one motion carrier continuous across it.
6. Let the camera follow one meaningful carrier when movement is needed: the forming material, an active limb, a projectile, a moving subject, or an attention shift. Do not add motion solely to prevent a pause.

## Effect-outcome audit

When the difference among blocking, redirecting, dismantling, absorbing, reflecting, or evading matters, define the visible terminal state rather than relying on a broad verb:

- blocking: forward motion stops at a maintained boundary
- redirecting: the effect remains coherent enough to leave along a changed route
- dismantling: internal structure or propagation breaks down and the effect loses coherence at the interaction point
- absorbing: material or energy visibly transfers into another subject or system
- reflecting: the effect leaves along a return route
- evading: the original route continues while the target changes position

These are diagnostic distinctions, not mandatory effect designs. Preserve the user's chosen mechanism and material language; add only enough intermediate change to make that outcome visible.

## Final check

- each shot has one visual priority, one main action, and no contradictory camera instruction
- intended framing can contain the requested visible envelope without relying on a repeated shot-size label
- a cut that continues the same event inherits its current action phase rather than restarting it
- any intended dominance, unusual scale, reveal continuation, or effect outcome is visible without forcing an unrelated composition
- duration fits the locked beats without speculative micro-control
- Seedance 2.5 new/reference shots use continuous exact ranges whenever total duration is known; edit intervals remain local to the requested operation
- reference generation uses `参考`; edit/extension addresses the source video directly
- start and terminal BoundaryStates are sparse rather than full shot duplicates
- terminal visible roster matches the shot purpose even when no next handoff exists
- next handoff is only a subset of terminal state
- world position, screen position, camera side, and screen direction agree when material
- asset operational roles, boundary scopes, and borrowed dimensions do not leak; reference-input anchors are normally bound once
- exact dialogue, visible text, required sound/silence, style, and initiating action remain intact
- every restriction passes the admission test: user/source lock, platform requirement, active-reference conflict, or observed failure
- deleting any remaining sentence would change the visible result, a costly lock, a necessary role, or platform execution

For an observed bad generation, paired success/failure comparison, ontology error, or unstable prior result, load `references/failure-recovery.md` instead of expanding this checklist.
