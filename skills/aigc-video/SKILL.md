---
name: aigc-video
description: Use when the user wants a final ready-to-paste Seedance, Doubao, Dreamina-family, or platform-neutral video prompt, or language-only cleanup of an existing video prompt. A generic AIGC prompt-cleanup request with temporal action, shot, duration, motion, audio, or endpoint cues routes here; artifact-ambiguous generic cleanup without temporal evidence routes to the image Skill's disambiguation gate. Covers text/reference generation,首尾帧, editing, extension, bridging, prompt optimization,白模,绿幕,多宫格分镜,智能编辑,高级编辑,超长视频,时间戳, dialogue/lip sync, continuity, dynamic-world interaction, previsualization, review, and failure recovery. This skill owns the final video artifact and its protected language repair.
---

# AIGC Video

Create one executable final video prompt from one protected production specification. Preserve source facts and continuity internally; render them through the active platform's grammar only at the end.

## Task routing — VIDEO-ROUTE-01

Choose the task path before loading references. Language-only cleanup reads `references/language-lint.md` and only the lock/ChangeSet/delivery sections of `references/video-contracts.md` and `references/change-impact-and-delivery.md`; preserve the existing grammar and do not enter generation, craft, duration, world, light, or structure-design passes. A source-preserving strict edit reads the source-operation, boundary, impact, and admission contracts; load craft/world/light detail only if the requested change or its dependency closure touches that field. New generation and structural work use the applicable rows below. An observed failure adds recovery to its base task path rather than replacing that path.

Load only the references required by that path. A section reference is sufficient; do not load a whole specialist merely to confirm that its field is unchanged.

| Condition | Read |
| --- | --- |
| Compilation: TaskEnvelope, evidence/locks, MotionSpec and admission; language-only: its protected spans and delivery only | `references/video-contracts.md` |
| Seedance-family generation; 2.0/2.0 Fast operations | `references/seedance-2-rules.md` |
| A named project, package, source lookup, or project shot range needs source resolution and has no validated VideoContext | Run `aigc-project-context` first; consume its VideoContext without rebuilding the source ledger. A self-contained pasted script/shot list stays local unless external project authority is needed. |
| Close combat, weapon exchange, spell clash, transformation or large technique needing new shot-level design, or a combat/VFX result described as flat, weightless, unclear, or lacking tension | Run the structure phase of `aigc-vfx-combat`; after this Skill resolves the canonical structure gate, resume its presentation/VFX/feasibility phase and consume a `design_ready` CombatHandoff |
| Any new/reference generation; any task that renders a structure-confirmation table; any edit, extension, or bridge that must inherit source world state; or any optimization that changes visible motion or physical interaction | + `references/world-dynamics.md` |
| Any new/reference generation; any task that renders a structure-confirmation table; any rebuilt visible unit; or any observed lighting/compositing mismatch | + `references/lighting-compositing.md` |
| Seedance version limits, duration, input counts, or feasibility | + `references/seedance-capability-matrix.md` |
| Strict edit, extension, or bridge | + `references/seedance-2-video-operations.md` |
| 白模、绿幕、多宫格、音色参考、局部标注或超长视频 | + `references/seedance-2.5-special-workflows.md` |
| Performance, camera movement, framing, optics, lighting, dialogue, lip sync, enriched cinematic visual specificity, a quality/style descriptor bundle for generation, or the cinematic 3D CG profile | + `references/shot-craft.md` |
| Complex blocking, occlusion, action handoff, or terminal composition | + `references/single-segment-quality-control.md` for extended checks; it consumes the core gate from `references/video-contracts.md` |
| Modifying, optimizing, or repairing an accepted/current prompt, shot, sequence, or shared field | + `references/change-impact-and-delivery.md` |
| The user requests or supplies a staging Diagram; an existing geometry asset needs role isolation or a route overlay; or direct asset binding still produces repeated geometry failure | + `references/blocking-diagram.md` |
| Product, UGC, already-designed or simple non-combat VFX, one-take, educational, or previsualization pattern | + `references/task-patterns.md` |
| Emotional, memory, or subjective intent | + `references/vibe-expression.md` |
| Multi-character dialogue/reaction; materially ambiguous motive; observed wooden/empty/overacted result; listener-dependent beat | + `references/collaboration-and-performance.md` |
| AI-flavored prose or an explicit natural-wording request | + `references/language-lint.md` |
| An observed failed or unstable result is supplied | + `references/failure-recovery.md` |
| Comparing with the observed 即梦 optimizer format or maintaining this Skill | + `references/seedance-2.5-optimizer-example.md` |

## Defaults and precedence

