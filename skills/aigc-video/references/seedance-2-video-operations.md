# Seedance 2.0 Video Operations

Load this file only for strict video editing, extension, or shot bridging. The source basis and provider version follow `seedance-2-rules.md`.

## Strict edit

Record the source anchor as `edit_target`. Address it directly; do not give it borrowed dimensions or introduce it with `参考`.

- add: name the new element, interval when needed, frame position, and visible action
- modify: `严格编辑@视频1，将[原特征]修改为[新特征]。`
- delete: name the removed element and one compact preservation boundary

Unmentioned content remains unchanged. Externalize only continuity layers the edit could disturb.

## Extension

Record the source anchor as `extension_source`. Use direct source grammar:

- `向后延长@视频1，生成……`
- `向前延长@视频1，生成……`
- `生成@视频1之后的内容，……`

For append-after, continue from the source ending BoundaryState. For prepend-before, generate a predecessor whose terminal BoundaryState converges on the source opening. Never use the source ending as the boundary for prepend-before.

The provider automatically takes the needed connection portion from the input; the original source segment is not regenerated. State only boundary facts that are required and not already readable. Use extension for continuous action, dialogue, emotional progression, or one movement path. Prefer separate generation/editing for scene changes, major action turns, chases, fights, or montages. Repeated extension can accumulate quality loss, especially on faces.

## Bridge / track completion

Record the first source as `bridge_predecessor` and the second as `bridge_successor`. Write sources in order and describe the visible bridge:

`@视频1，[可见过渡]，接@视频2。`

Start from video 1's ending BoundaryState and converge on video 2's opening BoundaryState. Carry only the necessary subject motion, camera motion, material, light, shape, or source-backed sound.

The checked official guide states at most three input videos with combined duration no more than 15 seconds. Re-check this limit for another provider or later model version.

## Combined intent

When one asset supplies a reference dimension and another is the edit target, keep both roles explicit:

`参考@图1的[参考维度]，严格编辑@视频1，[具体编辑内容]。`

Record `@图1` as `reference_input` with the named borrowed dimension and `@视频1` as `edit_target`. Do not assign a borrowed dimension to the edit target.
