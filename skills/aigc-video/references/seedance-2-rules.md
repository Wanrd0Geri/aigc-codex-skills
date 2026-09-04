# Seedance 2.5 Prompt Adapter

Use for Seedance-family generation and 2.0/2.0 Fast operations.

Source basis:

- [【即梦】Seedance 2.5 使用手册](https://bytedance.larkoffice.com/wiki/RXh5ww6EqighMdkVTMccm2d4n7e), document updated 2026-07-31 and checked 2026-08-02.
- Reusable observations from a user-supplied 即梦官网提示词优化助手 output, recorded in `seedance-2.5-optimizer-example.md` on 2026-08-03. They support plain colon headings, integer timestamp ranges, ordinary quotation marks for dialogue, and inline environmental/action sound. Treat them as one observed optimizer pattern, not universal mandatory grammar.
- [Volcengine, Doubao Seedance 2.0 系列提示词指南](https://www.volcengine.com/docs/82379/2222480?lang=zh), checked 2026-07-21.

Re-check version-specific limits after a provider update. Read `seedance-capability-matrix.md` for dated limits and recommendations.

## Material responsibilities

Use `素材编号（按上传顺序） + 具体用途`. Build this map internally. For Seedance new/reference generation, never render a generic `参考素材：` block: put subject-reference materials in `主体：`, scene-reference materials together with the environment in `场景：`, look/style references in `风格：`, and motion, camera, storyboard, audio, text, or time-scoped roles in their owning `情节` shot or active audio/text sentence. `主体：` is required whenever any character, animal, product, vehicle, or key prop appears anywhere in the clip. Omit it only for a clip that remains a pure environment or empty shot from beginning to end.

For one coarse white-model video that governs the whole clip, place one natural unheaded reference sentence before `主体：` and name only the dimensions actually borrowed. Put subject/prop correspondence in `主体：`; put an actual supplied or described environment in `场景：`; do not mention an absent scene, light, material, guide, or other unborrowed dimension merely to exclude it.

Default final labels are plain upload-order labels. Treat a supplied `@` handle, UUID, or filename as internal mapping evidence and normalize it to `图片1`、`视频1` or `音频1`. Preserve a literal handle only when the current user explicitly requests it for the current output. If upload order is unknown and the map matters, ask instead of guessing.

```text
主体：
图片1：罗大娘的外貌与服装。
图片2：苏云的外貌、服装与竹背篓。
图片3：仅补充苏云的浅白色瞳孔。

场景：
图片4：竹林山路的地形、晨雾与侧逆光。
```

- Give every material a specific job: identity/appearance, wardrobe, prop, environment, layout, light, material, action, motion, camera, timing, effect, audio, voice, text, or graphic.
- Consolidate all authorized jobs from the same material into one line.
- Bind materials once, then use semantic names in the timeline.
- Render `主体：` even when the opening frame is empty but a subject enters later. In a text-only case, use only the available stable description. Bind each material once, use semantic names afterward, and never ask the user to choose among equivalent field layouts.
- Use `作为[角色名]` only when selecting one subject among several or combining several sources for one character. Do not add routine `定义为` wording.
- A storyboard or multi-panel sheet must name its authorized dimensions such as shot order, framing, blocking, screen direction, and occlusion. Do not treat it as a generic style reference.
- A `staging_map` binds only its structure-resolved `composition` or `route` scope in the owning shot. Identity, style, environment, material, lighting, expression, and sound retain their normal owners. Follow `blocking-diagram.md` for direct-asset priority, versioning, and leakage checks.
- If one material applies only to a time interval, write that interval in the responsibility line.

## Unified generation structure

Use this ordered structure only after every affected shot passes the structure-delivery gate in `SKILL.md`. Use the same structure for every known-duration Seedance 2.5 new/reference generation. `主体：` is conditionally required by visible subject presence; omit the other optional headings when they have no material information. Never leave a heading empty or fill it with invented prose.

For two or more shots, multiple cut points, or a complete sequence, this structure produces one unified command with one `情节：` timeline. Separate prompts are allowed only for a single shot or an explicit user request for separate outputs. The timeline is not a set of independent prompt cards: each shot must restate its own current visible state, spatial relation, action phase, camera-visible result, and terminal state. Do not use `同上一镜`、`继续刚才`、`承接上一镜` or similar relative wording as a substitute for that state.

For each shot, declare only the fields relevant to its current visible set and execution: current visible semantic assets/subjects; current spatial relationship and state; current held, connected, or contacted object; current visible lighting result or light-source direction; current action phase; current dialogue/sound; and the visible endpoint. Omit absent optional fields; the required focus and light-composite relations remain visible, while only the audible prose may be suppressed under the explicit sound-description exception below. Bind global material labels and identity/appearance responsibilities once in their owning headings, then use semantic names in shot prose; never repeat `图片N`/`视频N` labels per shot. A pure environment shot receives no human-only fields.

```text
主体：
[required whenever any character, animal, product, vehicle, or key prop appears; omit only for a clip that remains a pure environment or empty shot throughout]

场景：
[optional: scene-reference materials plus time, location, the smallest shared stable topology, light, atmosphere, persistent ambience, and any driver/background baseline that remains active across every shot]

风格：
[optional: medium, palette, and shared rendering/material/texture behavior; local subject and scene surfaces stay in their owning headings]

情节：
[required]
镜头1（0-5秒）：[framing/camera]；[current visible state and space]；[current light/composite relation]；[action/performance and causal response]；[camera's visible result]；[visual focus]；[per-shot sound, including dialogue/narration when active]；[ending or handoff].

[standing final sentence for new/reference generation]
不添加字幕，不添加背景音乐。
```

Do not open with `生成一段N秒的……`. Duration belongs in the shot-heading ranges and remains an exact production fact. The explicit unreadable-cut coarse-model route omits those ranges instead of inventing them.

Never render a `全局补充：` heading. Put an owned whole-clip requirement naturally in `主体：`, `场景：`, `风格：`, or `情节：`. If a genuine cross-shot control has no better owner, append it once as a natural unheaded sentence after the last shot and before the standing subtitle/music sentence.

## Timeline rules

- Number rendered headings with contiguous prompt-local indices beginning at `镜头1`, even when source/project identifiers are `场10镜5`, `10-12`, UUIDs, filenames, or non-contiguous storyboard labels. Preserve that source-to-local mapping internally; never render `镜头10-5`、`镜头10-12` or another project id as the Seedance shot heading.
- Use `镜头N（开始-结束秒）：` for 5-second, 15-second, 30-second, and ultra-long outputs alike, except for the unreadable-cut coarse-white-model route below.
- The shot heading is the default owner of exact generation timing. Inside that shot paragraph, write `开镜时的当前状态 -> 连续因果过程 -> 可见终点` in natural causal prose and let Seedance distribute the phases across the heading range. A shot may contain several necessary action phases without becoming a second timestamped timeline.
- Do not infer or render shot-body ranges such as `4-6秒`、`6-8秒`、`17-18秒` from action complexity, planning estimates, keyframe spacing, or a failed result. Use `随后`、`当……时`、`过程中`、`落地后`、`最终` or equivalent observable transitions instead.
- A narrow exception applies only when the current user or readable authoritative source explicitly locks an internal second/frame time. This may govern an action or visibility change, dialogue, visible text, audio, VFX, or frame-accurate synchronization. Preserve only the stated time or stated subdivision and do not create neighboring subdivisions. Edit, extension, and bridge intervals follow their operation grammar rather than this generation-shot rule.
- Start at 0, use continuous non-overlapping ranges, and end exactly at total duration.
- Use integer-second boundaries by default. Never introduce decimals; preserve them only when the current user or an exact source explicitly requires sub-second timing.
- If locked shot count and duration cannot give every shot a positive integer range, ask for a longer duration or restructuring permission instead of using decimals.
- Use frame ranges only for frame-accurate sync, and state the active frame rate and total frame count.
- Keep one readable beat and one main camera strategy per shot. A short cut may carry an instantaneous state or action phase. Render each shot through its resolved world-dynamics mode.
- Shots use semantic names and state only visible changes or continuity-critical inheritance.
- Each shot paragraph is executable in isolation from its current frame through its terminal frame. Describe inherited facts as present current state (for example, an already-open door or an already-connected beam), never as an instruction to consult an earlier shot. Keep the full command unified while keeping per-shot semantic closure.
- When a dialogue, reaction, or close shot has a material `ActingTask`, write its playable task inline with the smallest visible execution cue. Add what feedback the character checks and how the strategy changes only when those turns are source-backed. Do not output `目标：`、`策略：` or another analysis label, and do not replace task logic with an expression list.
- When a performance continuity anchor controls the shot, state the inherited relation, attention, intensity, or decision at cut-in before advancing the performance. Do not output the anchor label or repeat the full earlier task.
- When an authorized audio/video rhythm materially controls a visual event, state the event's causal alignment to the relevant strong beat, rhythm change, speech turn, or sound cue in the owning shot. Mention the material label only at its single binding point; rhythm-only borrowing does not authorize the source music, lyrics, or background audio.
- When a cut continues one event, state the inherited phase and advance it. Do not repeat approach, wind-up, launch, contact, or another completed onset.
- For previsualization, use the same timeline formula once total duration is known; establish the selected representative state at cut-in.
- For a coarse white-model video, inherit the source duration, shot order, and cuts without asking for or separately writing total duration. Reuse exact ranges only when they are readable. When the cut ranges are unreadable, preserve the source order and cuts and render `镜头1：`、`镜头2：` in order without time ranges; this explicit exception overrides the normal timestamp formula and never authorizes invented seconds.
- Every final shot states a compact framing/camera relation from its resolved source authority and the current visible spatial relation. A generic whole-clip reference sentence never substitutes for either field in an individual shot.

## Shot sentence order

Use this stable order:

1. shot size, angle, and camera mode
2. subject's current visible state and material spatial relationship
3. current subject/scene light-composite relation at the smallest visible scope
4. action, performance, local body/material/environment coupling, and causal response
5. main camera movement and the visible result it creates
6. one visual focus and any supported attention/focal-plane shift
7. per-shot sound: dialogue/narration, causal foley, active ambience, or explicit no-new-event/silence; render spoken content here once rather than duplicating it in the action clause, and never add BGM
8. ending state, residual world motion, or next-shot handoff

Do not omit visual focus, per-shot sound, or the current light-composite relation for a generated, rebuilt, extended, or bridged visible unit. Keep each concise. The sole sound exception is a current-user request to omit all sound-description prose; retain its audible state internally and omit only that prose. Other irrelevant fields may be omitted. A self-explanatory `固定机位` needs no restatement; a push, pan, crane, optical zoom, rack focus, orbit, or track should state what becomes larger, smaller, revealed, hidden, sharp, softened, compressed, expanded, or repositioned. Never substitute a dolly/track for a locked optical zoom.

## Audio and visible text

Use the natural-language pattern demonstrated by the observed optimizer example:

- dialogue: `角色说道：“台词。”`
- persistent ambience: establish it inside `场景：`, then state its current audible presence compactly in every shot
- local sound effect: write it inside the relevant shot and tie it to its visible cause
- subtitles and BGM remain inactive under the standing user lock; diegetic visible text keeps its separate text owner

Do not create a standalone sound section. Every generated, rebuilt, extended, or bridged visible unit must contain one audible clause. When it has no supported dialogue, narration, foley, or ambience change, state `无对白，无新增声音事件` or the source-locked silence rather than inventing one. A current-user request for silence still renders the locked silence; a request to omit all sound-description prose retains the plan internally but suppresses only that per-shot prose. Preserve exact dialogue and speaker ownership. Keep the mouth visible when lip sync matters. Sound effects are allowed; BGM is not.

Within the dialogue, narration, ambience, foley, and effect-sound fields allowed by the standing lock, use this authority for the audible plan: current user -> active project/source -> a low-risk sound directly caused by the visible action or environment -> explicit no-new-event/silence. Rain, a visible footstep, cloth contact, a door, water, or an impact may supply its ordinary causal sound when the current shot shows that cause. Do not invent an offscreen crowd, animal, vehicle, device, alarm, voice, music, or story cue merely to fill the cell.

For every Seedance 2.5 new/reference generation, always end the prompt with the standalone sentence `不添加字幕，不添加背景音乐。` outside any heading and do not attach it to the final shot. This is a user-owned standing lock, not a fallback: a brief, active project/source, reference audio/text, or request-local content instruction cannot remove either clause or activate subtitles/BGM. Only an explicit request to revise this standing Skill rule may change it. `不添加字幕` bans subtitle overlays, not source-backed signs, logos, titles, or other diegetic visible text. `不添加背景音乐` does not suppress dialogue, narration, ambience, action foley, or effect sound. A request to omit sound-description prose suppresses only per-shot sound prose and does not remove this final sentence. Edit, extension, and bridge preserve already embedded source audio/text under their operation rules, add no new subtitles or BGM, and never receive this generation sentence automatically.

For visible text, state exact content, timing, frame position, appearance method, and only necessary style. Use a dedicated material responsibility for exact logo, typography, or layout.

## Control and repetition

- Evaluate each world driver independently. Put one in `场景：` only when it remains active and useful across every shot in the complete command. Put a partial, changing, or mixed-mode driver and its local response in the owning shot. Operation commands keep seam dynamics inside their operation grammar.
- Render `coupled_world` as one compact cause and selected response chain, `primary_action` as the main action plus necessary body/prop mechanics, and `intentional_stillness` as stable fields plus the sole activity beat. Do not render a `世界动态：` or `环境动态：` heading.
- Render each active stable-topology fact once at the smallest common scope. Multiple locations keep their topology with their owning shots or segments. Keep internal contract names out of the final prompt.
- Put per-shot visibility, blocking, occlusion, action phase, dialogue, and ending in the timeline.
- Apply `VisibleSetGate` to every shot, including pure environment and object shots. Do not write a character field, human body cue, gait, clothing, or hair for a shot whose current visible set contains no such subject; a pure environment clip may omit `主体：` entirely, and an environment/object interval inside a mixed clip receives only its visible environment/object facts.
- Treat confirmed viewer priority and rendered `画面重心` as one field, and render it once in every shot.
- Apply `LightCompositeSpec` from `lighting-compositing.md`: bind a stable source anchor at its smallest shared scope and keep a local, moving, or effect source in its owning shot; every shot owns its current subject-facing response plus the smallest contact, nearby-receiver, depth, atmosphere, or exposure cue needed to show one shared light system.
- Do not repeat a material label, global scene description, world driver, character appearance, camera rule, or negative instruction in every shot.
- Do not repeat exact timing inside a shot after its range is established in the heading unless the explicit internal-time exception applies.
- Do not use a generic suffix such as `微风吹动衣摆和树叶，水面泛起涟漪`. Select only visible receivers, connect them to one supported cause, and vary timing and amplitude by material and depth.
- A longer prompt is acceptable when it adds distinct executable information. Different wording of the same fact is redundancy, not stronger control.

## UI parameters

Keep resolution, frame rate, and aspect-ratio settings outside the prompt when the UI exposes them. If the user requires an aspect ratio inside an ultra-long prompt, place it in `场景：` without adding a duration-specific section. Never infer it.

## Seedance 2.0 legacy note

When the user explicitly selects 2.0 or 2.0 Fast:

- keep the same protected facts and material-responsibility map
- preserve user-supplied timing, but do not promise 2.5-level second accuracy
- apply the 2.0 limits from `seedance-capability-matrix.md`
- do not expose 2.5-only modes such as ultra-long generation or advanced editing as available
