# FightStory — 白话打斗故事与短打斗编剧

Read this file when a user needs to decide what a multi-beat fight means before technical choreography or when a failed fight needs a new escalation, initiative curve, reversal, or ending. Do not use it to turn a fixed single beat, mechanics question, or audit into an extra story round.

## Purpose and boundary

FightStory is the user-readable contract for one fight or fight segment. It explains what happens, why the pressure changes, and where the sequence stops before camera, VFX, or platform wording can hide a weak progression.

It may design only what the assigned fight needs:

- each side's immediate visible goal;
- the obstacle that forces a response;
- escalation through distance, position, freedom, terrain, number, scale, ability boundary, or time pressure;
- visible causes for initiative changes;
- a false-victory impression, reversal seed, reversal cost, or suspense ending when requested;
- the function of an existing or authorized location, prop, weapon, or ability.

It must not add long-form character history, dialogue, lore, a subplot, a new power system, a different winner, extra fighters, injury, damage, or destruction.

## Story contract

Write one compact continuous narrative that lets the user answer these questions without production vocabulary:

1. What is each side trying to achieve right now?
2. What concrete advantage or restriction makes the opening difficult?
3. What does the first meaningful exchange change?
4. How does danger escalate instead of merely adding attacks?
5. Which visible action transfers or contests initiative?
6. If the viewer is meant to expect victory, what evidence earns that belief and what already-visible fact enables the reversal?
7. Does the ending settle the fight, expose a cost, separate the fighters, or reveal a new threat?

Every paragraph must advance at least one observable state: distance, posture, facing, height, location, weapon relationship, freedom of movement, ability stage, or initiative. Remove exchanges that return every relevant state to its starting value without revealing a tactic or paying a cost.

## Escalation and reversal

- Escalate by changing the problem, not by listing stronger adjectives or more attacks.
- Build advantage cumulatively: one side gains better distance, angle, height, support, recovery time, route access, or control of an existing weapon or ability.
- A false victory requires repeated visible evidence before the apparent finishing opportunity.
- A reversal must use an authorized fact that was visible, stated, or naturally prepared earlier. Do not invent its material, shape, element, damage, or exact mechanism when only its tactical function is known.
- A suspense ending stops after the new threat becomes readable through activation, entry, occupation of routes, aim, or changed range. It does not continue into another attack or outcome.

## Terrain and props

Use terrain or a prop only when it changes a route, support, line of sight, distance, landing, leverage, contact receiver, or recovery option. Preserve its location and condition after use. A doorway, roof, pillar, railing, weapon, or other object does not teleport between beats and is not destroyed merely to signal intensity.

## Plain-language rendering

- Use ordinary continuous Chinese, normally two to four short paragraphs.
- Name the fighters and concrete actions. Prefer “B逼得A只能沿墙退” over “B掌握主动权”.
- Do not use FightBeat, action axis, contact ledger, MotionSpec, structure version, lens, camera movement, timestamp, platform syntax, or prompt labels.
- Do not include a technical checklist after the story unless the user explicitly asks for one.
- End with the exact visible state where later technical design must begin or stop.

## Failure branches

| Trigger | First response | If still unresolved |
|---|---|---|
| Two supplied facts require different winners, abilities, or endings | Identify the one root conflict and give the two smallest story outcomes | Ask one choice; output no technical design |
| A named ability exists but its appearance or mechanism is unspecified | Use only its minimum tactical function and visible ownership | Keep form/material/damage unresolved for later design |
| The sequence contains attacks but no state change | Remove repetition and make one exchange alter position, freedom, recovery, weapon relation, or initiative | If no change is authorized, frame the segment as a test/stalemate and end honestly |
| A reversal has no prior seed | Reuse an authorized weapon, terrain fact, recovery pattern, or ability already present | If none exists, ask for the reversal source instead of inventing one |
| A suspense ending continues into contact | Stop at readable activation, occupation, aim, or range change | Move any later attack into a separately approved continuation |
| The user supplies a fixed accepted story | Preserve it and check dramaturgy internally | Repair only missing visible causality; do not reopen the story review |

## Output form

Return only:

```text
【白话打斗故事】
<two to four compact paragraphs in ordinary Chinese>

请确认这版打斗走向；确认后再进入动作、镜头与特效设计。
```

If the user explicitly asks for only the story, omit any additional analysis. If review is explicitly skipped, render nothing from this file and continue internally.
