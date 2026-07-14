# Diagnose mode

Use this mode to explain the frame and rank the smallest high-leverage fixes. Diagnosis is an artifact, not a pretext to write an unrequested prompt.

## Sequence

1. Describe the readable frame neutrally.
2. State the likely creative intention and its evidence.
3. Inspect only lenses that contain real findings:
   - director: story function, attention priority, action, emotional carrier
   - cinematography: framing, camera motivation, depth, exposure, light, color
   - production design: silhouette, costume, props, materials, era, world coherence
   - storyboard/editing: readable pose, screen direction, implied before/after state, crop
   - AIGC control: reference conflict, identity drift, artifacts, style averaging, malformed detail
4. Rank up to three issues by impact. For each, state visible evidence, why it matters, and the smallest practical fix.
5. When asked whether the frame can proceed, choose one:
   - `can proceed`: structure already supports the intended use
   - `repair first`: bounded defects block use but composition and motion support remain valid
   - `redesign first`: subject scale/position, pose, silhouette, camera relation, or spatial structure must change

Give one decisive reason for readiness. Do not use red/yellow/green labels.

## Depth

- Quick: 3-5 sentences plus the top issues.
- Standard: observation, intention, relevant lenses, ranked fixes, next action.
- Deep: only when the user asks for a full breakdown, comparison, grading, or art-direction review.

Do not force five lens headings or exactly three problems. Separate functional failure from optional taste.

## Combined diagnose -> edit

Keep a silent handoff with:

- preserve: what already works
- fix: ranked authorized changes
- release: any protection the user explicitly gives up
- avoid: concrete drift risks

Pass this directly into edit mode without re-reading or repeating the full diagnosis.
