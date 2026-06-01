# AIGC Codex Skills

这是一套面向 AIGC 影视、动画、图像和视频生产的个人 Codex skills。它不是通用 prompt 模板库，而是一组按任务阶段分工的工作流入口：从想法梳理、项目规划、画面诊断、生产决策，到图像反推、图像编辑、自然语言提示词和 Seedance 视频提示词。

## 使用方式

所有 skill 都使用 `aigc-` 前缀，方便在 Codex 里搜索和显式调用。你可以直接用自然语言描述任务；当任务很关键、容易误路由，或你想固定使用某个工作流时，建议显式点名：

```text
用 $aigc-visual-diagnose 看看这张图为什么不好看。
用 $aigc-shot-diagnosis-pipeline 判断这帧能不能进入视频。
用 $aigc-image-reverse-prompt 反推这张图的中英文提示词。
用 $aigc-image-edit-prompt 写一份 Nano Banana 修图 prompt。
用 $aigc-seedance-prompt 写一个 15 秒 Seedance 视频 prompt。
```

当前这套 skills 的共同设计原则：

- 先判断任务入口，再输出内容，避免把诊断、修图、反推、视频提示词混在一起。
- 每个 skill 都有 `CHECKPOINT` 和 `Failure Branches`，用于处理缺图、范围不清、任务过大、画面逻辑冲突等情况。
- 输出按任务复杂度控制长度，不为了显得专业而堆镜头词、参数、风格形容词。
- 专业 skill 之间可以交接，但不会强制所有 prompt 最后都经过同一个“最终润色层”。
- 每个主要 skill 配有 `test-prompts.json`，用于压力测试触发条件和边界场景。

## Skill 入口

### `aigc-project-planner`

用于规划整个 AIGC 项目、短片流程、多镜头制作顺序、多资产协同和“下一步该做什么”。它处理项目级问题，不处理单张图、单个镜头或单条 prompt。

适合这样说：

```text
用 $aigc-project-planner 帮我规划这个 AIGC 短片项目的整体流程。
用 $aigc-project-planner 看看我现在有角色图、场景图和故事想法，下一步该做什么。
```

### `aigc-creative-director`

用于把模糊想法、场景、角色、故事或情绪整理成导演方向、视觉策略、镜头目的和拍摄设计。它适合在还没有明确 prompt 之前，先确定这个画面或镜头到底要表达什么。

适合这样说：

```text
用 $aigc-creative-director 把这个短片想法整理成导演方向和镜头策略。
用 $aigc-creative-director 从导演角度看看这个角色出场怎么拍。
```

### `aigc-visual-diagnose`

用于分析单张图、关键帧、视频帧、分镜或概念图为什么弱、哪里怪、为什么 AI 味重、为什么不电影感。它回答的是“画面问题是什么，以及从导演、摄影、美术、AIGC 控制角度怎么修”。

适合这样说：

```text
用 $aigc-visual-diagnose 看一下这张画面为什么不好。
用 $aigc-visual-diagnose 从导演、摄影、美术角度诊断这帧哪里怪。
```

### `aigc-shot-diagnosis-pipeline`

用于把单张关键帧、生成图或视频帧当作生产检查点，判断它能不能继续推进、该先修图还是重做、能不能进入 Seedance，并把下一步交给正确的专业 skill。它回答的是“能不能用 / 下一步去哪”，不是完整美术诊断。

适合这样说：

```text
用 $aigc-shot-diagnosis-pipeline 判断这张关键帧能不能进入视频。
用 $aigc-shot-diagnosis-pipeline 看这个镜头下一步应该修图还是重做。
```

### `aigc-image-reverse-prompt`

用于在有参考图时，反推、复刻、仿写或改写成适合 Midjourney、即梦、Nano Banana/Gemini、GPT Image、ChatGPT Images 等图像模型的中英文提示词。它会先做可见事实盘点，再区分必须锁定的元素和可以变化的元素。

默认输出中文和英文两版；英文 prompt 本体不追加 `--ar`、`--style`、`--v` 等参数，平台设置会放在单独建议里。

