# Diagnosis Rubric

Use this reference to decide whether a single AIGC shot frame should move forward, be repaired, or be redesigned.

The goal is not to score beauty. The goal is to prevent wasting production time on frames that cannot support the next step.

## Decision Matrix

| Dimension | Green | Yellow | Red |
|---|---|---|---|
| Story purpose | Clear shot function and emotional read | Readable but weak or generic | Unclear, empty, or contradictory |
| Subject readability | Main subject is readable at first glance | Subject exists but framing, contrast, or environment weakens it | Main subject cannot be read quickly |
| Composition and camera | Shot size, angle, crop, and depth support the purpose | Usable but weakens subject, emotion, or implied motion | Crop, pose, silhouette, or angle makes the frame unusable |
| Lighting and color | Motivated light, useful contrast, and coherent color mood | Direction is close but depth, hierarchy, or atmosphere is weak | Light, color, and exposure fight each other |
| Production design | Costume, props, setting, and materials belong to one world | Mostly usable but details feel random, cheap, or inconsistent | World, era, costume, props, or materials conflict at the root |
| AIGC control | Minor artifacts only; identity and structure are stable | Visible instability that can be repaired without changing the shot | Identity drift, malformed anatomy, broken structure, or severe artifacts |
| Video potential | Clear action, motion direction, camera possibility, or continuation | Video is possible but action path, camera behavior, or end state is vague | No plausible action, motion direction, or continuation when the target is video |

## Single-Point Red Blocks

Some Red findings can block the whole shot even if other dimensions look good.

### AI Can Judge Directly

Treat these as Red when clearly visible:

- Identity drift that changes the character.
- Malformed anatomy, broken hands, broken eyes, or impossible body structure.
- Severe artifacts that damage the subject or shot structure.
- Crop, silhouette, or pose that makes the frame unusable as a shot.

### Needs User Confirmation

Treat these as **Suspected Red** unless the user already supplied enough context:

- Story purpose is unclear.
- Main subject may not be readable at first glance.
- Video extension may be impossible or unmotivated.

Only check video-extension Red when the user's target is video. If the frame is only meant to become a still image, poster, concept art, or repair prompt, lack of motion is not a Red block.

Use this format for Suspected Red:

```markdown
状态：疑似 Red（需要确认）
原因：[specific visible reason]
请确认：[one concrete question the user can answer quickly]
```

Example:

```markdown
状态：疑似 Red（需要确认）
原因：主角和环境的明度接近，我能识别主体，但观众第一眼可能先看到背景。
请确认：你打开这张图的第一秒，视线先落在主角脸上吗？如果不是，建议判 Red。
```

## Production Status Rules

- **Green**: all core dimensions are usable, no Red block, and only minor repair is needed.
- **Yellow**: 1-3 important issues should be fixed, but the shot structure can survive repair.
- **Red**: at least one root-level block makes prompt writing wasteful.
- **Suspected Red**: likely root-level block, but final judgment depends on user intent or first-glance human perception.

Local prop issues, small material errors, minor background clutter, or small color mismatches should usually be Yellow, not Red, if the main shot structure remains usable.

## Recommended Paths

- **Direct edit**: Green or Yellow, still-image target, no video required.
- **Edit then video**: Yellow with a video target; repair the keyframe before Seedance.
- **Direct video**: Green with stable subject, clear action potential, and usable camera continuation.
- **Redesign first**: Red due to concept, shot design, or structural image failure.
- **Deep diagnose first**: the frame needs deeper visual analysis before a production decision.

## Boundary Note

This reference defines status and path criteria only. Use the main `SKILL.md` for routing language, output structure, and handoff summaries so the same boundary is not maintained in two places.
