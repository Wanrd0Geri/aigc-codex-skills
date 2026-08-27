# Semantic palette-transfer capability

Use a scene image plus a positional semantic palette card to change grade, color temperature, or color relationships without importing the card as scene content.

## Evidence gate

Confirm which image is the scene base, which is the palette card, the card's grid dimensions, row/column order, and the exact authorized color changes. If the card order is unreadable or differs from the standard 3 x 4 map, request its mapping instead of guessing.

## Fixed role assignment

- Image 1 owns people, objects, identity, pose, composition, camera, geometry, material identity, text, luminance hierarchy, light direction, shadow geometry, weather, and time.
- Image 2 owns only the twelve positional color roles.

## Canonical prompt

```text
输入职责：图1是唯一场景底图；图2只是一张三行四列的十二色语义色卡，只提供固定位置的颜色职责。

只使用图2的位置颜色关系调整图1的[综合色调／白平衡／色温／授权的局部颜色关系]。第一行从左到右依次映射到黑位、深暗部、普通阴影和暗部偏色；第二行依次映射到环境主色、主体或主要物体的固有色、辅助色和大气中间调；第三行依次映射到环境光色、主光色、柔和高光色和峰值强调色。峰值强调色只用于小面积视觉焦点或高反射区域，不扩散到全画面。

保持图1的人物、物体、身份、姿态、构图、镜头关系、几何、材质可辨识度、文字、明暗层级、光线方向、阴影形状、天气和时间不变；不得把图2的网格、色块形状、排列布局、分隔线、纹理、文字或任何场景内容带入图1。其余未提及内容保持不变。
```

## Prohibited drift and fallback

- A palette card does not authorize new light direction, shadow shape, exposure hierarchy, material identity, scene content, or composition.
- Map by semantic position, not by nearest-looking color or equal coverage.
- If the user requests only color temperature, change warm/cool relationships while preserving luminance and saturation unless separately authorized.