- Respond in Chinese and lead with the result.
- Default to 即梦 Seedance 2.5 when the request is not explicitly platform-neutral and names no platform or version. Use the 2.0 legacy rules only when the user explicitly selects 2.0 or 2.0 Fast.
- Every new, reference-generated, structurally rebuilt, extended, or bridged visible unit starts with `structure_status: pending` and `structure_review_mode: review_required`. An explicit current-user instruction to remove the structure-review pause sets `structure_review_mode: direct_authorized` for the named units in that logical request. A previously confirmed structure remains confirmed only while the current operation preserves its `structure_version`.
- Render through the admission contract `VIDEO-STATE-01` in `references/video-contracts.md`: each designed unit needs current-version confirmation or current-request direct authorization; a strictly source-preserving edit may instead use `source_preserved`. A review-required pending unit produces only the compact structure table and one grouped confirmation request. Direct authorization removes that table pause while preserving evidence, feasibility, Diagram-validation, and hard-conflict checks. Language-only cleanup uses its protected-delivery path.
- For new or explicitly recompiled platform artifacts, use plain upload-order labels under `VIDEO-LITERAL-01` in `references/language-lint.md`. Language-only cleanup preserves supplied handles, filenames, material labels, headings, and timing literally; it does not run this normalization.
- For every new/reference generation, keep subtitles and background music disabled as a user-owned standing lock; dialogue, narration, ambience, action foley, and effect sound remain available. Seedance 2.5 renders the exact final sentence `不添加字幕，不添加背景音乐。`; a platform-neutral or other maintained adapter preserves the same meaning in its own ordinary grammar. A brief, project/source field, or reference asset cannot activate subtitles or BGM while this lock stands. Change it only when the user explicitly asks to revise this standing Skill rule. Edit, extension, and bridge do not add new subtitles or BGM, but preserve already embedded source audio/text unless the operation explicitly removes it.
- Favor restrained performance and do not add unsupported people, props, gestures, emotions, or events.
- When the visual-specificity route is active, its pass is mandatory after structure resolves and before final rendering. It assigns concrete visible facts to existing owners; it is never a universal quality suffix and never claims to guarantee base image quality.
- Review world dynamics for every affected shot or operation segment. Resolve the review before delivery, then render an added world-response layer only when its selected mode materially improves the visible result. Source operations preserve driver, direction, disturbance, and residual phase through `EvidenceLedger` and `BoundaryState`.
- Review light/composite applicability and the audible plan for every generated, rebuilt, extended, or bridged visible unit. Physical scenes expose one shared light-response chain; explicit flat graphics, screen recordings, or black frames use the non-physical path in `VIDEO-LIGHT-01` without invented lighting. A scene or boundary light owns relighting over baked illumination in an appearance-only subject asset. Every unit retains one sound state.
- Enforce user-owned standing locks first; a current request changes one only when it explicitly asks to revise that standing rule. For every other field, apply authority as: current user > active project/source > explicitly authorized readable-asset dimension > personal default > platform default.

## Cross-mode safety contracts

Before compiling/displaying any structure row or rendering a final artifact, apply the shared contracts in `references/video-contracts.md`:

- **Delivery topology:** Apply the `DeliveryTopology` contract. The active adapter renders one unified continuous timeline by default and enforces current-state semantic closure; separate prompts are an explicit exception only.
- **Shot-timing topology:** For generation with readable or otherwise authorized shot timing, let each shot heading own its exact range. Inside the shot, express one current opening state, causally ordered action process, and visible terminal state without derived sub-ranges. Preserve an internal exact time only when the current user or readable authoritative source explicitly locks that time; never infer neighboring subdivisions. The unreadable-cut coarse-model exception uses ordered untimed shot headings, while edit/extension/bridge intervals remain owned by their operation grammar.
- **Visible-set/current-frame gate:** Run before every structure row is compiled/displayed and before every final shot/operation is rendered. Keep only what the camera can see from the current start through the terminal frame, what enters the frame, what visibly interacts, or what a visible response proves. World existence alone is not visibility. Apply this gate to simple, environment, object, previsualization, and complex shots alike.
- **Intent/fact gate:** Run before structure compilation/display and again before final rendering. A missing/unreadable fact blocks before the row only when the shot or visible structure cannot be identified reliably, competing readings change the structure/result, or a direct conflict, evidence-backed suspected typo, or capability mismatch changes the result. If the row remains reliable and only duration, exact dialogue, identity, or one material relationship is missing, write that field `待确认` in the same table and grouped question; this does not permit final rendering until resolved.
- **Change authority:** Apply `VIDEO-IMPACT-01` in `references/change-impact-and-delivery.md`: dependency invalidation requires rechecking, not permission to rewrite locked action; camera-only revisions preserve the subject performance while recomputing its visible projection.
- **Renderability gate:** Before delivery, give every active decision that materially changes the visible, audible, synchronization, performance, or continuity result one natural owner in the final artifact. Keep evidence ids, confidence, diagnosis, rejected options, and validation history internal. Never solve a missing output owner by printing the internal schema.
- **Light/composite and sound gate:** Before every generated, rebuilt, extended, or bridged structure row and before its final rendered unit, resolve `LightCompositeSpec` applicability under `VIDEO-LIGHT-01` and one current audible state. Appearance-only assets never own baked lighting. A shot without dialogue still states causal ambience/foley, explicit no-new-event, or locked silence; BGM is inactive for new/reference generation. If the current user explicitly requests omission of all sound-description prose, retain that audible state internally and omit only the forbidden per-shot prose; the standing no-subtitle/no-BGM sentence remains.

Detailed adapter, white-model, world-dynamics, impact, visibility, and language rules remain in their routed references; this section is the final admission contract, not a second procedure.

## 1. Classify the task

Record the platform/version, output mode, and one base task kind:

- new text-to-video
- image or multimodal reference generation
- strict video edit
- video extension
- bridge or track completion

Record optimization, project scope, Vibe, A/B, previsualization, and ultra-long mode separately. They do not replace the base task kind. Platform-neutral final prompts remain owned here but receive no Seedance-specific syntax.

For language-only cleanup of an existing video prompt, set `operation: language_only` and inherit its task kind, platform mode, structure, and production locks. Do not run a new structure review or platform redesign when no semantic or structural field changes. If the request also changes action, shot structure, material roles, timing, platform grammar, or another production decision, leave language-only mode and run the normal impact and delivery workflow.

Record per shot or generated operation segment:

