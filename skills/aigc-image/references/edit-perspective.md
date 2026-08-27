# Perspective capability

Use to repair convergence, horizon, foreshortening, projection, or an inserted element whose perspective conflicts with the base image.

## Evidence gate

Identify readable horizontal and vertical structure, ground plane, dominant vanishing direction, target object, and intended camera relation. If the image intentionally uses a Dutch angle, fisheye distortion, miniature projection, or stylized geometry, do not normalize it without authorization.

## Variables

- `[目标对象或结构]`
- `[地平线或主消失方向]`
- `[应保持垂直／平行／汇聚的边线]`
- `[接地平面]`
- `[允许改变的边界]`

## Canonical prompt

```text
图1是唯一底图。只修正[目标对象或结构]的透视，使其边线按照图1现有的[地平线或主消失方向]一致汇聚；让[应保持垂直／平行／汇聚的边线]保持正确关系，并让对象稳定落在[接地平面]上。只在[允许改变的边界]内调整必要的形变、缩短和尺度递减。保持主体身份、物体设计、构图范围、光线、色彩、材质及其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not change lens character, crop, camera height, or composition unless separately authorized.
- Do not straighten an intentional tilt or remove stylized projection by default.
- If structural lines are unreadable, request a clearer source or restrict the edit to the clearly visible target.
