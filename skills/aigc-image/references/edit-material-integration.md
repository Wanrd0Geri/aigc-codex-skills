# Material and edge integration capability

Use when a subject or edited region looks pasted, plastic, waxy, over-sharp, texture-mismatched, or inconsistent with surrounding material response.

## Evidence gate

Identify the target material, surrounding roughness and reflectivity, edge softness, local color spill, grain or texture frequency, shadow behavior, and protected design details. Diagnose the specific mismatch instead of applying a global quality stack.

## Variables

- `[目标对象或区域]`
- `[目标材质行为]`
- `[环境反射、粗糙度、边缘和纹理关系]`
- `[必须保留的设计细节]`

## Canonical prompt

```text
图1是唯一底图。只修复[目标对象或区域]与环境之间的材质和边缘融合：让其呈现[目标材质行为]，并匹配图1现有的[环境反射、粗糙度、边缘和纹理关系]。同步修正必要的局部色彩污染、反射强度、接触边缘和纹理频率，使对象属于同一画面而不改变其设计。保持[必须保留的设计细节]、身份、形状、构图、透视、光线方向、综合色调及其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not turn every surface glossy, matte, hyper-detailed, photoreal, or uniformly sharp.
- Do not add generic PBR, 8K, masterpiece, film grain, or Unreal-style language unless it describes the actual requested medium.
- If light or contact is the root mismatch, route to lighting or placement/contact first.
