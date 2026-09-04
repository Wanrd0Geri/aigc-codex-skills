# Object change and cleanup capability

Use for one named add, remove, replace, recolor, repair, or defect-cleanup operation.

## Evidence gate

Identify the target boundary, operation, newly exposed or occupied background, nearby edges, protected text or identity, and minimum reconstruction. For removal, replacement, or movement with shadows/reflections, read `IMG-SUPPORT-01` in [edit-operation-state.md](edit-operation-state.md): include only effects attributable to this object, even when outside its silhouette. If the target is not readable, request a crop.

## Variables

- `[添加／删除／替换／改色／修复／清理]`
- `[目标对象或缺陷]`
- `[目标区域]`
- `[可见终态]`
- `[可归属的阴影、反射或接触影响及必要的局部重建]` — omit absent effects
- `[高风险锁]`

## Canonical prompt

```text
图1是唯一底图。在[目标区域][添加／删除／替换／改色／修复／清理][目标对象或缺陷]，使其呈现为[可见终态]；同步处理[可归属的阴影、反射或接触影响及必要的局部重建]，使局部透视、遮挡、光线、材质和纹理连续。范围限于该对象及其必要影响区域，保持[高风险锁]不变；其余未提及内容保持不变。
```

## Prohibited drift and fallback

- Do not redesign the scene for a local cleanup.
- Do not alter exact labels, identity, pose, geometry, or nearby objects unless named.
- For removal, clear identifiable owned shadows/reflections and reconstruct only the object's attributable support and exposed background. Respect an explicitly retained stylized effect. For replacement or addition, use placement/contact and material integration when those dependencies are material.
