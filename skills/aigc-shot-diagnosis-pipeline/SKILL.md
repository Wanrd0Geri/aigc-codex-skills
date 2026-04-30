---
name: aigc-shot-diagnosis-pipeline
description: Diagnose a single AIGC shot frame, generated still, keyframe, storyboard frame, or video frame as a production pipeline checkpoint. Use when the user asks whether one frame can move forward, whether it can enter image editing or Seedance video generation, whether it should be repaired or redesigned, what blocks production, or which AIGC skill should be used next. Do not use for detailed artistic image critique; use aigc-visual-diagnose for "why does this look wrong" analysis.
---

# AIGC Shot Diagnosis Pipeline

Use this skill as a single-shot production checkpoint. Decide whether the current frame can move forward, what blocks it, and which specialist workflow should handle the next step.

Do not treat this as a full visual critique. The goal is to answer: "Can this shot move forward, and if not, what must be fixed first?"

## Boundary

- Use this skill for production decisions: `能不能用`, `能不能进视频`, `下一步去哪`, `该修图还是重做`, `是否可以进入 Seedance`.
- Do not do complete deep visual diagnosis here. If the user asks `为什么不好`, `哪里怪`, `详细分析画面问题`, or wants director/cinematography/art-direction critique, route to `aigc-visual-diagnose`.
- Do not write full image-edit or Seedance prompts by default. Route to `aigc-image-edit-prompt` or `aigc-seedance-prompt` after the production decision.

## Workflow

### 1. Identify the Current Stage

Classify the frame into one primary problem stage:

- **Concept problem**: the idea, story function, emotion, or shot purpose is unclear.
- **Shot design problem**: blocking, camera angle, composition, silhouette, or implied motion does not support the shot.
- **Image quality problem**: lighting, color, production design, texture, integration, or AIGC artifacts weaken an otherwise usable shot.
- **Ready**: the concept, shot design, and image structure are stable enough to choose an execution path.

If the frame cannot be judged without deeper artistic analysis, choose **Deep diagnose first** as the recommended path and hand off to `aigc-visual-diagnose`.

### 2. Assign a Production Status

Use `references/diagnosis-rubric.md` to classify the frame:

- **Green**: proceed. The frame can move into image editing or video generation.
- **Yellow**: proceed only after fixing 1-3 high-impact issues.
- **Red**: do not write prompts yet. Redesign, regenerate, or return to an upstream creative/shot-design step.
- **Suspected Red**: the model sees a likely blocker but needs user confirmation, usually for story purpose, first-glance subject readability, or video-extension potential.

### 3. Choose the Recommended Path

Pick one path, not a list of possibilities:

- **Direct edit**: the frame is not intended for video or only needs a still-image repair.
- **Edit then video**: the frame can become video, but targeted image repair should happen first.
- **Direct video**: the frame is stable enough for `aigc-seedance-prompt` without prior image repair.
- **Redesign first**: the frame has a root problem that prompt writing will not fix.
- **Deep diagnose first**: the production decision depends on a deeper visual diagnosis.

### 4. Rank the Production Blockers

Name the top 3 blockers by impact. For each blocker, state:

- Why it blocks the shot.
- What must change.
- Whether it is a concept, shot design, image repair, or video-readiness problem.
- Whether it must be fixed before moving to video.

Do not list every flaw. Focus on the problems that most affect production progress.

### 5. Preserve What Works

Explicitly identify what should not be changed:

- Character identity, face, costume, pose, camera angle, environment, color mood, or composition if they are already useful.
- Any visual choice that supports the shot intention, even if it is unusual.

### 6. Prompt-Writing Boundary

Default behavior: output diagnosis, production status, recommended path, and handoff summary. Do not write a full image-edit or Seedance prompt.

Exception: if the user explicitly asks in the same request for diagnosis plus a prompt, continue only when the production status allows it.

- **Green**: proceed to the relevant prompt workflow.
- **Yellow**: explain the risk first, then proceed only if the user explicitly wants to accept the risk.
- **Red**: do not write the prompt. Explain which upstream fix is needed first.
- **Suspected Red**: ask one concrete confirmation question before writing a prompt.

Use this risk format when the user insists on a prompt from a Yellow frame:

```markdown
状态：Yellow（建议先修图）
你明确要求直接进入 [Seedance / image editing]，可以继续，但有这些风险：
- [Unfixed issue] may cause [specific production consequence].
- [Unfixed issue] may cause [specific production consequence].
如果接受这些风险，下一步交给 `[target skill]`。
```

## Output Structure

Use this structure in Chinese:

```markdown
## 当前阶段判断
[Concept problem / Shot design problem / Image quality problem / Ready, with one-sentence reason.]

## 生产状态
[Green / Yellow / Red / Suspected Red, with the decisive evidence.]

## 能保留的部分
[What already works and should be protected.]

## 最影响推进的 3 个问题
1. [Problem / why it matters / what to change.]
2. [Problem / why it matters / what to change.]
3. [Problem / why it matters / what to change.]

## 推荐路径
[Direct edit / Edit then video / Direct video / Redesign first / Deep diagnose first, plus exact next skill.]

## 交接摘要
[Context the next skill needs: preserve, fix, avoid, shot goal, motion/camera if relevant.]
```

If the status is Suspected Red, replace `推荐路径` with:

```markdown
## 需要你确认
[One concrete question the user can answer quickly.]
```

## Standards

- Prefer production judgment over aesthetic commentary.
- Separate "not beautiful" from "not usable for this shot".
- Pick one next step.
- Be direct about whether the frame is ready, repairable, blocked, or uncertain.
- Use practical Chinese by default.
