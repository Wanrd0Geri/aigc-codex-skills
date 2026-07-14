# Scope-Safe Prompt Rewrite Examples

Load these examples only for teaching or an unfamiliar language shape. They demonstrate preservation, not creative expansion.

## Compact tag cleanup

**Source**

```text
中景，雨夜街口，女孩站在路边，低头看积水，冷色调，高质量，电影感。
```

**Rewrite**

```text
中景拍摄雨夜街口，女孩站在路边，低头看着脚边的积水，画面保持冷色调。
```

The rewrite removes unsupported quality boosters and keeps every supplied visual fact. It does not add a light source, reflection, sound, camera move, or story.

## Exact locks survive cleanup

**Source**

```text
@庠序场景.png控制环境，@图2控制人物外貌。总时长12秒，人物说“门一直开着”，停顿两秒，最后黑场。
```

**Rewrite**

```text
@庠序场景.png作为环境参考，@图2作为人物外貌参考。总时长12秒，人物说道“门一直开着”，随后停顿两秒，最后黑场。
```

The anchors, quoted line, `12秒`, `两秒`, and black-frame cue remain literal.

## Numbered shots remain numbered

**Source**

```text
镜头1：少年站在门外没有进去。镜头2：他慢慢抬头看门框。镜头3：右手离开行李箱把手。
```

**Rewrite**

```text
镜头1：少年站在门外，没有进去。

镜头2：他慢慢抬头看向门框。

镜头3：他的右手离开行李箱把手。
```

No shot, action, emotion, camera, or timing is added.

## Mature prompt stays mature

**Source**

```text
中近景固定拍摄门内的男人。他仍保持倚墙的姿势，听见门轴轻响后才慢慢转头，目光停在门口，右手没有离开外套口袋。
```

**Result**

Return it unchanged. Rewriting it into a longer director brief would reduce rather than improve control.

## Ambiguity requires discussion

**Source**

```text
他回到多年没住过的房子，感觉时间停止了。
```

This source lacks a locked visible action and supports materially different performances. State the likely restrained-recognition reading, contrast it with the strongest plausible alternative, recommend one, and ask one focused question. Do not fabricate a doorway, furniture, dust, flashback, prop, or camera setup before the user decides.

## Specialist ownership remains intact

- `把这段最终 Seedance prompt 去 AI 味` → `aigc-video`
- `根据这张图给最终修图提示词` → `aigc-image`
- `只把下面这段平台中立的画面描述改自然，不做平台格式` → this skill

Language cleanup never overrides the owner of the requested final artifact.
