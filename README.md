# AIGC Codex Skills

这是一套个人 AIGC 创作工作流 skills，用于短片、动画、电影感关键帧、分镜、图像编辑提示词和 Seedance 视频提示词。

## 命名规则

所有 skill 都使用 `aigc-` 前缀，方便在 Codex 里搜索和显式调用。

## Skills 与使用方式

### `aigc-project-planner`

用于规划整个 AIGC 项目、短片流程、多镜头制作顺序和多资产协同。它只处理项目级问题，不处理单张图、单个镜头、单条 prompt。

适合这样说：

```text
用 $aigc-project-planner 帮我规划这个 AIGC 短片项目的整体流程。
用 $aigc-project-planner 看看我现在有角色图、场景图和故事想法，下一步该做什么。
用 $aigc-project-planner 把这个项目从想法到成片拆成步骤。
```

### `aigc-creative-director`

用于把模糊想法、场景、角色、故事或情绪，整理成导演方向、创意 brief、视觉策略和镜头方案。它会解释关键导演选择背后的观众心理或叙事作用。

适合这样说：

```text
用 $aigc-creative-director 把这个短片想法整理成导演方向和镜头策略。
用 $aigc-creative-director 从导演角度看看这个角色出场怎么拍。
用 $aigc-creative-director 帮我把这个场景拆成分镜。
```

### `aigc-visual-diagnose`

用于诊断单张图、关键帧、视频帧、分镜或概念图为什么不好看。它会从导演、摄影、美术、分镜剪辑和 AIGC 控制角度分析，并告诉你最应该先修哪里。

适合这样说：

```text
用 $aigc-visual-diagnose 看一下这张画面为什么不好。
用 $aigc-visual-diagnose 分析这张图为什么 AI 味重。
用 $aigc-visual-diagnose 从导演、摄影、美术角度诊断这帧哪里怪。
```

### `aigc-shot-diagnosis-pipeline`

用于把单张关键帧、生成图或视频帧当作镜头生产检查点，判断它能不能进入修图或 Seedance 视频生成，并给出下一步执行路径。它更关注“是否能继续推进”和“先修哪里”，不直接替代完整画面诊断、修图 prompt 或视频 prompt。

适合这样说：

```text
用 $aigc-shot-diagnosis-pipeline 判断这张关键帧能不能进入视频。
用 $aigc-shot-diagnosis-pipeline 看这个镜头下一步应该修图还是重做。
用 $aigc-shot-diagnosis-pipeline 给这张图做生产检查。
```

### `aigc-image-edit-prompt`

用于在你已经决定要修图时，输出适合 Nano Banana 系列、Gemini 图像编辑器、ChatGPT Images 或 OpenAI 图像编辑器的中英双语修图 prompt。它会尽量保留人物、构图、服装、姿态等你想保留的内容。

适合这样说：

```text
用 $aigc-image-edit-prompt 给这张关键帧写一份电影感修图 prompt。
用 $aigc-image-edit-prompt 按刚才的诊断结果写 Nano Banana 修图提示词。
用 $aigc-image-edit-prompt 给 ChatGPT Images 写一份中英双语图像编辑 prompt。
```

### `aigc-seedance-prompt`

用于 Seedance 系列视频提示词，包括文生视频、图生视频、视频延展、视频编辑、镜头桥接、多镜头段落和提示词优化。

适合这样说：

```text
用 $aigc-seedance-prompt 把这个镜头写成 Seedance 图生视频提示词。
用 $aigc-seedance-prompt 优化这段 Seedance prompt。
用 $aigc-seedance-prompt 设计这个镜头的延展提示词。
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

## 日常使用建议

可以直接自然表达，不一定要记住固定触发词。表达的意思匹配 skill 的用途时，Codex 会自动触发。

关键任务建议显式点名，例如：

```text
用 $aigc-visual-diagnose 看这张图。
用 $aigc-shot-diagnosis-pipeline 判断这帧能不能进入视频。
用 $aigc-image-edit-prompt 写修图 prompt。
用 $aigc-seedance-prompt 写 Seedance 视频 prompt。
```

## 来源说明

这套仓库借鉴了 Matt Pocock `mattpocock/skills` 项目中“小型、可触发、面向工作流的 agent skill”思路。该项目使用 MIT license。本仓库没有复制其 skill 文件内容，而是把这种方法改造成适合 AIGC 影视创作、动画、分镜、图像编辑和视频提示词生产的个人工作流。