- `source_shot_id`: optional project/storyboard/source identifier kept only for traceability
- `prompt_shot_index`: contiguous local output index beginning at 1 for the current rendered sequence
- `structure_source`: current_text | visual_asset | inherited | unresolved
- `structure_status`: pending | confirmed | source_preserved
- `structure_version`: incrementing integer for a designed structure; null for an unversioned `source_preserved` edit
- `structure_review_mode`: review_required | direct_authorized; null only for `source_preserved`
- `world_dynamics_review`: pending | resolved
- `world_dynamics_mode`: coupled_world | primary_action | intentional_stillness, when the unit generates or redesigns visible motion
- `light_composite_review`: pending | resolved | not_applicable, with `light_composite_applicability: physical | non_physical`; use `not_applicable` only under `VIDEO-LIGHT-01`. A preserving operation inherits unchanged source light/integration.
- `combat_design_required`: true only when the combat route applies
- `combat_design_status`: not_started | structure_ready | design_ready, when combat design is required
- `combat_structure_version`: the exact structure version bound to a design-ready CombatHandoff
- `scene_spatial_ref`: `scene_id@spatial_version`, only when a continuous multi-shot location uses a `SceneSpatialContract`

Structure fields are: shot size, frame crop, camera relation, POV viewpoint owner, and any deliberate camera move or optical zoom that changes the visible composition; one per-shot viewer priority, focal-plane/depth-of-field state, and any supported focus shift; visible roster with material primary/partial visibility and material offscreen presence; screen order, screen position, current subject world position, and depth placement; blocking-critical pose, facing, path, and occlusion; locked action, dialogue or narration owner, and visible endpoint. A pose is blocking-critical when it changes body footprint, crop, occlusion, contact geometry, route, locked opening/action boundary, or endpoint. Expressive posture inside the accepted blocking envelope belongs to performance. `声音` exposes the current shot's audible plan, but only its dialogue/narration owner is a structure field; exact wording, foley, ambience, music, silence, and sound-prose omission do not increment `structure_version` while that owner and every other structure field remain stable. `光影、合成与环境连续性` exposes visible integration and continuity without versioning structure unless its dependency closure changes a listed structure field. `structure_status` records versioned design state or explicit source preservation; it never implies acceptance without evidence. `structure_review_mode` records current-request delivery authorization. World-dynamics and light-composite reviews remain separate from both.

Set `structure_review_mode: direct_authorized` only when the current user explicitly removes the structure-review pause, for example 「跳过结构确认」, 「不用结构表」, or 「无需我确认，直接生成」. Scope a named instruction to its named units; scope a whole-request instruction to all affected units and rebuilt versions inside that logical request. The authorization remains active while required assets or hard decisions are collected, then expires after delivery, cancellation, or request replacement. It never becomes `confirmed`.

Delivery-speed and brevity requests such as 「直接给提示词」, 「尽快输出」, 「少解释」, or 「你自己决定」 keep `structure_review_mode: review_required`. A current request that both requires confirmation and removes it contains a hard instruction conflict; ask one grouped question. Silence keeps the default review mode.

An explicit user confirmation, or current project context that explicitly records acceptance of this exact version, marks the current `structure_version` as `confirmed`. A first source-video edit that creates no structural change uses `source_preserved` under `VIDEO-STRUCTURE-01`; it carries no invented version or acceptance record and does not require approval of unchanged source geometry. A supplied composition frame, storyboard, coarse model, white model, or staging map provides structure evidence while its acceptance remains unrecorded. A structural dependency change increments the affected unit's version and sets `structure_status: pending`. A later operation inherits confirmation only while it references the same version and preserves every structure field.

Project `context_status: validated` proves source integrity, not structure acceptance. Inherit `confirmed` from a VideoContext only when its `structure_acceptance` explicitly records `accepted`, the exact matching `structure_version`, and acceptance evidence.

For optimization, strict edit, or repair, inherit `confirmed` only when the impact audit preserves the accepted current structure version. Reopen only affected shots for a structural dependency, including camera viewpoint, material offscreen presence, a `SceneSpatialContract` change that alters visible structure, or another structure-bearing asset. Lighting or performance reopens only when its dependency closure changes one of the structure fields defined above. Read `references/change-impact-and-delivery.md` before deciding the range.

Extension and bridge create new visible material: the added segment or transition starts `pending`, while source boundaries inherit under `references/video-contracts.md`. A structure-preserving strict edit retains actual confirmation or uses `source_preserved`; a structural change creates version 1 from null or increments the affected interval's existing version. Apply the current request's review mode to each new or reopened unit, then use the shared delivery gate above.

## 2. Build evidence, material roles, and locks

Classify each asset as readable, label-only, or missing. Assign every supplied asset one operational role or retain it as evidence only. Never silently drop or merge an asset.

Keep supplied filenames, platform handles, UUIDs, and upload order so the material mapping cannot drift. `VIDEO-LITERAL-01` owns the output transformation: new/substantive compilation uses plain ordered labels by default, while language-only cleanup keeps every supplied literal. Do not apply one path's normalization to the other.

For new or reference generation, compile one material-responsibility map internally using `素材标签：具体用途`. Use the active platform adapter to decide whether that map must appear in the final prompt.

