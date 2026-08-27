# Reference roles and text gate

## Attribute whitelist

Assign each reference only the fields named by the user. Record unassigned fields as unavailable.

| Role | Authorized | Not authorized unless separately assigned |
| --- | --- | --- |
| identity | face, hair, apparent age, body identity, named costume traits | pose, camera, lighting, environment |
| composition | framing, crop, camera relation, placement, scale, overlap, layers, negative space | object identity, environment, palette, material, light, text, style |
| pose | body configuration, gesture, gaze, contact | identity, costume, setting, camera |
| environment | named set, weather, light, material, props | identity, pose, camera changes |
| style axis | only named medium/shape/edge/surface/texture/palette/light/finish axes | reference subject, layout, text, brand, unassigned axes |
| semantic palette | only the declared positional color roles | scene content, layout, texture, typography, light direction, shadow geometry |

If a composition reference contains a circle, preserve its geometry without naming it as a moon unless the user or target facts establish that meaning.

If a reference role is ambiguous and different mappings produce different images, show your assumed mapping and ask. Otherwise keep the unassigned field neutral.

## Text and marks

- Fully legible and authorized: preserve exact characters, case, line breaks, count, placement, hierarchy, and legibility.
- Partly legible: record only certain characters outside the prompt; do not complete the rest.
- Unreadable: describe size, color, density, and placement only when composition needs it.
- Logo or brand not verified: describe visible mark geometry; do not guess identity.
- Watermark: do not reproduce or quote it.
- Text excluded by a reference role: do not quote it even inside a negative instruction.
