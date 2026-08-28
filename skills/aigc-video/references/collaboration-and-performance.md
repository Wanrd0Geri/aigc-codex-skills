# Collaboration and performance translation

The user prefers active creative dialogue. Do not confuse autonomy with silence.

These communication actions resolve interpretation only. Structure review follows `SKILL.md`; only a current-user direct authorization removes its pause.

## Communication action

- `discuss`: evidence is insufficient, at least two readings are well supported, and choosing between them changes performance, action, rhythm, composition, continuity, or ending.
- `assume and proceed`: the gap is non-material; choose the lowest-risk option.
- `state and proceed`: after structure review resolves for the affected unit, the source gives a clear emotional direction; briefly state the bounded interpretation when useful, then deliver without adding another performance-approval round.
- `warn and deliver`: the requested artifact remains executable but carries a stability tradeoff, such as exceeding a provider recommendation while staying inside hard limits.
- `structural replan`: locked time, space, subject count, action load, or camera load cannot fit the current structure; reopen the affected structure and present the smallest executable replan.
- `silent`: routine platform syntax and non-material craft choices.

When discussing, use this shape:

1. `我的理解` — cite the evidence and state the current reading.
2. `不确定点` — explain what could change the result.
3. `方向` — present only materially different alternatives.
4. `我的建议` — recommend one and explain why.
5. Ask 1-3 related questions together.

Do not ask `这里是什么情绪？` without first doing the interpretive work. Do not invent a competing interpretation merely to create a question.
Do not present synonymous wording, equivalent heading placement, duplicate material binding, or another presentation-only difference as alternatives. Resolve those mechanically from field ownership and ask only when the choice changes the produced performance, action, composition, continuity, or ending.

## Authority for performance intent

1. Current user instruction.
2. Current storyboard and its existing directing choices.
3. Current script.
4. Project/world context that does not conflict with current production sources.
5. Bounded agent interpretation.

Keep three fields separate:

- locked action: what physically must happen
- performance intent: why or how the moment should feel
- visible performance: the supported behavior the model can render

Record the interpretation source and confidence internally.

## Scene acting pass

While a review-required structure version is pending, extract only the one concise source-backed intention needed by the table; if it is materially ambiguous, mark that cell `待确认`. For a directly authorized unit, keep the same compact intent internal. Run the full motive/goal/obstacle/tactic analysis, listener task, turn, and visible-performance handoff after structure review resolves.

Run the full pass only for multi-character dialogue/reaction, materially ambiguous motivation, a result described as wooden/empty/overacted, or a beat whose meaning depends on the listener. A routine single-subject action uses the compact translation below.

Read the complete available scene, including what happens immediately before and after. Record internally:

1. the shared scene direction: what is changing between the people by the end
2. for each active person: current motive, concrete goal, obstacle, and tactic toward the other person
3. what the speaker is testing, concealing, pressing, avoiding, or obtaining
4. the listener's task: what they hear, check, resist, decide, or prepare to do
5. the turn where the tactic, attention, distance, or control changes

Do not print this analysis block or its field labels in the final prompt. Convert the material result into one `ActingTask` per active character and keep the group inside one shared direction; do not give every visible person an equally strong simultaneous reaction. The analysis may remain internal, but a task that materially changes performance must not remain hidden.

When the shared scene direction materially changes distance, attention, turn-taking, object control, willingness, refusal, or another visible relationship by the end, give that change one rendered owner in the relevant shot process or endpoint. Do not leave the group change only in the internal scene analysis, and do not add a prose summary when the same relation is already visible in the acting sentence or endpoint.

## Performance capacity gate

Run this gate for every material reaction, realization, refusal, loss of control, or relationship turn after structure review resolves:

