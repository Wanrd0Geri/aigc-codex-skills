---
name: aigc-workflow-router
description: Route AIGC short-film, animation, storyboard, keyframe, image, and video-production requests to the right creative workflow. Use when the user asks how to推进一个AIGC项目, plan a short film workflow, decide the next step for an image/video, connect director judgment with prompt production, or says things like "这个项目怎么做", "下一步怎么办", "帮我拆流程", "这个图/视频该怎么改", "从想法到成片怎么推进". Coordinates with aigc-creative-director, aigc-shot-diagnose, cinematic-storyboard-enhancer, and seedance-prompt-master.
---

# AIGC Workflow Router

Use this skill as the production coordinator for AIGC film, animation, short video, and cinematic image work. Decide the right workflow first, then either perform the routing-level planning or hand off to the specialized skill.

## Routing Rules

Choose one primary path. Do not run every skill at once.

- **Idea, script, scene, or mood without a clear shooting plan**: use `aigc-creative-director`.
- **Uploaded image/frame feels wrong, ugly, flat, AI-looking, or the user cannot name the problem**: use `aigc-shot-diagnose`.
- **Image/keyframe already needs a ready image-to-image edit prompt for Nano Banana Pro, ChatGPT Images 2.0, or another image editor**: use `cinematic-storyboard-enhancer`.
- **Seedance, Doubao Seedance, Dreamina Seedance, image-to-video, text-to-video, video extension, video editing, or shot-bridge prompt**: use `seedance-prompt-master`.
- **Whole project or short-film pipeline**: stay in this router, build the production path, then name the next specialized skill to use first.

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
[A ready sentence the user can send next, such as "Use $aigc-shot-diagnose...".]
```

For whole-project planning, include a compact pipeline:

1. Creative brief and core expression.
2. Director plan and shot strategy.
3. Keyframe or storyboard production.
4. Still-frame diagnosis and image prompt repair.
5. Seedance video prompt drafting.
6. Review, regenerate, edit, and lock continuity.

## Handoff Contracts

When handing off, preserve the decision context:

- To `aigc-creative-director`: provide theme, audience/platform, duration, protagonist, conflict, mood, and reference style if known.
- To `aigc-shot-diagnose`: provide the image/frame plus the user's target feeling and what they already like.
- To `cinematic-storyboard-enhancer`: provide what must be preserved, target model, and the top visual problems to fix.
- To `seedance-prompt-master`: provide shot goal, duration, reference asset roles, start/end state, motion, camera behavior, and continuity constraints.

## Avoid

- Do not answer every request with a long production bible.
- Do not produce final Seedance prompts when the user is still asking for creative direction.
- Do not produce image-edit prompts when the user only asked why an image feels wrong.
- Do not overwrite specialized skill rules; route to them when the task is clearly specialized.
