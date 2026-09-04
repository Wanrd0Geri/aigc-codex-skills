# Lens-flare capability

Use only when a strong visible or clearly motivated source enters the lens, faces the camera, or sits near the frame edge.

## Evidence gate

Identify the source, its resolved screen position, source-to-frame-center axis, visibility to the lens, and protected focal details. A bright object alone does not establish a flare-producing incident light path. A source produced or moved by an authorized operation uses the planned state in [edit-operation-state.md](edit-operation-state.md); re-evaluate the axis and incidence after that change.

## IMG-OPTICS-01 — Scene space and imaging space

- Scene objects, particles and participating media obey their world-depth occlusion.
- Lens ghosts/streaks arise within the imaging system. A foreground object blocking the inducing light changes the incident light and may weaken, alter or eliminate flare; do not cut each ghost at foreground silhouettes as though it occupied the scene behind them.
- A user-authorized graphic overlay follows its stated layout and protection constraints. Do not describe that choice as physical evidence.

This does not mean flare ignores all occlusion. Check whether the source-to-lens path is blocked. See [Cambridge in Colour — Understanding Camera Lens Flare](https://www.cambridgeincolour.com/tutorials/lens-flare.htm), especially internal reflection and composition-based source obstruction.

## Shape rules

Choose one coherent artifact family:

- circular or flattened ghost discs for a compact source
- mildly polygonal ghosts only when an aperture-shaped treatment is requested or visibly established
- one restrained horizontal streak only when an anamorphic treatment is requested or established

Default quantity is `[one to three restrained artifacts]`, limited by the source and empty image area. Never freeze the count when the actual frame supports a different amount.

## Variables

- `[本轮确定的强光源及其入镜条件]`
- `[数量]`
- `[圆形／扁椭圆／轻微多边形／单条水平光带]`
- `[允许分布范围]`
- `[受保护区域]`

## Canonical prompt

```text
图1是唯一底图。依据[本轮确定的强光源及其入镜条件]，沿光源与画面中心的连线，在[允许分布范围]内添加[数量]个克制的[形状]镜头光斑。光斑保持半透明、低对比度和柔和边缘，颜色只轻微继承光源；强度随光源进入镜头的光量与遮挡情况变化，不按前景物体轮廓逐段裁断镜头鬼影。分布避开[受保护区域]；保持[任务级保留项]，其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not mix disc ghosts, aperture polygons, rainbow streaks, and anamorphic bars by default.
- Do not use decorative floating spots unrelated to the optical axis.
- If neither an observed nor an authorized planned source supports flare, propose halo/lighting repair when supported, or clarify a non-physical overlay target. Do not re-ask permission already supplied.