1. identify the trigger and its current readable evidence when it occurs in this shot, the current starting state, the change, and the terminal state that must remain visible through the cut; when the trigger occurred before cut-in, inherit the reached state without replaying it
2. count competing load in the same shot: exact dialogue, body or prop action, another person's handoff, occlusion, and camera movement
3. keep one primary performance carrier whose start and endpoint are distinguishable in the chosen crop; restrained acting limits amplitude but never makes a material change invisible
4. protect stable screen time for the change and terminal hold without rendering inferred shot-body timestamps

If optional facial, breath, hand, atmosphere, or camera cues compete with the material turn, remove those mutable cues first. If locked dialogue, action, framing, and the material turn still cannot fit, select `structural replan` for the affected unit rather than compressing the reaction into a transient expression that resets. Do not apply one universal second count: use the feasibility estimates in `single-segment-quality-control.md` against the actual beat and competing load.

Choose the lowest amplitude that still makes the start and endpoint unambiguous in the actual crop. Do not default a plot-critical change to `微妙`、`轻微` or another low-amplitude label merely because the performance is restrained. When a controlled comparison shows that the current amplitude remains unreadable, increase only the primary carrier's visible amplitude in the next hypothesis and keep its terminal hold; do not add a longer micro-action chain. Treat a strong amplitude as case-specific escalation because it may shift the meaning toward shock or injury, not as a universal default.

## Performance handoff

Use the internal beat only as a reasoning aid:

`starting relational state -> trigger -> tactic or attention turn -> intended visible endpoint`

An `ActingTask` contains only the parts that materially control this beat:

- `playable_task`: what the character is trying to make the other person, situation, or self do, reveal, believe, stop, or permit
- `feedback_target`: what response, look, sound, distance change, or result the character checks, only when the task depends on feedback
- `strategy_turn`: how the character changes approach when the expected feedback succeeds or fails, only when the script/accepted scene contains that turn
- `visible_execution`: the smallest crop-readable action selected through `shot-craft.md`
- `continuity_anchor`: relation, attention, intensity, or decision state that the next shot must inherit, only when material

Prefer a playable relation over an emotion adjective when the distinction affects the result: `一边回答一边判断对方是否相信` is more actionable than `表现怀疑`; `用停顿迫使对方继续说` is clearer than `沉默` or `显得压迫`. Emotion emerges from the task succeeding, failing, or changing; do not use eyebrow, lip, breath, or another expression checklist as a substitute for the task.

Choose start and endpoint as visibly different states inside the current crop. If the character already begins with a stern frown, do not encode disappointment as a deeper version of the same frown; move the primary carrier to attention, head or shoulder set, relational distance, object control, or another supported channel. A continuity anchor inherits the reached endpoint, not the earlier mask or a momentary peak.

In the final shot prose, render the task and visible execution together without schema labels. Default to one compact causal sentence per materially active character; give a listener a second full task only when their independent decision materially affects the beat. For example: `他试图让对方相信自己没事；每说完一个理由便确认对方的反应，对方仍未相信时，他换一种说法，原本稳定的语速出现一次短暂停顿。` A task without visible execution remains too abstract for video; visible gestures without the task lose the performance logic. A compact structure-table intention records only the source-backed core and does not carry this expanded sentence before confirmation.

If `continuity_anchor` controls the next shot, render it there as the current relation, attention, intensity, or decision state before the next trigger or tactic advances it. This is a cut-in state, not an instruction such as `承接上一镜`, and it does not require repeating the earlier task.

Pass the `ActingTask` to `shot-craft.md`, which chooses its visible execution and supporting cues but may not delete the playable task. Any environment response remains owned by `world-dynamics.md`; any sound remains owned by the active platform/audio rules. This file never creates a second rendering list.

Treat intent as motivation, not permission to add props, flashbacks, people, environment changes, or another plot event.

If the evidence genuinely supports both `nostalgia` and `vigilance` at near-equal strength, discuss the choice because they create different body tension, gaze speed, and ending state. If the user has already specified restrained recognition, or only a minor pause length is unspecified, translate or decide it and proceed.
