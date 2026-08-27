# Semantic palette-card capability

Use to turn one readable image into a reusable positional color card. The default is twelve colors because semantic role mapping matters more than adding unassigned swatches.

## Evidence gate

Confirm that the source exposes enough dark, local-color, and light information to distinguish the twelve roles. If the image is monochrome, clipped, heavily compressed, or contains fewer meaningful roles, preserve repeated or near-related roles instead of inventing unrelated colors.

## Fixed 3 x 4 map

| Row | Left to right |
| --- | --- |
| 1: dark structure | black point; deep shadow; ordinary shadow; shadow tint |
| 2: local color | environment dominant; subject or main-object local color; secondary color; atmospheric midtone |
| 3: light structure | ambient light; key light; soft highlight; peak accent |

When no person is present, `subject local color` means the main building, product, prop, creature, or natural subject.

## Canonical prompt

```text
以图1的实际色彩为唯一来源，生成一张三行四列的十二色语义调色色卡。

第一行从左到右：黑位色、深暗部色、普通阴影色、暗部偏色。
第二行从左到右：环境主色、主体或主要物体的固有色、辅助色、大气中间调色。
第三行从左到右：环境光色、主光色、柔和高光色、峰值强调色。

每个色块大小一致、边界清楚、无纹理。色块位置严格对应上述职责；不改变排列顺序，不添加渐变、阴影、装饰、人物、物体、场景、文字、标志或未经真实采样的 HEX／RGB 数值。
```

## Boundary

This creates a semantic visual card, not measured color data. If exact codes are required, use deterministic pixel sampling outside the image model and report the method. Do not claim image-model-generated HEX or RGB values are measured samples.
