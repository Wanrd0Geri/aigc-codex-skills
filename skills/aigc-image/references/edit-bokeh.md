# Background-bokeh capability

Use for converting small highlights behind the resolved focal plane into optical bokeh. Highlights may be observed in the source or explicitly produced by another authorized edit.

## Evidence gate

Confirm the resolved focal plane, background region, eligible highlight count/colors and protected subject/text areas. Read [edit-operation-state.md](edit-operation-state.md) when focus, sources or geometry change in this edit. A planned light producer can supply highlights; bokeh alone cannot invent point lights. With neither observed highlights nor an authorized producer, omit physical bokeh or clarify the requested overlay.

## Shape rules

- near frame center: mostly circular
- near frame edge: may stretch into ellipses or cat-eye shapes
- polygonal aperture shape only when explicitly requested or established
- Use the requested or established lens/medium response. Smoothly filled discs and gently edge-weighted discs are alternatives; translucent centers or bright rims are not mandatory.

Quantity is `[the user-specified count within the authorized highlight set]` or `[a restrained subset of that set]`. If the requested count exceeds it, identify the missing producer rather than silently invent lights. Never force seven or another fixed count.

## Variables

- `[背景区域]`
- `[数量或少量]`
- `[本轮亮点集合及其颜色]`
- `[主体、产品、文字或标志保护区]`
- `[本轮确定的焦点；若未修改焦点则为原有焦点]` and `[与既定镜头或媒介相符的光斑形态]`

## Canonical prompt

```text
图1是唯一底图。只在焦平面之后的[背景区域]，把[本轮亮点集合及其颜色]中的[数量或少量]亮点转为焦外光斑，呈现[与既定镜头或媒介相符的光斑形态]，不额外创造亮点或光源。所有光斑保持在[本轮确定的焦点；若未修改焦点则为原有焦点]之后，不覆盖[主体、产品、文字或标志保护区]。保持[任务级保留项]，其余未提及内容不变。
```

## Prohibited drift and fallback

- Do not place bokeh on the focal subject or convert unrelated objects into lights.
- Do not impose a grid, uniform sizes across differing depths, hard circles, or arbitrary rainbow colors without image/task support.
- If the focal plane is undefined, establish it from the task or resolve that choice first. If the source/highlight set changes, refresh bokeh evidence; planned highlights are not verified pixels.
