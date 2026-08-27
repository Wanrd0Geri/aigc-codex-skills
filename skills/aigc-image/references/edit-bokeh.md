# Background-bokeh capability

Use for converting existing small highlights behind the focal plane into optical bokeh.

## Evidence gate

Confirm the focal plane, background region, existing highlight count, highlight colors, and protected subject/text areas. No background highlights means no physical bokeh; do not invent point lights.

## Shape rules

- near frame center: mostly circular
- near frame edge: may stretch into ellipses or cat-eye shapes
- polygonal aperture shape only when explicitly requested or established
- translucent centers, softly brighter rims, no hard outlines

Quantity is `[the user-specified count]` or `[a restrained subset of existing highlights]`. Never force seven or another fixed count when the image contains a different usable set.

## Variables

- `[背景区域]`
- `[数量或少量]`
- `[现有亮点颜色]`
- `[主体、产品、文字或标志保护区]`
- `[本轮确定的焦点；若未修改焦点则为原有焦点]`

## Canonical prompt

```text
图1是唯一底图。只在焦平面之后的[背景区域]，将[数量或少量]现有小型亮点转为焦外光斑，不新增亮点或光源。画面中央附近以柔和圆形为主，靠近边缘的光斑可轻微拉伸为椭圆或猫眼形；中心半透明、边缘略亮且没有硬轮廓，颜色只来自原有亮点。所有光斑保持在[本轮确定的焦点；若未修改焦点则为原有焦点]之后，不覆盖[主体、产品、文字或标志保护区]。保持综合色调、曝光、光线方向、构图及其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not place bokeh on the focal subject or convert unrelated objects into lights.
- Do not use uniform size, grid distribution, hard circles, or arbitrary rainbow colors.
- If the focal plane is undefined, establish focus first. If highlights are absent, omit bokeh or request a stylized overlay authorization.
