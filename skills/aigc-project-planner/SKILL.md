---
name: aigc-project-planner
description: Plan and route multi-stage AIGC projects across concepts, keyframes, image repair, and video prompts. Use for whole short-film/animation workflows, multi-shot or multi-asset planning, pipeline questions, and "下一步该做什么" at project level. Do not use for a single image, frame, shot, prompt, or reference asset; route those directly to the relevant specialist skill.
---

# AIGC Project Planner

Use this skill as the production coordinator for AIGC film, animation, short video, and cinematic image work when the task spans a whole project, multiple shots, or multiple production stages.

Do not use this skill for single-asset requests. If the user asks about one uploaded image, one frame, one shot, one prompt, or one reference asset, route directly to the relevant specialist.

## Routing Rules

Choose one primary path. Do not run every skill at once.

- **Whole project or short-film pipeline**: stay in this router, build the production path, then name the first specialized skill to use.
- **Multi-shot sequence with unclear order**: map stages first, then hand off the next concrete task.
- **Multiple assets with unclear roles**: define asset roles before handing off.
- **Prompt wording problem**: when the user asks for `自然语言提示词`, `导演讲戏式提示词`, `prompt 更自然`, `不要参数堆叠`, or wants a rough idea/old prompt rewritten into visible, executable image or video language, use `aigc-natural-language-prompt`.
- **Idea, script, scene, or mood without a clear shooting plan**: use `aigc-creative-director`.
- **Uploaded image/frame feels wrong, ugly, flat, AI-looking, or the user cannot name the problem**: use `aigc-visual-diagnose`.
- **Single frame needs a production decision such as whether it can move forward, enter video, be repaired, be redesigned, or what next skill should be used**: use `aigc-shot-diagnosis-pipeline`.
- **Image/keyframe already needs a ready image-to-image edit prompt for Nano Banana series, ChatGPT image editor series, or another image editor**: use `aigc-image-edit-prompt`.
- **Seedance series, Doubao Seedance, Dreamina Seedance, image-to-video, text-to-video, video extension, video editing, or shot-bridge prompt**: use `aigc-seedance-prompt`.

If multiple paths apply, pick the earliest unresolved creative bottleneck:
1. Intent and story problem.
2. Shot design problem.
3. Prompt wording and natural-language execution problem.
4. Still-frame quality problem.
5. Image-edit prompt problem.
6. Video-generation prompt problem.

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
- To `aigc-natural-language-prompt`: provide the rough idea or old prompt, target artifact if known, style/reference constraints, and any wording concern such as parameter stacking, unsupported off-screen causes, unclear cuts, or abstract mood words.
- To `aigc-visual-diagnose`: provide the image/frame plus the user's target feeling and what they already like.
- To `aigc-shot-diagnosis-pipeline`: provide the frame, user target, intended next step if known, what already works, and any known production concern.
- To `aigc-image-edit-prompt`: provide what must be preserved, target model, and the top visual problems to fix.
- To `aigc-seedance-prompt`: provide shot goal, duration, reference asset roles, starting state, motion, camera behavior, and only the continuity anchors needed for connected shots or segments.

## Avoid

- Do not answer every request with a long production bible.
- Do not keep single-image, single-frame, single-shot, or single-prompt requests inside project planning; route them to the relevant specialist.
- Do not send pure wording rewrites directly to Seedance or image editing when the user is first asking what a natural-language prompt should be; route to `aigc-natural-language-prompt`.
- Do not produce final Seedance prompts when the user is still asking for creative direction.
- Do not produce image-edit prompts when the user only asked why an image feels wrong.
- Do not overwrite specialized skill rules; route to them when the task is clearly specialized.
