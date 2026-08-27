# Composition capability

Use to move, resize, crop, reframe, or rebalance visible elements. Composition changes are not conservative cleanup; require explicit authorization.

## Evidence gate

Identify the focal subject, current crop, protected content, intended negative space, and the exact composition property the user allows to change. If several layouts satisfy the request but communicate different priorities, ask which priority wins.

## Variables

- `[主体或对象]`
- `[新位置和占画面比例]`
- `[裁切或扩展边界]`
- `[负空间用途]`
- `[必须完整保留的内容]`

## Canonical prompt

```text
图1是唯一底图。只调整构图：将[主体或对象]移动或缩放到[新位置和占画面比例]，并按[裁切或扩展边界]重新组织画面，为[负空间用途]保留清晰空间。保持主体外形、身份、姿态、对象关系和[必须完整保留的内容]不变；被移动区域按原场景连续重建，不复制、删除或新增未授权内容。保持原有透视、光线、色彩、材质及其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not change pose, camera angle, scene identity, or subject count merely to rebalance framing.
- Do not crop hands, feet, props, text, or action-critical contact unless authorized.
- If the request says only `构图更好`, diagnose the attention problem and ask or recommend one concrete layout before editing.
