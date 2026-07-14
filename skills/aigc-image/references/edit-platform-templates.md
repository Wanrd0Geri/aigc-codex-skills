# 提示词模板 / Prompt Templates

This file provides version-tolerant prompt structures for **Nano Banana/Gemini image editing** and **ChatGPT/OpenAI GPT Image editing**. Both families accept a source image plus natural-language edit instructions. Keep the stable shared rule: identify the exact change, state what must remain unchanged, and describe how the edited area should integrate. Do not hardcode prompt-length limits or claim that one provider inherently follows numerical values, bilingual text, or negative lists better unless the user provides current evidence.

Default to **bilingual (Chinese + English)** versions unless the user asks for one language only. They are semantic mirrors, not literal translations.

---

## Universal structure: `[Preserve] / [Transform] / [Avoid]`

Use this three-block grammar as this skill's delivery format. It is not vendor-required syntax; its purpose is to make the change set auditable:

```
[Preserve] What must NOT change about the source image
[Transform] What SHOULD change, with task-appropriate visible directives
[Avoid] What the model should actively NOT introduce (negative prompt)
```

Use this structure to separate locked source facts from authorized changes. The headings are a working grammar, not permission to populate every category.

### Natural directive style

The block format is structural, but the lines inside it should read like clear editing instructions. Apply the natural-language rules embedded in `aigc-image`: visible subjects, actions, locations, and results. Avoid both extremes: a poetic paragraph with no constraints, or a keyword pile that ignores the source image.

Good edit directives usually name:

- **where** the change appears: face side, costume edge, background layer, foreground haze, window light, ground shadow
- **what** changes: direction, hardness, color temperature, density, contrast, saturation, material response
- **what must remain stable**: identity, pose, composition, character count, prop shape, clean surface quality
- **visible result**: subject integrates with environment, depth separates layers, shadows stop looking milky, highlights stop clipping

Rewrite parameter-like lines before output:

- Weak: `cinematic lighting, dramatic contrast, premium atmosphere`
- Better: `Replace the flat front light with one soft key from camera-left, deepen the background shadows, and keep the face readable with a narrow warm fill.`
- Weak: `高级电影感，氛围更强，质感更好`
- Better: `把正面平光改为画面左侧的柔和主光，背景阴影压深，人物面部保留可读的暖色补光，让主体和环境光线统一。`

Use this style for both Chinese and English prompts. They do not need literal word-for-word translation, but they must preserve the same edit intent and protection boundaries.

---

## Nano Banana / Gemini template

Use a descriptive edit request tied to the supplied image. Name the specific element to change, describe how it should fit the source's style, lighting, perspective, or material logic, and explicitly keep everything else unchanged. For multiple input images, identify each image by role instead of assuming their order is self-explanatory.

Keep the request focused. Use numbers only when the user supplied them or a measurable boundary prevents ambiguity; do not add percentages, IRE values, or hex codes merely to make the prompt look precise.

### Template — English version

```
Edit the provided source image. Apply only the requested visible changes and preserve every unmentioned element.

[Preserve]
- All character faces, hair, and identifying features — do not redraw faces
- Costume design, fabric patterns, accessories, and props
- Character poses, blocking, and positions in frame
- Camera angle, focal length, and overall composition
- Number and identity of characters — do not add or remove anyone

[Transform]
- [Authorized edit 1: name the location, visible change, and endpoint]
- [Authorized edit 2]
- [Add only the changes required in this edit pass]

[Avoid]
- [Only the likely drift or addition that would violate this edit]

Output one edited image that applies only the changes above and keeps the protected source facts unchanged.
```

### Template — 中文版

```
编辑所提供的原图。只执行点名的可见修改，所有未提及内容保持不变。

[保留 / Preserve]
- 所有人物面部、发型、识别性特征——不要重绘面部
- 服装设计、面料图案、饰品、道具
- 人物姿势、走位、画面中的位置
- 镜头角度、焦距感、整体构图
- 人物数量与身份——不增减人物

[改造 / Transform]
- [授权修改1：写明位置、可见变化与结束状态]
- [授权修改2]
- [只保留本轮编辑真正需要的修改]

[避免 / Avoid]
- [只写最可能违反本次编辑边界的漂移或新增项]

输出一张编辑后的单图，只应用上述修改，并保持受保护的原图事实不变。
```

---

## ChatGPT / OpenAI GPT Image template

Use explicit `change only X` and `keep Y unchanged` instructions. For identity-, geometry-, layout-, brand-, or text-sensitive edits, repeat the protected facts in each new iteration if drift appears. Keep platform/API parameters such as quality, size, output format, mask, or input fidelity outside a paste-ready visual prompt unless the user explicitly asks for API settings.

Prefer a clean base edit followed by small single-change iterations over one overloaded prompt. The adaptive surface-cleanliness section below is a local repair heuristic; invoke it only when the source or requested style actually shows that failure.

### Adaptive surface cleanliness controls — local/eval-derived heuristic

This section records a local observed failure pattern, not vendor-documented model behavior. Use it only when the image or user complaint points to **碎裂感 / fragmented rendering**: broken edges, noisy surfaces, visible brush texture, painterly buildup, random ornament density, gritty micro-detail, or concept-art patchwork. Do **not** paste the whole list by default. Choose the smallest set that fixes the diagnosed problem.

