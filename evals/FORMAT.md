# 数据格式 v1

文件均为 UTF-8 JSON，`schema_version: 1`。`harness.py` 中的显式验证函数是标准库实现的结构校验器；这里定义字段及证据含义，不依赖第三方 JSON Schema 库。

## Rule registry

`rules.json`：`rules` 数组，每项有 `id`、`owner`（仓库相对路径）、`summary`、`evidence`。owner 指规范定义位置，不能仅为碰巧提及 ID 的文件。CLI 验证定义文件存在及包含 ID；唯一语义归属仍需维护审查。规则 ID 的存在不证明执行结果。

## Case

| 字段 | 内容 |
| --- | --- |
| `id/title/family` | 稳定用例 ID、标题、报告案例族 |
| `rule_ids` | 适用规范 ID；断言和审阅的 rule_ids 必须为其子集 |
| `messages` | 按顺序的 `{id,role:"user",content,request_id,output_turn}`；request_id 表示逻辑任务，不能因缺输入后的续问随意重置 |
| `fixtures` | `{id,kind,role,required,path,sha256}`；路径基于 case 目录；未提供时 path/sha256 同为 null |
| `authorizations` | 可选 `{message_id,request_id,units,actions}`；引用真实输入消息，`skip_structure_review` 按 unit 与逻辑请求限定；`units:["*"]` 是明确的全请求范围 |
| `acceptances` | 可选 `{id?,message_id,unit_id,structure_version,covers_structure_changes?}`；输入已明确确认的版本，不从模型自称 confirmed 反推。可选 coverage 是不重复的非空字符串数组，逐项列出该输入明确接受的结构变更；只有当前轮的 coverage 可覆盖当前轮结构变化，旧版本的接受不自动扩张 |
| `assertions` | 独立机械检查，见下表；空数组表示未做机械判定 |
| `manual_checks` | `{id,question,rule_ids,evidence_kind}`；evidence_kind 为 prompt/trace/media，开始均为 pending |

### Assertion

共有 `id/kind/turn_id/rule_ids`；语义无法稳定机械判定时使用 manual_checks。

| kind | 参数与范围 |
| --- | --- |
| `literal` | `text/count`（默认1）；精确字面出现次数，用于锚点、参数、准确间隔。避免把普通措辞变成无意义 exact-match |
| `dialogue` | `text/count`、可选 `allow_terminal_punctuation`；检查中文/英文双引号中的完整内容，防止仅包含子串却改写台词。可显式容许末尾句号等标点；不验说话人、口型或音频 |
| `interval` | `start/end/count`；核对秒数区间，允许普通横线、en/em dash、到/至，不把等价间隔写法误判为时间改变 |
| `forbid` | `text`；精确禁止字面，仅用于确实字面受控的内容 |
| `ordered` | `texts`；字面出现顺序，不等于语义动作顺序或真实帧序 |
| `timeline` | `duration/shot_count`；解析 `镜头N（a-b秒）：`/ASCII括号及普通横线变体，验证索引、正区间、无间隙/重叠、总时长；不验视频实际时长 |
| `trace_fields` | `selector` 按事件顶层字段匹配且恰好一条，`fields` 做字段子集精确比较。缺事件 blocked |
| `state_consistency` | `structure_fields` 显式列出规范化结构字段；不猜自然语言。source_preserved 为 edit、版本/确认字段空且无结构变更；confirmed 必须匹配可用 acceptance，本轮结构变更还需本轮 acceptance 的显式 coverage。physical 不得 not_applicable；deliver 不得留未 rechecked 依赖、明确 pending 的灯光或世界审查；非编辑的物理设计若未捕获已完成灯光审查则 blocked。未改的源字段可继承/null，language_only 不新增设计审查但不可改结构。pending 结构直接交付需正确准入依据 |
| `permission_scope` | 对 artifact 事件中 `direct_authorized` 的交付，核对当前轮及此前真实输入的授权、request_id、unit 和 evidence。无 artifact 或缺少/未知 admission_basis 时 blocked；明确合法的其他准入依据不做直接授权检查 |

结构字段枚举、ChangeSet 完整性和事实读取是否真实仍须人工核查；模型可以漏报字段，机械一致性不能发现所有语义遗漏。`state_consistency` 的字段来自现有 TaskEnvelope/ChangeSet，只在测试捕获层按可检查的名称表达，不要求常规 prompt 输出内部 schema。

源字段继承不能覆盖已失效的审查：当 changed/invalidated 字段明确触及 `light`、`lighting`、`light_composite`、`light_composite_applicability/review`（含点号子字段）时，物理灯光 review 为 null 的交付 blocked；明确触及 `world`、`world_dynamics`、`world_dynamics_review/mode` 时，world review 缺失/null 也 blocked。未触及的源字段仍可继承；未捕获的其他自然语言变化不由这些规范根名推断。

## Submission

必填：`run_id/case_id/source_kind/variant/provider/model/settings/skill_revision/captured_at/provenance/outputs`。

