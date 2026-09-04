# Model Priors — Seedance 2.5 风险与降级档案

This file combines repeated observed behaviors from the existing production archive with Seedance 2.5 operating rules. A legacy observation is a risk signal, not proof that 2.5 behaves identically. Treat a prior as active for the current setup only after the same protected invariant fails three times on Seedance 2.5; then change method instead of rewording. A historical success is only evidence that one asset once landed, not a default recommendation for another fight. Current source facts and user locks always outrank every prior; a banned device stays closed in text, references and post.

## Combat-specific high-risk combinations

**多人物同时进攻**
风险：人物数量、攻击归属、触点和屏幕方向同时漂移。
路线：把威胁路线排成顺序；每个 FightBeat 只保留一个主要攻击-回应关系。必须同时发生时，优先使用经过检查的动作/白模参考，并减少镜头运动。

**精确兵器接触 + 大幅运镜**
风险：兵器换手、穿模、接触点漂移，或镜头遮住格挡关系。
路线：先用锁定或简单跟随镜头证明兵器接触，再增加摄影表现；必要时把接触和位移拆成相邻单元。

**交叉走位 + 轴线翻转**
风险：人物左右关系和运动方向突然反转。
路线：明确谁从前/后经过、结束位置和可见锚；让交叉本身可见，或插入中性机位重新建立轴线。

**动作参考职责泄漏**
风险：模型把参考视频中的身份、服装、场景或VFX一并带入。
路线：为每个参考写窄职责白名单；动作视频只承担用户授权的编排、节奏、重心、位移或机位维度，身份与场景由各自来源负责。

**长时长能力被误当作复杂一镜到底能力**
风险：时长增加后，多次接触、多人互动、跨场景和复合运镜的错误累积。
路线：按战斗目标、行动轴、地点或主动权转折拆分；用上一单元终态作为下一单元起始边界。不要仅因为 Seedance 2.5 支持更长生成就取消结构拆分。

## 强先验（文字拧不过来的）

**竖立屏障 → 漩涡盘/半球罩**
意图：竖立的圆形镜海水墙，平面正对斜向来袭的洪流。
实测：连续 3 次生成全部变成正对镜头的旋转漩涡盘或罩住人物的半球穹顶，光柱从头顶垂直砸入盘心。加了"像立起的水墙""不是半球形罩子""不悬在头顶"负向声明后依然如此。"圆形屏障"在模型先验里就长这样。
路线：① 上一张屏障形态参考图（最有效）；② 顺势设计——把设定改成漩涡盘吸收攻击，实测画面反而张力十足；③ 若必须竖墙，改叫"一面矩形水幕/水镜屏风"绕开"圆形屏障"词根（未验证，属假设）。

**斜向洪流 → 垂直砸落**
意图：洪流斜向轰在屏障正面。
实测：与漩涡盘先验绑定出现——攻击自动改为从正上方垂直落入盘心。屏障形态被纠正前，弹道跟着先验走。

## 可修复先验（换写法能过的）

**悬浮 → 站立/散步**
意图：人物悬浮在屋顶上空。
实测：首次生成变成平视机位站在屋顶间路面上朝镜头走，天空裂隙同时消失。
修复 ✓：低机位仰拍 + "双脚离地悬空" + "脚下屋脊在画面下缘远处缩成一片" + 气流吹动衣袍长须向上翻卷。悬浮需要"证据链"（脚下有远景+离地+气流反应），单写"悬浮"必丢。

**人小景大 + 面部细节 = 冲突**
意图：同一镜头里"身形偏小"+"皱眉/面部无伤痕"。
实测：模型折中成平淡中景，两头都没拿到。
修复 ✓：一镜只选一头——要么剪影/小人物大场面，要么顶天立地拍脸；或用镜头运动分时满足（推近过程从全景到面部）。

**复合运镜方向不稳**
意图：急速后拉+弧线环绕半圈+微上仰。
实测风险：后拉偶尔做成前推，环绕幅度不稳（概率性，非必然）。
降级路径：去掉环绕，只保留"急速后拉+微上仰"，成功率显著更高。先试全版，失败即降级。

## 历史成功信号（仅在当前功能需要且获授权时复用）

