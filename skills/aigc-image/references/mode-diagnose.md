# Diagnose mode

Use diagnosis to find the first failing visual relationship and select the smallest edit capability. Diagnosis is a terminal artifact when the user asks only why; do not append a prompt without permission.

## Sequence

1. Describe only the readable image evidence.
2. State the likely visual intention and the evidence supporting that reading.
3. Classify the root failure into one or more edit systems: geometry, composition, placement/contact, lighting, color, focus/depth, optical effects, material integration, object cleanup, or production design.
4. Rank up to three issues by impact on the user's purpose. For each, state evidence, consequence, and the smallest repair.
5. Map every recommended repair to one capability in `capability-router.md`.

Do not repeat one root cause under several headings. Separate functional failure from optional taste. If the intended visual priority is unknown and different choices would produce different edits, ask one focused question.

## Readiness

When asked whether the image can proceed, choose one:

- `can proceed`: the image already supports its intended use
- `repair first`: bounded defects block use but the main structure remains valid
- `redesign first`: identity, count, subject scale, pose, composition, camera relation, or spatial structure must change

Give one decisive reason. Do not use red/yellow/green labels.

## Combined diagnose -> edit

Pass a silent handoff into edit mode:

- `preserve`: what already works
- `fix`: ranked authorized changes and selected capabilities
- `release`: protections explicitly surrendered by the user
- `avoid`: concrete drift risks

Read the image once. Do not repeat the full diagnosis inside the final prompt.
