---
name: aigc-vibe-creating-prompt
description: Use when the user explicitly calls this skill or asks for Vibe Creating, vibe-driven AIGC video prompts, atmosphere, emotion, imagery, memory, subjective feeling, or experiential continuity. Preserve anchors, dialogue, duration, action order, sound, and other hard constraints. Do not use for final Seedance formatting, image diagnosis, UI demos, or strict long-dialogue sync.
---

# AIGC Vibe Creating Prompt

## Core Position

Vibe Creating is a creative production entry and optional exploration layer. Its goal is to preserve the user's real expressive intent while making the prompt easier for a video model to understand through image center, emotional direction, key imagery, and experiential continuity.

Use it when the user wants a more atmospheric, emotional, memory-like, image-driven, or experiential video prompt. It can be used directly as a production candidate for simple text-to-video scenes, and it can also provide the expressive core for a later Seedance final prompt. Do not use it as the universal final layer for complex reference mapping, video edit, extension, strict lip sync, or project continuity work.

## Quick Start

收到用户输入后，按三步执行：

1. **先判断是否适合 VC**：识别这是不是一个适合通过创意转写放大效果的场景。
2. **再判断当前怎么处理最合适**：直接放行、轻度提纯、直接改写、先补问、原样保留，还是提供可选 VC 版。
3. **信息不够时反问、补充**：只问完成当前动作所必需的信息，不为了分类本身反复追问。

CHECKPOINT - VC Fit And Constraint Gate:

- If the user did not explicitly call this skill or ask for VC/vibe-style expression, do not take over another AIGC skill's job.
- If final Seedance/Doubao/Dreamina formatting, exact reference mapping, platform execution, video edit, extension, or shot bridge is the main request, hand off to `aigc-seedance-prompt`.
- If the user asks for pure text-to-video with atmosphere, memory, emotion, imagery, or subjective feeling, this skill may produce the production candidate directly; mention Seedance handoff only when the user asks for final platform formatting or A/B comparison.
- If any hard constraint conflicts with a vibe rewrite, keep the hard constraint and make the VC version optional.
- If the input lacks a visible anchor, action/state, or tone, ask the minimum questions before rewriting.

## Scene And Expression Judgment

先根据场景判断（S）确定是否适合 VC，再结合表达判断（E）确定处理方式。信息密度检查（I）优先于具体动作：只要关键信息不足，就先补问，再进入对应动作。

### S1: VC 原生适配

- **E1: 接近 VC 表达**  
  默认 **直接改写**；若原文已成熟，可改为 **轻度提纯** 或 **直接放行**。
- **E2: 混合表达**  
  默认 **轻度提纯后再改写**，保留有效结构、叙事顺序和情绪推进。
- **E3: 精准控制表达**  
  识别为 **可 VC 转译**；不因执行写法直接拦截。去掉低价值技术控制后，转成更利于生成的自然画面表达。

### S2: VC 部分适配

- **E1: 接近 VC 表达**  
  默认 **轻度提纯**；如原文已足够可用，可 **直接放行**。
- **E2: 混合表达**  
  默认给出 **可选 VC 版**，让用户决定是否采用更强体验化表达。
- **E3: 精准控制表达**  
  默认 **保留原意**，并说明如需要可额外提供一版 VC 转写。

### S3: VC 低适配

- **E1: 接近 VC 表达**  
  尽量 **贴近原意**，不强行 VC 化；必要时 **原样保留**。
- **E2: 混合表达**  
  优先 **原样保留** 或仅做非常有限的清理；只有用户明确要求时才局部风格化。
- **E3: 精准控制表达**  
  默认 **原样保留**；说明该需求更适合传统分镜工作流或执行型 prompt，而不是继续做 VC 改写。

Routing rules:

- **信息不足优先补问**：场景再适合，只要视觉锚点、主动作或风格方向缺失，就先问再写。
- **用户硬约束优先**：只要用户明确要求保留台词、音乐、镜头编号、参数、段落结构或交付格式，就不能擅自删除；如需 VC 版，应作为额外版本或在用户同意后提供。
- **多镜头优先保结构**：当用户本来就在用镜头段落表达统一体验时，不要把结构强行压成一段散文；但除非用户明确要求保留编号或列表格式，否则不默认延续编号输出。
- **精准控制写法不等于低适配场景**：先看场景目标，再决定是否转译。