**Level 0 — omit**
Use no texture-control terms when the source already has clean surfaces and the edit only needs light, grade, depth, or subject integration.

**Level 0.5 — clean source, preventive guard**
Use this when the uploaded source image is already clean, but the edit target or model family may add unwanted micro-texture. Keep it as a light preserve/transform instruction, not a heavy negative list:

```
Preserve the source image's clean surface quality and clear large shapes. Do not add unnecessary micro-detail or fragmented texture.
```

Chinese equivalent:

```
保留原图干净的表面质感和清晰的大形结构，不要额外增加不必要的微细节或碎片化纹理。
```

Do not add `no painterly texture`, `no visible brush strokes`, or the full Level 2/3 negative list unless fragmentation is already visible or strongly likely from the requested style change.

**Level 1 — mild cleanup**
Add 1-2 positive terms to `TRANSFORM`:

```
clear large shapes
clean smooth surfaces
soft natural shading
simple material planes
```

Chinese equivalents:

```
清晰的大形结构
干净平滑的表面
柔和自然的明暗过渡
简洁的材质块面
```

**Level 2 — visible fragmentation**
Add 2-3 positive terms and 1-3 targeted negatives:

```
low micro-detail
minimal texture
smooth rendering
no fragmented details
no visible brush strokes
no noisy surface patterns
```

Chinese equivalents:

```
降低微细节密度
最小化纹理噪声
平滑干净的渲染
不要碎片化细节
不要可见笔触
不要随机表面噪纹
```

**Level 3 — severe broken/painterly texture**
Use one compact surface directive plus targeted negatives:

```
Surface cleanliness: preserve clear large shapes, clean smooth surfaces, simple material planes, soft natural shading, low micro-detail, and smooth rendering.

NEGATIVE: painterly texture, visible brush strokes, fragmented details, noisy surface patterns, excessive micro-texture, gritty concept-art texture.
```

Chinese equivalent:

```
表面控制：保留清晰的大形结构、干净平滑的表面、简洁材质块面、柔和自然明暗、低微细节密度和平滑渲染。

负面词：绘画化纹理、可见笔触、碎片化细节、随机表面噪纹、过度微纹理、粗粝概念图质感。
```

Before adding surface-control terms, remove or replace prompt words that push the opposite direction: `masterpiece`, `ultra detailed`, `highly detailed`, `intricate`, `dramatic texture`, `cinematic texture`, `painterly`, `concept art`, `artstation`, `gritty`. Use `volumetric`, `moody`, or `cinematic` only when anchored to a concrete visual technique, e.g. `gentle atmospheric depth`, `single soft directional key`, or `clean cinematic composition`.

### Template — English version

```
Image edit task. Preserve the protected source facts and apply only the requested visible changes.

PRESERVE EXACTLY:
- Character faces, hair, costumes, props, poses, positions, camera angle, composition, character count

TRANSFORM:
- [Authorized edit 1: location, visible change, endpoint]
- [Authorized edit 2]
- [Use only the directives required in this edit pass]

AVOID:
- [Only the likely drift or addition that would violate this edit]
```

### Template — 中文版

```
图像编辑任务。保留受保护的原图事实，只执行本次点名的可见修改。

严格保留：
- 人物面部、发型、服装、道具、姿势、位置、镜头角度、构图、人物数量

改造：
- [授权修改1：位置、可见变化与结束状态]
- [授权修改2]
- [只保留本轮编辑真正需要的修改]

避免：
- [只写最可能违反本次编辑边界的漂移或新增项]
```

---

## Final quality checks before outputting

Before delivering the prompt to the user, verify:

1. **Preservation block names the critical invariants.** List identity, geometry, layout, text, brand, or material facts that would be costly to lose, then use `keep every other unmentioned element unchanged` as a catch-all.
2. **Transformation block is focused.** Keep only the highest-impact changes for this pass; split many independent changes into later iterations.
3. **Each transformation directive uses task-appropriate visible language.** Use cinematography vocabulary only for cinematic or lighting work; use material, surface, geometry, typography, or product language for those edit types.
4. **Avoid controls match real drift risk.** State the desired positive visible result first. Add a short targeted exclusion only when it prevents a likely violation of the edit boundary; do not dump generic negatives.
5. **Both Chinese and English versions exist and say the same thing semantically.** Do not omit one.
6. **The prompt reads as natural edit language, not keyword stuffing.** Each directive should connect the edit target, the visual change, and the intended result.
7. **The prompt would make sense to a real cinematographer.** If you wouldn't dare show it to a DP, it's still too vague.
8. **Surface cleanliness terms are adaptive.** If fragmented rendering is not part of the diagnosis, omit clean/smooth/no-texture terms. If the source is clean but the edit may introduce fragmentation, use Level 0.5. If fragmentation is already visible, choose Level 1, 2, or 3 instead of dumping every negative word into the prompt.
9. **Conservative scopes stay closed.** When the user says `只/仅/保持/不要重做/不要电影感`, every transform line must map to a named request; remove cinematic grade, depth, atmosphere, or styling that was not requested.
10. **Exact text stays exact.** Quote protected label copy verbatim in both languages and keep spelling, count, placement, hierarchy, and legibility unchanged.
