# Composition capability

Use to move, resize, crop, reframe, or rebalance visible elements. Composition changes are not conservative cleanup; require explicit authorization.

## Evidence gate

Identify the focal subject, current crop, protected content, intended negative space, and the exact composition property the user allows to change. If several layouts satisfy the request but communicate different priorities, ask which priority wins.

For actual object movement, read `IMG-SUPPORT-01` in [edit-operation-state.md](edit-operation-state.md): clear its attributable effects at the old position and establish necessary contact/shadow/reflection at the new one. A crop or uniform reframe that does not relocate objects in the scene needs no new physical effects. Other capabilities consume the resulting placement and frame geometry.

## Variables

- `[主体或对象]`
- `[新位置和占画面比例]`
- `[裁切或扩展边界]`
- `[负空间用途]`
- `[必须完整保留的内容]`

## Canonical prompt

```text
图1是唯一底图。将[主体或对象]移动或缩放到[新位置和占画面比例]，并按[裁切或扩展边界]重新组织画面，为[负空间用途]保留清晰空间。保持[必须完整保留的内容]；对实际移位对象，局部重建原位置，并同步更新该对象可归属的接触、阴影、反射与遮挡关系，沿用本轮确定的场景光线。保持[任务级保留项]，其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not change pose, camera angle, scene identity, or subject count merely to rebalance framing.
- Do not crop hands, feet, props, text, or action-critical contact unless authorized.
- Omit movement/support clauses for crop-only or reframe-only requests; fragments must express only the selected operation.
- If the request says only `构图更好`, diagnose the attention problem and ask or recommend one concrete layout before editing.
