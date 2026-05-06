---
name: aigc-project-planner
description: Plan and route whole AIGC short-film, animation, storyboard, keyframe, image, and video-production projects across multiple stages or assets. Use when the user asks how to推进一个AIGC项目, plan a whole short film workflow, coordinate multi-shot or multi-asset production, connect creative direction with keyframes and video prompts, or says things like "整个项目怎么做", "从想法到成片怎么推进", "帮我拆全片流程", "这个短片 pipeline 怎么安排". Do not use for single-image, single-frame, single-shot, single-prompt, or single-reference requests; route single-frame production decisions to aigc-shot-diagnosis-pipeline, deep visual critique to aigc-visual-diagnose, creative direction to aigc-creative-director, ready image-edit prompts to aigc-image-edit-prompt, or Seedance/video prompts to aigc-seedance-prompt.
---

# AIGC Project Planner

Use this skill as the production coordinator for AIGC film, animation, short video, and cinematic image work when the task spans a whole project, multiple shots, or multiple production stages.

Do not use this skill for single-asset requests. If the user asks about one uploaded image, one frame, one shot, one prompt, or one reference asset, route directly to the relevant specialist.

## Routing Rules

Choose one primary path. Do not run every skill at once.

- **Whole project or short-film pipeline**: stay in this router, build the production path, then name the first specialized skill to use.
- **Multi-shot sequence with unclear order**: map stages first, then hand off the next concrete task.
- **Multiple assets with unclear roles**: define asset roles before handing off.
- **Idea, script, scene, or mood without a clear shooting plan**: use `aigc-creative-director`.
- **Uploaded image/frame feels wrong, ugly, flat, AI-looking, or the user cannot name the problem**: use `aigc-visual-diagnose`.
- **Single frame needs a production decision such as whether it can move forward, enter video, be repaired, be redesigned, or what next skill should be used**: use `aigc-shot-diagnosis-pipeline`.
- **Image/keyframe already needs a ready image-to-image edit prompt for Nano Banana series, ChatGPT image editor series, or another image editor**: use `aigc-image-edit-prompt`.
- **Seedance series, Doubao Seedance, Dreamina Seedance, image-to-video, text-to-video, video extension, video editing, or shot-bridge prompt**: use `aigc-seedance-prompt`.

If multiple paths apply, pick the earliest unresolved creative bottleneck:
1. Intent and story problem.
2. Shot design problem.
3. Still-frame quality problem.
4. Image-edit prompt problem.
5. Video-generation prompt problem.

## Operating Style

- Read the user's assets and request before asking questions.
- Ask only when the answer changes the creative direction, target platform, reference role, or generation strategy.
- When asking, give the recommended default so the user can accept or override quickly.
- Keep the output practical: name the current stage, the best next action, and the specialized workflow to use.
- Prefer Chinese output unless the user asks otherwise.

## Output Structure

Use this structure for routing or project-flow requests:

```markdown
## 当前判断
[What stage the project/request is in and the main bottleneck.]

## 推荐路径
[One primary workflow, with the exact skill name if relevant.]

## 下一步
[Concrete action: answer 1-3 questions, upload asset, diagnose image, produce shot plan, or draft Seedance prompt.]

## 执行提示
[A ready sentence the user can send next, such as "Use $aigc-visual-diagnose...".]
```

For whole-project planning, include a compact pipeline:

1. Define creative intent, assets, and stage order.
2. Produce or diagnose the next concrete artifact.
3. Hand off to the specialist skill needed for that artifact.

## Handoff Contracts

When handing off, preserve the decision context:

- To `aigc-creative-director`: provide theme, audience/platform, duration, protagonist, conflict, mood, and reference style if known.
- To `aigc-visual-diagnose`: provide the image/frame plus the user's target feeling and what they already like.
- To `aigc-shot-diagnosis-pipeline`: provide the frame, user target, intended next step if known, what already works, and any known production concern.
- To `aigc-image-edit-prompt`: provide what must be preserved, target model, and the top visual problems to fix.
- To `aigc-seedance-prompt`: provide shot goal, duration, reference asset roles, start/end state, motion, camera behavior, and continuity constraints.

## Avoid

- Do not answer every request with a long production bible.
- Do not keep single-image, single-frame, single-shot, or single-prompt requests inside project planning; route them to the relevant specialist.
- Do not produce final Seedance prompts when the user is still asking for creative direction.
- Do not produce image-edit prompts when the user only asked why an image feels wrong.
- Do not overwrite specialized skill rules; route to them when the task is clearly specialized.
