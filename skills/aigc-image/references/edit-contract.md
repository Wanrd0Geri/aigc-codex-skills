# Universal edit contract

Use this semantic contract for GPT Image, Gemini/Nano Banana, Seedream, and unknown multimodal image editors. Fixed structure does not mean fixed wording or fixed image-specific values.

## Fields

1. `Input roles`: which image owns the scene and which attributes each reference may contribute.
2. `Target`: exact object, region, plane, or whole-image property to edit.
3. `Change`: one operation and its visible endpoint.
4. `Integration`: only relationships required to make changed pixels belong in the source.
5. `Keep`: costly locks plus one general unchanged boundary.

## Standalone shape

```text
图1是唯一底图。只修改图1中[目标对象或区域]的[授权属性]：将其变为[可见终态]。[仅添加所需的融合关系]。保持[本轮高风险锁]不变；其余未提及内容保持不变。
```

Omit `图1是唯一底图` when the interface already exposes one unambiguous base image and the statement adds no control.

## Multi-reference shape

```text
输入职责：图1是唯一场景底图；图2只提供[属性]；图3只提供[属性]。
修改：[目标 + 操作 + 可见终态]。
融合：[必要的比例、透视、遮挡、接触、光线、阴影、材质、边缘或景深关系]。
保留：[关键锁]；其余未提及内容保持不变。
```

## Composition rules

- One capability: use that capability's standalone fragment.
- Several capabilities: preserve their unique actions, merge duplicate roles and locks, and state shared dependencies once.
- Never append several full templates end to end.
- Do not print an empty section.
- Do not include diagnosis, evidence labels, validation status, model parameters, or API controls inside the prompt.
- Prefer a positive endpoint. Use a direct exclusion only for a concrete likely drift that cannot be expressed by Target, Change, Integration, or Keep.

## Fixed versus variable

Fixed:

- semantic field order
- evidence gate
- physical relationships
- prohibited drift
- fallback

Variable:

- target, region, count, shape, intensity, direction, depth plane, color role, and protected locks read from the actual task

Never freeze an image-dependent variable merely to make the template look standardized.
