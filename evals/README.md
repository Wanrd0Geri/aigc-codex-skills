# 可重放验证基础设施

这是离线导入器和确定性检查器，只使用 Python 标准库（Python 3.10+）。它不调用模型，不编辑或生成媒体，不根据手写预期制造“模型通过”记录。

`cases/` 包含 15 个案例、13 个案例族：诊断报告的 12 类，加“删除白杯及其归属倒影”。有 2 份已归档真实可读输入：本轮 imagegen 创建的镜面桌源图，以及由源图构造的 5 秒静态视频。其他 5 份图像/上下文要求明确待注入。静态视频只能验证该静态输入上的源保留工作流，不能验证复杂动作、接缝运动或口型质量。

## 先运行维护检查

在仓库根目录：

```sh
python3 evals/harness.py validate
python3 -m unittest discover -s evals/tests -v
```

第一条验证 case/rule 引用、规则定义文件及素材哈希，并列出待提供素材。第二条是 harness 自测，包含会故意改坏锚点、台词、时间轴、授权作用域、状态、哈希的负例；也检查视频 Skill 的手写状态示例是否自洽。两者都不计作模型前向测试。自测文件只在临时目录构造 synthetic 数据。

## 发起独立前向测试

```sh
python3 evals/harness.py packet \
  --case evals/cases/video-literal-anchors.json \
  --out work/eval-inputs/video-literal-anchors.json
```

packet 只包含原始用户消息、逻辑请求/轮次标识、附件角色、路径及哈希，**不包含 assertion、manual_checks、rule_ids 或预期赢家**。测试者另行使用当前宿主支持的模型/agent 执行请求；保持附件、消息顺序和原话一致，单独保存实际回复与来源标识。

分别记录 `baseline`（固定旧快照）、`current`（固定当前快照）、`candidate`（候选快照）或 `no-skill`。这些是比较标签，不自动加载、隔离或调用对应 Skill。运行者必须自行确保实际上下文与标签匹配；候选未提交时记录工作树快照说明，并优先附 `skill_files` 的实际文件哈希。不得给无 Skill 组载入候选规则或测试预期。

多轮测试按 `messages` 顺序逐轮执行。后续输入引用真实上一轮输出；不得用人工理想回复替代上一轮。需要状态观测时，保留外部可见状态记录或模型明确报告的审计字段；正常用户 prompt 仍按 Skill 输出要求交付。没有捕获的状态只能为 `blocked` 或人工待审，不能补写“模型当时肯定有”的状态。

## 导入真实已捕获输出

创建 `submission.json`（完整字段定义见 [FORMAT.md](FORMAT.md)）：

```json
{
  "schema_version": 1,
  "run_id": "candidate-anchors-001",
  "case_id": "video-literal-anchors",
  "source_kind": "imported_forward",
  "variant": "candidate",
  "provider": "actual-provider",
  "model": "actual-model-version",
  "settings": {"temperature": "not_exposed"},
  "skill_revision": "actual-git-revision-or-working-tree-snapshot",
  "captured_at": "2026-09-05T00:00:00+00:00",
  "provenance": {"capture_method": "agent-export", "source_ref": "actual-task-or-run-id"},
  "outputs": [{"turn_id": "t1", "text_path": "actual-output.txt"}]
}
```

这是录入模板，不是运行结果。路径以 submission 所在目录为基准，支持明确的绝对路径。若图片/视频实际被展示给测试 agent，添加 `fixture_inputs`；文件已存在并不等于它被展示。完整 transcript 和实际加载的 Skill 文件可选，但缺失时报告明确标记证据不足。

```sh
python3 evals/harness.py import-run \
  --case evals/cases/video-literal-anchors.json \
  --submission work/eval-inputs/submission.json \
  --out work/eval-runs/candidate-anchors-001
python3 evals/harness.py verify-run work/eval-runs/candidate-anchors-001
```

导入目录保存 case、rule、submission 原件、实际文本、可选 transcript/trace、被绑定的输入素材、可选媒体结果与实际 provider prompt、可选 Skill 文件，以及 SHA-256 清单和逐断言报告。导入目录已存在时拒绝覆盖。`verify-run` 验证归档字节和离线重放结果，不再次调用模型。哈希用于可追踪和发现文件变化，不是执行来源的密码学认证。

退出码：`0` 表示命令执行成功；`import-run` 的确定性检查失败或被缺失证据阻断返回 `1`，但仍保存结果；结构/路径/哈希错误返回 `2`。没有确定性断言的案例是 `not_assessed`，不会显示为通过。

## 导入生成结果与人工审阅

实际 provider 编辑输出通过可选 `media_outputs` 导入：

```json
{
  "media_outputs": [{
    "path": "actual-edit.png",
    "role": "edited-image",
    "provider": "actual-provider",
    "model": "actual-model-version",
    "settings": {"seed": "not_exposed"},
    "prompt_turn_id": "t1",
    "prompt_path": "actual-provider-prompt.txt"
  }]
}
```

它只归档和校验文件，状态为 `captured_pending_review`，不会自动判断像素或音视频。实际送入 provider 的提示词与捕获回复不完全相同时，务必附 `prompt_path`，不要把手动修过的 provider prompt 偷算作 agent 原始输出。

人工/独立模型评审另存 JSON 后追加：

```sh
python3 evals/harness.py import-review work/eval-runs/candidate-anchors-001 work/eval-inputs/review.json
```

每项评审必须引用归档文件及行号、区域、帧号或时间段，记录审阅者、human/model 类型、是否对版本盲化、通过/失败/无法判断/不适用和理由。真实媒体判定只能引用已捕获的 `media_output`。不同审阅者的记录独立保留，不覆盖原始证据或合并成总分。

## 证据边界

- `harness_self_test_only`：验证检查器和手写示例，没有模型执行。
- `imported_forward_output`：实际回复由运行者导入；来源仍是运行者声明。可独立检查文字和材料，不等于整个语义或工具链通过。
- `assistant_reported` trace：只能检查状态声明的一致性，不能证明内部私有推理、工具真的运行或实际像素正确。
- 人工语义审查独立 `pending`；缺 trace、缺 fixture、未声明实际展示不能以文字中的“已读取/已验证”补足。
- 媒体归档与媒体评审分别记录。任何文字格式通过都不会把 `overall_skill_pass` 从 `null` 改成 true，也不会生成通用效果评分。

后续需要的是补充真实多模态输入、独立前向输出和实际 provider 产物。请把运行产物放在仓库的 `work/` 或明确的外部证据目录，不把批量运行记录混入日常 Skill 上下文。
