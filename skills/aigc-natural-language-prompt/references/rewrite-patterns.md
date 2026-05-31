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

## Final Compression Pass

After rewriting:

- remove repeated style words once the visual evidence is present
- split sentences with more than 4-5 comma clauses
- keep simple shots short
- keep only the endpoint or continuity anchor that prevents real confusion
- keep only platform terms that change the model's output
- remove AI-flavored filler such as generic praise, abstract taste words, "not only...but also..." reasoning, rule-of-three padding, and forced conclusion sentences
