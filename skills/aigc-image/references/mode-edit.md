# Edit mode

Treat every edit as a closed change request.

## Internal change set

- `Preserve`: visible source facts and user locks outside the requested edit.
- `Transform`: authorized properties plus the minimum integration needed for changed pixels.
- `Avoid`: one concrete likely drift only when Transform and Preserve cannot prevent it.
- `Released`: identity, count, text, camera, composition, geometry, light, color, or physical consistency the user explicitly allows to change.

Unmentioned content remains unchanged. Light, grade, depth, atmosphere, material, background, text, and props are independent permissions.

## Edit size

- `surgical`: one local operation; use 1-3 direct sentences.
- `controlled`: linked changes inside one visual system; use compact labeled blocks only when they improve auditability.
- `staged`: several capabilities with dependency or drift risk; recommend the order before compiling.

Do not silently split a requested deliverable or drop an authorized change. If the user keeps one integrated pass, compile all compatible modules and state the stability risk outside the prompt.

## Rendering rule

Use the common contract in `edit-contract.md`, then load only selected capability files. A single capability may supply the full Change and Integration text. Multiple capabilities supply fragments; merge shared roles and locks once.

When a result fails, identify the first failed capability or dependency and revise only that part. Do not rebuild the entire prompt unless the source, terminal artifact, or edit scope changed.
