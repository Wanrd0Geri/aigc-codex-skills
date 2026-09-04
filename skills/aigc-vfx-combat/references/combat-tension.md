# Combat Tension — 因果、几何、触点与主动权

Read this file for any fight with a meaningful attacker-defender exchange. It defines the action structure before VFX or camera styling.

## Design choices and source gaps

In an open action-design request, unspecified ordinary body actions, attacking limbs, defensive responses, contact points and relative blocking are design choices. Choose one simple concrete exchange that fulfills the supplied order and result; do not return these choices as fictitious “既定” slots. Preserve all source locks and do not invent identities, weapons, powers, injuries, damage or new environment surfaces. Missing source-dependent facts or decisions explicitly reserved by the user remain unresolved. The aerial target/landing exception in `state-relay.md` remains in force; story review and fixed-shot audits keep their existing boundaries.

## Root-cause map

| Visible failure | Root cause | Tempting but wrong fix | Structural fix |
|---|---|---|---|
| 动作很多但不紧张 | 没有战术目标和主动权变化 | 加“激烈、快速、燃” | 定义双方即时目标和主动权曲线 |
| 拳脚像隔空比划 | 没有路径、触点和接触结果 | 加火花、震屏、慢动作 | 写清攻击路径、触点、支撑和双方反作用 |
| 人物位置漂移或穿插 | 起始几何和终态未锁 | 重复人物外观 | 锁左右、前后、距离、朝向、行动轴和结束位移 |
| 全程快但没有重量 | 没有速度差和恢复成本 | 更快剪辑、更多模糊 | 预备停顿 → 突然加速 → 接触强调 → 后果停留 |
| 特效很大但看不清谁赢 | VFX抢占动作层级 | 再加颜色和爆炸 | 先完成攻防链，再让VFX只证明触点、力量或阵营 |
| 运镜很炫但肢体失真 | 动作与摄影同时过载 | 加更多机位术语 | 先用锁定/简单跟随镜头验证动作，再加摄影表现 |

## Combat modes

### 真实攻防

价值来自身体、兵器、距离与决策。允许零 VFX。必须能在关闭粒子、闪光和震屏后仍读懂谁攻击、谁回应、谁取得结果。

### 混合打斗

身体攻防成立后，VFX附着在可见的力量来源、运动路线或关键触点上。常规接触克制，高潮或终结技才扩大尺度。

### 招式奇观

重点是技术显形、规模和环境后果；若没有对手回应，可以使用 `蓄力 → 爆发 → 余波` 而不强造一套攻防链。

## The FightBeat contract

A FightBeat is one readable cause-effect exchange, not a count of punches. It can contain a short combination only when the combination has one tactical intention and one result.

Each FightBeat records:

1. **time or order** — its place in the current generation unit;
2. **tactical intent** — the immediate visible problem, not backstory;
3. **start geometry** — A/B screen side, world depth, distance, height, facing, support, obstacles and action axis;
4. **initiative** — who currently forces the other to react;
5. **commitment** — the initiator's preparation, limb/weapon and movement path;
6. **response** — block, evade, absorb, deflect, counter, interrupt, grapple or fail;
7. **contact state** — hit, block, scrape, near miss, lock, release or no contact;
8. **contact point and moment** — where the relationship becomes readable;
9. **force chain** — support foot or anchor, center-of-mass shift, torso/weapon transfer and follow-through;
10. **reaction and displacement** — both bodies or weapons respond; direction and scale stay consistent with the source;
11. **initiative change** — retained, contested or reversed, with a visible reason;
12. **terminal boundary** — exact ending positions, postures, contact/effect state, recovery cost and residual motion.

If these facts cannot be stated without ambiguity, the beat is not ready for VFX or final prompting.

## Macro rhythm: 压 → 抢 → 碰 → 翻 → 留

- **压**: create a readable disadvantage using distance, mass, weapon reach, terrain, line of attack, injury or limited escape space.
- **抢**: one fighter commits first. State the source limb/weapon, route and intended target or control point.
- **碰**: resolve one explicit relationship: hit, block, evade, deflect, bind, absorb, counter or interrupted attack.
- **翻**: the response must change something visible — distance, posture, facing, weapon position, freedom of movement or initiative.
- **留**: hold the cost or result long enough to establish the next state: stagger, slide, pin, guard break, lost weapon, separated distance, unresolved bind or recovered stance.

The five phases are a diagnostic model, not a required five-shot template. Compress or combine them when the action remains readable.

## Initiative curve

Write the curve before camera styling. Examples:

- `长枪手以距离压制 → 剑客被迫退至栏杆 → 剑客借栏杆偏开枪尖 → 剑客贴身夺回主动权`
- `巨体对手逼近 → 小体型角色抢先贴身连击 → 巨体吸收前几击 → 决定性一拳改变重心并击飞 → 小体型角色追击后压制`

