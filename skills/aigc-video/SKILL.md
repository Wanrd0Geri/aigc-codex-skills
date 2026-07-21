---
name: aigc-video
description: Use when the user wants a final ready-to-paste Seedance, Doubao, Dreamina-family, or explicitly platform-neutral video prompt from a brief, image/video references, script, storyboard, or project context; including text/reference-to-video, editing, extension, bridging, prompt optimization, duration compression, dialogue/lip sync, visible text, continuity, and Vibe/experiential direction. This skill owns the final video artifact and its protected language pass. Language-only cleanup of an existing platform-neutral prompt without new video production belongs to aigc-prompt-rewrite.
---

# AIGC Video

Own every final Seedance/Doubao/Dreamina-family prompt and every explicitly requested platform-neutral final video prompt. Combine expressive direction, production reasoning, platform adaptation when active, and protected language control inside one workflow.

## Personal defaults

Apply these defaults unless the current user instruction or active project overrides them:

- respond in Chinese and lead with the result
- use Seedance as the default platform when none is named
- deliver one final prompt in one fenced code block
- do not add music, subtitles, ambience, or action sound; preserve audio only when the user, active source, or project supplies it, and include spoken dialogue when dialogue or lip sync is requested
- preserve exact dialogue and request visible lip sync when dialogue is meant to be spoken on screen
- favor restrained performance and avoid unrequested gestures or automatic melodrama
- discuss meaningful creative uncertainty with the user instead of silently choosing a different interpretation

Precedence is field-specific: current user instruction > current readable-asset or literal-anchor facts > active project facts/defaults > personal defaults > platform defaults. An operational role, boundary scope, or borrowed dimension inherits the authority of the user/source/project that assigned it; it is not an independent evidence tier.

## 1. Establish ownership and task type

Identify the final artifact, platform/version, output mode, and one base production task kind:

- new text-to-video
- image or multimodal reference generation
- strict video edit
- video extension
- shot bridge or track completion

Record prompt optimization, project scope, Vibe, and A/B separately; none replaces the base production task. A project-bound extension is still `extension`; optimizing an edit command is still `strict video edit`.

A project-bound final prompt remains owned here. Consume the lightweight `VideoContext` from `aigc-project-context` as already compiled evidence, locks, references, and boundaries; map it directly into MotionSpec without rebuilding full cards or asking again about resolved fields.

Record Vibe as an expression request and A/B as an output request; neither replaces the production task kind. `按 Vibe 的方式向后延长@视频1` remains an extension and must use extension grammar.

If the user asks only to clean an existing platform-neutral prompt and does not want new video-production decisions, use `aigc-prompt-rewrite`. Creating a final platform-neutral prompt from a brief, script, storyboard, or project remains here. Cleanup or optimization of an existing Seedance/Doubao/Dreamina prompt also remains here. Do not apply Seedance markers or grammar to Kling, Runway, Pika, or another named platform; this skill does not claim their final adapters.

## 2. Gate evidence and assets

Build an evidence ledger and reference map before drafting:

- `available_readable`: the image/frame/video is present and can support visual claims.
- `anchor_only`: a literal `@...` anchor and its user-assigned operational role exist, but the asset is not visually readable here; a `reference_input` may also have supplied borrowed dimensions, and a boundary input may have a supplied boundary scope. Preserve the anchor and supplied facts; never claim unseen detail.
- `missing`: a required source or anchor is absent.

Pure text-to-video can proceed from the brief. Reference generation, editing, extension, and bridging require the relevant asset or literal anchor. If an unreadable asset's relevant boundary state, identity, composition, or motion is necessary and the user has not described it, explain the gap and ask for the asset or missing visible state. Use the source ending for `向后延长` / append-after and the first bridge input; use the source opening for `向前延长` / prepend-before and the second bridge input.

Preserve literal anchors such as `@图1`, `@视频1`, `@音频1`, and filename anchors exactly. Record each anchor's operational role before assigning transfer meaning: reference input, start-frame source, end-frame target, strict-edit target, extension source, or first/second bridge input. Only a reference input receives borrowed dimensions. A start/end-frame input receives a boundary lock scope; an edit target, extension source, or bridge input carries preservation, inherited state, or boundary obligations. These are not borrowed dimensions, and none of these anchors may be recast as a reference merely because it is an asset anchor. Give every identity/appearance reference subject one semantic label. Treat a user-supplied character name or group roster as a semantic lock, not as an identity dimension borrowed from the image unless the user explicitly authorizes that transfer. Add two or three stable identifying traits only when subject selection is ambiguous and those traits come from a readable asset or the user/source. For `anchor_only`, preserve the supplied label and facts without inventing identifying traits.

