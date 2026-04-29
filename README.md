# AIGC Codex Skills

Private Codex skills for AIGC short-film, animation, cinematic image, storyboard, and Seedance prompt workflows.

## Skills

- `aigc-workflow-router`: plans multi-stage AIGC projects and routes whole-project workflows to the correct specialized skill.
- `aigc-creative-director`: turns vague short-film or animation ideas into director-level creative plans and shot strategy.
- `aigc-shot-diagnose`: explains why an AIGC image/frame feels weak from director, cinematography, production design, storyboard, and prompt-control perspectives.
- `cinematic-storyboard-enhancer`: writes bilingual image-to-image edit prompts for Nano Banana Pro or ChatGPT Images 2.0.
- `seedance-prompt-master`: writes and improves Seedance series text-to-video, image-to-video, extension, edit, and bridge prompts.

## Install On Windows

Clone the private repository, then link the skills into Codex:

```powershell
git clone https://github.com/Wanrd0Geri/aigc-codex-skills.git
cd aigc-codex-skills
.\scripts\link-skills.ps1 -Force
```

If you do not want to replace existing installed skills, omit `-Force`. Restart Codex after linking.

## Install On Mac

Clone the private repository, then link the skills into Codex:

```bash
git clone git@github.com:Wanrd0Geri/aigc-codex-skills.git
cd aigc-codex-skills
chmod +x scripts/link-skills.sh
./scripts/link-skills.sh --force
```

If you do not want to replace existing installed skills, omit `--force`. Restart Codex after linking.

## Daily Use

Use natural language. The skill descriptions are written to catch common working phrases:

- "这张图不好看，但我说不上来为什么"
- "我有一个短片想法，帮我设计怎么拍"
- "这个 AIGC 短片项目下一步怎么办"
- "把这个镜头变成 Seedance 图生视频提示词"
- "把这张关键帧提升电影感，给 Nano Banana Pro prompt"

For maximum control, explicitly name a skill:

```text
用 $aigc-shot-diagnose 看一下这张画面为什么不好。
用 $aigc-creative-director 把这个想法整理成短片镜头方案。
用 $seedance-prompt-master 写一份 Seedance 图生视频提示词。
```

## Source Notes

This repository borrows the workflow idea of small, triggerable agent skills from Matt Pocock's `mattpocock/skills` project, which is MIT licensed. It does not vendor that repository's skill files; the workflows here are adapted for AIGC filmmaking, animation, storyboarding, and prompt production.
