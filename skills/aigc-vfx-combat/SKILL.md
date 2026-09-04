---
name: aigc-vfx-combat
description: Design readable, high-tension donghua, xianxia, or wuxia combat and optional VFX before a final Seedance 2.5 video prompt. Use for fight stories, close combat, weapon exchanges, spells, transformations, clashes, large-scale techniques, or results described as flat, weightless, unclear, or lacking tension. This skill owns short fight dramaturgy, shot-level combat causality, contact physics, initiative changes, effect form, and presentation; `aigc-video` owns final prompt compilation, reference grammar, locks, and delivery.
---

# AIGC VFX & Combat Design

Turn a fight or technique into a readable chain of causes and consequences, then add only the VFX that helps the action read. This skill is optimized for Seedance 2.5 video generation. It designs the shot; `aigc-video` compiles the final platform prompt.

## Ownership and handoff

- This skill owns the plain-language FightStory and only the short fight dramaturgy visible inside the assigned exchange: immediate goals, resistance, escalation, initiative change, false victory or reversal when requested, and ending function. It does not create long-form character arcs, subplots, lore, or a new outcome.
- This skill owns shot-level combat logic: combat objective, starting geometry, initiative, attack-response chain, contact, momentum transfer, ending state, and optional VFX presentation.
- `aigc-video` owns the final Seedance 2.5 prompt, duration, timestamps, reference labels, locks, sound grammar, and complete deliverable.
- For a final video request, use a two-phase handoff: build only the combat structure, let `aigc-video` resolve its canonical structure gate, then resume this skill for presentation, optional VFX, and feasibility before `aigc-video` renders the final prompt. For design-only requests, return the design card below and stop.
- Do not redesign story-level intent already fixed by a script, storyboard, or `aigc-project-context`; solve only the visible fight inside the assigned shot or shot range.

## Root-cause model

A weak fight is rarely fixed by adding `快速`, `震撼`, camera shake, particles, or destruction. The usual root causes are:

1. no visible tactical problem between the fighters;
2. no stable starting geometry or screen direction;
3. actions listed without an attack-response causal chain;
4. no precise contact state or momentum transfer;
5. no change of distance, posture, cost, or initiative after contact;
6. camera and VFX hiding motion that was never made readable.

Solve those causes before styling. Tension comes from **readable threat + speed contrast + contact consequence + initiative change**. VFX is an optional evidence layer, not the source of combat logic.

## Workflow

### 1. Classify the request

- **真实攻防**: close combat, grappling, dodging, weapon work, pursuit, or any exchange whose value is bodily action. Run the combat-tension pass. VFX may be absent.
- **混合打斗**: readable physical exchange plus supernatural force. Run the combat-tension pass first, then attach VFX to selected contacts or the finisher.
- **招式奇观**: transformation, technique reveal, environmental-scale spell, or effect display with no meaningful opponent response. Build its source, spatial envelope, trigger, route, visible result, and terminal boundary before the shared structure gate; after the gate resolves, use the VFX spectacle pass.

Do not force every request into `蓄力 → 爆发 → 余波`; that arc belongs to technique spectacle, not every punch, parry, or reversal.

### 2. Resolve the plain-language FightStory when the fight arc is still being designed

Read `references/fight-story.md` when the request asks for a fight story or synopsis, creates or rewrites a multi-beat fight, or asks to repair a fight whose escalation, initiative curve, reversal, or ending is not yet accepted.

- Preserve every supplied winner, ability, weapon, location, damage limit, beat order, and ending. Add only the visible causality needed to connect them.
- Render the FightStory as ordinary continuous Chinese. Do not expose FightBeat, axis, ledger, structure-version, camera-table, platform, or prompt terminology.
- Do not force this stage onto one isolated attack-response beat, a mechanics-only question, an audit of fixed shots, a fixed accepted story, or a pure spectacle with no fight arc. Check the same dramaturgy internally and continue to the owning technical stage.
- A request for speed such as “直接给提示词” does not waive story review. Only an explicit instruction to skip the story/synopsis review does; then keep the FightStory internal and continue.

**🔴 CHECKPOINT · 🛑 STOP — FightStory review:** when the FightStory is new or materially changed and review has not been explicitly skipped, return only the plain-language story plus one confirmation request. Do not add technical design, a structure table, VFX enrichment, or a final video prompt in that turn. After the user confirms that exact story, continue at the combat-tension or spectacle structure stage without retelling it.

### 3. Build the combat-tension pass when an exchange exists

Read `references/combat-tension.md`. Establish, in this order:

1. the visible combat problem — what A is trying to achieve now and how B prevents it;
2. starting geometry — left/right, depth, distance, height, facing, support surface, and action axis;
3. initiative curve — who controls the exchange, where it changes, and why;
4. atomic FightBeats — one primary attack-response relation per beat;
5. contact ledger — attack path, hit/block/evade state, exact contact point, support and weight transfer, reaction, displacement, and recovery cost;
6. terminal boundary — final positions, postures, contact/effect state, initiative, and residual motion.

Use the macro rhythm `压 → 抢 → 碰 → 翻 → 留` when the exchange needs a complete dramatic arc. A short beat may compress it, but must still answer: **who initiates, how contact resolves, and who changes the situation**.

### 4. Resolve the shared structure gate for every final video

For any new or reference-driven final video, pass the combat or spectacle structure packet into `aigc-video` before presentation or VFX enrichment. The packet contains only source locks, visible roster, starting geometry or spectacle envelope, action/FightBeat order, contact or effect result, and terminal boundary.

Follow the gate result instead of testing only whether the structure is approved:

- `review_required`: return only `aigc-video`'s canonical structure table and grouped request, then stop. “直接给提示词” does not waive this pause.
- `direct_authorized`: keep the structure pending and internal, skip the table, and continue immediately with the presentation/VFX and feasibility phases in this skill.
- `confirmed`: continue with the presentation/VFX and feasibility phases for the accepted structure version.

When the user later confirms a pending combat structure, resume this skill at the next phase before `aigc-video` renders. Do not let a confirmation reply bypass the unfinished combat design. A design-only request may receive the complete design card without this extra confirmation round.

### 5. Add VFX only after the action works

For mixed combat or spectacle, set one color family and one signature form root per side. Read `references/vfx-library.md` for form and material vocabulary. Pick one form and 2–3 material words; more dilutes.

Nest `蓄力 → 爆发 → 余波` inside the relevant technique or finisher:

- **蓄力**: a small visible signal and constrained anticipation;
- **爆发**: the form materializes at a clear source, route, and contact/result;
- **余波**: consequences that continue from the resolved contact.

For a normal hit, require one readable bodily or weapon reaction. Add at most one reachable environment receiver when the source or user authorizes it. Do not manufacture ground cracks, shockwaves, or building damage merely to prove force.

### 6. Design presentation around readability

Read `references/shot-language.md` for axis, screen direction, shot-distance contrast, speed contrast, contact emphasis, and VFX presentation. Establish the action before adding complex camera motion.

- The contact shot must let the viewer understand both the attack and the response.
- Camera shake, whip pans, motion blur, speed lines, slow motion, white flashes, and black-and-white inserts may emphasize an already readable contact; they must not replace it.
- Use close framing to prove contact, wider framing to prove displacement, and a held ending to prove the result when those functions are needed.

### 7. Run the Seedance 2.5 feasibility pass

Read `references/model-priors.md` for known priors and failure recovery.

- Treat a FightBeat as the minimum controllable unit. Keep more than one beat in a generation only when their causal and spatial continuity remains simple and visible.
- Split or use a motion/clay reference when the same unit combines simultaneous multi-person actions, crossing trajectories, exact weapon contact, aerial interaction, viewpoint reversal, or compound camera movement.
- When a motion reference exists, assign it only the requested dimensions, such as choreography, weight shift, timing, displacement, or camera rhythm. Identity, wardrobe, scene, and VFX remain with their declared sources.
- Validate body action with a locked or simple following camera before asking for aggressive camera choreography when contact accuracy is the main risk.
- Seedance 2.5 supporting a longer generation does not make a complex one-take the default. Split at changes of location, action axis, combat objective, or unstable multi-subject geometry.
- After the same protected invariant fails three times, stop rewriting. Change method: simplify the beat, reduce camera load, add a motion/clay/start-end reference, or split the unit.

## Final-video handoff

After the shared structure gate resolves, compile one internal `CombatHandoff` for every affected unit using the contract in `../aigc-video/references/video-contracts.md`. Bind it to the exact current `structure_version` and set `combat_design_status: design_ready` only after presentation, optional VFX, and feasibility are complete.

The handoff must preserve:

- source and user locks;
- the accepted FightStory and its immediate goals, escalation, initiative turns, reversal logic, and ending function when that stage applied;
- combat problem or spectacle intent;
- starting geometry or spatial envelope;
- initiative curve, FightBeats, contact ledger, and terminal boundary when an exchange exists;
- source, trigger, route, visible result, and terminal boundary for spectacle;
- body/weapon mechanics, presentation, optional VFX, sound cues, and feasibility decisions.

`aigc-video` maps this packet into MotionSpec without redesigning it. If a later structural change increments the bound `structure_version`, invalidate the presentation/VFX portion and return to the shared gate before rebuilding only the affected combat design.

## Design card

For design-only output, omit fields that truly do not apply:

```text
【CombatDesign｜交锋名】
类型与强度: <真实攻防 / 混合打斗 / 招式奇观；常规 / 高潮>
参考职责: <each source and only the dimensions it may contribute>
事实锁: <character count, identity, wardrobe, weapons, scene, allowed damage>
战斗问题: <A's immediate visible goal; how B prevents it>
空间基线: <left/right, depth, distance, height, facing, support, action axis>
主动权曲线: <A压制 → B化解 → B反转...>

FightBeat 1:
- 压/抢: <threat, preparation, initiator, attack route>
- 碰: <hit/block/evade/deflect, exact contact point>
- 翻: <body/weapon reaction, momentum, displacement, initiative change>
- 留: <recovery cost and terminal state>

身体力学: <support, center of mass, force chain, follow-through>
机位与屏幕方向: <how the action remains readable>
声音节拍: <only source-backed or intentionally designed cues>
起始边界: <positions, posture, contact and effect state>
终止边界: <positions, posture, initiative and residual motion>

VFX（无则省略）:
- 阵营色 / 形根 / 材质词
- 蓄力 / 爆发 / 余波
- VFX如何证明触点或力量，而不遮挡动作

Seedance 2.5 风险与降级: <risk; split/reference/camera fallback>
```

Keep it concrete and compact enough to hand to `aigc-video` without reinterpreting the fight.

## Avoid

- Do not render the final Seedance 2.5 prompt from this skill alone.
- Do not list both fighters' actions independently; pair every attack with the opponent's response and the resulting state change.
- Do not hide unclear choreography with VFX, fast cutting, blur, shake, or black-and-white flashes.
- Do not keep continuous maximum speed; tension needs anticipation, acceleration, contact emphasis, consequence, and recovery in proportions appropriate to the beat.
- Do not stack more than one form and three material words on one effect.
- Do not invent damage, props, powers, injuries, or environment interactions not authorized by the source.
- Do not force a verified strong model prior through repeated wording when a reference, simpler geometry, or split unit can solve it.