An initiative change must have a visible cause. Do not write `双方激烈交锋` or `局势突然逆转` without the action that produces it.

## Contact ledger

For each decisive contact, answer:

```text
发力者与来源：谁，用哪个肢体/武器
路径：从哪里沿什么方向到哪里
接触状态：命中 / 格挡 / 擦过 / 闪避 / 偏转 / 缠锁 / 中断
触点：身体部位、兵器部位或现有环境表面
支撑与重心：发力者靠什么站稳或失稳
力的传递：从支撑到躯干、肢体/兵器，再到对方
攻击者反作用：随动、回弹、收势或失衡
承受者反作用：压缩、扭转、滑移、后退、腾空或稳住
位移：方向、相对尺度和新的双方距离
恢复成本：重新站稳、回防、起身、抽出兵器或挣脱
```

Do not require environment destruction. One bodily/weapon reaction is mandatory; one reachable environment receiver is optional and must already exist or be authorized.

## Geometry and screen logic

- Establish left/right and the action axis before the first exchange.
- Preserve screen direction across contact unless a visible camera crossing or character crossover re-establishes the axis.
- Distinguish screen position from world position. `画面左侧` is not enough when depth or occlusion matters.
- Keep a named visible anchor when positions must persist: doorway, pillar, railing, wall edge, floor mark or weapon line.
- When fighters cross, state who passes in front/behind, where they end, and whether initiative changes.
- For one-to-many fights, sequence threat routes. Do not make all opponents attack simultaneously unless a verified motion reference and readable blocking support it.

## Speed and weight

Tension is contrast, not constant speed. Choose only the beats that need emphasis:

1. constrained anticipation or tactical pause;
2. sudden acceleration;
3. readable contact or near miss;
4. brief visual hold, compression or speed change at the decisive moment;
5. consequence and recovery;
6. renewed attack or terminal hold.

Slow motion, white flash, shake, speed lines and sound accents are presentation tools. They cannot supply missing contact geometry.

## Seedance 2.5 production route

### 1. Structure pass

Compile the fight problem, start geometry, FightBeats, contact ledger, initiative curve and terminal boundary before adding style. If the user supplied a script or accepted storyboard, preserve its facts and solve only missing execution logic.

For a new or reference-driven final video whose combat structure is not already approved, send these facts to `aigc-video`'s canonical structure-confirmation gate and stop. Do not add the performance pass or render the final Seedance 2.5 prompt in the same turn. A request for design only may return the full design card directly.

### 2. Reference-role pass

Assign every source a narrow whitelist. For an uploaded fight clip, a safe default is:

```text
视频1：仅参考动作编排、攻防节奏、身体重心、速度变化、位移规模和已明确授权的镜头节奏；
不承担人物身份、服装、场景、道具或VFX造型。
角色图A/B：仅负责对应人物身份、外观、服装与明确展示的武器。
场景图：仅负责空间、建筑、光线和材质。
```

Change this whitelist only when the user explicitly assigns more dimensions. Never call a motion source a generic `style reference`.

### 3. Motion proof

When contact accuracy is the primary risk, validate action with a locked or simple following camera. Check:

- both characters remain identifiable and count-stable;
- start geometry and screen direction are preserved;
- attack-response causality is visible;
- contact state and weapon ownership remain correct;
- support, reaction and displacement are plausible;
- terminal boundary is reached.

### 4. Presentation pass

After motion logic is viable, add only the camera path, speed emphasis, sound cue and VFX needed to express that logic. Preserve all structure-pass facts.

### 5. Final compilation

Hand the completed card to `aigc-video`, which owns the ready-to-paste Seedance 2.5 prompt and its exact reference syntax, timestamps, duration and delivery contract.

## When to split a generation unit

Split when two or more high-risk relationships must be solved at once, including:

- simultaneous attacks from multiple opponents;
- exact weapon contact plus a large viewpoint change;
- crossing bodies plus an axis reversal;
- aerial pursuit plus grapple plus environment collision;
- location change or a new combat objective;
- a compound camera move that hides the decisive contact;
- a start or terminal boundary that cannot be stated clearly.

Split at a causal boundary, not arbitrarily: after a block, launch, landing, pin, separation, weapon loss or initiative reversal. Pass the previous terminal boundary forward as the next start boundary.

## Failure recovery

Classify the failure before retrying:

- **identity/reference leak** → narrow source roles and restore identity locks;
- **contact failure** → simplify to one attack-response pair or use motion/pose reference;
- **geometry drift** → restore visible anchors, reduce crossing and split the beat;
- **body-camera interference** → lock/simplify camera and prove motion first;
- **VFX occlusion** → reduce effect scale, transparency or duration; keep the contact visible;
- **wrong consequence** → restate the terminal boundary and remove unsupported destruction;
- **same invariant fails three times** → stop rewording and change method.

Do not claim generated-video quality from prompt lint or structural coverage alone. Final confidence requires actual Seedance 2.5 output review.
