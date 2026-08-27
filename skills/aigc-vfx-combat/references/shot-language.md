# Shot Language — 攻防可读性 / 机位构图 / 特效强调

## 打斗镜头的第一原则

Camera design serves the attack-response relationship. Before choosing a dramatic move, establish:

- the action axis and both fighters' screen direction;
- who controls distance and who is forced to react;
- where the decisive contact or near miss occurs;
- which wider view will prove displacement or which held view will prove the result.

At a decisive contact, the viewer must understand both the attack and the response. Do not cut only to the striking limb if that hides how the defender blocks, evades, absorbs or counters.

### 轴线与屏幕方向

- Establish left/right, near/far and facing before the exchange.
- Preserve screen direction across contact. If the camera or fighters cross the axis, show the crossing or insert a neutral re-establishing view.
- Keep a visible spatial anchor when the next beat inherits position.
- For weapon contact, keep both weapon owners and the contact relationship readable before using an insert.

### 张力的景别函数

- **建立关系**: a view wide enough to read distance, obstacles and the action axis.
- **证明触点**: a closer view that still preserves attacker-response causality.
- **证明力量**: a wider view showing slide, launch, fall, pursuit or changed distance.
- **证明结果**: a brief hold on stagger, pin, separation, guard recovery or weapon loss.

These are functions, not a mandatory four-shot template. Use only what the beat needs.

### 速度函数

Use contrast: constrained anticipation → sudden acceleration → contact emphasis → consequence/recovery. Continuous maximum speed makes every action equal and removes tactical tension.

## 特效三拍式 (charge → burst → aftermath)

Use this arc for a technique reveal, transformation, spell, or finisher. Do not force it onto every physical exchange. The beats gain power from contrast, so avoid keeping one visual distance across all three when a distance change helps readability.

**蓄力 (1–2s, 近/特写, 慢推)**
- 指尖凝光、能量纹沿手臂爬升、武器出鞘半寸、瞳孔特写点亮阵营色
- 瞳孔特写是大招前的标准"标点符号"——情绪+节奏双重锚
- 施法手势要具体到腕指: "左袖短促一拂，右手划半圆，手腕一翻，指尖向前一点" ✓（实测手部动作连贯凌厉）

**爆发 (瞬间, 全屏)**
- 画面过曝白闪一瞬 ✓（实测有效，衔接干净）
- 或纯能量填屏：高潮对轰 2-3s 不画人，只有能量乱流+电弧+火星，人物剩剪影或消失 ✓（AI 最擅长、最出效果的镜头类型）
- 或黑白闪风格切换（见下）

**余波 (1–2s, 大远景, 慢拉/环绕)**
- 冲击波环扩散、光柱冲天、地面碎裂石块悬浮、烟尘中剪影缓缓落地
- 冲击波永远是环形：地面同心圆冲击环+垂直光柱 = "强者落地/开大"通用符号

## 机位构图五杠杆 (按有效度排序)

原则：**景别标签少写，构图关系多写**。"远景/特写"对生成模型是弱控制，会漂；下面四样才是杠杆。

1. **机位角度** — 仰拍=压迫/强大，俯拍=渺小/被压制。最强一档，一个词翻转气势。
2. **主体占比+纵深** — 写"谁占满画面、谁在边缘、前景是什么"。两个方向都成立：
   - 人小景大: 人占 5-15%，巨物(裂隙/巨日/巨佛/巨浪)占满天。AI 生成成功率最高、天然电影感 ✓
   - 顶天立地: 人物占据画面主体，背景巨物化作光晕轮廓 ✓
3. **画框式构图** — 门洞、屋檐、石柱把主体框住 ✓（实测牌坊门洞画框稳定生成）
4. **景别对比节奏** — 大远景接特写的落差才是爽感来源；写"变化"（推近/拉开），别每镜标景别。相邻镜头一大一小互为呼吸。
5. **对角线/失衡** — 洪流斜向贯穿、屏障立面对冲，比水平构图有冲击力 ✓

## 三大风格方法论 (按片型选用)

**法宝流·能量海** (凡人修仙传式)
颜色即阵营的全屏能量攻防。高潮直接切纯能量填屏。适合：法宝对轰、修仙大战。

**字卡流·留白史诗** (燃向歌词 MV 式)
人小景大 + 大面积留白构图，为书法字卡/标题留位置：`negative space composition, subject small in frame`。人物普遍只占 5-15%。适合：MV、片头、群像叙事。

**黑白闪·漫画帧** (打击感流)
用风格切换强调已经清楚的决定性触点，不替代动作设计：
- 命中瞬间画面切成黑白线稿风：黑色放射速度线、白色负空间、人物剪影，持续数帧
- 全片黑白中只保留一种颜色（阵营色电弧/瞳色/怒焰）= "超规格力量"信号
- 大招结束瞬间恢复全彩，落差即爽感
- 后期剪辑插单帧黑白效果通常比要求模型同时完成复杂接触和风格跳变更稳
适合：近身武打、爆气、变身、以弱胜强的一击。

## 高价值运镜 (含风险等级)

- **特写起手→急速后拉+环绕揭示**: 小(指尖水珠)瞬间炸开成大(屏障全貌)，信息落差大。风险：复合运镜方向可能反转（见 model-priors）。降级：只保留急速后拉+微上仰。
- **慢推特写收束**: 对抗段落末尾推近面部，前景虚焦粒子，眼中映阵营色光 ✓（实测稳定且情绪浓）
- **相邻镜景别互补**: 镜头 A 特写起→拉开收，镜头 B 全景起→推近收，衔接自然不跳。
- **镜头震动**: 只在清楚的接触之后轻微响应。震动证明冲击，不能掩盖触点。

## 剪辑与连续性

- Cut at a decision, contact resolution, displacement, landing, recovery or initiative reversal—not merely because a fixed interval elapsed.
- Preserve action direction, weapon ownership and terminal state across a cut.
- A contact insert must inherit the exact limb/weapon relationship from the surrounding views.
- 帧级黑白插帧、闪白和音效可以增强打击点，属强调层；真正的重量仍来自预备、触点、反作用和恢复成本。