## Information Density Check

即使场景适合 VC，也不能在关键信息缺失时强行改写。以下情况需要先补问：

- 没有明确视觉锚点
- 只有抽象感受，没有人物、物件或场景
- 有主体但没有动作或状态
- 有画面碎片但没有主关系或风格方向
- 极短输入虽已有主体和事件，但缺少明确风格方向、观看方式或重点瞬间
- 多镜头内容存在明显跳转，但看不出它们为什么放在一起

VC prompt 默认优先满足四层结构；缺哪一层，就优先补哪一层，不必机械按顺序全部追问：

1. **视觉锚点**：最该被看见的核心，人、物、已命名概念或特效本体。
2. **行为或状态**：正在发生什么，只写一个主要动作、状态或情节。
3. **局部调性**：这一幕的感觉，一个氛围词或形容词即可。
4. **视频主题**：应用场景加画面风格，如概念短片、微叙事、影视预演、情绪表达、通识还原、特效片段；超写实、电影感、动画、粘土风、东方写意、赛博、插画感。

对于极短、抽象、单意象输入，优先把抽象词转成可见画面所需的信息；如果方向已基本明确，可以先给出初步判断，再补问最关键的 1-3 个缺口。

## Interaction Policy

不要向用户暴露内部分类标签，如 `S1 + E2` 或 `Mode 5`。内部先完成三个判断：**场景判断（S）**、**表达判断（E）**、**信息密度检查（I）**。信息不足时允许是初步判断，不强行定类。

执行动作必须使用以下标签之一：

- `直接放行`
- `轻度提纯`
- `直接改写`
- `先补问`
- `原样保留`
- `可选 VC 版`

处理原则：

- 场景适合 VC 但信息不足时，优先补完成当前动作所必需的最小信息量。
- 当输入已同时具备清晰主体、结构、时间关系、核心意象和明确情绪目标，且文本本身已具有较强生成可用性时，默认优先直接放行；如仅需微调清晰度或收束表达，再做轻度提纯，不主动重写。
- 场景适合 VC 但输入中混有未声明是否保留的精准控制时，可默认弱化、删除或转译；若本次做了相关处理，必须补充说明，并提示用户如需保留可继续指定。
- 场景仅部分适配时，不默认强推 VC，优先保留原意或提供可选 VC 版。
- 场景低适配时，应说明是目标或工作流不匹配，不是否定用户创意本身。
- 用户明确指定的台词、旁白、音乐、音效、结构和参数要求优先保留。

## Hard Constraint Protection

Before rewriting, identify and preserve:

- `@图1`, `@视频1`, file names, asset IDs, and other anchors exactly
- character names, shot numbers, duration, platform limits, aspect/format constraints
- dialogue, narration, lyrics, music, sound effects, and spoken text exactly
- user-specified action order, reference image roles, required structure, and forbidden changes

If the user explicitly asks to preserve parameters, shot numbers, or structure, keep them. If not, low-value technical controls may be translated into viewer-facing results.

## Camera Language Policy

镜头语言不应一刀切删除。真正需要删除的是“告诉系统怎么拍”的低价值技术参数；真正需要保留或转译的是“让观众怎么感受”的镜头意图。

**默认降权或删除**：

- 焦段、毫米数
- 机位术语
- 运镜参数
- 镜头号
- 景深、光圈、曝光、快门
- 设备说明、A/B 机、coverage
- 纯剪辑指令

用户明确要求保留参数时，优先遵守约束，再决定是否额外提供 VC 版。

**未声明是否保留精准控制时**：

- 默认不把技术控制当作必须保留项
- 默认仍按更适合生成的 VC 创意版处理
- 优先保留其中对情绪、叙事、观看感受有贡献的部分
- 对纯技术性的镜头控制，默认删除或转译成自然结果
- 不必先中断确认；但若已弱化、删除或转译部分技术控制，输出中必须简短说明

