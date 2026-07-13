---
name: aigc-vibe-creating-prompt
description: Use only when the user explicitly names Vibe Creating, VC, vibe, this skill, or asks for a separate Vibe version or Vibe A/B comparison of an AIGC video prompt. Ordinary atmosphere/emotion/memory requests without naming Vibe belong to aigc-seedance-prompt. Preserve anchors, dialogue, duration, action order, sound, and other hard constraints. Do not perform final Seedance formatting or image diagnosis. When explicitly invoked on UI demos or strict long-dialogue sync, preserve or route rather than creatively rewrite.
---

# AIGC Vibe Creating Prompt

## Position And Ownership

Vibe Creating (VC) is a platform-neutral expression layer for turning a clear video idea into a more coherent viewing experience. It strengthens the image center, emotional direction, key imagery, and experiential continuity without changing the user's facts or hard constraints.

Activate only when the user explicitly names Vibe, VC, this skill, a Vibe version, or a Vibe A/B comparison. Do not infer activation from words such as 氛围、情绪、记忆、电影感.

Keep artifact ownership strict:

- Final Seedance, Doubao, or Dreamina wording; reference-role mapping; video edit; extension; shot bridge; duration compression; lip sync; and platform execution belong to aigc-seedance-prompt.
- Language-only cleanup, 去 AI 味, or 导演讲戏式改写 without a separate Vibe artifact belongs to aigc-natural-language-prompt.
- Visual quality diagnosis belongs to aigc-visual-diagnose.
- VC owns only the platform-neutral experiential prompt or an optional Vibe comparison version.

A VC output may be the direct production candidate for a simple text-to-video scene. It is not merely an exploration draft. Complex execution work still hands its expressive core to the specialist that owns the final artifact.

Artifact wording wins over scene simplicity: any explicit request for a final Seedance, Doubao, or Dreamina prompt routes to aigc-seedance-prompt even when the scene itself is simple.

## Core Workflow

Follow this order. Do not run the information check before ownership and scene fit.

### 1. Gate Trigger And Artifact Owner

- If Vibe was not explicitly invoked, stop the VC workflow. Do not expose VC labels or analysis; continue with the proper specialist.
- If the requested artifact is a final platform prompt, route to aigc-seedance-prompt. Do not create a competing pseudo-final VC prompt.
- If the task is only language cleanup, route to aigc-natural-language-prompt.
- If the user explicitly requests both artifacts in the current turn, author the VC side here and use aigc-seedance-prompt for the execution side. Do not infer platform constraints inside the VC workflow; let the execution specialist apply its own confirmation and default rules. If the user asks for the VC side first or only, return that side plus one handoff sentence; omit the sentence when the same request says prompt only or 不用解释.

When the needed specialist is unavailable, provide only the platform-neutral VC artifact that is safe to produce and state the missing finalization step in one sentence.

### 2. Judge Fit And Choose One Handling Action

Choose the handling action internally; do not show classification codes.

| Fit | Typical input | Default handling |
|---|---|---|
| Native | emotional scene, micro-narrative, memory, subjective perception, one shared multi-shot experience | direct rewrite; light refinement or direct pass when already mature |
| Partial | brand or character showcase, stylized product display, creative idea mixed with execution language | light refinement or optional VC version |
| Low | UI demo, tutorial, industrial procedure, functional explainer, strict word-level dialogue sync | preserve as-is or light cleanup; do not force atmosphere |

Available handling actions are: 直接放行, 轻度提纯, 直接改写, 先补问, 原样保留, 可选 VC 版. These are decision states, not mandatory output labels.

Judge the scene goal before judging its wording:

- Precision-control language can still describe a native VC scene.
- Treat a prompt as mature only when it already states a visible subject, action or state, space, and tone; contains no internal conflict; and needs no technical cleanup. Pass it directly instead of rewriting to demonstrate effort.
- A partial-fit task keeps its commercial or functional intent. Do not add drama or story.
- A low-fit task does not trigger style questions merely because it invoked Vibe.

Use these tie-breaks:

- Native: direct pass when mature; light refinement when complete and only redundant wording or raw technical values need cleanup; otherwise direct rewrite when complete.
- Partial: light refinement when the requested cleanup can preserve the commercial or functional intent; use an optional VC version when experiential rewriting would change that intent or format.
- Low: light cleanup only when wording or action order is unclear. Route when another workflow owns the requested artifact; otherwise preserve.
- Any chosen rewrite with a blocking information gap becomes 先补问.

