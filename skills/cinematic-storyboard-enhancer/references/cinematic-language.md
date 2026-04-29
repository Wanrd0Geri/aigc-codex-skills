# 电影语言术语库 / Cinematic Vocabulary Library

The point of this file: **specific cinematography terms beat generic adjectives** when prompting Nano Banana series and ChatGPT image editor series. "Make it moody" is interpreted dozens of ways. "Low-key 1:8 lighting ratio with crushed blacks" gives a precise target.

When writing the transformation prompt, reach for terms from this file rather than inventing your own.

---

## Lighting / 光线

### Lighting style names / 光线风格命名

| English | 中文 | What it means |
|---|---|---|
| Low-key lighting | 低调布光 | Predominantly dark image, small areas of light, high contrast (noir, horror, drama) |
| High-key lighting | 高调布光 | Bright overall, low contrast (commercial, comedy, romance) |
| Chiaroscuro | 明暗对比法 | Dramatic light/dark contrast, often with single source (Caravaggio-like) |
| Rembrandt lighting | 伦勃朗布光 | Triangle of light on cheek opposite the key, classical portrait |
| Split lighting | 分割布光 | Half face lit, half in shadow, side key |
| Motivated lighting | 动机光 | Light has a visible source in scene (window, lamp, fire) |
| Practical lighting | 现场光 | Light from props in the scene itself |
| Natural lighting | 自然光 | Sun, moon, fire — no artificial fill |
| Available light | 现场可用光 | Whatever light is naturally present, no setup |

### Light direction / 光线方向

| English | 中文 |
|---|---|
| Top light / overhead key | 顶光 |
| Side light / cross light | 侧光 |
| Backlight / kicker | 逆光 / 轮廓光 |
| Rim light / edge light | 边缘光 |
| Front light / camera-axis light | 正面光 |
| Three-quarter front | 前侧光 |
| Three-quarter back | 后侧光 |
| Underlight / horror light | 底光 |

### Light hardness / 光线硬度

| English | 中文 |
|---|---|
| Hard light (sharp shadow edges) | 硬光 |
| Soft light (gradual falloff) | 柔光 |
| Diffused light | 散射光 |
| Specular highlight | 高光镜面反射 |
| Wrap-around light | 环绕光 |

### Lighting ratio / 光比

Use specific numerical ratios. They translate well across both models.

- 1:1 — flat, no contrast (high-key)
- 1:2 — gentle, soft drama
- 1:4 — standard cinematic
- 1:8 — strong drama, moody
- 1:16 — extreme contrast, noir territory

In Chinese: "光比 1:8" reads correctly to both models.

---

## Color grading / 调色

### Common cinema looks / 常见电影色调

| English | 中文 | Description |
|---|---|---|
| Teal and orange | 青橙调 | Cool shadows, warm skin — the modern blockbuster default |
| Bleach bypass | 漂白工艺 | Desaturated, high-contrast, silver retention look |
| Cross-process | 反转冲洗 | Shifted complementary colors, vintage |
| Day-for-night | 日转夜 | Cool blue tint with crushed shadows simulating moonlight |
| Golden hour | 黄金时刻 | Warm, low-angle, long shadows |
| Blue hour | 蓝色时刻 | Cool, saturated blue, post-sunset |
| Monochromatic | 单色调 | All variants of one hue family |
| Desaturated | 去饱和 | Color present but muted |
| Warm grade | 暖调 | Pushed toward red/orange/yellow |
| Cool grade | 冷调 | Pushed toward blue/cyan/teal |

### Specific palette descriptions / 具体调色板描述

When you can, give *exact* palette anchors:

- "Cool blue-cyan palette, hex range #1a2832 to #4a6878 in shadows, #8aa8b8 in highlights"
- "Monochromatic teal grade, no warm tones permitted, skin shifted slightly cool"
- "Desaturated palette at ~40% saturation, with one accent color preserved at full saturation"

### Black point / 黑位 vocabulary

