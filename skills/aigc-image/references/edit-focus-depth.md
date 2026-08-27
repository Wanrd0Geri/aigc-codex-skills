# Focus and depth capability

Use for establishing a focal subject, transferring focus between depth planes, changing foreground/background defocus, or reconstructing a usable focus target from global blur.

## Evidence gate

Identify foreground, midground, background, current sharp regions, occlusion order, and the requested focal target. If several targets are plausible and the user has not chosen one, ask. If identity-critical or text-critical detail is unreadable, do not promise exact recovery.

## Variables

- `[新焦点]`
- `[新焦平面]`
- `[旧焦点或旧焦平面]` for transfer
- `[前景区域]` and `[背景区域]`
- `[必须保持清晰的同平面对象]`

## Establish focus

```text
图1是唯一底图。将[新焦点]及其所在的[新焦平面]设为画面唯一主要实焦，保持[必须保持清晰的同平面对象]清晰。按照离焦平面的实际距离，渐进降低[前景区域]与[背景区域]的细节和局部对比；保留头发、透明材质、轮廓、接触边缘和遮挡边界的自然过渡，不形成抠图硬边、白色锐化边、重影或统一强度的模糊。保持身份、姿态、物体、构图、光线、色彩、材质、文字及其余未提及内容不变。
```

## Transfer focus

```text
图1是唯一底图。把实焦从[旧焦点或旧焦平面]转移到[新焦点]及其所在的[新焦平面]。新焦点和必要的同平面对象保持清晰；旧焦点及其他前后景按照与新焦平面的距离渐进失焦，不让两个不同深度平面保持同等清晰。保留自然轮廓、接触和遮挡过渡；保持身份、姿态、构图、光线、色彩、材质、文字及其余未提及内容不变。
```

## Reconstruct from global blur

```text
图1是唯一底图。只使用源图中可验证的特征，将[新焦点]重建为主要实焦；提高轮廓连续性和可用局部细节，但不猜测无法辨认的人脸、文字、标志、图案或精确纹理。其余前后景按照深度渐进失焦并保持自然遮挡关系。保持构图、光线、色彩、材质及其余可验证内容不变。
```

## Prohibited drift and fallback

- Do not use uniform full-frame blur.
- Do not create white halos, sticker edges, doubled outlines, or invented bright points.
- If exact detail is unreadable, request a clearer crop; otherwise use the bounded reconstruction fragment and state the risk outside the prompt.
