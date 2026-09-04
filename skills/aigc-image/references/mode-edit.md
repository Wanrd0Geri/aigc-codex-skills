# Edit mode

Treat every edit as a closed change request.

## Internal change set

- `Preserve`: visible source facts and user locks outside the requested edit.
- `Transform`: authorized properties plus the minimum integration needed for changed pixels.
- `Avoid`: one concrete likely drift only when Transform and Preserve cannot prevent it.
- `Released`: identity, count, text, camera, composition, geometry, light, color, or physical consistency the user explicitly allows to change.

Unmentioned content remains unchanged. A change to light, grade, depth, atmosphere, material, background, text, or props does not generally authorize changing the others. Apply `IMG-AUTH-01` in [edit-contract.md](edit-contract.md) to distinguish global redesign from necessary local integration; standalone module Keep clauses are defaults.

## Edit size

- `surgical`: one local operation; use 1-3 direct sentences.
- `controlled`: linked changes inside one visual system; use compact labeled blocks only when they improve auditability.
- `staged`: a later edit needs the actual outcome of an earlier reconstruction, or observed failures support splitting; inspect the intermediate result before continuing.

Do not silently split a requested deliverable or drop an authorized change. Independent small changes and jointly specified visual systems can share one prompt. If a dependency makes one-pass execution uncertain, explain that specific dependency outside the prompt; do not infer instability from module count alone.

## Rendering rule

Use the common contract in `edit-contract.md`, then load only selected capability files. A single capability may supply the full Change and Integration text. Multiple capabilities supply fragments; merge shared roles and locks once.

For `perform-edit`, use [edit-operation-state.md](edit-operation-state.md) to retain the locked baseline and inspect each candidate. When a result fails, revise the failed operation and refresh affected dependents; preserve unrelated successful edits. Do not rebuild the entire prompt unless the source, terminal artifact, or edit scope changed.