| English | 中文 |
|---|---|
| Crushed blacks | 压黑 / 黑位下沉 |
| Lifted blacks (faded) | 提黑 / 灰雾感 |
| True black point | 纯黑点 |
| Inky shadows | 浓墨般的阴影 |
| Milky shadows (negative) | 灰朦朦的阴影（贬义） |

### Highlights / 高光 vocabulary

| English | 中文 |
|---|---|
| Protected highlights | 保护高光 |
| Rolled-off highlights | 平滑高光过渡 |
| Clipped highlights (negative) | 高光过曝 |
| Specular peaks | 高光反射点 |
| Bloom / glow | 高光弥散 |

---

## Atmosphere / 氛围

| English | 中文 |
|---|---|
| Atmospheric haze | 大气雾感 |
| Volumetric fog | 体积雾 |
| God rays / light shafts | 神光 / 光束 |
| Mist | 薄雾 |
| Smoke | 烟 |
| Depth gradient | 景深渐变 |
| Atmospheric perspective | 空气透视 |
| Particulates in light | 光中浮尘 |

**Important:** "God rays" / "神光" should usually be *reduced* not added when fixing wuxia/cinematic shots — they're an AI-image cliche. Replace with "subtle volumetric haze" or "soft moonlight diffusion" instead.

---

## Camera & lens / 镜头语言

| English | 中文 |
|---|---|
| Anamorphic lens look | 变形宽银幕镜头感 |
| Anamorphic flare (horizontal blue streak) | 变形镜头眩光（横向蓝色光斑） |
| Shallow depth of field | 浅景深 |
| Deep focus | 深焦 |
| Wide-angle distortion | 广角畸变 |
| Telephoto compression | 长焦压缩 |
| Bokeh | 焦外散景 |
| Lens vignetting | 镜头暗角 |
| Chromatic aberration | 色散 |
| Film grain | 胶片颗粒 |

---

## Film stock & medium / 胶片质感

| English | 中文 |
|---|---|
| 35mm film grain | 35毫米胶片颗粒 |
| Kodak Portra look (warm, soft skin) | 柯达 Portra 风格 |
| Kodak Vision3 (cinema stock) | 柯达 Vision3 电影胶片 |
| Fujifilm Eterna (muted, soft) | 富士 Eterna 风格 |
| Halation (red glow around highlights) | 光晕（高光红色弥散） |
| Cinematic color science | 电影级色彩科学 |

---

## Mood-to-technique translation table

When the user says... reach for these techniques:

| User says | Cinematography translation |
|---|---|
| "More cinematic" / "电影感" | Low-key lighting, controlled black point, single key with motivation, anamorphic aspect ratio, film grain |
| "More moody" / "氛围感" | Lifted contrast, atmospheric haze with depth, single warm or cool source, large negative space |
| "Less flat" / "不要这么平" | Increase lighting ratio, add black point, add atmospheric depth gradient, add rim light to subjects |
| "Lights are messy" / "光太乱" | Reduce to one motivated key, demote others to fill, unify color temperature |
| "Subject doesn't fit" / "人物没融入" | Add matching rim/edge light from environment key, shift subject shadow tone toward environment ambient |
| "Too bright" / "太亮了" | Lower exposure 1-2 stops, crush blacks, protect highlights, reduce haze brightness |
| "Wrong era feel" / "时代感不对" | Specify film stock emulation (Vision3 / Portra / black-and-white), add appropriate lens character |

---

## Words to AVOID in prompts

These read as noise to both models:

- "Beautiful" / "美丽" — meaningless
- "Stunning" / "惊艳" — meaningless
- "Masterpiece" / "杰作" — overused, no signal
- "8K" / "Ultra HD" — doesn't change cinematography
- "Trending on Artstation" — outdated and ineffective on these models
- "Hyperrealistic" — usually pushes toward uncanny
- "Award-winning" — meaningless
- Generic emotion words without technique ("epic", "magical", "dramatic") — pair with technique or drop

When you find yourself reaching for these, replace them with a specific technique from the tables above.