Read `references/video-contracts.md` for the Evidence Ledger, Reference Map, Lock Ledger, and MotionSpec.

## 3. Lock production facts

Classify fields before creative work:

- `exact`: literal anchors, names, dialogue, narration, lyrics, visible text, durations, edit intervals, shot ids/order, explicit ending cues, information markers, and user-retained numeric controls.
- `semantic`: identity/count, action order, pose and blocking, camera relationship, screen direction, composition, medium, asset operational roles, boundary scopes, borrowed dimensions, inherited state, and next-shot handoff.
- `mutable`: free descriptive language, supported atmosphere wording, and optional phrasing.
- `unresolved`: a choice that would create a materially different performance, action, composition, continuity state, or ending.

Vibe expression and language cleanup may change only `mutable` fields. Platform rendering may change syntax but not exact or semantic meaning.

A field becomes a semantic lock only when the current user, an authorized borrowed dimension, or an active source/project makes it necessary. Agent-designed camera, composition, micro-action, atmosphere, effect detail, and connective motion remain mutable until the user approves them or continuity requires them.

Separate world continuity from shot visibility. A subject, object, or place may continue to exist offscreen without being named in the delivered shot. For Seedance-family visual instruction prose, treat each concrete scene noun as a likely request to render or interact with it; keep offscreen continuity facts internal and externalize only their visible influence when causality needs support. Never apply this Seedance noun audit to protected exact spans such as dialogue, narration, lyrics, visible text, or literal `@...` anchors.

Keep internal control stricter than the delivered prompt. A restriction may enter the final prompt only when it is explicitly required by the current user, locked by an active source or project, required by platform grammar, needed to resolve a direct conflict among active references, or supported by an observed generation failure. Keep speculative failure prevention and `forbidden/unassigned` reference fields internal.

For an observed generation failure, read `references/failure-recovery.md`. Treat provider-documented troubleshooting as candidate checks for a controlled comparison, never as first-attempt defaults or universal model rules. Release and patch only the smallest evidenced field. If identical prompt text produces mixed results, treat the cause as unassigned generation variance and request a controlled rerun or more paired samples instead of changing the prompt.

## 4. Collaborate on creative uncertainty

Use proactive director-style communication when evidence is insufficient and two or more well-supported readings would materially change character motivation, performance, action, shot purpose, reference use, rhythm, continuity, or ending:

1. cite the user instruction, script, storyboard, or visible evidence
2. state your current understanding
3. name the meaningful alternatives
4. recommend one direction and explain why
5. ask 1-3 related questions together

Do not manufacture alternatives merely because an emotional scene contains nuance. When the user gives a clear direction such as restrained recognition on returning to an old home, translate it and proceed; a concise statement of understanding may be useful, but it does not require confirmation. Stop only for missing required assets, missing required exact dialogue/text, mutually incompatible hard locks, or an unanswered choice with near-equal readings that would create a materially different result. For a non-blocking gap, use the lowest-risk assumption and mention it only when it helps the user evaluate the result. Decide routine platform formatting and non-material technical details yourself.

Read `references/collaboration-and-performance.md` whenever performance intent is absent, inferred from project sources, or open to more than one meaningful interpretation.

## 5. Judge feasibility before writing

Decide one-shot versus multi-shot, action load, subject load, reference load, dialogue load, and duration fit.

- Keep one main action and one main camera strategy per generated shot.
- For clips of 15 seconds or less, favor one location, one action chain, one visual priority, and one ending beat.
- Treat every body part, prop, subject, and landmark requested in the same frame or boundary as part of its minimum framing envelope. If the requested framing cannot contain them, remove only mutable visibility detail or surface the hard-lock conflict; repeating the shot-size label does not resolve the geometry. A visible reframing may satisfy different envelopes over time when the camera move is allowed.
- Let a very short fast cut carry one instantaneous beat. Distribute a multi-stage action across cuts instead of making every insert repeat its onset, development, and result.
- If the user explicitly wants an ambitious integrated version, deliver it; briefly note the risk and optionally include a more stable alternative only when useful.
- Do not allocate exact seconds to every generated shot by default. Use event order or `前段 / 中段 / 后段`. Preserve exact timing for targeted source-video edits or explicit timing-critical requests.
- Keep the initiating action inside the generated window: entering, returning, opening, leaving, discovering, or turning must be visible rather than converted into backstory.
- For a first-generation attempt, use the minimum sufficient controls: identity, asset operational roles, active boundary scopes, authorized borrowed dimensions, material spatial relationships, locked action order, exact dialogue, and the required ending. Leave secondary motion, particles, cloth/hair response, effect micro-detail, and connective physics open unless they are source-locked or central to the request.

