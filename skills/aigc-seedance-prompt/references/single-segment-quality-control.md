# Single Segment Quality Control

Use this reference before finalizing any Seedance prompt. A long-form sequence only works if each segment can generate clearly on its own.

## Quality Order

Check the segment in this order:

1. Subject: the main subject has stable identity anchors.
2. Action: each shot has one main visible action.
3. Space: left/right, near/far, foreground/background, and key object positions are clear.
4. Camera: each shot has one shot size, one angle, and at most one main camera movement.
5. Emotion carrier: emotion is shown through gaze, pause, breath, hand movement, posture, light, or sound.
6. Readability: each shot has a clear visible action or state change when the action would otherwise be ambiguous.
7. Handoff: if this is part of a longer sequence, preserve only the posture, gaze, object position, movement direction, light state, or camera position the next segment must inherit.

If one of these is missing, fix it before adding style, atmosphere, or continuity details.

## Complexity Downgrade

When the requested shot includes multiple people, large action, occlusion, complex position changes, similar-looking subjects, or compound camera movement, simplify it:

- Split the action into more than one shot.
- Use fixed camera or one simple camera movement.
- Reduce the number of active subjects in the same shot.
- Keep the main subject's size and screen position stable.
- Give each important subject a position or prop anchor.
- Make the action readable before starting the next action; use an endpoint only when overlapping actions would confuse the model.

## Duration Budget

Before drafting, back-calculate how many readable beats the requested duration can hold. Do not compress too many actions into a short segment.

Rough timing:

- one readable action beat: about 2-3 seconds
- one camera movement plus one action: about 3-4 seconds
- one expression or attention transition: about 1-2 seconds on its own
- one object interaction with contact and reaction: about 2-3 seconds
- one multi-character handoff or chase beat: about 3-5 seconds

If the requested duration cannot hold all beats, split shots, reduce actions, or suggest extending the segment. Preserve the visible start state, main action, and necessary continuity anchor instead of squeezing several beats into one unreadable shot.

## Positive Motion Boundaries

Prefer positive boundaries over negative warning lists:

- `动作限制在画面中景范围内，主角只向前移动两步，主体大小保持稳定。`
- `镜头保持固定机位，人物从画面左侧前景走到中央，不改变朝向。`
- `两名角色保持前后关系，前景角色停在桌边，背景角色只抬头看向门口。`
- `UFO悬停在天空中央，下降幅度缓慢，光束落点保持在主人公前方地面。`

## Final Check

Before returning the final prompt, silently scan against the `Common Failures To Avoid` list in the main `SKILL.md`. In addition, verify these segment-level points:

- Each shot has one main action and one main camera movement.
- The duration can realistically hold the number of action, camera, expression, and handoff beats.
- The final shot includes a continuity anchor only when a next segment depends on posture, gaze, object position, movement direction, light state, or camera position.
- Subject identity anchors are stable (clothing, silhouette, prop, or position) for every important subject.
- Spatial relationships (left/right, foreground/background, near/far) are stated where they affect the action.

If anything is missing, fix it before adding style or atmosphere details.

## Minimal Example

```text
时长：8秒。夜晚开阔地，巨大的飞行器从云层下方缓慢下降，冷蓝色光束落向地面。@图1（飞行器外形与材质参考）作为UFO主体；@图2（环境与地表空间参考）作为地形、云层和光线基准；@图3（主人公外观参考）作为人物脸部、服装和体态参考。无配乐，无旁白，无字幕，无配音，仅保留环境风声、低频空气震动声和尘土被气流卷起的细小声响。

镜头1：4秒，远景。低角度固定机位贴近开阔地面拍摄，地面位于前景，云层和UFO位于画面中央上方。@图2（环境参考）的地面压在画面下方，远处云层被冷蓝色光线照亮。@图1（飞行器参考）的UFO从云层下方缓慢下降到画面中央，地面草叶被气流压低，少量尘土向外扩散，UFO的光束落点始终保持在画面中景范围内。

镜头2：4秒，中近景。机位来到主人公侧前方并缓慢推近，人物站在画面左侧前景，UFO光束落在画面右上方。@图3（主人公参考）保持脸部、服装和体态稳定，身体朝向天空中的UFO，衣摆被风向后带起，右手手指轻轻收紧。冷蓝色光线从上方照到主人公脸侧，他缓慢抬头看向光束，最后停在仰望姿态，身体仍朝向光束，为下一段走向光束的片段保留接点。主体识别稳定，空间关系清晰，动作承接清楚。
```