- 纯能量填屏开场：火云+光核+电弧+粒子，三次历史生成成立；只适用于已授权且不需保留身体/触点信息的效果段落 ✓
- 抽象人形残影粒子汇入裂隙：可正确渲染 ✓
- 白闪过曝转场：曾生成成功；只有用户允许且不取代接触、空间或状态桥时才使用 ✓
- 逆光剪影登场（人物立于屋脊，被身后能量体压成剪影）✓
- 手部大特写施法起手（腕指动作连贯凌厉）✓
- 牌坊/门洞画框构图 + 人小景大 ✓
- 收束面部特写（前景虚焦粒子、眼中映光）✓
- 颜色阵营对抗（赤金 vs 深蓝）无需解释即可读 ✓

## 通用规律

- **三连律**：同一受保护事实在 Seedance 2.5 连续 3 次失败 = 当前设置下的强先验，停止改词，改用参考、简化几何、降低机位负担、拆分单元或顺势设计。
- **几何关系是文字控制的上限**：颜色、材质、氛围、单体动作文字可控；多物体精确空间关系（谁面对谁、什么角度撞什么面）是最先失控的维度，优先用图锁。
- **位置锚要每镜重申**：镜头 N 确立的位置，镜头 N+2 不重申就会漂移（实测施法者从门洞漂到街心）。写法：位置 + 可见锚物（"仍站在门洞下，两侧石柱在画面边缘可见"）✓
- **动作与摄影分层**：接触正确性风险高时，先锁定/简化摄影验证身体动作，再增加运镜、速度变化和特效强调。
- **结构检查不等于成片质量**：提示词和设计卡通过检查，只证明因果、事实锁和降级路线齐全；必须审看真实 Seedance 2.5 结果才能评价打斗质量。

## Combat Audit — evidence, scope and repair ownership

Use this pass internally before `design_ready`, or externally when the user requests an audit or supplies an observed failure. Identify the artifact and layer first: source, story/design, compiled prompt, or actual rendered media. A description of a clean design is not the design itself; if it is absent, mark the relevant checks unknown and request only what this review needs. Do not require a video for a text-only design audit.

| Status | Evidence rule |
| --- | --- |
| PASS | A directly locatable fact supports this check at the stated layer. |
| FAIL | A quoted lock, action relation, continuity boundary or execution contract is explicitly violated. |
| WARN | A concrete tradeoff or local incompleteness remains; identify its impact and whether it blocks the requested stage. Generic model difficulty is not a finding. |
| UNKNOWN | Necessary evidence is missing or unreadable. State what would resolve it; never count it as passed. |
| N/A | The feature or layer does not apply to this artifact, with a reason. Absence of required evidence is not N/A. |

Check only applicable layers:

1. facts and authorization: roster, identity, weapon/ability, location, outcome/damage locks, prohibited devices and reference dimensions;
2. fight story: visible goal, resistance, escalation, initiative, requested reversal and ending, only when that arc applies;
3. space and physics: support, route, exact contact/result, reciprocal reaction, recovery and terminal state;
4. direction: shot purpose, composition proof, camera carrier/anchor, causal cut, speed contrast, clarity and authorized VFX/sound;
5. continuity: the material six-family relay and visible bridges across ownership, position, support or form changes;
6. compilation/feasibility: only applicable duration, timing, reference roles, load and platform contract; video owns final grammar;
7. rendered result: observed identity, contact accuracy, weight, blur, rhythm, occlusion and continuity. With no actual video these properties remain UNKNOWN even when their text specification passes. An absent optional VFX design may be N/A while overall rendered action remains UNKNOWN.

For each relevant finding record `check/layer; status; evidence location or missing input; impact; smallest affected closure; responsible layer`. Evidence is a shot plus a short exact quote, or a readable media timestamp/frame; never invent coordinates. For PASS/N/A, repair is none. Prefer compact grouped clean results and local actionable findings over a long checklist; do not force all five statuses to appear.

Protect clean fields. A discrepancy confined to one shot is repaired there plus only the boundaries whose inherited state changes; propagate until a stable unaffected boundary. Combat repairs story/action/direction/relay; video repairs mapping, grammar and delivery; motion reference or post owns only its authorized mechanics or frame-exact execution. Missing evidence goes to its source owner. If actual footage permits several causes, report the visible error and keep causal attribution unknown rather than blaming a layer without evidence.

A required textual conflict or unresolved generation-critical fact blocks `design_ready`; a concrete non-blocking tradeoff may remain WARN. Render-only UNKNOWN never becomes a text-level FAIL or an extra generation approval gate. Repair mutable internal inconsistencies within the authorized task, recheck the affected closure, and ask only when a required fact or hard choice remains. An audit-only request receives findings and the minimal proposed repair, without silently editing its subject. Ordinary final prompts contain the corrected current instructions, not this report or its metadata.
