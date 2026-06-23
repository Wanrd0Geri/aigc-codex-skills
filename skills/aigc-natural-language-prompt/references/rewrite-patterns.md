# Natural-Language Rewrite Patterns

Use these patterns when converting rough AIGC prompts into director-style natural language.

## Parameter Stack To Visual Sentence

Pattern:

```text
[shot size / camera] + [visible subject] + [position] + [action] + [environment relation] + [continuity anchor when needed]
```

Before:

```text
中景，夜晚，女孩，雨街，孤独，电影感，冷色调，高级质感。
```

After:

```text
中景固定拍摄一条雨夜街口，女孩独自站在画面偏左的冷白路灯下，低头看着脚边积水里的倒影。远处店铺灯光被雨水拉成长线，街道空旷，只剩雨滴落在地面上的声音。
```

## Abstract Mood To Visible Carrier

Translate mood into physical evidence.

- `孤独` -> one person isolated in frame, empty space, no eye contact, distant sound, small posture
- `紧张` -> held breath, tightened fingers, delayed gaze, blocked doorway, shallow movement
- `高级感` -> restrained composition, clean material hierarchy, controlled color, readable silhouette
- `童话感` -> softened scale contrast, warm object light, gentle prop motion, clear character silhouette
- `热闹` -> overlapping but readable actions, reactions, footsteps, object contact, changing positions

Before:

```text
气氛灵动、热闹、顽皮。
```

After:

```text
一只小狐狸抱着木勺绕过桌脚，另一只从长凳旁追上来，第三只踮脚扶住快要歪倒的小碗，最安静的那只从桌角后探出耳朵观察它们。
```

## Off-Screen Cause To Visible Result

If the source is not in frame, remove the source and keep the effect.

Before:

```text
风从山门方向吹来，带动他额前的碎发。
```

After:

```text
额前碎发被轻轻吹开，衣领边缘也跟着颤动。
```

If the source is established:

```text
山门仍在他身后的远处虚化可见，画面深处的风带动他额前碎发。
```

## Cut Relation

When continuity matters, connect the shot to the previous frame.

Before:

```text
镜头切到少年侧前方。
```

After:

```text
从上一镜头的远景切到少年右侧前方的中近景，机位略低，只保留他的上半身、右手和身后虚化的石阶。
```

For simple cuts, write the current view directly:

```text
镜头来到少年右侧前方的中近景，画面里只保留他的上半身、右手和身后虚化的石阶。
```

## Platform Or Quality Words To Global Setup

Move broad style constraints to the setup. Do not repeat them in every shot.

Global setup:

```text
全片为虚幻引擎渲染的精致三维角色动画风格，非写实摄影。角色毛发、耳朵、尾巴和布料保持柔顺稳定，木屋光线干净，体积光和木质材质清楚。
```

Shot body should then describe visible action:

```text
@图3的小狐狸从长凳左侧冲入画面，脚掌踩过石地时身体略微前倾，布袋贴着背后一晃一晃。
```

## Multi-Character Action

Use role and path instead of chaos.

Before:

```text
四只小狐狸在屋里嬉闹玩耍，热闹可爱。
```

After:

```text
@图2的小狐狸站在桌边发起追逐，先伸手去拿桌上的木勺；@图3的小狐狸抱着小布袋从长凳旁跑过，顺手把木勺抢走；@图4的小狐狸踮脚扶住桌边快要歪倒的小碗；@图5的小狐狸从桌角后露出耳朵，观察前方空隙后绕到另一侧截住它们。
```

## Image-Edit Natural Directive

Keep edit blocks, but make each line an instruction with visible outcome.

Before:

```text
增强电影感，提升光影，氛围更高级，不要 AI 感。
```

After:

```text
[Transform]
把原本平直的正面光改为画面左侧的柔和主光，让人物右侧脸颊进入更深的阴影。背景整体压暗，保留少量冷色环境光，使人物轮廓从暗部中分离出来。
```

