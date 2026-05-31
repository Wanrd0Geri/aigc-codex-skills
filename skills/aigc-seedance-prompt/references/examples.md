# Seedance Prompt Examples

Optional calibration examples covering the main task types this skill handles. Do not load this file for routine prompts. Read it only when the output shape is unfamiliar, when checking a diagnostic-mode format, or when a user explicitly asks for examples.

All examples below follow the natural-prose writing style: structured shot lead-in (`镜头N：x秒，景别。`) followed by complete Chinese sentences with verbs and connectives, not comma-chained parameter lists. See SKILL.md `Shot Line And Execution Body` for the underlying discipline.

For the image-to-video case with multiple references, see also the UFO example in `single-segment-quality-control.md`.

## Example 1: Pure Text-to-Video (No References)

**User input**: 「想要一个雨夜便利店的镜头,女主在自动门外犹豫了一下,然后推门进去。8秒。」

**Inferred task type**: text-to-video, single segment, two-shot.

**Why two shots**: the emotional beat is the hesitation before entering. One shot would either lose the hesitation or compress it. Two shots let the hesitation read clearly, and let the entry land.

**Final prompt**:

```text
时长：8秒。深夜的城市街道上，一家二十四小时便利店亮着冷白色的灯光，店外正下着小雨，路面反射着店招的颜色。无配乐，无旁白，无字幕，无配音，仅保留环境雨声、自动门感应声、店内冰柜的低频运转声以及脚步声。

镜头1：4秒，中景。机位架在便利店玻璃门外，正面固定拍摄，人物站在画面中央偏前的位置，玻璃门与店内的冷白灯光构成背景。一位年轻女性站在自动门前两步开外，她的黑色长款风衣肩部已经被雨水打湿，右手握着一把还没撑开的折叠伞。她抬头看向店内透出的冷白色灯光，脚步在原地停住，肩膀也跟着微微下沉，呼出的白气在冷空气里缓缓消散。与此同时，背景里雨水正从店招边缘一滴一滴落到路面。

镜头2：4秒，中近景。机位翻转到门内向外的反向角度，缓慢向女主推近，货架位于画面深处。女主从画面外侧迈出一步，身体进入自动门的感应范围，玻璃门向两侧滑开。此时店内暖气与门外冷空气在交界处生出一层短暂的雾气，女主的脚踏过店内地垫，左手将湿漉漉的伞收紧到身侧，目光投向画面深处的货架方向。她跨入店内时，身后的自动门正在缓缓关闭，身体朝向画面深处；如果下一段继续拍她挑选商品，这个朝向可以作为接点。整段保持主体识别稳定，动作承接清楚，光线由冷白外光过渡到店内暖光的方向不变。
```

---

## Example 2: Video Extension (Continuation From `@视频1`)

**User input**: 「我有一个3秒的镜头,女主从画面右边走到中央停下来。我想接一段5秒的延续,她应该转过头看向左边窗外。」

**Inferred task type**: video extension. The source clip's final frame provides the new clip's starting posture, light, and camera relationship.

**Inheritance points**: position (画面中央), facing (背对/朝向需明确), light (与原片一致), camera momentum (原片是固定还是有运动需继承或停下).

**Final prompt**:

```text
时长：5秒。承接@视频1（原始镜头参考）的结尾画面，女主已停在房间画面中央，身体朝向画面深处。房间内的暖色台灯光线、地面材质和墙面陈设都与@视频1保持一致。无配乐，无旁白，无字幕，无配音，仅保留环境室内底噪、衣物摩擦声以及窗外远处隐约的风声。

镜头1：5秒，中景。保持@视频1结尾的机位与角度固定拍摄，女主停在房间画面中央，窗户位于画面左侧。她从@视频1的停步姿态开始，先有一个短暂的静止停顿，随后头部缓慢向左转动，肩膀略微跟着转动但脚步不动，目光停在画面左侧的窗户方向。此时窗外的冷色环境光照在她的左脸侧，与室内暖色台灯形成对比。整段中服装、发型、光线方向与机位都与@视频1保持连续；如果下一段要走向窗户，保留她侧脸朝向窗户、身体仍朝向画面深处的关系即可。
```

---

## Example 3: Video Editing (Add Element To Existing Clip)

**User input**: 「这个10秒的镜头,我想在3-7秒的画面左下角加一只缓慢走过的黑猫,其他都不要变。」

**Inferred task type**: video editing. Need: time range, spatial location, what to add, what to keep continuous.

**Final prompt**:

```text
在@视频1（原始镜头参考）的3-7秒区间内，画面左下角增加一只黑色短毛猫。这只猫从画面左侧边缘走入，沿着地面缓慢向画面中央方向移动两步后停下，身体朝向画面右侧，尾巴自然下垂。它的体型与画面中其他物体的近大远小关系保持一致，地面上的投影方向也与原片光线方向匹配。

需要保持不变的部分：人物的位置、朝向与动作节奏，镜头的机位与运动，背景的几何结构与陈设，整体光线方向、色温与阴影关系，以及环境音和动作声的原有节奏。整段只新增黑猫本身与它在地面上投下的微弱影子，不引入新的光源，不改变景深，也不调整色调。
```

---

## Example 4: Diagnostic Mode (Optimizing A Weak Prompt)

**User input**: 「帮我优化下这个 prompt:『一个很有氛围感的镜头,女孩站在樱花树下,非常唯美,电影感拉满,3D 风格,4K 高清。』」

**Inferred task type**: diagnostic. Apply the fixed three-part output template.

### 当前问题

- `氛围感`、`唯美`、`电影感拉满` 都是抽象品味词,Seedance 无法解析为可见动作或光线状态。
- `3D 风格` 是用户没有用参考图建立的风格标签,会让模型从默认风格库随机抽样,结果不可控。
- `4K 高清` 属于平台 UI 参数,放在 prompt 里既无效又占用注意力预算。
- 缺少时长、镜头组织和主体动作，画面只剩风格愿望，Seedance 很难判断真正要生成什么。

### 改进 prompt

```text
时长：6秒。春日午后，一棵盛开的樱花树立在画面中央，少量花瓣正在缓缓飘落。无配乐，无旁白，无字幕，无配音，仅保留环境风声、远处的鸟鸣以及花瓣落地的细微声响。

镜头1：6秒，中景。机位略微仰角，缓慢向女孩推近，她站在樱花树下偏左的位置，树冠与飘落的花瓣占据画面上方。年轻女孩穿着浅色长款连衣裙，裙摆被微风轻轻带起，双手自然垂在身侧，左手指尖轻轻收拢。阳光从画面右上方斜射穿过花瓣，在她的左肩和发丝上落下柔和的光斑。她缓慢抬起头看向飘落的花瓣，嘴角微微放松，呼吸保持自然。整段主体识别稳定，光线方向连贯，动作承接清楚。
```

### 关键修改

- 把 `氛围感 / 唯美 / 电影感` 翻译成可见载体：仰角 + 慢推 + 斜射阳光 + 风带起裙摆 + 仰望姿态。
- 删除 `3D 风格` 和 `4K 高清`：风格未由用户或参考建立时只写中性执行质量,分辨率交给平台 UI。
- 补全时长、镜头编号、单一主动作与单一运镜，让单段有明确的生成重点。
- 把原来逗号串联的镜头描述改写为带主谓的完整句子，结构标头（`镜头1：6秒，中景。`）之后转入散文式执行说明。
