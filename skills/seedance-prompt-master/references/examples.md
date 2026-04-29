# Seedance Prompt Examples

End-to-end examples covering the main task types this skill handles. Each example shows the user input, the inferred task type, and the final prompt. Read this reference when drafting a prompt and you want to see the target shape for that task type.

For the image-to-video case with multiple references, see also the UFO example in `single-segment-quality-control.md`.

## Example 1: Pure Text-to-Video (No References)

**User input**: 「想要一个雨夜便利店的镜头,女主在自动门外犹豫了一下,然后推门进去。8秒。」

**Inferred task type**: text-to-video, single segment, two-shot.

**Why two shots**: the emotional beat is the hesitation before entering. One shot would either lose the hesitation or compress it. Two shots let the hesitation read clearly, and let the entry land.

**Final prompt**:

```text
时长：8秒。深夜城市街道，一家二十四小时便利店亮着冷白色灯光，店外正在下小雨，路面反射店招的颜色。无配乐，无旁白，无字幕，无配音，仅保留环境雨声、自动门感应声、店内冰柜低频运转声与脚步声。

镜头1：中景（MS），便利店玻璃门外正面角度，固定机位（locked-off）。年轻女性站在自动门前两步距离，黑色长款风衣肩部已被雨水打湿，右手握着一把没有撑开的折叠伞。她抬头看向店内冷白色的灯光，脚步停住，肩膀微微下沉，呼出的白气在冷空气中缓慢消散。背景中雨水从店招边缘滴落到地面。

镜头2：中近景（MCU），从门内向外的反向角度，缓慢推近（slow push in）。女主向前走一步，身体进入自动门感应范围，玻璃门向两侧分开，店内暖气与门外冷空气交界处出现一层短暂的雾气。女主的脚踏过店内地垫，左手将湿漉漉的伞收紧到身侧，眼神看向画面深处的货架方向。结束在她跨入店内、自动门正在关闭的瞬间，身体朝向画面深处，为下一段进入店内挑选商品的片段保留接点。主体识别稳定，动作承接清楚，光线由冷白外光过渡到店内暖光的方向不变。
```

---

## Example 2: Video Extension (Continuation From `@视频1`)

**User input**: 「我有一个3秒的镜头,女主从画面右边走到中央停下来。我想接一段5秒的延续,她应该转过头看向左边窗外。」

**Inferred task type**: video extension. Source clip's ending state is the new clip's starting state.

**Inheritance points**: position (画面中央), facing (背对/朝向需明确), light (与原片一致), camera momentum (原片是固定还是有运动需继承或停下).

**Final prompt**:

```text
时长：5秒。承接@视频1（原始镜头 / Video 1 source clip）结尾画面，女主已停在房间画面中央，身体朝向画面深处，房间内的暖色台灯光线、地面材质和墙面陈设保持与@视频1一致。无配乐，无旁白，无字幕，无配音，仅保留环境室内底噪、衣物摩擦声和窗外远处隐约的风声。

镜头1：中景（MS），保持@视频1结尾的机位与角度，固定机位（locked-off）。女主从@视频1的停步姿态开始，先有一个短暂的静止停顿，随后头部缓慢向左转动，肩膀略微跟随转动但脚步不动，目光最终停在画面左侧的窗户方向。窗外光线为冷色环境光，与室内暖色台灯形成对比，照在女主的左脸侧。最后停在她侧脸朝向窗户、身体仍朝向画面深处的姿态，为下一段走向窗户的片段保留接点。服装、发型、光线方向、机位与@视频1保持连续，动作承接清楚。
```

---

## Example 3: Video Editing (Add Element To Existing Clip)

**User input**: 「这个10秒的镜头,我想在3-7秒的画面左下角加一只缓慢走过的黑猫,其他都不要变。」

**Inferred task type**: video editing. Need: time range, spatial location, what to add, what to keep continuous.

**Final prompt**:

```text
在@视频1（原始镜头 / Video 1 source clip）的3-7秒区间内，画面左下角增加一只黑色短毛猫，从画面左侧边缘走入，沿地面缓慢向画面中央方向移动两步后停下，身体朝向画面右侧，尾巴自然下垂。猫的体型与画面中其他物体的近大远小关系一致，地面投影方向与原片光线方向匹配。

保持不变：人物的位置、朝向、动作节奏，镜头的机位与运动，背景的几何结构与陈设，整体光线方向、色温和阴影关系，环境音与动作声的原有节奏。仅新增黑猫与其在地面上的微弱影子，不引入新的光源、不改变景深、不调整色调。
```

---

## Example 4: Diagnostic Mode (Optimizing A Weak Prompt)

**User input**: 「帮我优化下这个 prompt:『一个很有氛围感的镜头,女孩站在樱花树下,非常唯美,电影感拉满,3D 风格,4K 高清。』」

**Inferred task type**: diagnostic. Apply the fixed three-part output template.

### 当前问题

- `氛围感`、`唯美`、`电影感拉满` 都是抽象品味词,Seedance 无法解析为可见动作或光线状态。
- `3D 风格` 是用户没有用参考图建立的风格标签,会让模型从默认风格库随机抽样,结果不可控。
- `4K 高清` 属于平台 UI 参数,放在 prompt 里既无效又占用注意力预算。
- 缺少时长、镜头组织、主体动作和镜头结束态,无法生成稳定结果。

### 改进 prompt

```text
时长：6秒。春日午后，一棵盛开的樱花树立在画面中央，少量花瓣正在飘落。无配乐，无旁白，无字幕，无配音，仅保留环境风声、远处鸟鸣和花瓣落地的细微声响。

镜头1：中景（MS），略微仰角，缓慢推近（slow push in）。年轻女孩站在樱花树下偏左的位置，浅色长款连衣裙的裙摆被微风轻轻带起，双手自然垂在身侧，左手指尖轻轻收拢。阳光从画面右上方斜射穿过花瓣，在女孩的左肩和发丝上形成柔和的光斑。女孩缓慢抬头看向飘落的花瓣，最后停在仰望姿态，嘴角微微放松，呼吸保持自然。主体识别稳定，光线方向连贯，动作承接清楚。
```

### 关键修改

- 把 `氛围感 / 唯美 / 电影感` 翻译成可见载体：仰角 + 慢推 + 斜射阳光 + 风带起裙摆 + 仰望姿态。
- 删除 `3D 风格` 和 `4K 高清`：风格未由用户或参考建立时只写中性执行质量,分辨率交给平台 UI。
- 补全时长、镜头编号、单一主动作、单一运镜与可读结束态,让单段可稳定生成。
