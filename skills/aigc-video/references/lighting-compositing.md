# Lighting And Composite Integration

Use this reference for every new/reference generation, every displayed structure table, any rebuilt, extended, or bridged visible unit, and any observed lighting or compositing mismatch. It converts production lighting/compositing practice into visible prompt language; it does not ask a video model to reproduce a DCC or Nuke workflow.

## Research basis

- In the 2023 interview with *Deep Sea* technical director Liu Lu, the project treats lighting and compositing as a joined stage. Compositing carries color richness, spatial depth, underwater atmosphere, suspended particles, caustic-like light spots, and camera-optical realism rather than merely stacking rendered layers: <https://www.renderbus.com/news/post-id-1195/>.
- The 2024 *Modern Film Technology* interview with Light Chaser Animation describes complex effect lighting as coordinated control of lighting, rendering, and compositing: render the emissive effect, match the scene lighting/render response, then refine the result in post. It also describes per-shot layered projection for correct 3D depth and the need to balance 2D composition with breathable 3D space: <https://www.163.com/dy/article/JI5BMAM50517D0O2.html>.

These examples support one prompt-level rule: a convincing composite is a shared cause-and-response system across subject, ground, nearby materials, atmosphere, depth, and camera exposure. A light direction attached only to the character is insufficient.

## LightCompositeSpec

Resolve this chain for each generated, rebuilt, extended, or bridged visible unit. For a pure environment or object shot, the primary visible surface/object replaces the subject position in the chain:

`source anchor -> subject response -> contact and nearby receivers -> depth/atmosphere -> camera-visible exposure result`

The arrows define diagnostic order, not a requirement to invent every layer. The minimum is one active source anchor, one subject or primary-surface response, and at least one currently visible integration cue from contact/nearby material, depth/atmosphere, or exposure.

Keep only fields that materially change the visible result:

- **Source anchor:** physical or authorized emissive source, world position/direction and height, color tendency, and whether it is visible, offscreen, moving, or occluded. In a continuous multi-shot location, consume fixed source identity and world location from `SceneSpatialContract`; do not establish a competing anchor here.
- **Subject response:** current lit and shadow planes; face/eye readability; material-specific response on skin, hair, cloth, metal, wet, glass, translucent, or emissive surfaces.
- **Contact and nearby receivers:** cast/contact shadow, grounding, reflected or bounced color, nearby wall/ground/prop response, and effect-caused interactive light when present.
- **Depth and atmosphere:** foreground/midground/background separation, aerial or volumetric attenuation, haze/particles, and reflection depth only when those receivers exist.
- **Camera-visible result:** coherent exposure, contrast, color temperature, black level, highlight roll-off, or light-through-medium atmosphere only when materially visible. Focal plane, depth of field, defocus, and focus shifts retain their confirmed structure owner; motion blur remains a shot/camera execution field in `shot-craft.md`.
- **Continuity state:** the static source anchor and exposure relation that the next shot must inherit. `world-dynamics.md` and `BoundaryState` own moving-light phase, flicker, occlusion change, and residual-glow timing; this spec consumes their current state to describe the visible receiving result.

For a simple shot, one compact sentence can carry source anchor, subject response, and one grounding or depth cue. Add more only for a side/back/low-key setup, reflective/translucent material, moving/occluded source, VFX, several shots in one space, or an observed failure.

## Authority and reference conflict

Apply authority per lighting field:

`current user light instruction > active project/source light lock > current scene or boundary evidence > asset explicitly assigned lighting > coherent text-only design > platform default`

A character, product, costume, or prop reference assigned only identity, appearance, wardrobe, shape, or material does not own its baked key light, shadow direction, background color cast, rim light, or exposure. Re-light that subject from the active scene source while preserving its authorized base appearance and material behavior.

When a scene image owns lighting, borrow the visible source direction, color relation, exposure, shadow family, and atmosphere that the current crop can support. Do not copy a screen-left/screen-right label blindly across a camera cut; preserve the world anchor and recalculate which subject plane the new camera sees.

If two authoritative assets assign incompatible light anchors or exposure states to the same shot, route the conflict through `IntentFactGate`. A merely unassigned character-reference light is not a conflict and must not override the scene.

## Structure-table rendering

The `光影、合成与环境连续性` cell is a compact visible integration preview, not a mood label or software recipe. For every new/reference-generated, rebuilt, extended, or bridged visible unit, state:

1. the active source anchor or inherited world-light relation;
2. how the subject—or primary visible environment/object—and at least one visible ground, nearby-material, depth, or atmosphere receiver belong to that same light;
3. any continuity-critical static source anchor or exposure relation; take moving phase or residual state from `world-dynamics.md` without owning it twice.

Use `待确认` only when a materially required source anchor or boundary light cannot be read and competing choices change the result. A source-preserving edit may say `沿用视频1当前光影合成关系`. Do not use a bare phrase such as `电影感光影`、`冷暖对比`、`角色融入场景` or `光影统一`.

Examples:

- `站台顶灯从人物右上方落下，暖光同时照亮面部、伞面和湿地反光，脚下接触影朝左后方，远处冷雨雾降低对比。`
- `法术光球是当前主光源，青光先照亮施术手与近侧面部，再扫过石地和浮尘；背景仍保持低曝光。`
- `夕阳世界方位不变；切到反打后人物改为左后侧轮廓受光，台阶投影和远山空气透视保持同一方向。`

## Final prompt ownership

- Put a stable source anchor and baseline atmosphere once at their smallest shared scope. Use `场景：` only when they remain valid across the complete sequence; otherwise keep each local, moving, or effect source in its owning shot.
- In every owning shot, render the current subject-facing response plus the smallest contact, nearby-receiver, depth, or exposure cue needed to prove integration. The sentence must stand on its current visible state and must not say `同上一镜`.
- Keep appearance materials in `主体：`; describe only their current response to the active light in the shot.
- For an emissive effect, state the receiver order and visible exposure consequence. A glow that affects no subject, ground, nearby surface, particles, shadow, or reflection reads as an overlay.
- Translate production methods into visible results. Terms such as AOV, render pass, light wrap, grade, comp, or denoise belong only in an actual production-plan request.
- Consume the confirmed focal plane, depth of field, defocus, focus shift, and motion blur without redesigning them. Any change to those fields routes through the structure impact rules in `change-impact-and-delivery.md`.

## Failure diagnosis and smallest repair

| Observed result | Likely cause | Smallest repair |
| --- | --- | --- |
| Character looks pasted into the scene | appearance reference retained baked light or no shared receiver chain exists | make the scene the light authority; state subject relighting plus contact/depth response |
| Feet float or body lacks weight | missing or inconsistent contact/cast shadow and ground response | add one directionally coherent contact/cast shadow and ground reflection/bounce cue |
| Face is lit from the wrong side after a cut | screen direction was copied instead of preserving the world light | keep the source world anchor and recompute the camera-visible lit plane |
| VFX looks like a sticker | emissive effect has no interactive light or exposure consequence | connect it to the nearest subject/material/atmosphere receivers in causal order |
| Character and background have different color worlds | exposure, color temperature, black level, or atmospheric attenuation is split | state one camera-visible exposure/color relation and depth falloff for both |
| Shot is flat despite correct key direction | no foreground/background attenuation, occlusion, haze, reflection depth, or exposure separation | add the one existing light/atmosphere depth carrier that best serves the shot; route any focal-plane or depth-of-field change through structure impact |

Do not respond to these failures with a generic quality suffix or a list of every compositing term. Repair the first broken causal link and recheck the complete shot.
