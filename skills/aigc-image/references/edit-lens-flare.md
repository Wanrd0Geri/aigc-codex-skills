# Lens-flare capability

Use only when a strong visible or clearly motivated source enters the lens, faces the camera, or sits near the frame edge.

## Evidence gate

Identify the source, its screen position, source-to-frame-center axis, foreground occluders, and protected focal details. A bright object that does not face the lens may support halo but not lens flare.

## Shape rules

Choose one coherent artifact family:

- circular or flattened ghost discs for a compact source
- mildly polygonal ghosts only when an aperture-shaped treatment is requested or visibly established
- one restrained horizontal streak only when an anamorphic treatment is requested or established

Default quantity is `[one to three restrained artifacts]`, limited by the source and empty image area. Never freeze the count when the actual frame supports a different amount.

## Variables

- `[现有强光源]`
- `[数量]`
- `[圆形／扁椭圆／轻微多边形／单条水平光带]`
- `[允许分布范围]`
- `[受保护区域]`

## Canonical prompt

```text
图1是唯一底图。以[现有强光源]为唯一来源，沿光源与画面中心的连线，在[允许分布范围]内添加[数量]个克制的[形状]镜头光斑。光斑保持半透明、低对比度和柔和边缘，颜色只轻微继承光源；经过前景物体时按实际遮挡关系自然中断。不得覆盖[受保护区域]，不得新增发光体；保持原有曝光、综合色调、白平衡、光线方向、构图、主体及其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not mix disc ghosts, aperture polygons, rainbow streaks, and anamorphic bars by default.
- Do not use decorative floating spots unrelated to the optical axis.
- If the source does not support flare, route to halo or lighting repair; require explicit authorization for a non-physical overlay.
