# Object change and cleanup capability

Use for one named add, remove, replace, recolor, repair, or defect-cleanup operation.

## Evidence gate

Identify the target boundary, operation, newly exposed or occupied background, nearby edges, protected text or identity, and the minimum reconstruction needed. If the target is not readable, request a crop.

## Variables

- `[添加／删除／替换／改色／修复／清理]`
- `[目标对象或缺陷]`
- `[目标区域]`
- `[可见终态]`
- `[必要的背景、边缘或材质重建]`
- `[高风险锁]`

## Canonical prompt

```text
图1是唯一底图。只在[目标区域][添加／删除／替换／改色／修复／清理][目标对象或缺陷]，使该区域呈现为[可见终态]；仅重建[必要的背景、边缘或材质重建]，并保持与周围透视、遮挡、光线、阴影、材质和纹理连续。保持[高风险锁]不变；其余未提及内容保持不变。
```

## Prohibited drift and fallback

- Do not redesign the scene for a local cleanup.
- Do not alter exact labels, identity, pose, geometry, or nearby objects unless named.
- For removal, reconstruct only the newly exposed pixels; for replacement or addition, use placement/contact and material integration when those dependencies are material.
