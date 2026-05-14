# 提示词模板 / Prompt Templates

This file specifies the current prompt structure for **Nano Banana Pro** and **ChatGPT Images 2.0**. Treat later Nano Banana, Gemini image editor, ChatGPT image editor, or OpenAI image editor versions as the closest matching family unless the user provides newer constraints. They solve the same image-editing task, but they respond best to different prompt densities and vocabulary.

Always output **bilingual (Chinese + English)** versions. They are semantic mirrors, not literal translations.

---

## Universal structure: `[Preserve] / [Transform] / [Avoid]`

Both models respond to this three-block edit grammar. The blocks should always be in this order:

```
[Preserve] What must NOT change about the source image
[Transform] What SHOULD change, with specific cinematography directives
[Avoid] What the model should actively NOT introduce (negative prompt)
```

This structure outperforms freeform prose for image-editing tasks on both models because it gives them an explicit lock-list before the creative directives.

---

## Nano Banana Pro template

Nano Banana Pro (Google's `gemini-3-pro-image` family) is **conversational** — it parses natural language well, handles longer prompts (up to ~4000 tokens) without losing focus, and responds excellently to numerical specificity (light angles, ratios, IRE values, hex codes).

**Strengths to lean into:**
- Long, structured prompts
- Numerical precision (degrees, ratios, percentages)
- Explicit preservation instructions
- Multiple sequential directives in one block
- Bilingual prompts (it actually handles mixed Chinese-English well)

**Weaknesses to work around:**
- Can over-interpret single descriptive adjectives ("dramatic" might trigger over-the-top changes)
- Sometimes adds details not requested if the prompt feels "incomplete"

### Template — English version

```
Edit this image with the following cinematic adjustments. Preserve the source faithfully where specified.

[Preserve]
- All character faces, hair, and identifying features — do not redraw faces
- Costume design, fabric patterns, accessories, and props
- Character poses, blocking, and positions in frame
- Camera angle, focal length, and overall composition
- Number and identity of characters — do not add or remove anyone

[Transform]
- Lighting: [specific direction, hardness, source, ratio]
- Color grade: [specific palette, temperature, saturation level]
- Black point: [crushed / lifted / specific IRE]
- Atmosphere: [haze density, depth gradient, color]
- Subject integration: [rim light direction and color, shadow temperature shift]
- Overall exposure: [stops adjustment, midtone target]

[Avoid]
- [Specific issues from the diagnosis — e.g., "intense god rays", "green or yellow tint in atmosphere", "blown-out highlights", "uniform fog"]
- Generic AI-image artifacts: oversaturation, plastic skin, symmetrical lighting

Output: a single edited image preserving subject identity while applying the cinematographic transformations above.
```

### Template — 中文版

```
按以下电影级调整对此图进行编辑。在指定保留项上忠实于原图。

[保留 / Preserve]
- 所有人物面部、发型、识别性特征——不要重绘面部
- 服装设计、面料图案、饰品、道具
- 人物姿势、走位、画面中的位置
- 镜头角度、焦距感、整体构图
- 人物数量与身份——不增减人物

[改造 / Transform]
- 光线：[具体方向、硬度、光源、光比]
- 调色：[具体色板、色温、饱和度]
- 黑位：[压黑 / 提黑 / 具体 IRE 值]
- 氛围：[雾感浓度、景深渐变、颜色]
- 主体融入：[轮廓光方向与颜色、阴影色温偏移]
- 整体曝光：[档位调整、中间调目标值]

[避免 / Avoid]
- [来自诊断的具体问题——如"强烈神光柱"、"大气中的绿色/黄色色调"、"过曝高光"、"均匀雾气"]
- 通用 AI 图像问题：过饱和、塑料质感皮肤、对称布光

输出：一张编辑后的单图，保留主体身份的同时应用上述电影级改造。
```

---

## ChatGPT Images 2.0 template

ChatGPT Images 2.0 (the ChatGPT image editor / OpenAI image surface) is more **intent-oriented** — it does best with clear preservation constraints, concise transformation goals, and a focused negative list. Treat "GPT image 2.0", "GPT image", "OpenAI image", and "ChatGPT image editor" as aliases for this template.

**Strengths to lean into:**
- Clear edit intent in natural language
- Named techniques and named DPs/film stocks when they sharpen the target
- Compact, high-density directives
- Direct preserve/transform contrast
- Strong negative prompt response

**Weaknesses to work around:**
- Can drift if given too many transformation directives
- Numerical values (IRE, degrees, hex codes) help less than they do for Nano Banana Pro — prefer named ratios and plain-language visual outcomes
- Can over-stylize if given too many evocative adjectives
- Can create fragmented, over-textured rendering when prompts pile up "detailed", "painterly", "concept art", "volumetric", or gritty atmosphere language

### Adaptive surface cleanliness controls

Use this only when the image or user complaint points to **碎裂感 / fragmented rendering**: broken edges, noisy surfaces, visible brush texture, painterly buildup, random ornament density, gritty micro-detail, or concept-art patchwork. Do **not** paste the whole list by default. Choose the smallest set that fixes the diagnosed problem.

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
Image edit task. Preserve subject identity; transform cinematography only.

PRESERVE EXACTLY:
- Character faces, hair, costumes, props, poses, positions, camera angle, composition, character count

TRANSFORM:
- Lighting: [single named technique, e.g., "low-key Rembrandt key from camera-left, soft moonlight motivated"]
- Grade: [named palette, e.g., "monochromatic cool teal, day-for-night style"]
- Contrast: [named ratio, e.g., "1:8 dramatic ratio with crushed blacks"]
- Atmosphere: [named effect, e.g., "atmospheric haze with depth gradient, foreground clear, background dissolved"]
- Subject integration: [named technique, e.g., "cool blue rim light tying subjects to environment key"]

NEGATIVE:
- god rays, green tint in atmosphere, lifted milky shadows, blown highlights, plastic skin, oversaturation, uniform fog wall, multiple competing keys

Style reference: [optional — name a DP, film, or stock if it sharpens the target, e.g., "Roger Deakins / Wong Kar-wai night palette / Kodak Vision3 250D emulation"]
```

### Template — 中文版

```
图像编辑任务。保留主体身份，仅改造摄影语言。

严格保留：
- 人物面部、发型、服装、道具、姿势、位置、镜头角度、构图、人物数量

改造：
- 光线：[一个具名技法，如"低调伦勃朗式布光，摄影机左侧软光月光为动机"]
- 调色：[具名色板，如"单色冷青调，日转夜风格"]
- 对比：[具名光比，如"1:8 戏剧性光比，黑位下沉"]
- 氛围：[具名效果，如"具有景深渐变的大气雾感，前景清晰，背景溶解"]
- 主体融入：[具名技法，如"冷蓝轮廓光将主体与环境主光绑定"]

负面词：
- 神光柱、大气中的绿色色调、灰朦朦的提黑阴影、过曝高光、塑料皮肤、过饱和、均匀的雾墙、多个竞争性主光

风格参考：[可选——若能锐化目标，可指定摄影师、电影、胶片，如"Roger Deakins / 王家卫夜景调色 / 柯达 Vision3 250D 模拟"]
```

---

## Worked example — wuxia night forest scene

This is the example case the skill was originally built around. Use it as a calibration reference.

### Diagnosis summary
Source image: two riders in foggy forest, but image was over-bright with strong god rays, green-tinted fog, lifted blacks, and subjects lit independently from the scene.

### Nano Banana Pro prompt (English)

```
Edit this image with the following cinematic adjustments. Preserve the source faithfully where specified.

[Preserve]
- All character faces, hair, robes, sword pommels, and Tang-dynasty styling
- Both foreground riders' poses and the bay horses' postures
- Background figures (the standing woman, the rider in blue, the standing figure on right edge)
- Camera angle, framing, and the layered depth composition

[Transform]
- Lighting: replace the strong overhead god ray shafts with diffuse cool moonlight from upper-left at roughly 30 degrees, soft falloff, single motivated key
- Color grade: unified cool blue-cyan palette, monochromatic, remove all green and yellow tints from atmosphere and shadows; shift skin tones slightly cool
- Black point: crush blacks deeply, true black at IRE 0-10, no lifted shadows
- Atmosphere: keep haze but reduce its brightness by 50%, give it depth gradient — foreground crisp, midground softly veiled, background dissolved into darkness
- Subject integration: add subtle cool blue rim light on both foreground riders' shoulders and horse manes from the upper-left moonlight direction
- Overall exposure: push the whole image 1.5 stops darker, target a low-key night-scene exposure

[Avoid]
- Bright god ray shafts (the original's biggest problem)
- Green or yellow tint anywhere in the fog or shadows
- Bright glowing fog that flattens depth
- Lifted milky shadows
- Multiple competing light sources

Output: a single edited image, low-key wuxia night forest cinematography, subjects fully integrated into the cool moonlight.
```

### ChatGPT Images 2.0 prompt (English)

```
Image edit task. Preserve subject identity; transform cinematography only.

PRESERVE EXACTLY:
- Both foreground riders' faces, hair, robes, horses, poses
- Background figures and their positions
- Camera angle and composition

TRANSFORM:
- Lighting: single soft moonlight key from upper-left, motivated, no god rays
- Grade: monochromatic cool teal day-for-night palette, all green removed
- Contrast: 1:8 dramatic ratio with crushed blacks
- Atmosphere: depth-graded haze, foreground clear background dissolved, haze 50% darker than source
- Subject integration: cool blue rim light on riders matching the moonlight direction

NEGATIVE:
- god rays, light shafts, green tint, yellow tint, lifted shadows, bright fog, multiple keys, oversaturation

Style reference: Wong Kar-wai night photography meets wuxia cinematography — Christopher Doyle's cool-blue forest sequences.
```

These two prompts targeting the same image will produce slightly different results — Nano Banana Pro will hew closer to numerical specs, while ChatGPT Images 2.0 will usually follow concise natural-language edit intent more reliably. Recommend the user try both only when they asked for compatibility or comparison.

---

## Final quality checks before outputting

Before delivering the prompt to the user, verify:

1. **Preservation block is specific.** "Preserve everything else" is too vague — name the things that matter.
2. **Transformation block has 3-7 directives, not 12.** More than 7 = model loses focus. Pick the highest-leverage from the diagnosis.
3. **Each transformation directive uses vocabulary from `cinematic-language.md`.** No vague mood words.
4. **Negative prompt directly mirrors the diagnosis's ❌ findings.** Don't list generic negatives — list the specific issues this image has.
5. **Both Chinese and English versions exist and say the same thing semantically.** Do not omit one.
6. **The prompt would make sense to a real cinematographer.** If you wouldn't dare show it to a DP, it's still too vague.
7. **Surface cleanliness terms are adaptive.** If fragmented rendering is not part of the diagnosis, omit clean/smooth/no-texture terms. If the source is clean but the edit may introduce fragmentation, use Level 0.5. If fragmentation is already visible, choose Level 1, 2, or 3 instead of dumping every negative word into the prompt.