### 3. Lock Constraints Before Rewriting

CHECKPOINT — build a silent lock list before changing any text.

Lock all stated facts and dependencies:

- literal reference anchors and their assigned roles
- subject identity, subject count, relationships, location, medium, and required objects
- duration, aspect or format, shot count, shot order, action order, timing, ending state, and edit points
- dialogue, narration, lyrics, on-screen text, music, sound effects, silence, no-music, and no-subtitle requirements
- required structure, delivery format, forbidden changes, and any parameters the user explicitly asks to retain

Apply this priority:

1. User facts and hard constraints
2. Clarity and generation usefulness
3. VC expression

If VC expression conflicts with a lock, keep the lock. Offer an optional variant only when it does not confuse the requested deliverable.

### 4. Check Information Only For The Chosen Action

Ask questions only when an actual rewrite would otherwise require invention. Do not ask when routing, preserving, passing through, or lightly cleaning a complete functional instruction.

For a rewrite, check only:

1. Visible anchor — what must be seen
2. Main action or state — what happens
3. Local tone or experiential direction — how this moment feels
4. Shared relation — what connects multiple shots, when applicable

If a required item is missing, ask 1-3 short questions covering only the blocking gaps. For an abstract input such as 自由、高级感、很有力量, ask for a visible anchor, an action or state, and a style or use direction before drafting.

🔴 STOP — when any blocking gap remains, ask the minimum questions and end the turn. Do not draft until the user answers, unless the user explicitly requests a placeholder version.

Do not demand camera mode, medium, style, or theme when the visible anchor and main action or state are present and any applicable multi-shot relation is clear. A request to continue with placeholders or a skeleton counts as explicit placeholder authorization; a generic request to continue anyway does not. Without explicit authorization, preserve the source instead of filling gaps.

Treat local tone as blocking only when the user requests a creative rewrite but supplies no emotional or experiential direction. Do not turn tone into a mandatory camera style, medium, or platform format.

### 5. Rewrite At The Minimum Necessary Strength

Use the source's dominant force:

- Narrative: preserve event order, causal relations, and emotional turns.
- Emotion: strengthen environment, rhythm, texture, and felt state without adding a plot.
- Memory: preserve fragility, absence, recurrence, and time slippage without inventing flashbacks.
- Stream of consciousness: allow fragments while keeping every frame perceivable and the imagery internally related.
- Multi-shot experience: preserve segment order and the shared motif; keep the requested structure.
- Mixed refinement: retain useful execution information and remove only redundant explanation or the raw optical and equipment values defined in Step 6.

Make only supported changes:

- Clarify the visible subject-action-space relation.
- Concentrate attention on one image center and one experiential direction.
- Add no new subject, prop, relationship, backstory, plot turn, symbolic meaning, or emotional reversal.
- Do not inflate a short input into long prose.
- Keep a single clear scene concise; expand only when dialogue, timing, or multi-shot continuity requires it.

### 6. Translate Technical Controls Conservatively

Do not delete camera language wholesale.

- Apply camera translation only to light refinement, direct rewrite, or optional VC actions. For direct pass, preserve as-is, and route actions, leave camera wording untouched.
- If the user names camera controls to retain, keep those named controls exactly. A generic instruction such as 保留全部参数 freezes every supplied camera value; undeclared values still follow the next rule.
- If retention is undeclared during a rewrite, remove raw focal-length, aperture, shutter, ISO, exposure-compensation, and camera or lens model values. Translate only their supported effect on spatial breadth, subject separation, motion rendering, or brightness; do not reproduce the raw values.
- Preserve qualitative constraints — fixed camera, handheld movement, viewpoint, shot distance, and movement direction — verbatim by default. Translate their perceptual effect only when the user explicitly requests a fully experiential version; keep the same viewing relationship and direction.
- Shot labels may be removed only when their format is not protected and the original order remains unambiguous.

Preserve literal platform anchors beginning with @ exactly, including labels such as @图1, @视频1, @音频1, and file-name anchors. Never remove @, rename, translate, reorder, or replace an anchor with a generic phrase. Preserve the role assigned to each anchor.

Preserve audio wording, presence, absence, order, and timing. Never rearrange dialogue, narration, music, sound effects, or silence relative to actions unless the user permits it. If strict word-level sync defines the task, do not VC-rewrite it.

