---
name: aigc-visual-diagnose
description: Use when the user provides an AIGC image, frame, storyboard, keyframe, or concept and asks why it looks weak, ugly, flat, cheap, AI-looking, visually inconsistent, not cinematic, 哪里怪, 为什么不好看, 质感差, or has composition/light/art-direction problems.
---

# AIGC Visual Diagnose

Use this skill when the user has an image or frame that feels weak and wants to understand why. Diagnose before writing prompts. The goal is to teach the visual problem and identify the highest-leverage fixes.

Cross-skill routing in this file assumes the companion AIGC skills are installed. If a named skill is unavailable, provide the diagnosis handoff summary and stop; do not silently imitate the missing specialist's final prompt.

If the user asks whether a frame can move forward, enter Seedance, be repaired, or should be redesigned, include a concise production-readiness note after the visual diagnosis. Keep it practical: name the blocker, then point to `aigc-image-edit-prompt` for repair prompts or `aigc-seedance-prompt` when the user has decided to proceed.

## Workflow

CHECKPOINT - Diagnosis Scope:

- If no image or frame is available, ask the user to upload one before diagnosing.
- If the user asks whether it can move forward, enter video, be repaired, or should be redesigned, give a short readiness judgment and name the next practical step.
- If the user asks for a ready image-edit prompt in the same turn, diagnose first, then hand off only the high-impact repair summary to `aigc-image-edit-prompt`.
- If the user asks for a Seedance prompt, do not write it here; provide the diagnosis summary and route to `aigc-seedance-prompt` only when the user has already decided to proceed.

### Failure Branches

Apply this table before the normal diagnosis. Never invent evidence to fill an unavailable or unreadable image region.

| Trigger | First response | If still unresolved |
|---|---|---|
| No image or frame is available | Ask for the actual image or frame. | If upload is impossible, label the response `text-only assumption check`, request visible facts, and do not claim a visual diagnosis. |
| The image is too small, blurred, cropped, or blocked | Name exactly what cannot be verified and request the original or a useful crop. | Restrict findings to readable evidence and omit any affected lens. |
| Two creative intentions would produce different rankings | State the most likely assumption and ask one question. | If the user cannot clarify, proceed under the stated assumption and mark the verdict provisional. |
| Multiple frames are unlabeled or their roles are unclear | Label them A/B in input order and state the assumed role of each. | Ask for the mapping before recommending which frame to keep. |
| The stated intent has no visible functional failure | Say that the frame works for that intent and separate optional taste refinements. | Do not manufacture three problems to satisfy the output template. |
| The problem is concept-level rather than visual execution | Name the missing shot purpose and ask for it before diagnosing execution. | Without a purpose, stop at the missing-intention diagnosis. |
| The user asks for a final repair or Seedance prompt | Finish the diagnosis and provide only the handoff summary. | Route to the named specialist; if unavailable, stop at the summary. |

#### Production Intervention Gate

When the user asks whether to proceed, repair, or redo, compare the intended use with the current frame's structural support:

- **`can proceed`**: composition, subject scale, pose or silhouette, spatial geometry, and identity already support the intended use; remaining issues are optional refinements.
- **`repair first`**: the same composition, pose, and spatial logic remain usable; blockers are localized to anatomy cleanup, material, lighting, hierarchy, artifacts, or another bounded region.
- **`redesign first`**: the intended use requires rebuilding subject scale or position, pose or silhouette, camera relationship, spatial layout, or motion supports. Preserve any working world, palette, identity, or style, but do not call a structural rebuild a repair.

Give one decisive blocker with the verdict. Do not default to `repair first` merely because it is less disruptive. If the visible evidence cannot support the choice, say that the verdict is unavailable and request the missing crop or frame.

### 1. Read the Frame Neutrally

Describe what is actually visible before judging:

- Subject, action, pose, expression, and blocking.
- Composition, shot size, angle, depth layers, and visual hierarchy.
- Light direction, contrast, softness/hardness, and apparent source.
- Color palette, saturation, temperature, and where color attention sits.
- Production design: costume, props, environment, material, era, and texture.
- Mood read: what emotion the image currently communicates.

If no image is available, ask the user to upload the image or frame. If the user can provide only text, treat the response as a text-only creative assumption check, not as visual diagnosis.

### Diagnosis Depth Budget

Use the smallest diagnosis that teaches the decisive issue:

- **Quick diagnosis**: 3-5 sentences plus the top 3 problems.
- **Standard diagnosis**: neutral read, likely intent, relevant lenses, top 3 problems, and next suggestion.
- **Deep diagnosis**: use only when the user asks for a full breakdown, comparison, grading, or art-direction analysis.

Do not force all five lenses into the final answer when only two contain decisive findings. If production readiness is requested, keep it to a short next-step note after the diagnosis.

### 2. Infer the Intended Effect

State the likely creative intention in one sentence. If the intention is unclear, say so and offer the most likely assumption. Do not over-question unless the image could support two very different creative goals.

### 3. Diagnose Through Five Lenses

Use concise, specific observations. Cover only lenses with real findings in the final answer; do not force all five lenses into equal-length sections.

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

Read `references/production-design-dimensions.md` only when the image shows art-direction, material, world-coherence, character-silhouette, prop, or subject-environment hierarchy problems. Do not load it for ordinary exposure, grading, lens, or composition issues.

### 5. Choose the Next Handoff

- If the user wants to understand the problem only, stop after diagnosis and next steps.
- If they want an image-to-image repair prompt, hand off to `aigc-image-edit-prompt`.
- If they want the frame to become a Seedance video shot, hand off to `aigc-seedance-prompt` only when the user has already decided to proceed.
- If the concept itself is weak, state the missing shot purpose and ask for it before recommending repairs.
- If the user asks after diagnosis `能不能用`, `能不能进视频`, `下一步是什么`, or `该修图还是重做`, answer with a concise next-step note and pass the diagnosis summary to `aigc-image-edit-prompt` or `aigc-seedance-prompt` when useful.

## Output Structure

Use this structure by default:

```markdown
## 画面观察
[Neutral read of the frame.]

## 可能的创作意图
[What the image appears to be trying to do.]

## 五类诊断
[Only the lenses that contain real findings. If the user asks for a full breakdown, include all five lenses.]

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

If the next user turn becomes a production-routing question, use this response pattern:

```markdown
这是生产推进问题，先给一个轻量判断：
- Next step: [can proceed / repair first / redesign first]
- Reason: [single decisive blocker or enabling condition]

可交接的诊断摘要：
- Preserve: [what works]
- Main blockers: [top issues]
- Risk: [why this may block progress]
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
- Do not use Green/Yellow/Red production labels; use plain next-step wording.
- Do not list every possible flaw with equal weight.
- Do not say only "add cinematic lighting", "improve composition", or other generic fixes.
- Do not treat every image as live-action cinema; animation, stylized art, and commercial visuals have their own standards.
- Do not turn the whole answer into a production checklist; keep readiness notes secondary to the visual diagnosis.
- Do not turn a diagnosis into a ready prompt unless the user explicitly asks for the next prompt.
