# AIGC Codex Skills

这是一套按实际创作交付物组织的个人 AIGC Skills。新版把原来的七个入口收束为四个：图像、视频、项目上下文、提示词改写。目标不是减少功能，而是让 Agent 更容易选对入口、少做重复转换，并在创作判断不确定时主动和你讨论。

## 四个入口

| Skill | 它负责什么 | 典型说法 |
|---|---|---|
| `aigc-image` | 从文字 brief 生成图像提示词、画面诊断、参考图反推、图像编辑提示词，以及组合任务 | “给 Nano Banana 写人物海报提示词” |
| `aigc-video` | Seedance、豆包、Dreamina 或明确要求的平台中立最终视频提示词：生成、编辑、延长、桥接、对白、口型和连续性 | “将 @视频1 向后延长 5 秒……” |
| `aigc-project-context` | 把剧本、分镜、镜头表和项目设定整理成镜头任务卡、连续性与表演理解 | “把这场戏整理成后续视频生成能直接接手的镜头卡” |
| `aigc-prompt-rewrite` | 只做已有平台中立提示词或无专用适配器平台的语言清理；保护锚点、数字、参数和生产事实 | “只改这段画面描述的自然语言，不做最终平台适配” |

可以直接用自然语言，不必记 Skill 名。关键任务也可以显式点名：

```text
用 $aigc-image 诊断这张图，然后给一版保守修图提示词。
用 $aigc-video 将 @视频1 向后延长 5 秒，人物保持原姿势，缓慢转头看向门口。
用 $aigc-project-context 根据剧本和分镜整理这一场的镜头任务卡。
用 $aigc-prompt-rewrite 保留全部 @锚点和对白，把这段提示词改自然。
```

## 新版工作逻辑

### 图像只保留一个入口

`aigc-image` 内部判断当前要做的是：

- 根据文字 brief 直接写最终图像提示词；
- 诊断画面为什么弱；
- 反推或复刻参考图；
- 写图像编辑提示词；
- 按用户要求把诊断和修图串在同一轮完成。

它先做一次中性读图和事实锁定，后面的模式共用这份事实，不再由三个 Skill 重复读图。多张参考图会先区分角色、构图、场景、风格或动作各自控制什么。

生成或修图提示词默认把中文与英文放在两个独立代码块中；两版语义一致，但实际提交模型时只选一版，不把中英文拼在一起。提示词采用“最小充分”原则：单一局部修改通常只写一句直接指令和关键保持项，只有多参考图、精确文字或复杂版式才展开结构。平台适配目前按 GPT Image 2、Nano Banana 2 / Pro 与 Seedream 5.0 Pro 的官方公开指导处理；界面有独立控件时，比例、分辨率、质量等设置不混入提示词正文。

### Vibe 已并入视频

`aigc-video` 同时负责自然的创作表达和平台执行结构。Vibe 不再是另一个最终稿，也没有需要用户选择的“强度档位”。它只在内部按任务需要：

- 保留用户已经写好的表达；
- 对局部情绪和表演做克制提纯；
- 当用户只有粗想法时，补齐可见、可执行的表达骨架。

最终仍由同一个 Skill 完成素材锁定、动作链、平台格式和检查，因此不会出现 Vibe 版本与 Seedance 版本互相覆盖。

### 自然语言是视频内部的受保护局部终检

视频提示词完成后，`aigc-video` 只检查允许修改的语言字段：去掉空泛套话，补清楚主体、动作、空间与顺序。它不会在最后把整份提示词重新写一遍，也不会改动 `@锚点`、对白、时长、镜头顺序、动作顺序、参考角色和连续性。

独立的 `aigc-prompt-rewrite` 仍然保留，供你只做已有平台中立提示词或无专用适配器平台提示词的语言清理；它不是每个 AIGC 任务的必经环节。GPT Image 2、Nano Banana、Seedream 的最终图像提示词优化由 `aigc-image` 处理；Seedance、豆包、Dreamina 或从剧本新建的平台中立最终视频提示词由 `aigc-video` 处理。

### Agent 会主动讨论创作判断

当情绪、表演、参考角色或镜头意图存在会改变成片的歧义时，Agent 应先告诉你：

1. 它从剧本、分镜或当前描述里理解到什么；
2. 还有哪一种主要可能；
3. 它推荐哪一种，以及原因；
4. 一个真正影响结果的问题。

已有上下文足够时直接继续；不会为标点、普通措辞或容易自行判断的技术细节反复提问。

例如：

```text
将 @视频1 向后延长 5 秒，人物保持原姿势，缓慢转头看向门口。
仿佛他回到多年没有住过的老房子，有一种时间已经停止的感觉。
```

“时间停止”不会被机械地塞进提示词。Agent 会优先从剧本、分镜和前后镜头理解表演；证据不足且不同演法会明显改变结果时，再与你确认是迟疑、陌生、怀念，还是更接近麻木。

## 个人默认值

除非当前任务、项目或素材另有明确要求：

- 交流、视频与普通文本默认中文；`aigc-image` 的生成、反推和修图提示词默认提供中英文两个独立版本；
- 最终视频平台默认按 Seedance 兼容结构处理；
- 默认不额外添加配乐和字幕；
- 已有的环境声、对白和口型要求会保留；
- 表演偏克制，以一个主要可见载体承接情绪；
- 当前用户指令始终高于项目默认和个人默认。

这些是可覆盖的个人习惯，不会被伪装成平台硬规则。

## 旧版迁移

| 旧入口 | 新入口 |
|---|---|
| `aigc-visual-diagnose` | `aigc-image` 的诊断模式 |
| `aigc-image-reverse-prompt` | `aigc-image` 的反推模式 |
| `aigc-image-edit-prompt` | `aigc-image` 的编辑模式 |
| `aigc-vibe-creating-prompt` | `aigc-video` 的表达阶段 |
| `aigc-seedance-prompt` | `aigc-video` 的平台适配与最终交付 |
| `aigc-script-context` | `aigc-project-context` |
| `aigc-natural-language-prompt` | `aigc-prompt-rewrite`；最终视频内部另有受保护的局部语言终检 |

旧版完整快照保存在 Git 分支 `backup/aigc-skills-pre-v2-20260715`。新版可直接作为主力使用；需要回滚时切回该分支即可。

## 安装到 macOS Codex

```bash
git clone git@github.com:Wanrd0Geri/aigc-codex-skills.git
cd aigc-codex-skills
chmod +x scripts/link-skills.sh
./scripts/link-skills.sh --force
```

脚本会先确认四个新 Skill 文件完整，再清理旧链接并建立新链接。已有同名真实目录只会在 `--force` 下备份后替换。完成后重启 Codex。

## 安装到 Windows Codex

```powershell
git clone https://github.com/Wanrd0Geri/aigc-codex-skills.git
cd aigc-codex-skills
.\scripts\link-skills.ps1 -Force
```

PowerShell 脚本同样只安装四个主 Skill，并能识别和清理已经失效的旧链接。完成后重启 Codex。

## 实战迭代

每个 Skill 都有 `test-prompts.json`，用于检查触发边界、事实锁、素材状态和交付所有权。带 `requires: ["readable_source_image"]` 的用例必须由测试运行者注入真实可读图片，不能当作纯文本测试。测试文件不是自动打分器，也不代替你的成片判断。
