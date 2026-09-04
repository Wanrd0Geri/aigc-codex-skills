# Placement, scale, contact, and occlusion capability

Use when inserting or reconciling a person, product, prop, building, or other element inside a base scene.

## Evidence gate

Identify the support plane, local scale anchors, front/back order, contact points, light direction, receiving surface, and any foreground occluders. If no scale anchor or support plane is readable, state the uncertainty instead of inventing precise placement.

For relocation or a support/light condition changed by another operation, use [edit-operation-state.md](edit-operation-state.md). Consume the resolved placement and lighting, clear old effects attributable to the moved object, and update only its necessary support. Do not preserve stale contact or recheck unrelated objects.

## Variables

- `[目标对象]`
- `[目标位置和尺度]`
- `[支撑面或接触点]`
- `[前景／后景遮挡对象]`
- `[接触阴影和环境反射要求]`

## Canonical prompt

```text
图1是唯一场景底图。将[目标对象]放置在[目标位置和尺度]，使其稳定接触[支撑面或接触点]，并按照图1现有空间建立正确的前后尺度递减和[前景／后景遮挡对象]遮挡关系。在接触处生成与图1光线一致的[接触阴影和环境反射要求]，让重量、落点和边缘过渡可信。保持对象身份与设计、场景构图、透视、光线方向、综合色调及其余未提及内容不变。
```

For multiple inputs, precede the fragment with explicit roles: Image 1 owns the scene; the object reference owns only the named object's identity and design.

## Prohibited drift and fallback

- Do not float the object, sink it through the support surface, or place contact shadow on the wrong side.
- Do not import the reference object's original background, camera, lighting, or composition.
- If perspective is wrong, repair perspective before contact and material integration.
