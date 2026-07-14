---
name: aigc-video
description: Use when the user wants a final, ready-to-paste Seedance, Doubao, or Dreamina-family video prompt, including text-to-video, image/reference-to-video, video editing, extension, shot bridging, project-bound shots, prompt optimization, duration compression, dialogue and lip sync, visible text, scene continuity, a Vibe/experiential version, or natural-language cleanup of an existing Seedance-family prompt. This skill owns the final supported-platform video artifact and combines expressive direction, performance translation, platform execution, and a protected language-quality pass. Explicitly platform-neutral language-only rewriting without a final video artifact belongs to aigc-prompt-rewrite.
---

# AIGC Video

Own every final Seedance/Doubao/Dreamina-family video prompt. Combine the useful parts of Vibe Creating, Seedance execution, and natural-language quality control inside one workflow. Never make the user move through separate Vibe, language, and platform skills.

## Personal defaults

Apply these defaults unless the current user instruction or active project overrides them:

- respond in Chinese and lead with the result
- use Seedance as the default platform when none is named
- deliver one final prompt in one fenced code block
- use no music and no subtitles; preserve dialogue, room tone, environment sound, and necessary action sound
- preserve exact dialogue and request visible lip sync when dialogue is meant to be spoken on screen
- favor restrained performance and avoid unrequested gestures or automatic melodrama
- discuss meaningful creative uncertainty with the user instead of silently choosing a different interpretation

Precedence is field-specific: current user instruction > current asset's assigned role > active project facts/defaults > personal defaults > platform defaults.

## 1. Establish ownership and task type

Identify the final artifact, platform/version, output mode, and one base production task kind:

- new text-to-video
- image or multimodal reference generation
- strict video edit
- video extension
- shot bridge or track completion

Record prompt optimization, project scope, Vibe, and A/B separately; none replaces the base production task. A project-bound extension is still `extension`; optimizing an edit command is still `strict video edit`.

A project-bound final prompt remains owned here. Compile the needed project facts and shot card first using the `aigc-project-context` contract, then continue to the final prompt in the same task. Do not stop at a user-visible handoff when enough information exists.

Record Vibe as an expression request and A/B as an output request; neither replaces the production task kind. `按 Vibe 的方式向后延长@视频1` remains an extension and must use extension grammar.

If the user asks only for explicitly platform-neutral language cleanup and does not want final platform structure, use `aigc-prompt-rewrite` instead. Cleanup or optimization of an existing Seedance/Doubao/Dreamina prompt remains here because the requested result is still a final supported-platform prompt. Do not apply Seedance markers or grammar to Kling, Runway, Pika, or another named platform; this skill does not claim their final adapters.

## 2. Gate evidence and assets

Build an evidence ledger and reference map before drafting:

- `available_readable`: the image/frame/video is present and can support visual claims.
- `anchor_only`: a literal `@...` anchor and its user-assigned role exist, but the asset is not visually readable here. Preserve the anchor and supplied facts; never claim unseen detail.
- `missing`: a required source or anchor is absent.

Pure text-to-video can proceed from the brief. Reference generation, editing, extension, and bridging require the relevant asset or literal anchor. If an unreadable asset's ending state, identity, composition, or motion is necessary and the user has not described it, explain the gap and ask for the asset or the missing visible state.

Preserve literal anchors such as `@图1`, `@视频1`, `@音频1`, and filename anchors exactly. Assign every anchor a semantic role immediately. Each role is an attribute whitelist; unassigned attributes cannot leak into the prompt.

Read `references/video-contracts.md` for the Evidence Ledger, Reference Map, Lock Ledger, and MotionSpec.

## 3. Lock production facts

Classify fields before creative work:

- `exact`: literal anchors, names, dialogue, narration, lyrics, visible text, durations, edit intervals, shot ids/order, explicit ending cues, information markers, and user-retained numeric controls.
- `semantic`: identity/count, action order, pose and blocking, camera relationship, screen direction, composition, medium, reference roles, inherited state, and next-shot handoff.
- `mutable`: free descriptive language, supported atmosphere wording, and optional phrasing.
- `unresolved`: a choice that would create a materially different performance, action, composition, continuity state, or ending.

Vibe expression and language cleanup may change only `mutable` fields. Platform rendering may change syntax but not exact or semantic meaning.

## 4. Collaborate on creative uncertainty

Use proactive director-style communication when evidence is insufficient and two or more well-supported readings would materially change character motivation, performance, action, shot purpose, reference use, rhythm, continuity, or ending:

1. cite the user instruction, script, storyboard, or visible evidence
2. state your current understanding
3. name the meaningful alternatives
4. recommend one direction and explain why
5. ask 1-3 related questions together

