# VFX Library — 功能 / 形 / 材质 / 颜色阵营词库

Curated from frame-level combat analysis and prior Seedance generations. Words marked ✓ landed in at least one historical generation; they are vocabulary evidence, not default recommendations. Current source facts, force propagation and user locks decide whether any form is allowed.

## VFX contract

Build an effect in this order: `function → owner/source → route or envelope → contact/result → occlusion boundary → exit/residue`. If any required fact is unknown, keep it unresolved rather than filling the screen. Environment damage, flashes, shockwaves, creature silhouettes and full-screen coverage require source support or user authorization.

## 颜色即阵营 (color as faction)

Give each character/faction ONE exclusive color family + ONE signature form root. Every effect that side produces derives from these two words. Verified: 赤金(攻方) vs 深蓝(守方) reads instantly with zero explanation ✓.

Suggested pairings (pick, don't stack):

| 阵营气质 | 色系 | 常配形根 |
|---|---|---|
| 天威/霸道 | 赤金、金红 | 裂隙、洪流、巨日 |
| 冷静/守御 | 深蓝、蓝白 | 镜海、水墙、漩涡 |
| 雷法/天罚 | 金雷、白金 | 雷柱、电弧网 |
| 邪魅/魔功 | 血红、暗红 | 血雾、绸带、红瞳 |
| 仙气/星辰 | 紫白、银紫 | 星月背轮、光柱雨 |
| 妖异/兽性 | 橘焰、黑金 | 兽形虚影、怒焰鬃毛 |
| 生机/木系 | 青绿、玉色 | 法环、藤蔓、玉光 |

## 能量形态词库 (form roots)

An effect must BE something, not just an element. Verified forms:

- **裂隙**: 半空被撕开的赤金灵力裂隙，竖向炽白光核，火云旋涡环绕 ✓（注意声明"不出现眼球/瞳孔形态"，竖缝+放射纹易被读成眼睛）
- **洪流**: 一束粗壮连续的灵力洪流，斜向轰下，火星与碎裂光片沿途剥落 ✓
- **镜海/水墙**: 竖立的圆形镜海屏障，像一面立起的水墙（见 model-priors：会被做成漩涡盘）
- **法环**: 多层同心圆环旋转，环上带铭文，中心半透明玉质球体
- **雷柱**: 连接天地的巨型闪电柱，全屏放射状电弧
- **光柱雨**: 数十根垂直光柱如帘幕砸落
- **星月背轮**: 人物背后悬浮巨大日轮/月轮，星尘粒子环绕
- **冲击环**: only for an authorized radial or ground-centered force; the ring expands from the true contact/source and any debris follows that force ✓
- **剑气弧线**: 燃烧的橘色弧形刀光拖尾横贯画面
- **兽形虚影**: 爆气时背后浮现的巨大兽头虚影（狼/凤/龙），火焰鬃毛
- **粒子汇入**: 大量半透明性灵粒子从四周汇入，拖出长尾影，只保留抽象人形残影 ✓（人形残影可正确渲染）
- **血雾绸带**: 绸缎状血雾流体拖尾，暗色碎屑飞散

## 材质质感词库 (material words)

质感藏在材质词里，不在"华丽/震撼"里。每个特效配 2-3 个，多则稀释：

熔金流体 / 黑烟金边 / 琉璃质感 / 玉质半透明 / 墨流 ✓ / 绸缎状流体 / 星尘粒子 / 碎裂光片 ✓ / 粒子丝 ✓ / 流体丝线 ✓ / 镜面反光 ✓ / 细密水流纹 ✓ / 向内旋转的暗流 ✓ / 火星剥落 ✓ / 紫白电弧游走 ✓ / 长尾影 ✓

## 从功能到可见形态

| 功能意图 | 可见形态示例 |
|---|---|
| 火焰沿掌击路线进攻 | 掌心作为来源，熔金流体沿真实攻击线展开为已授权的火焰形根，接触后只保留沿受力方向剥落的黑烟金边 |
| 水系力量偏转攻击 | 指尖或掌心深蓝源点展开为有明确平面的水幕，入射流在可见触点改变方向，镜面反光与流体丝线沿偏转路线延续 |
| 雷力从身体传入目标 | 电弧从已声明的身体或兵器连接点沿接触链传播，离开触点后衰减；是否形成雷柱由尺度与授权决定 |
| 气场压迫但不破坏环境 | 衣袍、尘雾或已有悬浮物沿压力方向响应，人物支撑和对手反应证明力量；不自动裂地或生成冲击环 |
| 剑气延长兵器攻击线 | 弧形能量从刃口沿挥击切线离开，终点、命中/擦过状态和残余轨迹可读；不自动切换背景或重复冲击画 |
| 变身阶段显形 | 形态从明确附着点按覆盖边界逐段生成，继承上阶段拓扑；不自动补全兽头、巨龙或完整生物 |

Construction rule: `one function + one owner/source + one form root + 2–3 material words + one route/result + one terminal residue`. Scale follows the shot's evidence need; “larger” is not an automatic upgrade.
