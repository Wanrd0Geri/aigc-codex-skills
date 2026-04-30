---
name: aigc-shot-diagnosis-pipeline
description: Diagnose a single AIGC shot frame, generated still, keyframe, storyboard frame, or video frame as a production pipeline checkpoint. Use when the user wants to know whether a frame is good enough, why it feels wrong, what should be fixed first, whether it can move into image editing or Seedance video generation, or which AIGC skill should be used next. Prioritize production decisions over full prompt writing.
---

# AIGC Shot Diagnosis Pipeline

Use this skill as a single-shot production checkpoint. Diagnose the current frame, decide what production stage it is in, and route the user to the next concrete action.

Do not treat this as a general image critique. The goal is to answer: "Can this shot move forward, and if not, what must be fixed first?"

## Workflow

### 1. Identify the Current Stage

Classify the frame into one primary stage:

- **Concept problem**: the idea, story function, emotion, or shot purpose is unclear.
- **Shot design problem**: blocking, camera angle, composition, silhouette, or implied motion does not support the shot.
- **Image quality problem**: lighting, color, production design, texture, integration, or AI artifacts weaken the frame.
- **Edit-prompt ready**: the frame has enough structure and only needs targeted image repair.
- **Video-prompt ready**: the frame is visually stable enough to become a Seedance image-to-video shot.

Read `references/diagnosis-rubric.md` when the frame's production status is ambiguous, when the user asks whether it is ready for video, or when you need to separate Greenlight, Yellowlight, and Redlight decisions.

If no image/frame is available, ask the user to upload the frame or describe the shot.

### 2. Diagnose the Frame

Read the frame through these lenses:

- **Story function**: what this shot is supposed to communicate.
- **Subject readability**: whether the viewer knows where to look first.
- **Camera and composition**: shot size, angle, depth, crop, and visual hierarchy.
- **Lighting and color**: motivated light, contrast, mood, and color priority.
- **Production design**: costume, props, setting, materials, era, and world consistency.
- **AIGC control**: identity drift, style averaging, over-processing, malformed details, or prompt ambiguity.
- **Video readiness**: whether the frame implies a clear action, camera movement, start state, and continuation path.

### 3. Rank the Production Blockers

Name the top 3 blockers by impact. For each blocker, state:

- Why it blocks the shot.
- What must change.
- Whether it is a concept, shot design, image repair, or video-readiness problem.
- Whether it should be fixed before moving to video.

Do not list every flaw. Focus on the problems that most affect production progress.

### 4. Preserve What Works

Explicitly identify what should not be changed:

- Character identity, face, costume, pose, camera angle, environment, color mood, or composition if they are already useful.
- Any visual choice that supports the shot intention, even if it is unusual.

### 5. Choose the Next Handoff

Route to one next action:

- Use `aigc-creative-director` if the shot idea or emotional purpose is weak.
- Use `aigc-visual-diagnose` if the user needs a deeper artistic diagnosis of the frame.
- Use `aigc-image-edit-prompt` if the frame is structurally good and needs a repair prompt.
- Use `aigc-seedance-prompt` if the frame is ready for image-to-video or video extension.
- Stay in this skill if the user only needs a production decision and next-step checklist.

## Output Structure

Use this structure in Chinese:

```markdown
## 当前阶段判断
[One stage classification and why.]

## 能保留的部分
[What already works and should be protected.]

## 最影响成片的 3 个问题
1. [Problem / why it matters / what to change.]
2. [Problem / why it matters / what to change.]
3. [Problem / why it matters / what to change.]

## 是否可以进入下一步
[Ready for image edit, ready for Seedance, or must fix first.]

## 推荐修正路径
[Concrete next action and the exact skill to use.]

## 交接摘要
[Context the next skill needs: preserve, fix, avoid, shot goal, motion/camera if relevant.]
```

## Standards

- Prefer production judgment over aesthetic commentary.
- Separate "not beautiful" from "not usable for this shot".
- Never write a full image-edit or Seedance prompt unless the user explicitly asks.
- Do not route to every skill. Pick one next step.
- Be direct about whether the frame is ready or not ready.
- Use practical Chinese by default.
