# Seedance Prompt Examples

Optional calibration examples for unfamiliar output shapes or diagnostic checks. Do not load this file for routine prompts.

These examples are original adaptations of the task patterns in the [official Seedance 2.0 prompt guide](https://www.volcengine.com/docs/82379/2222480?lang=zh). They demonstrate task wording, not a mandatory house template.

## Contents

1. Pure text-to-video
2. Video extension
3. Video editing
4. Diagnostic optimization
5. Multimodal reference with subject definition
6. Dialogue and sound markers
7. Shot bridge
8. Explicit visible text

## 1. Pure Text-To-Video

**User**: `雨夜便利店，女主在自动门外犹豫一下再进去，8秒。`

```text
本视频总时长 8 秒，两个镜头。深夜街角的小型便利店亮着冷白灯，细雨落在空旷路面上，画面重点是女孩在门外短暂停住后跨进店内的情绪变化。无配乐，无字幕。

镜头1：中景。固定机位从玻璃门外正面拍摄，女孩停在感应区外两步的位置，右手握着收拢的湿伞。她望向店内，肩膀轻轻下沉，手指在伞柄上收紧，门内灯光映在潮湿路面上。

镜头2：中近景。镜头切到店内朝门外的角度并缓慢推近，女孩向前迈步，自动门向两侧滑开。她跨过门槛，把湿伞收在身侧，目光转向店内深处；身后的玻璃门缓缓合拢，冷雨声被室内轻微的电器低鸣取代。
```

## 2. Video Extension

**User**: `@视频1结尾是女主走到房间中央停下。向后延长5秒，她转头看左边窗外。`

```text
向后延长@视频1（原始镜头），生成其后的 5 秒内容。延续原片的固定机位、室内暖色台灯、人物服装和空间关系，女主从结尾的停步姿态自然继续。无配乐，无字幕。

镜头1：中景。女主停在画面中央，身体仍朝向房间深处，左侧窗户保持在原有位置。她先短暂停顿，随后缓慢向左转头，肩膀只跟随转动少许，双脚不移动，目光最终停在窗外；窗外冷色环境光落到她的左脸侧，与室内暖光保持连续。
```

## 3. Video Editing

**User**: `在10秒原片的3-7秒左下角加一只慢慢走过的黑猫，其他不变。`

```text
在@视频1（原始镜头）的3-7秒画面左下角增加一只黑色短毛猫。黑猫从左侧边缘走入，沿地面缓慢向右移动两步后停下，体型、接触阴影和近大远小关系与原片一致。人物动作、机位与运镜、背景陈设、光线、对白、环境声和动作声保持不变。成片无配乐，无字幕。
```

## 4. Diagnostic Optimization

**Weak prompt**: `一个很有氛围感的镜头，女孩站在樱花树下，非常唯美，电影感拉满，3D风格，4K高清。`

**Problems**:

- `氛围感`、`唯美` and `电影感拉满` have no visible carrier.
- `3D风格` is a valid medium request but needs material and motion cues.
- `4K` is normally selected in the platform UI.
- No duration, action, or camera strategy is defined.

```text
本视频总时长 6 秒，单镜头。全片保持风格化三维动画媒介，人物轮廓清楚，材质柔和哑光。春日下午，女孩站在盛开的樱花树下，画面重点是她从低头静立到抬头望向花瓣的微小情绪变化。无配乐，无字幕。

镜头1：中景。机位略微仰拍并缓慢向女孩推近，树冠和零星飘落的花瓣占据画面上方。女孩双手自然垂在身侧，裙摆被轻风带起；她先微微低头，随后缓慢抬眼看向花瓣，嘴角逐渐放松。斜射阳光在她的发丝和左肩留下柔和光斑。
```

## 5. Multimodal Reference With Subject Definition

**User**: `@图1里有两个人，用红裙草帽女孩做主角；动作和运镜参考@视频1。`

```text
将@图1中穿红色连衣裙、戴草帽的年轻女孩定义为小岚。参考@视频1的人物转身动作和平稳横移运镜，生成小岚在海边木栈道回头看向远处灯塔的 8 秒视频。无配乐，无字幕。

镜头1：中景。镜头从小岚侧后方平稳横向移动，她沿木栈道缓慢向前走，右手轻扶草帽。走到栏杆旁时，她借着停步的惯性转动上身，先转肩再回头，目光越过海面落向远处灯塔，红裙下摆被海风轻轻带向身后。全程只使用@图1中已定义的小岚作为人物主体。
```

## 6. Dialogue And Sound Markers

**User**: `女孩在便利店窗边告诉朋友“我明天就走”，看得到嘴型，不要配乐字幕。`

```text
本视频总时长 8 秒，单镜头。夜间便利店窗边，两位朋友隔桌而坐，画面重点是女孩说出决定前的停顿和朋友听见后的克制反应。无配乐，无字幕。

镜头1：中近景。固定机位从桌侧拍摄，女孩的正脸和嘴部清楚可见，朋友保持在画面另一侧。女孩先低头用拇指摩挲纸杯边缘，吸气后抬眼看向朋友，平静地说道{我明天就走}。朋友没有立刻回答，只把握住杯子的手指收紧。<窗外一辆车驶过湿路面的轻响>与店内冰柜低鸣自然保留。
```

## 7. Shot Bridge

**User**: `用@视频1树叶落下接到@视频2金色粒子出现。`

```text
@视频1（前段原始镜头）中树叶接近地面时继续下落；树叶触地的一瞬间，从接触点向外扩散细小金色粒子，粒子被一阵横向气流卷起并充满画面，亮度和运动方向自然过渡到@视频2（金色粒子后段镜头），接@视频2。成片无配乐，无字幕。
```

## 8. Explicit Visible Text

**User**: `结尾要出现广告语“快乐尽在 Seedance”。`

```text
本视频总时长 8 秒，单镜头。三位朋友围坐分享炸鸡，气氛轻松，结尾明确显示广告语。无配乐。

镜头1：中景。固定机位拍摄三人相互递食物并笑着交谈，动作自然连贯。后段人物与桌面逐渐轻微虚化，画面中央淡入白色手写体广告语“快乐尽在 Seedance”，文字保持清楚、完整、位置稳定直到结束。
```
