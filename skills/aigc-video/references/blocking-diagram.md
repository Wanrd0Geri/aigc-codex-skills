# Conditional Blocking Diagram

Use a Diagram as a fallback geometry asset after ordinary source geometry has been scoped and tested. It consumes a structure-resolved shot; it never confirms structure or creates cross-shot world topology.

## When to use it

First inspect every readable composition frame, storyboard panel, coarse model, white-model video, or user-supplied staging map. Assign a clear existing asset directly to its authorized composition, blocking, crop, occlusion, camera, or route fields when it already expresses them. A complex shot alone does not trigger Diagram generation.

Enter the generated Diagram path only when one of these conditions holds:

- direct binding of an existing geometry asset has repeatedly produced the same position, facing, occlusion, crop, swap, route, or camera-path failure
- the only useful geometry source contains identity, wardrobe, style, environment, material, or lighting that would contaminate its final rendered role, so a neutral geometry asset is needed
- a static source composition needs a separate route overlay
- the current user explicitly requests a generated Diagram

When the user supplies a staging map, validate and bind it directly when faithful. A single subject, an unoccluded simple two-person setup, a performance/light/material/sound-only change, and geometry already held by a readable stable asset stay on the direct-asset path.

## Order

1. Resolve structure review under `SKILL.md`. A confirmed path compares against the confirmed version; a directly authorized path compares against the compiled internal MotionSpec.
2. Audit existing geometry assets. Directly bind a faithful asset with a narrow responsibility. Validate a supplied staging map before activation.
3. When generation is justified, output one image-generation prompt, a candidate version, its `map_scope`, and a text color-to-character/prop key; wait for the returned map.
4. Compare the returned map with the current structure version or directly authorized MotionSpec. A faithful map becomes active without another routine approval round. A candidate that changes or obscures a resolved fact retires. Generate a replacement only when one fresh evidence-backed geometry hypothesis and one explicit discriminating criterion can guide it. When no fresh hypothesis exists, or a replacement is rejected under the same structure, hypothesis, and criterion, end the generated-Diagram path and set `stage_status: blocked`; request a corrected geometry source or user-supplied map, or re-open attribution. Reopen structure only when new evidence exposes a genuine structural ambiguity.
5. Bind the active map versions, then enrich performance and render the complete final shot or sequence.

## Geometry contract

A Diagram may control only:

- frame/crop and camera side
- screen and depth position
- rough pose plus body and head facing
- occlusion and relative scale
- subject, prop, effect, or camera route

These are macro geometry responsibilities. A Diagram does not by itself guarantee a fine hand-to-body, prop-to-body, or surface-to-surface contact gap. Bind an exact contact or non-contact boundary from readable accepted evidence only when the crop can verify it; after a repeated fine-gap failure, do not generate another Diagram unless a fresh geometry hypothesis and discriminating criterion exist.

Identity, face, wardrobe, detailed prop design, environment, visual style, material, lighting, expression, and sound remain owned by their normal text or assets. Treat the map as `staging_map`, not as a generic style or identity reference.

Use `map_scope: composition` for frame, crop, camera side, screen/depth position, pose, facing, occlusion, relative scale, and route start. Use `map_scope: route` only for a sparse subject, prop, effect, or camera trajectory. A route map supplements the active composition source and never changes its framing.

Default to a camera-facing straight view of the structure-resolved or source composition, with the same aspect ratio, frame edges, crop, subject scale, screen position, depth overlap, and occlusion. It is not a bird's-eye floor plan. A body or object cut by the source frame stays cut; preserve hidden and off-frame boundaries and every established person, furniture item, prop, and landmark. When an explicit route cannot be read in this view, add a separate sparse route overlay or route map; keep the camera-view composition map unchanged.

Narrative gaze and eye target remain owned by `shot-craft.md`. If a gaze direction is structurally critical to the composition, resolve its attention hierarchy in `画面重心` and its visible action consequence in `动作与终点` before the Diagram step; the map may show only the resulting coarse head facing.

A Diagram may check a shot against its `SceneSpatialContract`, but it cannot establish regions, connectivity, world distances, or other cross-shot topology. A single source composition has the same boundary.

Keep the map visually sparse: neutral background and thin low-saturation color-coded outlines for simplified figures or trajectories, with no fill, shading, solid color block, or decorative detail. Put names and color correspondence in the accompanying text rather than embedding letters, captions, or character designs into the image. The image-generation prompt must state the camera-facing view, source aspect/crop lock, no completion of cropped/hidden content, and no additions. When exact existing framing is being preserved, a readable source frame or coarse model is required; ask for it if absent. Never present a text-invented map as an observed source layout.

## Version and rendering

- One `composition` map covers one initial composition state: camera side, crop, subject order, depth, occlusion, facing, and route start.
- One `route` map covers one authorized trajectory. A composition map and route map may coexist because their scopes differ.
- Change a field inside one scope and create a new version for that scope. Performance and lighting changes preserve both scopes.
- Keep one active version per scope and owning shot. Retire older versions inside that scope.
- Once a validated composition map is active, keep its source composition frame as evidence unless the user assigns that frame a distinct non-conflicting rendered role. When only a route map is active, the source composition may continue to own framing and blocking.
- Map upload order to a plain label such as `图片6` in the final prompt. Bind it once in the owning shot and include the text key, for example: `镜头2按图片6的站位、朝向、遮挡与路线组织；红色轮廓对应罗大娘，蓝色轮廓对应曲伯，颜色仅用于站位对应；角色身份与服装、场景与灯光仍由各自已绑定素材或文本负责。`
- Place the staging map after identity, scene, and other authoritative assets in the material order when the interface allows it.
- Do not render words such as line drawing, wireframe, color figure, grid, label, or Diagram as final-video style instructions.

## Final check

- The existing-asset path was checked before Diagram generation.
- A generated Diagram satisfies one activation condition above.
- Every replacement candidate tests a fresh geometry hypothesis with an explicit criterion; a repeated rejection under the same structure, hypothesis, and criterion ended the generated-Diagram path.
- It matches the current confirmed version or directly authorized internal MotionSpec.
- Only one active version per map scope and owning shot is bound.
- The source frame and active map scopes do not duplicate geometry ownership.
- Geometry ownership did not leak into identity, style, light, or performance.
- Diagram contributed no `SceneSpatialContract` fact.
- Every outline color is bound to one semantic character/prop in the final connector, and color does not become wardrobe or final-video styling.
- The final result is still a complete shot/sequence prompt, not only a map connector.
