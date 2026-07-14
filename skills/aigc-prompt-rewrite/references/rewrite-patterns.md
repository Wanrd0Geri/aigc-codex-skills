# Scope-Safe Rewrite Patterns

These patterns change language, not creative facts. A smoother sentence is a failure if it adds an unsupported camera, subject, action, prop, light source, sound, reference anchor, or ending.

## Parameter stack to visual sentence

Reorder only supplied facts into a subject-action-space sentence.

**Source**

```text
中景，女孩站在雨夜街口，低头看脚边积水，冷色调。
```

**Rewrite**

```text
中景拍摄雨夜街口，一名女孩站在雨中，低头看着脚边的积水，画面保持冷色调。
```

Do not add a lamp, shop, reflection, traffic, camera move, sound, or emotional backstory merely because those details are common in a rain scene.

## Abstract intent

First look for a visible carrier already present in the source.

- If `紧张` appears beside `手指停在门把上，没有立刻压下去`, keep the action and remove the redundant label.
- If `孤独` appears but the source contains no subject, action, spacing, or environment that can carry it, ask for one visible choice.
- If several performances fit equally well, state the likely reading and recommendation, then ask before choosing.

Do not use a fixed dictionary that always turns one emotion into the same gaze, posture, lighting, or object action.

## Unsupported cause to supported result

When a stated cause is not visible or established, keep only the supplied visible result.

**Source**

```text
画面里看不到山门，风从山门方向吹来，带动少年额前碎发。
```

**Rewrite**

```text
少年额前的碎发被风轻轻吹动。
```

If the direction is a production lock, do not remove it; flag that the current visual setup does not establish the cause.

## Exact anchor and number protection

Keep literal anchors, dialogue, text, numbers, and edit cues unchanged. Change only the connective language around them.

**Source**

```text
@图1控制人物外貌，@视频1控制动作节奏；12秒，角色说道“你终于来了”，停顿两秒，最后黑场。
```

**Rewrite**

```text
@图1作为人物外貌参考，@视频1作为动作节奏参考。总时长12秒，角色说道“你终于来了”，随后停顿两秒，最后黑场。
```

Never change `12秒` to `约12秒`, `两秒` to `短暂停顿`, or normalize the literal anchors.

## Multi-shot preservation

One source shot remains one output shot unless the user explicitly authorizes restructuring.

**Source**

```text
镜头1：少年站在雨里，低头看地面。镜头2：他回头看门口。镜头3：右手慢慢握住剑柄。
```

**Rewrite**

```text
镜头1：少年站在雨里，低头看着地面。

镜头2：他回头看向门口。

镜头3：他的右手慢慢握住剑柄。
```

Do not add framing, lighting, exact shot durations, motives, reactions, or a dramatic ending when the source does not supply them.

## Multi-character clarity

Clarify pronouns and supplied positions or actions. Do not invent blocking to make a group scene more vivid.

**Source**

```text
姐姐站在桌子左侧扶住碗，弟弟从桌子右侧拿走木勺，两个人互相看了一眼。
```

**Rewrite**

```text
姐姐站在桌子左侧扶住碗，弟弟从桌子右侧拿走木勺；随后两人互相看了一眼。
```

If positions or action ownership are absent and matter to readability, ask rather than assigning them.

## Platform and quality words

- Preserve platform syntax that changes execution.
- Preserve user-locked medium, style, camera, duration, and reference roles.
- Remove decorative boosters such as repeated `高质量`, `masterpiece`, or `氛围拉满` only when no production meaning is lost.
- Do not replace a removed booster with invented craft detail.

If the requested result is still a final named-platform video prompt, route to `aigc-video`. If it is a final image edit, reverse prompt, or diagnosis, route to `aigc-image`.

## Final compression

After rewriting:

1. compare every exact lock character-for-character;
2. trace every semantic lock to the output;
3. delete any new noun, verb, number, anchor, or shot not supported by the source;
4. remove repetition only after lock safety is proven;
5. leave a mature prompt alone when no material language defect remains.
