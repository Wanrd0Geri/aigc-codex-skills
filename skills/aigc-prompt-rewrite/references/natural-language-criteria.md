# Natural-Language Prompt Criteria

Use this reference to judge whether an AIGC prompt is truly natural-language and director-style. Natural language is not a prose aesthetic; it is a control standard for visible, executable image or video generation.

## Core Definition

Natural-language prompt = complete visual sentences that organize source-supported facts into what the camera can see, what the viewer can hear, how the supplied subject acts inside the supplied space, and which existing continuity anchor matters when the shot must connect.

Director-style prompt = the wording a director could say to a camera, animation, lighting, or editing team: what the shot sees first, where subjects are, how action develops, how light or sound supports it, and where the shot lands.

## AIGC De-AI Is Not Prose Polishing

For this skill, removing AI flavor means making the prompt more generatable, not making it sound more like a human essay. The success test is whether the model receives clearer visual, motion, spatial, reference, and continuity control.

Do not add author voice, first-person commentary, jokes, personal opinions, literary reflections, or intentionally messy phrasing. Those may be useful in ordinary writing, but they weaken prompt control.

Convert AI-writing cliches only through visible controls already present in the source. The following are carrier categories, not permission to invent one:

- `这不仅是画面，更是情绪表达` -> retain a supplied posture, gaze, breath, distance, or contact point
- `通过光影展现命运感` -> retain supplied light direction, shadow, silhouette, path, or scale contrast
- `氛围拉满` -> retain supplied sound, movement, background reaction, light, or object motion
- `高级感/电影感/史诗感` -> retain supplied composition, material, depth, color, camera, or silhouette facts

If the source supplies no carrier and selecting one would change the creative result, ask instead of filling the gap.

Technical parameters may be removed when they are decorative or redundant, but production controls must survive: duration, shot count, shot labels, reference anchors, dialogue, action order, scene location, and continuity anchors.

## Pass Criteria

A prompt is natural-language enough when it meets these checks:

1. **Current-frame truth**: each claim is visible, audible, or established by a previous shot.
2. **Subject and verb**: important sentences name who or what acts, and what changes.
3. **Spatial relationship**: source-supplied foreground/background, left/right, near/far, or object relationships remain clear. Missing blocking is a question, not an invitation to assign it.
4. **Action order**: complex motion uses sequence words only when they clarify order: `先`, `随后`, `此时`, `紧接着`, `最终`.
5. **Visible carrier**: mood and quality words connect to a source-supported posture, gaze, contact, distance, light, material, sound, or movement; otherwise the gap is surfaced.
6. **Continuity anchor**: when connection matters, the prompt preserves one useful anchor such as pose, gaze, object position, light state, movement direction, or frame composition. Do not force an ending-state sentence into every shot.
7. **Scale control**: simple shots stay short; complex shots expand only to prevent misunderstanding.
8. **No AI-flavored padding**: the prompt avoids decorative boosters, rule-of-three filler, generic conclusions, and language that explains intent instead of describing visible action.
9. **Production-control preservation**: protected anchors, duration, shot count, dialogue, reference roles, and main action order remain traceable after cleanup.

## Off-Screen Causality Rule

Do not explain a visible effect with an off-screen source unless that source is visible in the current shot or already established.

- Weak: `风从山门方向吹来，带动他额前碎发。`
- Better when the source is not visible: `额前碎发被风轻轻吹开。`
- Better when the source is visible: `山门仍在他身后的远处虚化可见，画面深处的风带动他额前碎发。`

This rule also applies to sound, light, shadows, movement, and character attention. If the source is uncertain, describe the visible or audible result.

## Cut And Shot-Relation Rule

When a shot follows another shot, preserve how the source says the current view relates to the previous view if continuity matters.

- Weak: `镜头切到少年侧前方。`
- Better when all listed relations are supplied: `从上一镜头的山谷远景切到少年右侧前方的中近景，只保留他的上半身、右手和身后虚化的石阶。`
- Short version with the same supplied facts: `镜头来到少年右侧前方的中近景，只拍到他的上半身、右手和身后虚化的石阶。`

Do not over-explain the cut when it does not matter. The purpose is to prevent spatial confusion.

## Multi-Character Rule

For multiple subjects, clarify source-supplied identity, position, role, and interaction before writing group action.

Good multi-character prompts usually define:

- which literal `@...` reference anchor is used for each character or action
- where each character starts
- what each one wants or does in the beat
- who reacts to whom
- what path each character follows
- what visible arrangement the next beat needs to inherit, if continuity matters

If these fields are absent and materially affect the result, ask for them. Do not invent blocking, props, paths, or interactions to replace `热闹`, `顽皮`, or `灵动`.

## Style-Term Rule

Style terms can appear in the global setup when they constrain the whole output: `Unreal Engine 三维动画`, `古风木屋`, `非写实摄影`, `游戏过场动画质感`.

Inside shot bodies, retain visible evidence already supplied by the source—such as light direction, silhouette, material response, depth, motion, color, or prop interaction. Do not generate a checklist of new evidence merely to justify the style term.

Avoid repeating `高质量`, `高级感`, `电影感`, `cinematic`, or `Unreal Engine quality` in every shot. Repetition weakens control.

## Failure Signals

- The prompt can be rearranged as tags without losing meaning.
- Sentences contain many nouns and adjectives but few verbs.
- It describes feeling but not visible evidence.
- It explains a cause that is not visible.
- Characters are present but not spatially assigned.
- Camera movement is named but its subject relationship is unclear.
- The prompt forces a summary ending even when the generation task can naturally continue the action.
- The connected shot lacks a useful anchor even though the next view depends on pose, gaze, object position, movement direction, or light state.
