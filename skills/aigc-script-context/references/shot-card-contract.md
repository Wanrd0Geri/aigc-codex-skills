# Shot Card Contract

Use a shot card to bridge script/storyboard context into video prompt execution.

## Required Fields

| Field | Purpose |
| --- | --- |
| 项目 | Project name and package used. |
| 集/场/镜 | Exact episode, scene, and shot ids. |
| 源优先级 | Which source wins if facts conflict. |
| 本镜剧情功能 | What this shot does in the scene: reveal, setup, reaction, transition, confrontation, proof, or handoff. |
| 上一镜承接 | Pose, object, gaze, movement direction, emotion, or location inherited from the prior shot. |
| 当前画面事实 | What the camera must see in this shot. |
| 人物表演 | Visible body, gaze, breath, expression, contact, pause, and action detail. |
| 对白/声音 | Spoken line, off-screen reading, environment sound, or silence. |
| 参考图角色 | Which attached image controls character, scene, composition, action, or lighting. |
| 估计时长 | Duration estimate based on visual complexity. |
| 下一镜交接 | Only the state needed by the next shot. |
| 禁止偏移 | Story, identity, staging, or performance errors to avoid. |

## Performance Translation

Replace abstract emotion with visible behavior:

- `紧张`: shoulders tighten, gaze avoids a target, hand grips an object, breath pauses.
- `克制震惊`: eyes stop moving, hand motion freezes, body leans back half a step.
- `温和权威`: voice stays low, body remains still, gaze stays on the listener, no exaggerated gesture.
- `听觉判断`: head turns slightly toward sound, hand pauses, body reacts before eyes or face do.

## Duration Heuristic

- 4-6s: one object action, one reaction, one static reveal.
- 6-10s: one acting beat, one short line, one clean camera move.
- 10-15s: multiple subjects, spatial reveal, VFX, dialogue plus reaction, or important transition.

When duration and content conflict, preserve the story function first, then simplify action and camera.