## AI Writing Cliche To Visual Control

Do not keep AI-writing cliches as final prompt control. Translate them into what the frame can show or what the viewer can hear.

Before:

```text
这不仅是一个画面，更是少年命运感的表达，通过光影展现宿命，整体氛围拉满，高级电影感。
```

After:

```text
少年站在旧学堂门槛外，身体被门框分成一明一暗两侧。画面左侧的冷光只照到他的肩线和半张脸，身后的长廊逐层压暗，门内的木桌和书卷只留下模糊轮廓。他没有立刻进门，右手停在门边，指节微微收紧，雨声从空旷庭院里传来。
```

Pattern:

- `不仅是...更是...` -> remove the value-raising frame and keep the visible beat
- `命运感/宿命感` -> blocked path, scale contrast, delayed movement, shadow split, object threshold
- `氛围拉满` -> sound, light falloff, background reaction, object motion, spatial emptiness or density
- `高级感/电影感` -> controlled light direction, depth layers, silhouette, material response, restrained color

## Protected Anchor Rewrite

Reference anchors are production controls. Preserve the literal anchor and soften only the role wording around it.

Before:

```text
@图1控制角色外貌，@图2控制旧学堂场景，@视频1控制动作节奏，画面要有电影感和命运感。
```

After:

```text
@图1作为角色外貌和服装参考，@图2作为旧学堂空间、门口方向和室内陈设参考，@视频1作为动作节奏参考。镜头从学堂门口内侧固定拍摄，角色站在门槛外的半明半暗位置，先停住脚步，再慢慢抬眼看向屋内；门框把他的身体切成前景亮面和背景暗面，木桌、书卷和墙面在纵深里逐渐虚化。
```

Rules:

- preserve `@图1`, `@视频1`, `@音频1`, and file-name anchors like `@庠序场景.png` exactly
- do not rewrite anchors as `参考图1`, `图1`, plain file names, or generic labels
- `控制` may become `作为...参考`, `用于约束...`, or another soft role phrase after the literal anchor
- if dialogue or lyrics are attached to an anchor, do not paraphrase them unless the user explicitly asks

## Scope-Safe Multi-Shot Cleanup

When a source prompt already has numbered shots, preserve the shot count, order, duration, dialogue, and main action chain before removing AI flavor.

Before:

```text
三镜头去 AI 味：镜头1少年站在雨里宿命感拉满；镜头2他回头看门口，电影感高级；镜头3手慢慢握住剑，情绪复杂，最后有震撼收束。
```

After:

```text
镜头1：中景固定拍摄雨中的石阶，少年站在画面中央偏后的位置，肩线被雨水压低，身后的门口只剩一块暗色轮廓。他没有立刻移动，只低头看向脚边被雨水打散的倒影。

镜头2：镜头来到少年右侧前方的中近景，保留他身后的门口虚影。他慢慢回头看向门口，眼神先停在门槛处，再移到门内更深的暗处，雨声在画面外继续。

镜头3：近景只拍他的右手、剑柄和被雨水打湿的衣袖。手指先悬在剑柄旁边，随后一根一根收紧，剑柄上的水珠被指节挤开，画面停在握紧的一瞬间。
```

Rules:

- one source shot should remain one output shot unless the user asks for a structural rewrite
- preserve each shot's main action before adding visual carriers
- remove abstract endings such as `震撼收束` only after giving the shot a visible landing point
- do not collapse a multi-shot prompt into one paragraph just to make it sound smoother

## Final Compression Pass

After rewriting:

- remove repeated style words once the visual evidence is present
- split sentences with more than 4-5 comma clauses
- keep simple shots short
- keep only the endpoint or continuity anchor that prevents real confusion
- keep only platform terms that change the model's output
- remove AI-flavored filler such as generic praise, abstract taste words, "not only...but also..." reasoning, rule-of-three padding, and forced conclusion sentences
