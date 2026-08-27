# Color grade and temperature capability

Use to change whole-image or local hue relationships, white balance, saturation hierarchy, or color temperature without changing scene content or light geometry. Use `edit-palette-transfer.md` instead when a semantic palette card supplies the target colors.

## Evidence gate

Identify the target region, current grade, desired warm/cool relationship, protected local colors, luminance hierarchy, and whether a reference image is authorized for color only. If the request says only `更好看` or `更电影`, diagnose the intended color relationship instead of choosing a genre palette.

## Variables

- `[全画面或局部区域]`
- `[目标综合色调、白平衡、色温或饱和度关系]`
- `[必须保持的固有色]`
- `[必须保持的明暗与光线关系]`

## Canonical prompt

```text
图1是唯一底图。只调整[全画面或局部区域]的色彩关系，使其呈现[目标综合色调、白平衡、色温或饱和度关系]；保持[必须保持的固有色]可辨识，并让暗部、中间调和高光之间的颜色变化连续。保持[必须保持的明暗与光线关系]、人物、物体、构图、几何、材质、天气、时间及其余未提及内容不变。
```

For a color-only reference, state that the reference owns only the named grade, temperature, or saturation relationship and contributes no content, layout, texture, lighting direction, or shadow geometry.

## Prohibited drift and fallback

- Do not default to teal-orange, cold night, warm sunset, lifted blacks, crushed blacks, or a named film look.
- Do not change exposure hierarchy, light direction, shadow shape, material identity, weather, or time unless separately authorized.
- If the desired color endpoint is materially ambiguous, show the source-supported alternatives and ask which one wins.
