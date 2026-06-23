---
name: aigc-script-context
description: Use when turning a script, storyboard, shot list, or long-form AIGC video project such as 临渊行 into shot-level context cards, continuity handoffs, performance notes, and Seedance-ready story context before final video prompt writing.
---

# AIGC Script Context

Use this skill before `aigc-seedance-prompt` when a video prompt needs story knowledge beyond the current shot. The skill's job is not to write the final Seedance prompt by default; it prepares the compact story context that makes the final prompt accurate.

## Core Rule

Treat script context as a production handoff, not a plot summary. Convert story information into visible action, performance, blocking, continuity anchors, and shot intent.

CHECKPOINT - Source Priority:

First identify the active project or source package. If the project is ambiguous, ask one project-selection question. Do not merge sources across projects.

1. Latest user instruction and newly attached reference images.
2. Current storyboard or shot list.
3. Current episode script.
4. Project bible, outline, worldbuilding notes, and older summaries.

If sources conflict, keep the higher-priority source and note the conflict briefly. Do not let an old outline overwrite the current storyboard or script.

Current storyboard and script are production truth. Outline and worldbuilding can fill missing context only; they must not override current storyboard, script, exclusions, or latest user instructions.

Project exclusions override raw source rows. If a project package marks a scene, shot, placeholder row, or asset as excluded, skip it even when the original spreadsheet or script still contains it.

## Workflow

1. Identify the project and source package. If a matching project package exists in the current workspace, load its project context first. If the requested package is absent, ask the user for the project package, source files, or relevant excerpts instead of assuming project facts.
2. Locate the requested episode, scene, shot range, or reference image role.
3. If no prepared scene context exists, fall back to the project raw-source extraction rules before answering; do not rely on a scene-index summary alone.
4. Build a shot context card before drafting any video prompt.
5. Include only the context the current shot needs: scene function, current emotional state, previous shot ending state, required visual facts, performance cues, dialogue, and next-shot handoff.
6. Estimate duration by visual complexity when the storyboard has no duration.
7. Hand the card to `aigc-seedance-prompt` when the user asks for the final Seedance prompt.
8. Run a continuity check after the prompt: identity, action order, emotion, prop state, camera relation, and next-shot handoff.

## Output Modes

- **Context card only**: when the user asks for shot cards, script understanding, scene breakdown, or production preparation.
- **Handoff to Seedance**: when the user asks for a Seedance/Doubao/Dreamina prompt. Produce a compact card first internally, then draft using `aigc-seedance-prompt` rules.
- **Continuity audit**: when the user asks whether a prompt matches the script/storyboard. Compare against source priority and report mismatches before rewriting.

## Duration Heuristic

Use this when the storyboard has no per-shot duration:

- Simple object, still reaction, or one clean action: 4-6 seconds.
- Standard acting beat, dialogue beat, or one subject movement: 6-10 seconds.
- Complex blocking, multiple subjects, reveal, VFX, or strong camera move: 10-15 seconds.
- If one shot needs more than 15 seconds, split it or simplify before handing to Seedance.

Do not write frame rate, resolution, aspect ratio, or platform settings inside the prompt body unless the user explicitly asks.

## Shot Context Card

Use this compact structure:

```text
项目：
集/场/镜：
源优先级：
本镜剧情功能：
上一镜承接：
当前画面事实：
人物表演：
对白/声音：
参考图角色：
估计时长：
下一镜交接：
禁止偏移：
```

For performance, never stop at labels like `愤怒`, `震惊`, or `害怕`. Translate them into visible cues: gaze target, body part, contact point, posture shift, pause, breath, expression transition, and action endpoint.

## References

- Read `references/shot-card-contract.md` when building shot cards or duration estimates.
- Read `references/seedance-handoff.md` when the next step is a Seedance 2.0 prompt.
- Known project package: for `临渊行`, read the matching local project package only when it exists in the current workspace. Otherwise ask for the project package or source files.

## Failure Branches

- If the requested shot depends on a missing scene reference image, ask for it or proceed with story/performance context only, depending on the user's goal.
- If the named project package is absent from the current workspace, ask for the project package or source files; do not hallucinate project-specific facts from memory.
- If a prepared scene context file is missing, use the project's raw-source extraction reference to pull storyboard rows, script scene text, neighboring shots, and exclusions before building the card.
- If a project exclusion conflicts with a raw source row, follow the exclusion and do not create a card for that row.
- If the storyboard row has no executable image description, mark it as non-production or pending instead of inventing a shot.
- If a project outline and current storyboard disagree, follow the storyboard and mention that the outline is used only for world/personality context.
- If the final video prompt starts becoming a full plot recap, compress back to current shot facts and handoff anchors.
- If the user asks for a single finished Seedance prompt and provides all needed references, do not over-plan; generate the prompt after building the internal card.

## Avoid

- Do not merge storyboard, script, outline, character assets, or exclusions across different projects.
- Do not let outline/worldbuilding overwrite current storyboard rows, current script beats, latest user instructions, or explicit exclusions.
- Do not skip raw-source fallback when the prepared scene context is missing or too thin.
- Do not treat white-background character sheets as final scene lighting, color, camera angle, or environment reference.
- Do not turn a context card into a final Seedance prompt unless the user asks for final video prompt writing.
- Do not include full plot recap, lore explanation, or every neighboring shot when the current shot only needs locked facts and continuity anchors.
