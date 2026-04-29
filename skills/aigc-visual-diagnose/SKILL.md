---
name: aigc-visual-diagnose
description: Diagnose uploaded AIGC images, video frames, storyboards, keyframes, concept art, or generated stills when the user says the result feels wrong, ugly, flat, cheap, AI-looking, not cinematic, poorly composed, badly lit, visually inconsistent, or uses phrases like "不好看", "说不上来哪里怪", "AI味重", "不高级", "不电影感", "构图怪", "光影乱", "人物没融入画面", "质感差", "画面很平". Analyze from director, cinematography, production design, storyboard/editing, and AIGC generation-control perspectives, then rank what to fix first.
---

# AIGC Visual Diagnose

Use this skill when the user has an image or frame that feels weak but they cannot name why. Diagnose before writing prompts. The goal is to teach the visual problem and identify the highest-leverage fixes.

## Workflow

### 1. Read the Frame Neutrally

Describe what is actually visible before judging:

- Subject, action, pose, expression, and blocking.
- Composition, shot size, angle, depth layers, and visual hierarchy.
- Light direction, contrast, softness/hardness, and apparent source.
- Color palette, saturation, temperature, and where color attention sits.
- Production design: costume, props, environment, material, era, and texture.
- Mood read: what emotion the image currently communicates.

If no image is available, ask the user to upload one or describe the frame.

### 2. Infer the Intended Effect

State the likely creative intention in one sentence. If the intention is unclear, say so and offer the most likely assumption. Do not over-question unless the image could support two very different creative goals.

### 3. Diagnose Through Five Lenses

Use concise, specific observations:

- **Director**: unclear story function, weak emotional carrier, no subject desire, no readable action, or no attention priority.
- **Cinematography**: flat framing, wrong shot size, unmotivated camera, weak depth, confusing lens feel, poor exposure, or incoherent light.
- **Production design**: random props, mismatched costume/environment, texture noise, unclear era/world, weak material contrast, or color system without hierarchy.
- **Storyboard/editing**: unreadable silhouette, weak pose, bad screen direction, missing before/after state, awkward crop, or a frame that does not imply motion.
- **AIGC control**: prompt too abstract, references fighting each other, identity drift, over-smoothed skin/material, style averaging, malformed anatomy, or over-processed "cinematic" effects.

### 4. Rank the Fixes

Name the top 3 problems by impact. For each, provide:

- Why it hurts the image.
- What to change.
- Whether it is a director, camera/light, art-design, composition, or prompt-control fix.

Read `references/production-design-dimensions.md` when the image feels AI-looking, cheap, visually random, over-designed, texture-poor, cluttered, world-inconsistent, or when the user says `AI味重`, `不高级`, `质感差`, `背景乱`, `角色不突出`, `道具随机`, or `人物没融入画面`. Use it to separate art-direction problems from lighting, grading, and model-control problems.

### 5. Choose the Next Handoff

- If the user wants to understand the problem only, stop after diagnosis and next steps.
- If they want an image-to-image repair prompt, hand off to `aigc-image-edit-prompt`.
- If they want the frame to become a Seedance video shot, hand off to `aigc-seedance-prompt`.
- If the concept itself is weak, hand off to `aigc-creative-director`.

## Output Structure

Use this structure:

```markdown
## 画面观察
[Neutral read of the frame.]

## 可能的创作意图
[What the image appears to be trying to do.]

## 五类诊断
[Director / Cinematography / Production Design / Storyboard-Editing / AIGC Control.]

## 最关键的 3 个问题
[Ranked fixes with why and how.]

## 下一步建议
[Which specialized skill or action should follow.]
```

If the user asks for a repair prompt, says they want to continue into image editing, or the natural next step is `aigc-image-edit-prompt`, add this handoff block:

```markdown
## 给修图 prompt 的交接摘要
- Preserve: [Faces, identity, costume, pose, blocking, camera, or other elements to protect.]
- Fix: [Top 3 fixes by impact.]
- Cinematography: [Light, exposure, black point, temperature, atmosphere, depth.]
- Production Design: [Character, costume, prop, material, color hierarchy, world consistency.]
- Avoid: [Things the edit prompt must not change or introduce.]
```

## Diagnosis Standards

- Be concrete: name the visible evidence, not just the vibe.
- Separate taste from function. A weird choice is not a problem if it supports the scene.
- Preserve what works. Do not recommend redesigning faces, costumes, poses, or camera unless those are the actual issue.
- Prefer the smallest fix that changes the read of the image.
- Explain in practical language so the user learns director, cinematography, storyboard, and art-direction thinking over time.

## Avoid

- Do not call image generation tools.
- Do not immediately write a full prompt unless the user asks for one.
- Do not list every possible flaw with equal weight.
- Do not say only "add cinematic lighting", "improve composition", or other generic fixes.
- Do not treat every image as live-action cinema; animation, stylized art, and commercial visuals have their own standards.