## 6. Build one canonical MotionSpec

Before platform wording, silently define:

- segment goal and viewer priority
- relevant start and terminal boundary states
- visual anchor and initiating action
- emotional vector and performance carrier
- medium/style, space, light, duration, and only active sound/text constraints
- reference map
- shots with sparse start/terminal boundaries, shot-level camera and action, inherited action phase when a cut continues the same event, performance, only material spatial causality, next-handoff subset, and only source-backed sound when active

Every platform render must derive from the same MotionSpec. For explicit A/B output, keep one shared fact-and-lock core inside the MotionSpec and attach two expression overlays. Only an unlocked field or an explicitly variant-scoped user instruction may differ in viewer priority, supported performance carrier, atmosphere phrasing, or rhythm; every shared user/source/project lock stays identical.

Use only the boundary and spatial fields that materially affect the shot. Read `references/video-contracts.md` for the compact BoundaryState structure.

## 7. Apply the minimum necessary expression work

Vibe is an internal expression method, not a separate artifact and not a strength slider. Choose one action:

- `preserve`: the prompt is mature or control-heavy; keep it and add no creative display.
- `polish`: the intent is complete but expression is stiff; clarify only supported performance, attention, or continuity carriers.
- `compose`: the user or project supplies an emotional/experiential intention but not yet a clear viewing center; translate it into visible action and performance after discussing any meaningful ambiguity.

User-supplied performance intent has highest authority. Otherwise use current storyboard/script evidence. Agent inference is allowed only as a bounded interpretation and must never become a source fact.

Translate inner intention into one primary visible carrier: body/contact point > gaze/attention > breath/pause > expression change > spatial distance/object handling > environmental or sound response. Use 1-2 micro changes and one visible endpoint. Do not add a flashback, new person, prop, symbol, event, or emotional reversal merely to express a feeling.

Read `references/vibe-expression.md` for emotional, memory, subjective, or experiential scenes. Skip creative re-composition for strict editing, extension, bridging, UI/tutorial/procedure, dense reference control, word-level sync, or a mature prompt the user wants preserved.

## 8. Normalize only mutable language

Before platform rendering:

- turn label or parameter chains into visual sentences with subjects and verbs
- convert supported abstract intent into visible posture, gaze, contact, distance, light, material, sound, or timing
- remove template voice, repeated boosters, decorative summaries, and unsupported off-screen causes
- preserve exact and semantic locks verbatim or semantically intact

Do not make the text longer merely to sound natural. Targeted edit/extension commands and mature prompts may need no normalization.

Read `references/language-lint.md` when the source contains AI-flavored prose, parameter stacking, abstract mood language, or the user requests natural wording as part of the final video artifact.

## 9. Render the platform prompt

For Seedance-family output, read `references/seedance-2-rules.md`. For strict edit, extension, or bridge tasks also read `references/seedance-2-video-operations.md`. Apply the task-specific grammar:

- new/reference generation: `参考@图N中的[borrowed dimension]` or `参考@视频N的[borrowed dimension]`
- start/end-frame generation: preserve each boundary anchor's start-source or end-target role and its authorized boundary scope; do not render it as a generic `参考` unless the same anchor also has an explicit `reference_input` role
- strict edit: address `@视频N` directly with `严格编辑` or the concrete change; do not say `参考@视频N`
- extension: address `@视频N` directly with `向前延长`、`向后延长` or `生成@视频N之后的内容`
- bridge: state source order and visible transition: `@视频1，[visible transition]，接@视频2`

For an explicitly platform-neutral final prompt, skip Seedance references, markers, and task grammar. Preserve the same MotionSpec and write only executable natural-language shots or one continuous segment, matching the user's requested structure.

For Seedance-family output, use official information markers when active: dialogue `{台词}`, sound `<音效>`, music `（音乐）`, subtitles `【字幕】`. For platform-neutral output, preserve exact dialogue/text and ownership in ordinary natural language without Seedance marker syntax. The user's or project's music/subtitle instruction overrides the personal default.

For new or reference generation with multiple assets, bind each reference-input anchor once in a compact paragraph before the shots. Give every identity/appearance reference subject a semantic name; add identifying traits only from readable or supplied evidence when subject selection is ambiguous. Render the dimension-specific Seedance wording from `references/seedance-2-rules.md`, then use semantic subject and effect names in the shot paragraphs. Repeat an anchor only when its borrowed dimension changes, a real ambiguity remains, or platform grammar requires it. Do not include start-frame sources, end-frame targets, edit targets, extension sources, or bridge inputs in this reference paragraph unless the user explicitly gives the same anchor a separate reference-input role. Do not translate the internal reference blacklist into user-visible exclusions.