### 7. Run A Post-Rewrite Lock Audit

Compare the candidate against the silent lock list before delivery.

- Every locked fact must retain the same meaning, role, order, and timing.
- Verbatim-sensitive locks — literal anchors; proper names; quoted or spoken text; narration, lyrics, and on-screen text; numeric duration, aspect, shot-count, and timing values; all stated music, sound-effect, silence, no-music, and no-subtitle requirements; and explicitly retained parameters or format — must keep their exact wording or numeric value.
- No unsupported content may have appeared.
- The output must remain within VC ownership and must not imitate final platform formatting.
- The delivery mode must match the user's request.

If any check fails, correct the candidate before output. If correction would break another lock, return the preserved source or route the task instead of forcing a rewrite.

## Delivery Modes

Deliver the artifact first and use the least visible process.

After trigger and artifact ownership are resolved, choose among remaining mixed delivery requests in this order: Question Mode first when the VC side itself is blocked; an explicit A/B comparison second; an explicit prompt-only request third; Default Result-First Mode last. In A/B work, an execution-side blocker never suppresses a complete VC side. A final-platform-only request has already exited through Route Mode.

### Direct Draft Mode

When the user says 直接、只要提示词、可用于生成、prompt only, or otherwise asks for a ready candidate, output only the VC prompt. Do not prepend 判断、执行动作、输出结果, or internal routing language.

### Default Result-First Mode

Return the prompt or preserved text first. Add one short 说明 only when a technical control was translated, a hard-constraint conflict forced a weaker rewrite, the task is low-fit, or another specialist owns the final artifact.

### Review Or Comparison Mode

When the user asks for judgment, analysis, or reasons, show:

1. concise judgment
2. chosen handling action
3. VC result
4. only necessary constraint or handoff note

For A/B comparison, present both labeled artifacts only when the user requests both in the current turn and the execution specialist is ready to draft. If the user asks for the VC side first, return it plus one handoff sentence unless Direct Draft Mode was requested. If the execution side is blocked, return the VC version plus that specialist's minimum questions; if it is unavailable, return the VC version plus one missing-side sentence.

### Question Mode

When information is genuinely blocking, output only the 1-3 minimum questions. Do not surround them with a full diagnostic report.

### Route Mode

When another specialist owns the artifact, state the boundary and route in one concise sentence. Do not expose the VC workflow or provide a second deliverable unless the user explicitly requested both.

## Failure And Recovery

| Trigger | First action | If that still cannot satisfy the request |
|---|---|---|
| No explicit Vibe invocation | do not activate VC; use the proper specialist | ask only if artifact ownership is genuinely ambiguous |
| Final platform wording or complex execution | route to aigc-seedance-prompt | if unavailable, provide a platform-neutral VC core and mark the missing finalization step |
| A chosen rewrite lacks a visible anchor or action/state, or a shared-experience multi-shot rewrite lacks its linking relation | ask 1-3 blocking questions | use a bounded placeholder version only when explicitly requested; otherwise preserve the source |
| Hard constraint conflicts with creative rewriting | preserve the constraint and reduce rewrite strength | return the source or an explicitly optional variant |
| UI demo, tutorial, procedure, or functional explainer | preserve or lightly clean the instruction | route to the relevant execution workflow; do not add atmosphere |
| Strict long-dialogue or word-level sync | do not VC-rewrite the synchronized portion | extract only the separable visual portion when the user wants that |
| Mature prompt already works | pass through unchanged; classify any needed clarity fix as light refinement | explain nothing unless the user asked for a review |
| A requested shared-experience or continuity rewrite lacks a relation between shots | ask what links the shots | preserve separate segments and their order |

## Reference

Read references/seedance-official-vibe-guide.md only when the user asks for official Seedance Vibe guidance, official-style calibration, why Vibe works, a Vibe-versus-Seedance comparison, or style correction against the official method.

## Avoid

- Do not activate from ordinary atmosphere or emotion language alone.
- Do not make every prompt poetic, dreamy, nostalgic, or memory-like.
- Do not add relationships, plot, props, symbols, or emotional changes absent from the source.
- Do not overwrite hard constraints with creative preferences.
- Do not turn VC output into final Seedance formatting.
- Do not ask style questions for low-fit functional work.
- Do not expose internal fit codes, workflow steps, or mandatory wrapper labels.
- Do not rearrange sound or dialogue timing under the name of cleanup.
