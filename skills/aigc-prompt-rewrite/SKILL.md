---
name: aigc-prompt-rewrite
description: Use when the user already has a platform-neutral AIGC image/video prompt, visual core, or named-platform prompt and explicitly asks only to 改自然、改成导演讲戏、去 AI 味、去模板腔、去关键词或形容词堆叠, clarify visible subject-action-space logic, or review language executability while preserving production controls and syntax in place. Do not use as a mandatory final pass or to create or optimize a final media prompt. Final image-prompt generation, platform adaptation, settings changes, or optimization belongs to aigc-image; Seedance/Doubao/Dreamina and new platform-neutral final video prompts belong to aigc-video; project compilation belongs to aigc-project-context.
---

# AIGC Prompt Rewrite

Rewrite an existing prompt without quietly becoming its director, editor, or platform adapter. Natural language here means visible, audible, spatially clear, and executable—not literary, casual, longer, or more poetic.

## Ownership

Use this skill for one finished artifact: a language-cleaned prompt or a language review of an existing prompt.

Do not treat it as a universal finalizer. In particular:

- If the user asks for a final Seedance, Doubao, or Dreamina prompt, a new platform-neutral final video prompt, or cleanup of an existing supported-family prompt, let `aigc-video` own the result.
- If the user asks to generate, adapt, configure, or optimize a final image prompt for GPT Image 2, Nano Banana, Seedream, Midjourney, an unknown image platform, or multiple platforms, let `aigc-image` own the result. An existing image prompt stays here only when the user explicitly asks for language-only cleanup; preserve required syntax and inline parameters such as `--ar` and `--stylize` exactly where they appear. Any request to add, remove, reorder, or change those parameters belongs to `aigc-image`.
- If the user asks for a platform-specific final video outside the supported Seedance family, do not invent an adapter inside this language skill; use a current platform-specific workflow or official guidance. If neither is available, ask for the platform's current syntax or source, or offer to let `aigc-video` create a clearly labeled platform-neutral final prompt if the user accepts the artifact change. Never author that new prompt here or present neutral wording as a verified platform-ready prompt.
- If the user supplies an image and wants diagnosis, reverse reconstruction, or an edit prompt, use `aigc-image`.
- If the source is a script, storyboard, or shot list that still needs continuity and performance interpretation, use `aigc-project-context`, then let `aigc-video` own the final platform-specific or platform-neutral video prompt.
- If the user asks to actually generate or edit media, use the relevant generation capability instead of returning only rewritten text.

When the request combines language cleanup with a specialist final artifact, route to that specialist and complete the request there. Do not force the user through two separate passes.

## Core Rules

1. Preserve production meaning before improving prose.
2. Describe what the frame can show, what the viewer can hear, or what an earlier beat has established.
3. Connect abstract intent only to source-supported visible carriers such as posture, gaze, breath, contact, distance, light, material, sound, movement, or timing; ask when choosing a new carrier would change the creative result.
4. Keep useful platform syntax and remove only decorative prompt-engineering filler.
5. Make the smallest intervention that solves the real language problem.
6. Never invent plot, props, people, memories, symbols, camera moves, or emotional backstory merely to make the prompt sound richer.

Read `references/natural-language-criteria.md` when judging quality or explaining the standard. Read `references/rewrite-patterns.md` when a source contains tag stacks, abstract mood, unsupported causality, multi-character action, protected anchors, or multiple shots. Read `references/examples.md` only for teaching or unfamiliar output shapes.

## Workflow

### 1. Confirm the requested artifact

Separate a language-only request from a request for a final image, final video prompt, project card, diagnosis, or generated media. Route before rewriting when another skill owns the requested artifact.

If `改一下` or `处理一下` could mean either text cleanup or a different deliverable, ask one short question about the desired result. Do not ask about trivial wording choices that can be safely inferred.

### 2. Build a three-part lock ledger

Classify the source before changing it.

**Exact locks** must remain literal unless the user explicitly releases them:

- `@...` anchors, including ordered labels and filename anchors
- quoted dialogue, narration, lyrics, and visible on-screen text
- user-specified names, filenames, labels, and required syntax
- numeric duration, pause length, timestamps, edit intervals, shot ids, shot count, shot order, and executable ending cues such as an exact end pose, black frame, freeze, fade, or loop point