- When material responsibilities must be rendered, bind each material once under its owning field, then use semantic character, prop, and scene names in the timeline.
- Assign every fact to one rendered owner and bind each material once. The active platform adapter owns heading placement: for Seedance output, `references/seedance-2-rules.md` is the single source of truth for `主体：`/`场景：`/`风格：` ownership, subject-presence rules, and the coarse white-model opening sentence. Resolve equivalent layouts internally; never ask the user to choose among them.
- Name the exact borrowed dimensions; never write a bare `图片2：参考图`.
- Do not write `定义为` when one unambiguous subject already has a supplied name. Use `图片1中[稳定特征]的主体作为[角色名]` only when selecting among multiple subjects or merging several sources for one identity.
- If a material applies only to one interval, state that interval in its responsibility line rather than repeating the label in every shot.
- Keep unassigned dimensions internal. Externalize a targeted exclusion only for a user/source lock, an active personal default, a direct material conflict, a platform requirement, or an observed failure.
- Give each structural dimension in each shot or continuous scene exactly one active authority owner. Structural dimensions are topology/layout, blocking/route, composition/camera, timing/cuts, and boundary state. Other materials may supply only explicitly non-conflicting appearance, identity, wardrobe, prop, material, lighting, or environment dimensions. When two sources claim the same structural dimension and no stated priority resolves a material conflict, stop before the structure table and ask one grouped authority question; do not combine both by adding exclusions.

Classify facts as exact, semantic, mutable, or unresolved. Exact dialogue, visible text, material order and roles, durations, edit intervals, shot order, and explicit ending cues must not drift. Read `references/video-contracts.md` for the complete internal contracts.

Treat character identity, visible roster, material offscreen presence, screen order, foreground/background placement, occlusion, dialogue ownership, and source version as material production facts. When readable evidence does not resolve one of them, mark it unresolved and ask the user; never convert it into a bounded assumption.

## 3. Resolve duration and feasibility

For every Seedance 2.5 new or reference generation, obtain the intended total duration before final rendering. If it is missing, ask for it — grouped into the same round as the structure table when one is pending; do not invent it. This includes previsualization when the final prompt is expected to use the unified timeline formula. Exception: when a coarse white-model video supplies the whole clip's timing and cuts, inherit them without asking for or separately writing total duration. Reuse readable source shot ranges. When exact cut ranges are unreadable, preserve the source shot order and cuts, render ordered `镜头N：` entries without time ranges, and never invent seconds.

Judge action load, subject load, reference compatibility, dialogue occupancy, framing feasibility, world-motion load, and continuity internally before drafting.

- Keep one main action and one main camera strategy per generated shot.
- Preserve a user-supplied shot count and order.
- Let a very short cut carry one readable beat instead of repeating a full action cycle.
- Keep duration estimates and action-phase capacity internal. Do not turn them into shot-body timestamp ranges; simplify mutable action, camera, and descriptive load when a shot is crowded.
- For every material reaction or relationship turn, protect enough stable visible capacity for current trigger evidence when it occurs in the shot, a crop-readable change, and the terminal state to hold through the cut. If the trigger already occurred before the cut, inherit the reached current state and never replay it. If dialogue, body action, occlusion, or camera load competes with the change, remove mutable micro-cues and camera complexity first; if the locked beats still cannot fit, reopen only the affected structure.
- Do not delete or reorder locked beats to make timing fit. Compress mutable description and camera complexity first.
- Treat provider stability ranges as recommendations, not hard rejection limits. Read `references/seedance-capability-matrix.md` for exact hard limits and dated recommendations.
- **VIDEO-WARN-01 — sole warning authority:** Do not surface a generic `高负载`, cost, or split warning from character count, duration, shot count, reference count, or crossing an official recommendation alone. Intervene only when concrete script/prompt/material evidence exposes a missing required input, materially ambiguous wording, a result-changing conflict, a provider hard limit, or an evidenced feasibility failure. Otherwise simplify mutable density internally and continue. A recommendation is an internal risk candidate, not an automatic warning or approval. When concrete evidence leaves an executable stability tradeoff, give at most one relevant note; ask only when a hard decision or required fact remains unresolved.

## 4. Resolve structure review, then build one canonical MotionSpec

If the requested shot itself cannot yet be identified without inventing it—for example, the required start/reference image is absent or the user has supplied only an abstract theme with no visible anchor—ask for that prerequisite first. After it arrives, the shot still starts `pending`. When a meaningful row can already be built and only a field such as duration, exact dialogue, identity, or one material relationship is missing, put that field `待确认` in the table and combine the question with the same confirmation round.

Before compiling each row, run `VisibleSetGate` and `IntentFactGate` against the current crop, readable evidence, and authoritative facts. Treat `IntentFactGate` as a human-led reasoning safeguard: preserve the user's chosen result, actively test whether the script, current prompt, materials, and accepted facts form one clear executable specification, and neither invent objections nor obey a materially contradictory phrase blindly. If either gate finds a structural blocker or result-changing conflict, ask the grouped question before displaying a row; never place the blocked or unseen fact into the table. If it finds only a pending field and the row is otherwise reliable, write that cell `待确认` and include it in the same grouped question. When any affected unit has `structure_status: pending` and `structure_review_mode: review_required`, compare source-backed facts with the readable source and deliver one compact `镜头结构确认` table using exactly these columns:

| 镜头 | 构图与机位 | 画面重心 | 人物与空间 | 动作与终点 | 简短表演意图 | 声音 | 光影、合成与环境连续性 |
| --- | --- | --- | --- | --- | --- | --- | --- |

