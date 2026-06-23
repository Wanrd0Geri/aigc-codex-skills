# Seedance Handoff

Use this handoff when `aigc-script-context` prepares a shot for `aigc-seedance-prompt`.

## Handoff Inputs

Provide only these items unless the user asks for more:

```text
任务：为 Seedance 2.0 写视频提示词
项目上下文：<project and source priority>
镜头任务卡：<compact card>
参考图映射：<@图1 as character/reference/etc.>
风格默认：<project style, overridden by scene references>
输出要求：中文自然导演式执行段落；按复杂度估时；不写平台参数。
```

## Handoff Rules

- Keep the final prompt inside the current shot or requested shot range.
- Do not paste the whole script, scene, or outline into the video prompt.
- Preserve user-provided reference image anchors exactly when they exist.
- If scene reference images are missing, use story and performance context, but do not invent specific set design or color lighting.
- When an available project package states a default style, preserve it; for `临渊行`, that default is Unreal Engine rendered 3D cinematic CG. Color and lighting still follow the user's current scene reference images.
- Keep character identity stable from available project character assets unless the user supplies a newer reference.