**Semantic locks** may be rephrased but not changed:

- subject identity and count
- main action order, scene location, camera relationship, movement direction, reference roles, and continuity anchors
- silence, dialogue ownership, lip-sync requirements, and other production constraints

**Editable language** includes:

- generic quality boosters and repeated style words
- template openings, explanatory conclusions, comma-chained tags, and prompt-engineering filler
- abstract mood labels whose meaning can be represented without changing the scene
- abstract evaluative endings such as `震撼收束` or `情绪升华` when they do not specify an executable visible or audible cue

If a span could be either a lock or decoration, treat it as a lock until the user clarifies.

### 3. Discuss consequential ambiguity

Talk with the user when a wording choice would change the creative result. State:

1. the most likely interpretation from the source;
2. the strongest plausible alternative;
3. the recommended choice and why;
4. one focused question.

Examples include incompatible visual media, an emotion with several materially different performances, an unclear reference role, or a vague command that would require inventing action. Continue without asking when the source, project context, or user's established preference already answers the question.

### 4. Apply the smallest useful intervention

Use these internal actions; do not expose them as a strength slider unless the user asks.

- **Preserve:** the prompt is already clear and executable. Return it unchanged or make only obvious copy edits.
- **Micro-fix:** repair local abstract phrasing, causality, spatial ambiguity, or repetitive filler while preserving structure. This is the normal case.
- **Rebuild:** the source is mostly unusable tags or lacks subject-action relationships. Reconstruct sentences from the same locks and stated intent; do not add creative facts. If more than one reconstruction is plausible, discuss it first.

For numbered or multi-shot sources, keep the same shot count and order by default. Do not split, merge, reorder, or add exact per-shot timing unless the user asked or the source already locks it.

### 5. Rewrite into executable language

For each important beat, make the following legible where relevant:

- who or what is visible;
- where it is in frame or space;
- what starts, changes, and ends;
- what another subject, object, light source, or sound is doing in response;
- which existing state must carry into the next beat.

Use sequence words only when they clarify real order. If a cause is off screen and not previously established, describe the visible or audible result instead. Put global medium or style constraints once in the setup rather than repeating them inside every shot.

Do not translate `电影感`, `高级感`, `宿命感`, or another abstract word into a fixed cliché. Choose a carrier supported by this specific scene. When that choice is creatively consequential and unsupported, discuss it with the user.

### 6. Validate before output

Run two passes:

**Lock pass**

- every exact lock is still literal;
- every semantic lock is traceable;
- no subject, prop, event, shot, camera move, or ending was added or lost;
- multi-shot structure and reference roles did not drift.

**Language pass**

- important sentences contain a visible subject and action;
- spatial and causal relations are understandable;
- abstract intent has a restrained visible carrier;
- repeated quality words, AI-writing clichés, and empty conclusions are gone;
- the result is no longer than needed for control.

If lock safety and smooth prose conflict, preserve the lock.

## Output

Write Chinese by default. Match another language or bilingual request when the user asks. Use one fenced block per requested language; never concatenate Chinese and English inside one block.

- For `只给提示词`, `直接出稿`, `prompt only`, or equivalent, output only the requested language label(s) and fenced prompt block(s), one block per language.
- For a routine cleanup, output one short heading and the requested language block(s). Do not add a generic diagnosis.
- If a consequential ambiguity remains, discuss it before presenting a supposedly final rewrite.
- For teaching, review, or comparison requests, explain only the concrete changes and show compact before/after examples.
- If the prompt is already mature, say so plainly and avoid expanding it to prove that work was done.

## Failure Recovery

- **Too vague to rewrite safely:** identify the missing visible variable and ask one focused question.
- **Mixed incompatible targets:** explain the conflict, recommend the dominant target, and ask before discarding one.
- **Broken or ambiguous anchor:** preserve it literally and ask what role it controls.
- **Final specialist artifact requested:** hand ownership to the appropriate AIGC skill; do not emit an intermediate rewrite as if it were final.
- **Prompt-only plus unresolved ambiguity:** ask first; once answered, return only the requested language block or blocks.