- Keep each cell to one compact clause by default. `动作与终点` may use one short causal action sentence plus its endpoint; `声音` may combine exact dialogue with one compact ambience/foley clause. Use `—` only in optional fields; `画面重心`, `声音`, and `光影、合成与环境连续性` remain populated for every generated, rebuilt, extended, or bridged row. Never paste source analysis, repair history, validation reasoning, repeated appearance, or a negative-control list into the table.
- `构图与机位`: shot size, angle, camera relation, viewpoint owner when POV applies, frame crop, and any material camera move or optical zoom. Distinguish an optical zoom from a dolly/track by stating its visible framing or perspective result.
- `画面重心`: one primary viewer priority, the material focal-plane/depth-of-field state such as a softly defocused background, and any supported shift of attention or focus. State what remains sharp and what softens instead of adding generic shallow-depth language. Keep secondary subjects only as causal, spatial, or scale support. This field is required for every row and belongs to `structure_version`.
- `人物与空间`: current visible roster and only execution-critical position, depth, facing, blocking pose, route, occlusion, or partial/offscreen presence. Record an offscreen person here only when their presence changes visible blocking, attention, or causality; an authoritative offscreen voice may remain solely in `声音`. Do not put action process, appearance/material description, motive, diagnosis, or exclusions here.
- `动作与终点`: current positive action chain and visible endpoint only. Put spoken content and its owner in `声音`; do not duplicate dialogue here.
- `简短表演意图`: the smallest source-backed acting direction needed to preserve the scene meaning and performance continuity; it may be a purpose, relationship, attention target, or emotional turn. Use `—` when the shot has no material acting beat. Do not prescribe gaze micro-movement, breath, fingers, or facial choreography at this stage.
- `声音`: every row states its current audible plan: exact dialogue/narration and owner when active, plus supported visible-action foley and active ambience at the smallest useful scope. Distinguish visible speech, offscreen speech, and voiceover from a separate lip-sync requirement using `VIDEO-SPEECH-01`. An authoritative offscreen voice does not require its speaker to enter the visual roster. If the shot has no supported audible event, write `无对白；无新增声音事件` or an explicit locked silence instead of leaving the cell empty. When the current user explicitly forbids all sound-description prose, write `按要求省略声音描述` in a displayed table, retain the state internally, and omit that per-shot prose from the final artifact. Never add BGM; sound effects remain allowed.
- `光影、合成与环境连续性`: for physical imagery, every generated, rebuilt, extended, or bridged row states the active source anchor, the shared subject/scene response, and one material contact, depth, atmosphere, or exposure cue that makes the composite read as one world; add continuity state only when material. Keep it as visible image language, not a software recipe or generic mood adjective. For explicit non-physical imagery, state its relevant flat-color, layer, edge, or black-frame continuity instead; do not invent a lamp, monitor, shadow, depth, or atmosphere to fill the cell. This cell does not version structure while the listed structure fields remain stable.

Use this table as the only review view of the MotionSpec. A mapping uncertainty may appear as `待确认` only while the row's structure remains reliable under IntentFactGate; a structural blocker or result-changing conflict blocks the row first. Return only the table plus one grouped confirmation request; fold missing duration, exact dialogue, or asset questions into the same round. Hold platform rendering, Diagram generation, detailed performance, optics, production-method detail, and dynamic receiver-chain enrichment until structure review resolves under the shared delivery gate; the compact light/composite relation and sound plan remain visible in the table.

For a revision after an accepted version, keep this same eight-column header but follow the delta format in `references/change-impact-and-delivery.md`; the first confirmation remains a complete table.

For a directly authorized unit, compile the same internal structure without displaying the table. Ask only for a required asset, exact input, or hard decision that prevents faithful compilation. Continue directly after that requirement is supplied while the same logical request remains active.

For a unit with `combat_design_required: true`, resolving the structure gate is not final admission. If its CombatHandoff is absent, only `structure_ready`, or bound to an older structure version, resume `aigc-vfx-combat` for presentation, optional VFX, and feasibility. Continue to final rendering only when the handoff is `design_ready` for the current version. A later user reply of “确认” resumes this specialist phase; it does not skip it.

When structure review is resolved for every affected unit, define:

- overall goal and visual priority
- internal material-responsibility map and whether it must be rendered
- subject facts, scene, style, light, and the complete per-shot sound/text plan
- the active duration rule and, when required, continuous non-overlapping shot-heading ranges; keep any explicitly locked shot-internal time as a separate exact fact rather than expanding it into a second timeline
- each shot's framing/camera, viewer priority, visible subjects and spatial relationship, current action phase, action/performance, camera's visible result, per-shot sound including dialogue/narration when active, light/composite integration, ending state, and next handoff
- when material, one source-backed emotional/experiential direction mapped to an observable starting state, any supported change, and endpoint rather than stored as an internal label
- for every materially acting-driven dialogue, reaction, or close shot, the source-backed `ActingTask`: what the character is trying to make happen or find out, the feedback they watch/listen for when relevant, any supported strategy turn, a start and endpoint that remain distinguishable in the chosen crop, the smallest crop-readable execution cue, and any relation/attention/intensity/decision state the next shot must inherit; omit this contract for a routine physical action whose meaning is already unambiguous
- for a design-ready CombatHandoff, its FightBeat order, contact/effect result, body or weapon mechanics, initiative change, presentation, authorized VFX, feasibility decision, and terminal boundary, mapped without redesign
- each unit's resolved world-dynamics mode and only the driver, necessary body mechanics, visible receivers, causal coupling, stability lock, or residual state selected by that mode
- global locks and only evidence-backed targeted exclusions

When a cut continues the same event, inherit the current phase, contact point, direction, and active effect state; advance the event instead of restarting it.

Run the world-dynamics review on this generation/detail path; language-only and untouched preserving-edit fields follow their routed exemptions. For a new, reference-generated, rebuilt, extended, bridged, or dynamics-redesigned visible unit, set the review to `resolved` only after selecting one mode: `coupled_world` for a valuable visible causal exchange, `primary_action` for the main action plus necessary body and prop mechanics, or `intentional_stillness` for stable fields plus one authorized activity beat. A materially required unreadable source fact for generation, extension, bridge, or dynamics editing keeps the review `pending` and the stage blocked.

