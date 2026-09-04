# Lighting capability

Use to repair motivated light direction, local illumination, shadow ownership, exposure hierarchy, or subject-environment light integration.

## Evidence gate

Identify visible or motivated sources, target region, direction, hardness, falloff, shadow geometry, local bounce, and the grade properties the user protects. A request for `电影感` does not authorize a new LUT, camera emulation, time of day, or unrelated source.

An explicitly authorized new source supplies planned light conditions under [edit-operation-state.md](edit-operation-state.md); it is not evidence of a source already in the image. Refresh receiving surfaces, attributable shadows/reflections and downstream optical effects when source placement, output or occlusion changes. Weather/time defaults in the standalone fragment yield only when those changes are also authorized under the task contract.

## Variables

- `[目标区域]`
- `[现有或授权光源]`
- `[方向、软硬和衰减]`
- `[可见终态]`
- `[保持不变的综合色彩与曝光关系]`

## Canonical prompt

```text
图1是唯一底图。只调整[目标区域]的光线关系：以[现有或授权光源]为来源，按照[方向、软硬和衰减]形成[可见终态]，同步修正必要的受光面、背光面、投影、接触阴影和局部环境反射，使光源、几何和材质响应一致。保持[保持不变的综合色彩与曝光关系]、构图、身份、物体、天气、时间及其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not relight the entire frame for a local repair.
- Do not introduce camera brands, film stocks, color-science names, arbitrary light ratios, or unsupported rim light.
- If no source supports the requested direction, propose the smallest motivated source repair or require authorization for stylized lighting.