- `source_kind`: `imported_forward` 或 `synthetic_self_test`。手工回复、人工理想结果和 harness 自测必须为后者。
- `variant`: baseline/current/candidate/no-skill。no-skill 的 skill_revision 必须 null，不能携带 skill_files；其他标签需要实际 revision 或明确快照说明。
- `captured_at`: 包含时区的 ISO 时间。provider/model/settings 是运行时实际值；UI 不暴露的参数写 `not_exposed`，不得猜 seed 或模型子版本。
- `provenance`: `{capture_method,source_ref}`，记录导出方式和实际 agent/task/provider run 标识。harness 不把此声明当独立认证。
- `outputs`: `{turn_id,text_path,trace_path?}` 数组，完整覆盖 case 的 output_turn，各一次。text_path 是未经事后改写的真实回复。
- `case_sha256`：可选，使用 packet 时应回填其 case 哈希；提供后必须与导入 case 一致。
- `fixture_inputs`：可选数组 `{id,sha256,presented_as}`，逐项说明已展示的 case fixture。必需素材未声明展示时结果 blocked；文件字节校验与“实际展示”分别记录。
- `skill_files`：可选 `{path,sha256}` 数组，实际已加载的入口与参考文件。导入时校验、复制；没有时 skill_snapshot_status=not_recorded。不能用候选当前文件冒充旧运行加载文件。
- `transcript_path`：可选，对话 JSON 数组。user 条目 `{role:"user",id,content}`，assistant 条目 `{role:"assistant",turn_id,content}`；允许夹在其间的 system/tool 记录。校验用户原话、回复和轮次顺序与 case/captures 精确相同。附件的实际展示还需导出记录/工具事件审查。
- `media_outputs`：可选 `{path,role,provider,model,settings,prompt_turn_id,prompt_path?}`；媒体与实际送给 provider 的 prompt 分别归档。仅存档不会触发像素评分。

所有输入路径基于 submission 所在目录；fixture path 例外，基于 case 所在目录。支持显式绝对路径。新 run 目录拒绝覆盖。

## Captured trace

trace 文件是事件数组。每条：

```json
{
  "event_id": "state-t1",
  "type": "state_snapshot",
  "actor": "assistant_reported",
  "unit_id": "segment1",
  "fields": {
    "task_kind": "edit",
    "structure_status": "source_preserved",
    "structure_version": null,
    "structure_review_mode": null,
    "acceptance_ref": null,
    "delivery_decision": "deliver",
    "admission_basis": "source_preserved",
    "changed_fields": ["cloth.color"],
    "invalidated_fields": ["material_response"],
    "rechecked_fields": ["material_response"],
    "light_composite_applicability": "physical",
    "light_composite_review": "resolved"
  },
  "evidence": ["u1"]
}
```

这是格式示例，不是运行记录。`type`: state_snapshot/authorization/tool_call/artifact/operation_planned/condition_inspected；`actor`: user/assistant_reported/tool/harness/reviewer。fields 保留相应 Skill 已有状态；图像沿用 observed/planned/verified、reads/writes/produces/checks 和 recheck_required。不能把 planned 改写为 verified 填测试。

authorization 检查的 artifact 事件至少含 `fields.request_id/admission_basis`、`unit_id`，evidence 引用授权用户消息。acceptance_ref 可以引用 case acceptance.id 或其 message_id。枚举/事件只描述可观察记录，不要求输出模型私有推理；事后补写轨迹必须说明是重建，不能标 tool 原始证据。

## Review

```json
{
  "schema_version": 1,
  "run_id": "candidate-anchors-001",
  "reviewer": "reviewer-name-or-model-run-id",
  "reviewer_kind": "human",
  "blind_to_variant": false,
  "checks": [{
    "id": "same-operation",
    "status": "pass",
    "reason": "按实际对照填写判断理由",
    "evidence": [{"path": "captures/01-output.txt", "location": "lines 1-3"}]
  }]
}
```

可逐批审阅，未审项目继续 pending。status 为 pass/fail/uncertain/not_applicable，每项必须有理由和归档位置；媒体项必须引用 media_output。reviewer_kind=model 时不得冒称人工审阅。当前不聚合不同评审、不自动刷新 Skill 的 validation-status、不生成总分。

## Run archive

`case.json/submission.json/rules.json` 为精确保留的导入原件；`captures/fixtures/media/skills` 按需存放实际字节；`assets.json` 记录相对位置和哈希；`report.json` 记录每条机械判定、阻断、人工 pending 和证据界限；`reviews/<review-sha256>.json` 追加审阅原件。

`verify-run` 从冻结的 case/submission 推导全部输出、trace、fixture、transcript、media/provider prompt、skill 文件的精确归档覆盖范围，并检查唯一条目、字节哈希与 fixture/skill 原绑定；不依赖原始外部路径。它从归档重新检查对话、fixture 展示声明、断言和汇总状态，拒绝保存摘要与复算不一致。它不重跑模型；`harness_sha256` 记录创建报告时版本，升级导致规则输出不同会提示差异。源码可从所记录仓库版本恢复。hash 清单不是防恶意重签的认证系统。