Run `VIDEO-LIGHT-01` for every new, reference-generated, rebuilt, extended, bridged, or lighting-redesigned visible unit. First select applicability. Explicit non-physical imagery records `not_applicable` for the physical-light chain and checks its existing graphic/black-frame continuity. Physical imagery resolves only after one active source anchor produces a coherent subject or primary-surface response plus at least one currently visible integration cue from contact/nearby material, depth/atmosphere, or camera exposure. Add the other layers only when they materially affect the crop. A coherent text-only design may resolve as an assumption; an unreadable required boundary light or conflict between authoritative light sources keeps the review pending and the stage blocked.

A structure-preserving strict edit that leaves dynamics and lighting/compositing untouched may inherit both reviews; its preservation boundary carries the source state. Extension and bridge segments inherit their seam BoundaryState, then resolve both reviews independently. Read `references/world-dynamics.md` for evidence limits, driver placement, mode rendering, and continuity, and `references/lighting-compositing.md` for light authority and integration.

## 5. Render the final prompt

Enter this stage only when `VIDEO-STATE-01` admits every affected unit, required world-dynamics reviews are resolved, and light reviews are resolved or validly `not_applicable`. An unresolved physical light requirement cannot use `not_applicable`.

Run `VIDEO-DELIVERY-01` and `RenderabilityGate` against the complete current MotionSpec, then the selected delivered artifact in its declared replacement or standalone context. An active generation control with no rendered owner blocks delivery; an internal-only metadata field appearing in the executable prompt also blocks delivery. Repair the smallest ownership gap without duplicating the same fact elsewhere.

For a multi-shot request, render one complete command containing the unified timeline. Number its headings only with contiguous local `prompt_shot_index` values `镜头1` through `镜头N`, regardless of project scene/shot identifiers; keep each `source_shot_id` internal and never form headings such as `镜头10-5` or `镜头10-12`. Within each paragraph, restate the current visible subjects, spatial relation, action phase, camera-visible result, and terminal state needed to execute that interval. Do not use a prior paragraph as a state variable or output one prompt per cut unless the user explicitly requested separate prompts.

For generation, treat several movements inside one shot as one causal chain rather than a second timeline. Use current-state and causal language such as `开镜时`、`随后`、`当……时`、`过程中`、`最终`; let the model distribute those phases inside the heading range. Preserve an internal timestamp or frame cue only when the current user or readable authoritative source explicitly locks that exact timing; do not extend it into adjacent invented ranges or use timing as a speculative aid for natural motion.

### New and reference generation

Render through the unified generation structure in `references/seedance-2-rules.md`. That adapter is the single source of truth for Seedance heading order, timeline syntax, dialogue, sound, visible text, subject-presence placement, and the standing final subtitle/music sentence. Duration changes timeline density, not the grammar, except for the explicit coarse-white-model source-timing route in `references/seedance-2.5-special-workflows.md`.

Rules:

- Render one concise `画面重心` for every shot as the visible form of its current structure-resolved viewer priority; do not create a second explanation of the same idea.
- For a main camera movement, pair the term with its visible result. A self-explanatory fixed camera or shot size needs no redundant explanation.
- Apply the adapter's subject, scene, style, and timeline ownership without restating stable facts. Evaluate each world driver independently. Place a driver in `场景：` only when it remains active and useful across every shot in the complete generation command; otherwise place it in the owning `情节：` shots. A mixed sequence containing `primary_action` or `intentional_stillness` keeps its drivers local.
- When the `VisualSpecificityPass` in `references/shot-craft.md` is active, run its ownership and visibility pass before rendering these headings. Keep the selected profile phrase exact, replace empty quality language only with source-supported concrete subject/scene/shot facts, and otherwise remove it; remove any fact that the current crop cannot show.
- Apply `LightCompositeSpec` applicability after structure resolves. For physical imagery, bind each stable source anchor once at its smallest shared scene scope; keep a local, moving, or effect source in its owning shot. Then give each physical shot the current subject-facing response plus the smallest contact, nearby-receiver, depth, atmosphere, or exposure cue that proves the visible elements share one light system. Non-physical shots render only their relevant graphic continuity.
- Render a compact causal exchange for `coupled_world`; render the main action, necessary body mechanics, and necessary prop motion for `primary_action`; render stable fields and the sole authorized activity beat for `intentional_stillness`. Camera motion remains camera behavior.
- When an `ActingTask` materially controls the performance, render its playable task inside the owning shot in natural Chinese and attach the smallest visible execution cue. Preserve the protected visible capacity and a distinguishable start-to-end change selected by the performance references. Include the feedback check and strategy change only when the script or accepted scene supports them. Do not leave the task as hidden analysis, replace it with a facial-action list, or print field labels such as `目标`、`策略`、`反馈`.
- When a performance continuity anchor controls the next shot, write the inherited relation, attention, intensity, or decision as that shot's current cut-in state, then advance it. Do not write `同上一镜` or repeat the complete earlier ActingTask.
- Do not repeat material labels in the timeline after they have appeared in `主体：`, `场景：`, or `风格：`, unless the user supplies an exact time-scoped handle requirement.

### Edit, extension, and bridge

Do not force operational commands into the generation formula. Use their own compact stable formulas from `references/seedance-2-video-operations.md`:

- edit: target + change + interval + preservation boundary
- extension: source + direction + inherited boundary + new timeline + ending
- bridge: predecessor + visible transition + successor boundary

