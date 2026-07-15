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

Use these as internal beat budgets, not exact generated-shot timestamps:

- one action beat: about 2-3 seconds
- one camera move plus one action: about 3-4 seconds
- one expression/attention change: about 1-2 seconds
- one contact and reaction: about 2-3 seconds
- one multi-character handoff: about 3-5 seconds

If the duration cannot hold locked beats, simplify mutable camera and description first, then recommend extending or splitting. Never delete, merge, reorder, or add exact per-shot timestamps without authorization.

## Visibility, path, and terminal audit

Scan each shot silently:

1. Separate world existence from intended shot visibility.
2. In non-quoted visual instruction prose, keep a concrete scene noun only when it is visible, visibly interacting, or needed to establish the visible environment. Exclude protected dialogue, narration, lyrics, visible text, and literal `@...` anchors from this audit.
3. Describe a moving subject or effect with only the material route: origin or screen entry -> direction -> target. Keep an intermediate building, doorway, vehicle, or prop when the action visibly contacts, crosses, damages, avoids, or deliberately uses it; otherwise do not promote scenery into a waypoint.
4. Preserve an offscreen cause with the minimum visible clue needed to read the action, such as screen-entry direction, gaze/body axis, directional light, environmental response, or impact point.
5. When terminal composition matters, let the final clause or sentence state the visible endpoint. Do not append a world-continuity summary after it.
6. Preserve every explicitly requested opponent, landmark, group frame, interaction, or final standoff. This audit removes unintended visibility; it never creates a universal one-subject or landmark-free rule.

## Final check

- each shot has one visual priority, one main action, and no contradictory camera instruction
- duration fits the locked beats without speculative micro-control
- generated shots use event order; exact ranges remain for targeted edits or explicit timing-critical requests
- reference generation uses `参考`; edit/extension addresses the source video directly
- start and terminal BoundaryStates are sparse rather than full shot duplicates
- terminal visible roster matches the shot purpose even when no next handoff exists
- next handoff is only a subset of terminal state
- world position, screen position, camera side, and screen direction agree when material
- reference roles do not leak; anchors are normally bound once
- exact dialogue, visible text, required sound/silence, style, and initiating action remain intact
- every restriction passes the admission test: user/source lock, platform requirement, active-reference conflict, or observed failure
- deleting any remaining sentence would change the visible result, a costly lock, a necessary role, or platform execution

For an observed bad generation, paired success/failure comparison, ontology error, or unstable prior result, load `references/failure-recovery.md` instead of expanding this checklist.