## Sound And Constraint Priority Rules

台词、旁白、音乐、音效、歌词、口白和其他明确指定的声音内容，优先级高于创意优化。可以整理顺序，但**不能改写措辞、不能替换内容、不能删掉用户明确指定的声音要求**。

当规则冲突时，按以下顺序执行：

1. **用户明确指定的内容与硬约束**：台词、旁白、音乐、音效、镜头结构、参数保留要求、格式要求、风格限制等。
2. **创意优化**：在不破坏约束的前提下，提纯故事、情绪、记忆、意象和统一体验。
3. **VC 范式一致性**：只有在前两项满足后，才进一步收束语言，让提示词更适合模型理解和生成。

补充规则：

- 用户明确写出的台词、旁白、音乐或音效，应原样保留。
- 画面描述与声音要求混写在一起时，可以重排顺序，但不要改动声音内容本身。
- 如果画面部分适合 VC，声音部分不适合改写，可以只改写画面部分。
- 如果整条内容成立的前提是长篇、严格、逐字级的对白同步，则默认不走 VC 改写。

## Rewrite Modes

VC 的改写不是单一模板，应根据输入主导因素选择最合适的模式：

- **叙事改写**：适用于故事主导、关系主导、事件在推进的输入。可输出一条连续提示词，也可保留 2 至 5 段分幕提示，重点是保留事件顺序和情绪转折。
- **情绪改写**：适用于氛围、感受、状态主导的输入。集中强化环境、节奏、质感和观看感受，不要为了“像故事”而硬补因果链。
- **记忆改写**：适用于回忆、闪回、旧时感、消逝感、被重新想起的片段。保留模糊、发白、缺失和脆弱感，强化反复出现的意象与时间流失感。
- **意识流改写**：适用于联想、碎片、主观感知和非线性表达。允许不完整，但必须让画面仍然可感知，并在意象之间保持内部统一。
- **多镜头体验改写**：适用于多段、多场景、多切换，但共同服务同一体验的输入。可按自然分段或在用户明确要求时按编号分组，每段 1 至 3 句；保留场景流转、情绪递进和视觉母题，不保留低价值执行术语。
- **混合提纯**：适用于创意内容与执行语言混杂的输入。尽量保住原结构和有效信息，只移除技术噪声、重复说明和低价值控制语句，不过度重写，也不擅自补充新桥段。

## Failure Branches

- If the request is a UI demo, workflow tutorial, industrial procedure, or functional explainer, use `原样保留` or only light cleanup; do not make it atmospheric.
- If the user asks for final Seedance/Doubao/Dreamina wording, output a VC version only when useful and state that final platform drafting belongs to `aigc-seedance-prompt`.
- If the input contains exact dialogue, lyrics, narration, music, sound effects, or subtitles, preserve the wording exactly and rewrite only the visual portion.
- If the input has `@...` anchors, file names, role references, duration, shot count, or action order, preserve them exactly unless the user explicitly changes them.
- If a multi-shot request has disconnected images with no shared experience, ask what links the shots instead of forcing a mood arc.
- If a prompt is already strong, compact, and generative, use `直接放行` or `轻度提纯`; do not rewrite for style just to show effort.

## Output Rules

Skill 的目标是帮用户更准确地表达，不是替用户改写成另一部作品。

### 长度与形态原则

- 默认不要显著长于原文，也不要把极短输入扩成冗长散文。
- 没有依据的内容一律不补，尤其不能凭空增加人物关系、剧情反转、场景细节或情绪变化。
- 单段输出时，尽量收束为一条可直接用于生成的提示词。
- 保留结构不等于保留编号。只有当用户明确要求保留镜头号、段号、列表格式或交付结构时，才保留编号输出；否则多段内容默认以自然分段呈现。
- 在信息充分且无额外约束时，单段或单镜头通常控制在 30 至 120 字；如需保留结构、台词或多段体验推进，可适当放宽。
- 当用户明确要求保留原结构时，优先保留结构，而不是追求更短。