Do not manufacture alternatives merely because an emotional scene contains nuance. When the user gives a clear direction such as restrained recognition on returning to an old home, translate it and proceed; a concise statement of understanding may be useful, but it does not require confirmation. Stop only for missing required assets, mutually incompatible hard locks, or an unanswered choice with near-equal readings that would create a materially different result. For a non-blocking gap, use the lowest-risk assumption and mention it only when it helps the user evaluate the result. Decide routine platform formatting and non-material technical details yourself.

Read `references/collaboration-and-performance.md` whenever performance intent is absent, inferred from project sources, or open to more than one meaningful interpretation.

## 5. Judge feasibility before writing

Decide one-shot versus multi-shot, action load, subject load, reference load, dialogue load, and duration fit.

- Keep one main action and one main camera strategy per generated shot.
- For clips of 15 seconds or less, favor one location, one action chain, one visual priority, and one ending beat.
- If the user explicitly wants an ambitious integrated version, deliver it; briefly note the risk and optionally include a more stable alternative only when useful.
- Do not allocate exact seconds to every generated shot by default. Use event order or `前段 / 中段 / 后段`. Preserve exact timing for targeted source-video edits or explicit timing-critical requests.
- Keep the initiating action inside the generated window: entering, returning, opening, leaving, discovering, or turning must be visible rather than converted into backstory.

## 6. Build one canonical MotionSpec

Before platform wording, silently define:

- segment goal and viewer priority
- starting state and ending handoff
- visual anchor and initiating action
- emotional vector and performance carrier
- medium/style, space, light, sound, text, duration
- reference map
- shots with purpose, framing, camera, action chain, performance, spatial relation, sound, and end state

Every platform or A/B version must derive from the same MotionSpec.

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

For Seedance-family output, read `references/seedance-2-rules.md` and apply the task-specific grammar:

- new/reference generation: `参考@图N中的[assigned role]` or `参考@视频N的[assigned dimension]`
- strict edit: address `@视频N` directly with `严格编辑` or the concrete change; do not say `参考@视频N`
- extension: address `@视频N` directly with `向前延长`、`向后延长` or `生成@视频N之后的内容`
- bridge: state source order and visible transition: `@视频1，[visible transition]，接@视频2`

Use official information markers when present: dialogue `{台词}`, sound `<音效>`, music `（音乐）`, subtitles `【字幕】`. The user's or project's music/subtitle instruction overrides the personal default.

For generated shots, use `镜头N：景别。` followed by natural executable prose. Keep global locks consistent with per-shot wording. Load `references/shot-craft.md` for performance, camera movement, dialogue, or lip sync; load `references/single-segment-quality-control.md` for complex subjects, blocking, occlusion, or continuity; load `references/task-patterns.md` only for a matching specialized pattern.

## 10. Validate and deliver

Run these checks in order:

1. exact-lock preservation
2. semantic-lock, reference-role, and continuity preservation
3. correct task grammar and platform markers
4. duration and complexity feasibility
5. language quality
6. no unauthorized invention or reference leakage

If a check fails, patch only the failed field and run the checks again. Never solve a local failure with a full rewrite.

Default delivery: at most one useful judgment or risk sentence, then one Chinese final prompt in one fenced code block. `prompt only` removes the wrapper but never skips internal validation. An explicit A/B request may return two labeled prompts derived from the same locks and MotionSpec; only expression fields may differ.

## Failure recovery

| Trigger | First action | If unresolved |
| --- | --- | --- |
| Required reference state is unavailable | Ask for the asset or the exact visible state needed. | Do not invent visual continuity. |
| Two hard locks conflict | Explain the conflict and recommend which higher-priority field to preserve. | Ask one combined decision question. |
| Duration cannot hold locked beats | Compress description and camera complexity first. | Warn and deliver the requested integrated version or split only with user approval. |
| Bridge inputs exceed the current platform limit | State the exact input-count or combined-duration conflict. | Recommend staged bridges; do not emit one invalid command as executable. |
| Creative meaning has two valid readings | Show both readings and your recommendation. | Wait for the user's choice when the result would materially differ. |
| Platform/version is unspecified | Use the personal default. | Keep platform-specific claims out if no safe default applies. |

## Avoid

- Do not create a separate Vibe draft unless the user explicitly asks for A/B.
- Do not invoke another language skill as a mandatory last pass.
- Do not rewrite dialogue, anchors, durations, edit intervals, shot order, or platform grammar to sound more natural.
- Do not add people, props, background business, symbols, or plot events to make a scene feel complete.
- Do not expose internal mode names, ledgers, or MotionSpec in the final prompt.