适合这样说：

```text
用 $aigc-image-reverse-prompt 反推这张图的提示词。
用 $aigc-image-reverse-prompt 把这张图改写成 Midjourney 和即梦都能用的提示词。
用 $aigc-image-reverse-prompt 复刻这张图的主体关系、环境、天气、氛围、光影和色调。
```

### `aigc-image-edit-prompt`

用于已经决定要修图时，输出适合 Nano Banana/Gemini、ChatGPT Images、OpenAI 图像编辑器等 image-to-image 工具的修图 prompt。它重点保留人物身份、构图、服装、姿态、镜头关系和有价值的设计选择，同时清楚写出要改变什么、避免什么。

适合这样说：

```text
用 $aigc-image-edit-prompt 给这张关键帧写一份电影感修图 prompt。
用 $aigc-image-edit-prompt 按刚才的诊断结果写 Nano Banana 修图提示词。
```

### `aigc-natural-language-prompt`

用于把粗糙想法、关键词串、参数堆叠 prompt 或旧提示词，改写成自然语言、导演讲戏式、可执行的画面提示词。它重点处理可见主体、动作、空间关系、画面逻辑和无依据的画面外因果。

它不是所有 prompt 的强制最终润色层；只有当用户明确要求自然语言清理，或 prompt 本身有模板腔、AI 味、参数堆叠、画面逻辑不清时才使用。

适合这样说：

```text
用 $aigc-natural-language-prompt 把这段提示词改成自然语言、导演讲戏式 prompt。
用 $aigc-natural-language-prompt 判断这段 prompt 哪些地方不够自然。
```

### `aigc-seedance-prompt`

用于 Seedance、豆包、Dreamina 视频提示词，包括文生视频、图生视频、参考图生成、视频编辑、视频延展、镜头桥接、提示词优化、时长压缩、口型同步和镜头连续性。

它会优先判断素材是否真实存在、任务类型是否明确、时长是否能承载动作链。15 秒以内的任务会主动压缩成一个主场景、一个动作链、一个镜头策略和一个清晰结束点。

适合这样说：

```text
用 $aigc-seedance-prompt 把这个镜头写成 Seedance 图生视频提示词。
用 $aigc-seedance-prompt 优化这段 Seedance prompt。
用 $aigc-seedance-prompt 写一个 15 秒、一镜到底的短视频提示词。
```

## 快速选择

```text
整个项目怎么推进？                    -> aigc-project-planner
只有想法，还没镜头策略？              -> aigc-creative-director
为什么这张图不好看？                  -> aigc-visual-diagnose
这张图能不能继续 / 下一步去哪？       -> aigc-shot-diagnosis-pipeline
反推、复刻、仿写参考图？              -> aigc-image-reverse-prompt
已经决定要修图？                      -> aigc-image-edit-prompt
提示词像参数表，想改自然？            -> aigc-natural-language-prompt
已经决定要做 Seedance / 豆包视频？    -> aigc-seedance-prompt
```

## 安装到 Windows Codex

```powershell
git clone https://github.com/Wanrd0Geri/aigc-codex-skills.git
cd aigc-codex-skills
.\scripts\link-skills.ps1 -Force
```

如果不想覆盖已有同名 skills，去掉 `-Force`。链接后重启 Codex。

## 安装到 Mac Codex

```bash
git clone git@github.com:Wanrd0Geri/aigc-codex-skills.git
cd aigc-codex-skills
chmod +x scripts/link-skills.sh
./scripts/link-skills.sh --force
```

如果不想覆盖已有同名 skills，去掉 `--force`。链接后重启 Codex。

## 来源说明

这套仓库借鉴了 Matt Pocock `mattpocock/skills` 项目中“小型、可触发、面向工作流的 agent skill”思路。该项目使用 MIT license。本仓库没有复制其 skill 文件内容，而是把这种方法改造成适合 AIGC 影视创作、动画、分镜、图像编辑和视频提示词生产的个人工作流。