Include audio wording only when the user requests it, an active source or project locks it, or spoken dialogue/lip sync requires it. If the user asks for no sound description, omit sound effects, ambience, music, and audio-policy wording throughout subsequent revisions; preserve any separately requested dialogue, lip sync, subtitles, or other visible text. The personal no-music/no-subtitle default prevents additions; it does not require the literal sentence `无配乐，无字幕` in every prompt.

For generated multi-shot prompts, start each segment with `镜头N：` followed by natural executable prose; do not force a separate shot-size fragment when framing is not material. In an ordinary subject-led shot, the first clause after `镜头N：` must name the subject or visual anchor and its core action/change; do not open that clause with shot size, angle, camera position, lens, or movement. Then add material space and camera presentation only when useful. Let space or camera lead only when establishing geography, delaying the subject reveal, or executing a camera-led effect is the shot's actual purpose. Treat clause order as a salience heuristic, not a guaranteed numeric model weight. Write only the visible beats that actually occur and affect understanding. A simple shot may need only `subject -> action` or `subject -> action -> endpoint`; add a shot size, main camera move, explicit start, direction, response, or terminal composition only when it changes or clarifies the shot.

Keep global locks consistent with per-shot wording. Load `references/shot-craft.md` for performance, camera movement, dialogue, or lip sync. For complex Seedance-family subjects, blocking, occlusion, offscreen causality, action paths, terminal composition, or continuity, load `references/single-segment-quality-control.md`. Load `references/failure-recovery.md` only for an observed Seedance-family failure or unstable prior result; load `references/task-patterns.md` only for a matching specialized pattern.

## 10. Validate and deliver

Run these checks in order:

1. exact-lock preservation
2. semantic-lock, asset-operational-role, boundary-scope, and borrowed-dimension preservation
3. per-shot visibility, framing feasibility, spatial causality, inherited action phase, terminal-frame, and handoff preservation
4. correct active-platform grammar and markers, or their absence in platform-neutral output
5. duration and complexity feasibility
6. language quality
7. control budget: no speculative negative list, internal blacklist, repeated anchor binding, redundant lock, or nonessential micro-control
8. no unauthorized invention or reference leakage

If a check fails, patch only the failed field and run the checks again. Never solve a local failure with a full rewrite.

Default delivery: at most one useful judgment or risk sentence, then one Chinese final prompt in one fenced code block. `prompt only` removes the wrapper but never skips internal validation. An explicit A/B request may return two labeled prompts from one shared lock core and two expression overlays in the same MotionSpec; only permitted unlocked or explicitly variant-scoped expression fields may differ.

## Failure recovery

| Trigger | First action | If unresolved |
| --- | --- | --- |
| Required reference state is unavailable | Ask for the asset or the exact visible state needed. | Do not invent visual continuity. |
| Required exact dialogue, narration, or visible text is missing | Ask for the missing literal content in one grouped question. | Do not invent or paraphrase it. |
| Two hard locks conflict | Explain the conflict and recommend which higher-priority field to preserve. | Ask one combined decision question. |
| Duration cannot hold locked beats | Compress description and camera complexity first. | Warn and deliver the requested integrated version or split only with user approval. |
| Bridge inputs exceed the current platform limit | State the exact input-count or combined-duration conflict. | Recommend staged bridges; do not emit one invalid command as executable. |
| Creative meaning has two valid readings | Show both readings and your recommendation. | Wait for the user's choice when the result would materially differ. |
| Platform/version is unspecified | Use the personal default. | Keep platform-specific claims out if no safe default applies. |
| A generated result shows one concrete failure | Load `references/failure-recovery.md` and patch only the smallest evidenced field. | If attribution remains ambiguous or prompt delta is zero, request a controlled rerun or more paired samples; do not globally tighten the prompt. |

## Avoid

- Do not create a separate Vibe draft unless the user explicitly asks for A/B.
- Do not invoke another language skill as a mandatory last pass.
- Do not rewrite dialogue, anchors, durations, edit intervals, shot order, or platform grammar to sound more natural.
- Do not add people, props, background business, symbols, or plot events to make a scene feel complete.
- Do not expose internal mode names, ledgers, or MotionSpec in the final prompt.
- Do not externalize speculative `must_not`, reference blacklists, or alternative-action inventories merely because the model might fail.