### 用户可见格式

默认采用四段式输出，顺序固定：

```markdown
判断：
[是否适合 VC、原文是否已足够可用、信息是否充分]

执行动作：
[直接放行 / 轻度提纯 / 直接改写 / 先补问 / 原样保留 / 可选 VC 版]

输出结果：
[实际改写结果、原样保留文本，或补问内容]

补充说明：
[仅在需要时说明弱化/删除/转译的技术控制，已保留的台词、旁白、音乐、音效等硬约束，或提示用户如何保留参数、结构、节奏点]
```

当无需补充说明时，可省略第四段。简单请求可以把“判断”和“执行动作”各压缩成一行，但不要省略动作标签。

If the user asks for A/B comparison, provide the VC version and a handoff note: use `aigc-seedance-prompt` for the standard execution version or final platform version.

## References

Load references only when they materially change the answer:

- Read `references/seedance-official-vibe-guide.md` when the user explicitly asks for official Seedance Vibe guidance, wants official-style calibration, asks why Vibe works, compares Vibe vs Seedance outputs, or a Vibe draft needs style correction.
- Do not load the official guide for ordinary short Vibe prompts. The core workflow above is enough for normal use.

## Quick Reference

| 输入类型 | 优先判断 | 缺什么先问 | 默认动作 | 输出风格 |
|---|---|---|---|---|
| 已有明确主体、动作、氛围的单幕提示 | 高概率适合 VC；看是否已足够聚焦 | 缺风格、画面中心或主状态时再问 | 直接改写、轻度提纯，或直接放行 | 直接输出一条可生成提示词 |
| 多镜头叙事，但共同服务一个统一体验 | 适合 VC；关键看情绪线、主题线、记忆线是否连贯 | 镜头之间关系、递进逻辑不清时再问 | 保留结构改写，必要时分组 | 按分段或保留原结构输出 |
| 分镜号、参数很多，但底层是情绪或故事场景 | 属于可 VC 转译，不因执行写法拦截 | 主体验、主动作、主关系不清时先问 | 去噪后转译，保留叙事与情绪意图 | 删除参数，转成自然画面表达 |
| 品牌展示、角色展示、风格化广告 | VC 部分适配，不一定必须转写 | 情绪目标、风格方向不清时先问 | 轻度提纯或可选 VC 版 | 先保留原意，必要时给一版更有体验感表达 |
| 只有抽象词，如“自由”“高级感”“很有力量” | 信息不足，不应硬写 | 视觉锚点、场景、动作或状态 | 先补问，不直接改写 | 先提 1 至 3 个短问题 |
| 画面提示中已写清台词、旁白、音乐、音效 | 可部分 VC；声音内容优先级高 | 仅在画面部分信息不足时先问 | 保留声音内容，只改写画面部分 | 先说明“声音保留不改” |
| 用户明确要求保留镜头编号、参数、交付结构 | 约束优先；不应擅自删除 | 通常不需要补问 | 原样保留或额外提供可选 VC 版 | 说明“先按执行稿保留” |
| 功能演示、UI 教程、步骤说明 | 低适配；目标不在创意转化 | 通常不进入 VC 补问 | 原样保留，必要时拆分 | 自然说明不建议 VC |
| 长篇剧情且要求精确对白同步 | 低适配；属于能力或工作流边界 | 通常不进入 VC 补问 | 不做 VC 改写，可拆纯画面部分 | 说明可单独拆纯画面部分 |
| 中英混合、含少量技术术语的创意输入 | 若底层体验明确，仍适合 VC | 仅在主体、关系、风格不清时先问 | 转译术语，保留核心气质 | 输出中文自然画面表达 |

## Avoid

- Do not make every prompt poetic, dreamy, or memory-like.
- Do not add backstory, character relationships, symbolic interpretation, or emotional changes not present in the source.
- Do not erase technical constraints that the user explicitly asked to keep.
- Do not turn VC output into the final Seedance code block unless the user later routes it to `aigc-seedance-prompt`.
- Do not expose internal fit labels or explain the full classification process.
