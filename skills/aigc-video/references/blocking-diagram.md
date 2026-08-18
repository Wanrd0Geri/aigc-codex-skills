# Conditional Blocking Diagram

Use a Diagram only as a geometry asset for a confirmed high-risk shot. It is not required for every shot and never replaces the universal structure-confirmation table.

## When to use it

Enter the Diagram path when the user explicitly requests or supplies one, or when repeated results show that text alone cannot hold the required positions, facing, occlusion, crop, swap, route, or camera path. On a first attempt, recommend it only after the intended geometry is unambiguous and confirmed but remains high-risk to encode for generation, such as layered multi-person occlusion, exact crossing or handoff routes, or a deliberate camera-side change. Diagram improves execution stability; it never chooses among unresolved human alternatives.

Do not add this step for a single subject, an unoccluded simple two-person setup, a performance/light/material/sound-only change, or geometry already locked by a readable stable coarse-model video.

## Order

1. Confirm the ordinary `镜头结构确认` row first.
2. If the Diagram path is accepted and no current map exists, output only one image-generation prompt, a version id, and a text color-to-character/prop key; wait for the generated map.
3. Compare the returned map with the confirmed row. If it is faithful, mark that version active and continue without a second routine approval round. If it changes or obscures a confirmed fact, retire it and reopen only the mismatched row.
4. Bind only the active version, then enrich performance and render the complete final shot or sequence.

## Geometry contract

A Diagram may control only:

- frame/crop and camera side
- screen and depth position
- rough pose plus body and head facing
- occlusion and relative scale
- subject, prop, effect, or camera route

Identity, face, wardrobe, detailed prop design, environment, visual style, material, lighting, expression, and sound remain owned by their normal text or assets. Treat the map as `staging_map`, not as a generic style or identity reference.

Default to a camera-facing straight view of the confirmed/source composition, with the same aspect ratio, frame edges, crop, subject scale, screen position, depth overlap, and occlusion. It is not a bird's-eye floor plan. A body or object cut by the source frame stays cut; do not complete hidden/off-frame limbs, invent unseen geometry, or add a person, furniture item, prop, or landmark absent from the confirmed/source frame. When an explicit route cannot be read in this view, add a separate sparse route overlay or route map; never let it replace or alter the camera-view composition map.

Narrative gaze and eye target remain owned by `shot-craft.md`. If a gaze direction is structurally critical to the composition, confirm it in `动作、对白与终点` before the Diagram step; the map may show only the resulting coarse head facing.

Keep the map visually sparse: neutral background and thin low-saturation color-coded outlines for simplified figures or trajectories, with no fill, shading, solid color block, or decorative detail. Put names and color correspondence in the accompanying text rather than embedding letters, captions, or character designs into the image. The image-generation prompt must state the camera-facing view, source aspect/crop lock, no completion of cropped/hidden content, and no additions. When exact existing framing is being preserved, a readable source frame or coarse model is required; ask for it if absent. Never present a text-invented map as an observed source layout.

## Version and rendering

- One map covers one initial composition state: the same camera side, crop, subject order, depth, occlusion, facing, and route start.
- Change any of those fields or the route and create a new version. A performance or lighting-only change does not create a new version.
- Retire older versions; never bind active and stale maps together.
- Once a validated staging map is active, keep its source composition frame as geometry evidence rather than a second rendered composition owner. Bind both only when the user explicitly assigns the source frame a different non-conflicting role; never let two assets control the same blocking/crop fields.
- Map upload order to a plain label such as `图片6` in the final prompt. Bind it once in the owning shot and include the text key, for example: `镜头2按图片6的站位、朝向、遮挡与路线组织；红色轮廓对应罗大娘，蓝色轮廓对应曲伯，颜色仅用于站位对应；角色身份与服装、场景与灯光仍由各自已绑定素材或文本负责。`
- Place the staging map after identity, scene, and other authoritative assets in the material order when the interface allows it.
- Do not render words such as line drawing, wireframe, color figure, grid, label, or Diagram as final-video style instructions.

## Final check

- The Diagram was actually needed or explicitly requested.
- It matches the confirmed structure row.
- Only one active version is bound.
- The source frame and active map do not duplicate geometry ownership.
- Geometry ownership did not leak into identity, style, light, or performance.
- Every outline color is bound to one semantic character/prop in the final connector, and color does not become wardrobe or final-video styling.
- The final result is still a complete shot/sequence prompt, not only a map connector.
