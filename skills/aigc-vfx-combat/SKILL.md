---
name: aigc-vfx-combat
description: Use whenever a donghua/xianxia/wuxia fight, spell, technique, transformation, or energy effect needs visual design beyond a plain description — the user asks for 大场面, 大制作, 电影感, 燃, 震撼, 招式设计, 特效设计, 打斗设计, 法术对轰, or complains a generated effect looks 普通/平淡/没张力/没质感. Also use proactively before aigc-video or aigc-image renders any combat/VFX-heavy final prompt, so the effect gets structure, form, material, and camera design instead of a generic element. This skill owns the visual design layer only; final platform prompts stay with aigc-video (video) and aigc-image (image).
---

# AIGC VFX & Combat Design

Turn a plain move request ("女子发射火焰") into a production-grade visual design. The difference between an ordinary effect and a 大制作 effect is never adjectives — it is structure. This skill supplies that structure, then hands the design to `aigc-video` or `aigc-image` for final platform rendering.

## Ownership and handoff

- This skill owns: what the effect looks like — its stages, form, material, color regime, physical consequences, and camera presentation.
- `aigc-video` owns: the final video prompt, platform grammar, locks, references, delivery format.
- `aigc-image` owns: the final image prompt.
- When the user asks for a final prompt, run this skill's design pass first, then apply the owning skill's full workflow to render. Never skip the owning skill's lock and grammar rules. When the user asks for design only, deliver a design card (format below) and stop.

## Core principle: 结构 > 形容词

A generic result ("a flame from her hand") happens when the prompt contains only an *element*. Mature donghua teaches that a spectacle effect has three layers the model can actually execute:

1. **阶段 (stages)** — it unfolds over time: charge, burst, aftermath.
2. **形 (form)** — the element takes a nameable shape: not fire, but a molten-gold phoenix; not water, but a standing mirror-sea wall.
3. **后果 (consequences)** — the world reacts: shockwave rings, scorched ground, blown hair and robes, floating debris.

Adjectives like 震撼/华丽/炫酷 activate nothing. Concrete structure words activate the exact training-data cluster you want. The reference files below are curated activation vocabulary verified against real generations.

## Workflow

### 1. Gauge the tier

Decide how much design the moment deserves:

- **常规演出**: a passing move, transition beat, or background action. Apply only a form noun and one consequence. Do not inflate every minor gesture into a set piece — spectacle inflation cheapens the climax.
- **大制作**: a climax, reveal, duel exchange, ultimate technique, or any request containing 大场面/大制作/燃/震撼/电影感. Apply all five levers below.

### 2. Set the color regime and form (颜色即阵营)

Every character or faction gets one exclusive color family and one signature form root. All of that side's effects derive from these two words. This is what makes a fight readable and a series feel designed — 赤金 vs 深蓝 needs no explanation on screen.

Read `references/vfx-library.md` for the form lexicon (环/柱/雨/雾/浪/凤/镜海/裂隙…), the material lexicon (熔金流体/黑烟金边/琉璃质感/墨流…), and the ordinary→大制作 upgrade table per element. Pick one form and 2-3 material words; more dilutes.

### 3. Structure the beat (三拍式)

Design the move as 蓄力 → 爆发 → 余波:

- **蓄力** (1–2s): close framing, small signal — energy crawling up an arm, a bead of light at a fingertip, an eye catching color. Slow push-in.
- **爆发** (instant): one frame-filling event — overexposed white flash, pure-energy fill, or a style snap. Shortest beat, highest contrast.
- **余波** (1–2s): wide framing, the world responds — expanding ring shockwave, drifting debris, settling dust, held silhouette. Slow pull or orbit.

The burst reads as powerful *because* the charge was quiet and the aftermath is wide. Never deliver all three beats at the same shot size.

### 4. Add physical feedback

At least two consequences from different bodies: environment (cracked ground, ring scorch, floating rubble), person (hair/robe blown, heels sliding, steady gaze against the wind), atmosphere (heat distortion, ember rain, mist pushed outward). Physical feedback is what makes an effect feel heavy instead of pasted on.

### 5. Choose the camera lever

Write composition relationships, not shot-size labels. Read `references/shot-language.md` for the five levers (仰拍/俯拍, subject scale + depth, frame-in-frame, shot-size contrast between beats, diagonal energy paths), the three donghua methodologies (法宝流 energy-sea, 字卡流 negative-space epic, 黑白闪 manga impact frames), and high-value camera moves with their risk levels.

### 6. Check model priors before delivery

Read `references/model-priors.md` whenever the design includes barriers/shields, floating or hovering, small-subject epic framing combined with facial detail, or compound camera moves. These are the cases where verified generation behavior contradicts intuition, and a design that ignores them will fail identically on retry. Prefer designing *with* a strong prior over fighting it in text.

## Design card format

When delivering design-only output, use this structure:

```
【招式名】
阵营色: <exclusive color family>  形根: <signature form root>
蓄力: <visible small signal, framing>
爆发: <frame-filling event, the form materializing>
余波: <world consequences, framing>
材质词: <2-3 material words>
物理反馈: <2+ consequences, different bodies>
机位: <the one composition lever that carries tension>
先验风险: <only if a known prior applies, with the workaround>
```

Keep it in Chinese, concrete, and short enough to paste into a conversation with `aigc-video`.

## Avoid

- Do not render final Seedance/platform prompts from this skill alone; route through `aigc-video`/`aigc-image` so locks, references, and grammar rules apply.
- Do not stack more than one form and three material words on a single effect.
- Do not write bare shot-size labels (远景/特写) as the tension mechanism; write the composition relationship instead.
- Do not apply full five-lever treatment to every minor action.
- Do not fight a verified strong model prior in text when an image reference or design-with-the-prior route exists.
- Do not invent new vocabulary when the verified lexicon covers the need; new words are hypotheses, verified words are assets.