Return one complete operation command. A structure-preserving strict edit may render through either a genuinely inherited confirmation or the `source_preserved` admission; neither changes source structure. Extension, bridge, and any structure-changing strict edit render after structure review resolves for the new or reopened segment.

### Platform-neutral

Preserve the same MotionSpec, task kind, requested structure, and standing no-subtitle/no-BGM lock, but omit Seedance handles, markers, capability claims, and provider-specific command tokens. Render each platform-neutral operation through its own semantic formula in ordinary language: edit = target + requested change + interval + preservation boundary; extension = source + direction + inherited seam state + new segment + ending; bridge = predecessor ending + visible transition + successor opening. Add a preservation scope only where that operation could disturb an unchanged field; do not force an edit to invent a separate ending or flatten all three operations into one field list.

## 6. Expression and language

Preserve a mature prompt when its production meaning is already complete. Otherwise, after structure review resolves, translate emotional intent into visible body/contact, gaze, breath/pause, expression, distance, object handling, light, or sound response. Do not add flashbacks, symbols, people, or plot events merely to display emotion.

For language-only cleanup, follow `VIDEO-LANGUAGE-01` and `VIDEO-LITERAL-01` in `references/language-lint.md`, select preserve, micro-fix, or rebuild, and return the complete current prompt. The literal rule is the sole owner of normalization scope. Do not change task grammar or provider controls merely to sound natural.

Honor an explicit output-language and prompt-only contract. For bilingual output, render separate Chinese and English prompt blocks with identical production meaning, action order, locks, and endpoint; add no diagnosis between them. When a named platform has no maintained adapter or current verified official syntax, do not invent provider-ready grammar: request the current official syntax or offer a clearly labeled platform-neutral video prompt.

Use complete natural Chinese sentences inside the stable structure. Remove repeated boosters, background explanations that cannot be seen, and different wordings of the same lock. `结构固定` does not mean `每个字段必须写满`.

Before delivery, run one semantic complexity-recovery pass over every affected shot or sequence. Compare prior corrective clauses with the newest change and classify them as still active, supplemented, or superseded. Keep an active fact once, merge a supplement into the same current statement, and delete only wording whose meaning the new instruction actually replaces. Recency or similar wording alone never proves replacement. Preserve accepted locks and the final causal result, then remove duplicate micro-controls, repeated global facts, and diagnosis. Remove derived shot-internal timing only during new compilation or substantive recompilation; language-only cleanup preserves it under `VIDEO-LITERAL-01`. Prefer a positive current state; retain at most one local negative only when an observed failure cannot be prevented by an equivalent positive instruction. If replacement versus supplementation would materially change the result and is not uniquely inferable, route it through `IntentFactGate` instead of guessing.

## 7. Validate and deliver

Check in this order:

1. `VIDEO-STATE-01` admits each affected unit: a current confirmed/direct-authorized design, a valid `source_preserved` strict edit, or protected language-only delivery; every review-required pending design still waits
2. every combat-required unit has a design-ready CombatHandoff bound to the same current structure version
3. every source-backed structure or dynamic fact has been compared with its readable source; ambiguity remains unresolved rather than guessed
4. exact dialogue, text, duration, interval, shot order, material order, and roles are preserved; every material is accounted for and bound once
5. every visible character, animal, product, vehicle, or key prop has the adapter's required `主体：` owner; pure environment remains the only omission case
6. adapter structure and task grammar pass for timeline, dialogue, sound, visible text, edit, extension, bridge, or platform-neutral output
7. framing, viewpoint, deliberate camera move or optical zoom, focal-plane/depth-of-field state, visible roster, material offscreen presence, screen order, depth, occlusion, action phase, prop contact, endpoint, and handoff remain coherent; a camera cut has not rotated or repositioned subjects whose world-facing or position did not visibly change
8. required world-dynamics reviews are resolved; every visible-motion unit has the required mode; physical units have a shared light-response chain, non-physical units have a justified `not_applicable` physical-light review and relevant graphic continuity, and preserving edits carry source state without inventing one
9. no duplicate ownership, unsupported invention, stale asset fact, reference leakage, synchronized whole-frame motion, or decorative motion list remains
10. for applicable physical imagery, static optics and lighting direction are coherent; camera movement or a cut has not moved the world light source; appearance-only references have not imposed baked light; the subject or primary surface and at least one currently visible contact, nearby-material, depth/atmosphere, or exposure cue form the smallest complete composite relation for the crop
11. every modification passed the impact-closure audit and its delivery is at least one complete affected shot, complete affected sequence, complete prompt, or complete operation command
12. `agents/openai.yaml`, reference routing, and regression cases remain consistent after maintenance
13. delivery topology is correct: one unified multi-shot prompt by default, or separate prompts only under the explicit exception
14. every structure row and every final shot passed the visible-set/current-frame gate; no offscreen landmark, effect cause, or world region is present without a visible cue or interaction
15. every rendered shot has a current-state semantic closure and does not rely on relative prior-shot wording; global material identity/appearance is bound once and only current needed assets are restated
16. a coarse/white-model source locks order, readable cuts, camera/composition, spatial relations, route, key states, and visible endpoints while only evidence-supported in-between motion is completed; hard cuts are preserved and no shot/transition is invented
17. selected dynamic-world carriers and any requested visible-space progression are actually rendered in the affected timeline; no generic motion suffix or all-element animation remains
18. a revision has complete internal dependency closure and, when structure is incrementally delivered, visible delta markers and summary; unmarked fields are retained only after internal recheck
19. the intent/fact gate is resolved; any material conflict, suspected typo, or capability mismatch blocks final rendering until one grouped choice is answered
20. language lint leaves no empty evaluation adjective carrying control and no diagnostic/review explanation in the executable prompt
21. known/readable generation timing has one exact range at each shot heading, while the unreadable-cut coarse-model route uses ordered untimed headings; shot bodies use causal phase language and contain no derived sub-range, and every explicit user/source internal-time exception remains narrow and unexpanded
22. prompt shot headings use one contiguous local sequence beginning at `镜头1`; source/project shot ids remain internal traceability data and never replace the local heading index
23. every structural dimension has one active authority owner per scope; overlapping sources contribute only their explicitly assigned non-conflicting dimensions
24. every structure-table cell obeys its field boundary and compactness rule; every row has one `画面重心` and one `声音` plan, dialogue is not duplicated in `动作与终点`, no action process leaks into `人物与空间`, no software recipe leaks into `光影、合成与环境连续性`, and no repair history or exclusion stack remains
25. performance meaning, intensity, attention/relationship, and any continuity-critical visible cue agree with the script, current shot, and neighboring boundaries; every material `ActingTask` has protected visible capacity, a crop-readable difference between its start and endpoint, and a terminal hold inherited by the next cut when material; it appears in the final shot as playable task plus visible execution, with feedback/strategy turn only when supported, while routine action shots receive no invented acting loop
26. `VIDEO-DELIVERY-01` checks the complete current MotionSpec and the selected delivered unit; every active generation control has an explicit rendered owner at the smallest valid scope, including material experiential direction, shared relationship change, cross-shot performance state, and authorized beat synchronization; only continuity-critical endpoint/cut-in state is restated, needless duplicates are absent, and metadata-only reasoning remains outside the executable prompt
27. language-only cleanup preserves task kind, platform grammar, exact locks, semantic locks, structure version, action order, requested output language, prompt-only boundaries, and complete-artifact delivery; bilingual blocks have semantic parity, and an unsupported provider is never mislabeled platform-ready
28. Seedance new/reference generation without a whole-clip coarse white-model source begins at the first populated owning heading instead of a generic `生成一段N秒的……` summary; duration stays in shot-heading ranges, whole-clip medium/style stays in `风格：`, and any requested single-shot continuity is owned by the sole shot's camera clause
29. when visual specificity is active, every concrete appearance, surface, lighting, atmosphere, optics, focus, and crop fact has one visible owner at the smallest stable scope; the selected profile has not leaked into an unrelated style/task, and no generic quality or negative suffix remains

