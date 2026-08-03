# Local Project Packages

Project packages stored with this skill. Each subdirectory is one project and follows
`references/project-package-contract.md`. A package is project data, not a second copy of the skill.

Load a package only when the user names that project or the active work clearly belongs to it.
Never merge sources, assets, defaults, or exclusions across packages.

| Package | Project | Aliases | Scope | Status |
| --- | --- | --- | --- | --- |
| `linyuanxing/` | 临渊行 | 临渊行, linyuanxing, LYX | 第一集（完成，411 镜）、第二集（进行中，92 镜，止于 3-27） | current |

## Reading a package

1. `<pkg>/project.yaml` — manifest: sources, field-scoped precedence, defaults, exclusions.
2. `<pkg>/contexts/` — prepared, readable context. Start here.
3. `<pkg>/sources/` — the original files the context was converted from. Go here only to
   re-verify a disputed cell or when a needed field is absent from the prepared context.

## Note on .xlsx sources

Each spreadsheet source is converted verbatim to Markdown in `contexts/` at intake time, and
that Markdown is the working source of record. Read the Markdown first: it needs no runtime
and it already carries the intake decisions recorded under `conventions` in `project.yaml`.

The `.xlsx` sources are readable when a cell must be re-verified or a source re-converted.
Use the `py` launcher with openpyxl (verified 2026-08-04: Python 3.12.10, openpyxl 3.1.5);
plain `python`/`python3` resolve to a non-functional Windows Store alias here:

```python
wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
ws = wb[wb.sheetnames[0]]
```

Truncate each row to the header column count. Both workbooks report a wider raw dimension than
they use (`A1:AE412` and `A1:Q95`); the columns past the header are empty and otherwise trail
`None` through every row. Set stdout to UTF-8 before printing, or the console encoding mangles
Chinese output. Falling back to zip + `xl/sharedStrings.xml` parsing is no longer necessary.

When a source file is updated, re-convert it, bump `version` in `project.yaml`, and re-check
the anomaly list in the package's derived reference.