If a check fails, repair the smallest failed field internally and run the full affected-unit checks again. Never expose a field-only patch: re-render at least the complete affected shot, or the complete affected sequence/prompt/operation when the impact crosses that boundary. Default delivery is at most one necessary correction or feasibility sentence followed by the complete Chinese deliverable in one fenced code block.

## Stop conditions

Ask one grouped question and wait only when:

- a review-required structure version is pending
- a required asset or boundary state is missing
- a final Seedance 2.5 new/reference prompt lacks total duration and no coarse-white-model source-timing exception applies
- required exact dialogue, narration, or visible text is missing
- hard locks, camera relation, or visibility requirements conflict
- a materially required environment-dynamics field from a visual asset keeps its review pending
- two well-supported creative readings would materially change the result
- the intent/fact gate finds a structural blocker, direct conflict, evidence-backed suspected typo, or capability mismatch that cannot be uniquely resolved without changing the shootable result

When any stop condition applies, return no partial final prompt. For a conflict, collect all root conflicts in the affected request, cite the evidence, give the smallest distinct shootable options and recommendation, then ask once.

For a blocking conflict, scan the complete affected unit. Across its row and single request, state each root conflict once, give the smallest distinct shootable options (normally two), name the lock each changes, recommend one, and ask one choice—no restatement, serial rounds, or presentation-only variants.

## Avoid

- Do not create a second non-timestamped generation default; only the explicit unreadable-cut coarse-white-model route may use ordered `镜头N：` entries without time ranges.
- Do not subdivide a generation shot with inferred `4-6秒`、`17-18秒` or similar ranges merely to choreograph motion. Keep multiple phases causal unless exact internal sync is explicitly locked.
- Do not use `定义为` as routine boilerplate.
- Do not repeat material responsibilities inside every shot.
- Do not redesign a design-ready CombatHandoff through generic VFX task patterns or replace its contact/result mechanism with a visually adjacent one.
- Do not write the same camera, appearance, visual priority, or prohibition globally and per shot.
- Do not expose choices between synonymous wording, equivalent field layouts, or duplicate placements. Resolve them by field ownership and ask only when different outcomes or hard locks materially conflict.
- Do not expose EvidenceLedger, ReferenceMap, LockLedger, SceneSpatialContract, BoundaryState, MotionSpec, or internal status names in the final prompt.
- Do not infer character identity, visible roster, material offscreen presence, screen order, occlusion, dialogue ownership, or which similarly named asset is current when the evidence is insufficient.
- Do not treat `风吹、树叶摇曳、衣摆飘动、水面泛起涟漪` or similar motion nouns as a universal suffix. Select only existing receivers, connect them through one cause, vary response by material and depth, and keep the main action dominant.
- Do not animate every visible element, give unrelated objects identical timing, reverse an inherited wind or flow direction at a cut, or make all motion stop exactly when the subject stops.
- Do not append a generic quality, camera-brand, resolution, material, or negative-prompt tail. Run the conditional visual-specificity pass and keep only concrete facts with a visible owner.
- Do not narrate previous failures, revisions, tests, or debugging intent inside the current executable prompt.
- Do not route video-prompt language cleanup to a generic rewrite Skill or reopen structure when wording is the only changed field.
