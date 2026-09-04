"""Synthetic negative/positive checks of the harness, not Skill/model tests."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import harness as h


class AssertionTests(unittest.TestCase):
    def setUp(self):
        self.case = {
            "schema_version": 1, "id": "synthetic", "title": "self-test only", "family": "self-test",
            "rule_ids": ["VIDEO-STATE-01"], "fixtures": [], "authorizations": [],
            "messages": [{"id": "u1", "role": "user", "content": "测试输入", "request_id": "r1", "output_turn": "t1"}],
            "assertions": [], "manual_checks": [],
        }

    def check(self, kind, raw_text="", events=None, **params):
        assertion = {"id": "check", "kind": kind, "turn_id": "t1", **params}
        return h.check_assertion(assertion, {"text": raw_text, "events": events or []}, self.case)

    def test_literal_detects_normalized_anchor(self):
        self.assertEqual(self.check("literal", "参考@图1", **{"text": "@图1"})["status"], "pass")

    def test_literal_negative(self):
        result = h.check_assertion({"id": "x", "kind": "literal", "turn_id": "t1", "text": "@图1"},
                                   {"text": "参考图片1"}, self.case)
        self.assertEqual(result["status"], "fail")

    def test_literal_duplicate_detected(self):
        result = h.check_assertion({"id": "x", "kind": "literal", "turn_id": "t1", "text": "@图1"},
                                   {"text": "@图1，再写@图1"}, self.case)
        self.assertEqual(result["status"], "fail")

    def test_quoted_dialogue_not_substring(self):
        assertion = {"id": "d", "kind": "dialogue", "turn_id": "t1", "text": "钥匙在桌上", "allow_terminal_punctuation": True}
        self.assertEqual(h.check_assertion(assertion, {"text": "他说：“钥匙在桌上。”"}, self.case)["status"], "pass")
        self.assertEqual(h.check_assertion(assertion, {"text": "他说：“钥匙在桌上面。”"}, self.case)["status"], "fail")

    def test_timeline_contiguous_and_gap(self):
        kwargs = {"duration": 8, "shot_count": 2}
        self.assertEqual(self.check("timeline", "镜头1（0-4秒）：甲。镜头2（4-8秒）：乙。", **kwargs)["status"], "pass")
        for text in ("镜头1（0-3秒）：甲。镜头2（4-8秒）：乙。", "镜头1（0-5秒）：甲。镜头2（4-8秒）：乙。", "镜头2（0-4秒）：甲。镜头3（4-8秒）：乙。"):
            self.assertEqual(self.check("timeline", text, **kwargs)["status"], "fail")

    def test_interval_equivalent_spelling_and_wrong_value(self):
        for text in ("第2–4秒", "2-4秒", "第2到4秒"):
            self.assertEqual(self.check("interval", text, start=2, end=4)["status"], "pass")
        self.assertEqual(self.check("interval", "2-5秒", start=2, end=4)["status"], "fail")

    def test_missing_trace_blocked(self):
        self.assertEqual(self.check("trace_fields", selector={"type": "state_snapshot"}, fields={"structure_status": "confirmed"})["status"], "blocked")

    def state(self, **changes):
        fields = {"task_kind": "edit", "structure_status": "source_preserved", "structure_version": None,
                  "structure_review_mode": None, "acceptance_ref": None, "delivery_decision": "deliver",
                  "changed_fields": ["cloth.color"], "invalidated_fields": ["material"], "rechecked_fields": ["material"],
                  "light_composite_applicability": "physical", "light_composite_review": "resolved"}
        fields.update(changes)
        return {"event_id": "s1", "type": "state_snapshot", "actor": "assistant_reported", "unit_id": "shot1", "fields": fields, "evidence": ["u1"]}

    def state_check(self, event):
        return self.check("state_consistency", events=[event], structure_fields=["camera", "occlusion"])

    def test_state_source_preserved_legal(self):
        self.assertEqual(self.state_check(self.state())["status"], "pass")

    def test_state_source_preserved_cannot_extend_or_change_camera(self):
        for change in ({"task_kind": "extend"}, {"changed_fields": ["camera"]}, {"structure_version": 1}):
            self.assertEqual(self.state_check(self.state(**change))["status"], "fail")

    def test_confirmed_needs_acceptance(self):
        event = self.state(structure_status="confirmed", structure_version=3, acceptance_ref="u1")
        self.assertEqual(self.state_check(event)["status"], "fail")
        self.case["acceptances"] = [{"message_id": "u1", "unit_id": "shot1", "structure_version": 3}]
        self.assertEqual(self.state_check(event)["status"], "pass")

    def test_physical_na_and_stale_dependency_fail(self):
        for change in ({"light_composite_review": "not_applicable"}, {"rechecked_fields": []}):
            self.assertEqual(self.state_check(self.state(**change))["status"], "fail")

    def test_confirmed_change_needs_explicit_acceptance_coverage(self):
        self.case["acceptances"] = [{"message_id": "u1", "unit_id": "shot1", "structure_version": 3}]
        event = self.state(structure_status="confirmed", structure_version=3, acceptance_ref="u1", changed_fields=["camera"])
        self.assertEqual(self.state_check(event)["status"], "fail")
        self.case["acceptances"][0]["covers_structure_changes"] = ["camera"]
        self.assertEqual(self.state_check(event)["status"], "pass")

    def test_old_acceptance_cannot_cover_later_structure_changes(self):
        self.case["messages"].append({"id": "u2", "role": "user", "content": "新机位", "request_id": "r2", "output_turn": "t2"})
        self.case["acceptances"] = [{"message_id": "u1", "unit_id": "shot1", "structure_version": 3, "covers_structure_changes": ["camera"]}]
        event = self.state(structure_status="confirmed", structure_version=3, acceptance_ref="u1", changed_fields=["camera"])
        assertion = {"id": "check", "kind": "state_consistency", "turn_id": "t2", "structure_fields": ["camera"]}
        self.assertEqual(h.check_assertion(assertion, {"text": "", "events": [event]}, self.case)["status"], "fail")

    def test_missing_state_field_blocked(self):
        event = self.state()
        del event["fields"]["changed_fields"]
        self.assertEqual(self.state_check(event)["status"], "blocked")

    def test_pending_light_or_world_cannot_deliver(self):
        for field in ("light_composite_review", "world_dynamics_review"):
            event = self.state(**{field: "pending"})
            self.assertEqual(self.state_check(event)["status"], "fail")
            event["fields"]["delivery_decision"] = "wait_for_input"
            self.assertEqual(self.state_check(event)["status"], "pass")

    def test_review_exemptions_and_missing_new_physical_review(self):
        # Inherited untouched source state need not acquire a fabricated review.
        self.assertEqual(self.state_check(self.state(light_composite_review=None))["status"], "pass")
        self.assertEqual(self.state_check(self.state(operation="language_only", light_composite_review="pending"))["status"], "pass")
        self.assertEqual(self.state_check(self.state(light_composite_applicability="non_physical", light_composite_review="not_applicable"))["status"], "pass")
        event = self.state(task_kind="new_text", structure_status="pending", admission_basis="direct_authorized", light_composite_review=None)
        self.assertEqual(self.state_check(event)["status"], "blocked")

    def test_acceptance_change_coverage_schema(self):
        self.case["acceptances"] = [{"message_id": "u1", "unit_id": "shot1", "structure_version": 3, "covers_structure_changes": "camera"}]
        with self.assertRaisesRegex(ValueError, "string array"):
            h.validate_case(self.case, h.read_json(h.ROOT / "rules.json"))

    def test_touched_source_light_cannot_use_null_inheritance(self):
        event = self.state(changed_fields=["light.intensity"], invalidated_fields=["light_composite_review"],
                           rechecked_fields=["light_composite_review"], light_composite_review=None)
        self.assertEqual(self.state_check(event)["status"], "blocked")
        event["fields"]["light_composite_review"] = "resolved"
        self.assertEqual(self.state_check(event)["status"], "pass")

    def test_explicitly_invalidated_world_cannot_use_null_inheritance(self):
        event = self.state(changed_fields=["world.driver"], invalidated_fields=["world_dynamics_review"],
                           rechecked_fields=["world_dynamics_review"], world_dynamics_review=None)
        self.assertEqual(self.state_check(event)["status"], "blocked")
        event["fields"]["world_dynamics_review"] = "resolved"
        self.assertEqual(self.state_check(event)["status"], "pass")
        self.assertEqual(self.state_check(self.state(world_dynamics_review=None))["status"], "pass")

    def test_language_only_can_leave_uninitialized_design_state(self):
        event = self.state(operation="language_only", structure_status=None, admission_basis="language_only",
                           light_composite_applicability=None, light_composite_review=None,
                           changed_fields=[], invalidated_fields=[], rechecked_fields=[])
        self.assertEqual(self.state_check(event)["status"], "pass")
        event["fields"]["changed_fields"] = ["camera"]
        self.assertEqual(self.state_check(event)["status"], "fail")

    def test_candidate_authored_state_examples_are_consistent(self):
        path = h.ROOT.parent / "skills/aigc-video/tests/state-traces.json"
        data = h.read_json(path)
        self.assertEqual(data["evidence_level"], "fixture_only")
        for scenario in data["scenarios"]:
            case = copy.deepcopy(self.case)
            case["acceptances"] = scenario["acceptances"]
            case["authorizations"] = scenario["authorizations"]
            case["messages"] = [{"id": t["user_event"]["message_id"], "role": "user", "content": t["user_event"]["text"],
                                 "request_id": t["user_event"]["request_id"], "output_turn": f"t{i+1}"}
                                for i, t in enumerate(scenario["turns"])]
            for index, turn in enumerate(scenario["turns"], 1):
                with self.subTest(scenario=scenario["id"], turn=index):
                    h.validate_trace(turn["expected_events"])
                    assertion = {"id": "state", "kind": "state_consistency", "turn_id": f"t{index}", "structure_fields": scenario["structure_fields"]}
                    actual = h.check_assertion(assertion, {"text": "", "events": turn["expected_events"]}, case)
                    self.assertEqual(actual["status"], "pass", actual["detail"])

    def artifact(self, request="r1", unit="shot1", evidence=None):
        return {"event_id": "a1", "type": "artifact", "actor": "assistant_reported", "unit_id": unit,
                "fields": {"request_id": request, "admission_basis": "direct_authorized"}, "evidence": evidence or ["u1"]}

    def test_permission_scope_and_request(self):
        self.case["authorizations"] = [{"message_id": "u1", "request_id": "r1", "units": ["shot1"], "actions": ["skip_structure_review"]}]
        self.assertEqual(self.check("permission_scope", events=[self.artifact()])["status"], "pass")
        self.assertEqual(self.check("permission_scope", events=[self.artifact(unit="shot2")])["status"], "fail")
        self.assertEqual(self.check("permission_scope", events=[self.artifact(request="r2")])["status"], "fail")

    def test_future_permission_not_available(self):
        self.case["messages"].append({"id": "u2", "role": "user", "content": "稍后授权", "request_id": "r1", "output_turn": "t2"})
        self.case["authorizations"] = [{"message_id": "u2", "request_id": "r1", "units": ["shot1"], "actions": ["skip_structure_review"]}]
        self.assertEqual(self.check("permission_scope", events=[self.artifact(evidence=["u2"])])["status"], "fail")

    def test_permission_missing_basis_is_not_a_pass(self):
        event = self.artifact()
        del event["fields"]["admission_basis"]
        self.assertEqual(self.check("permission_scope", events=[event])["status"], "blocked")
        event["fields"]["admission_basis"] = "unknown_basis"
        self.assertEqual(self.check("permission_scope", events=[event])["status"], "blocked")
        event["fields"]["admission_basis"] = "confirmed_version"
        self.assertEqual(self.check("permission_scope", events=[event])["status"], "pass")


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.case = {"schema_version": 1, "id": "synthetic-import", "title": "synthetic", "family": "self-test",
                     "rule_ids": ["VIDEO-LITERAL-01"], "messages": [{"id": "u1", "role": "user", "content": "保留@图1", "request_id": "r1", "output_turn": "t1"}],
                     "fixtures": [], "assertions": [{"id": "anchor", "kind": "literal", "turn_id": "t1", "text": "@图1"}],
                     "manual_checks": [{"id": "semantic", "question": "语义是否保持？", "evidence_kind": "prompt", "rule_ids": []}]}
        self.sub = {"schema_version": 1, "run_id": "synthetic-001", "case_id": self.case["id"], "source_kind": "synthetic_self_test",
                    "variant": "candidate", "provider": "none-self-test", "model": "none-self-test", "settings": {},
                    "skill_revision": "synthetic-no-skill-loaded", "captured_at": "2026-09-05T00:00:00+00:00",
                    "provenance": {"capture_method": "handwritten-test-data", "source_ref": "unittest"},
                    "outputs": [{"turn_id": "t1", "text_path": "output.txt"}]}
        (self.root / "output.txt").write_text("保留@图1。", encoding="utf-8")

    def run_import(self):
        h.dump_json(self.root / "case.json", self.case)
        h.dump_json(self.root / "submission.json", self.sub)
        return h.import_run(self.root / "case.json", self.root / "submission.json", self.root / "run")

    def test_synthetic_is_not_forward_and_manual_stays_pending(self):
        report = self.run_import()
        self.assertEqual(report["deterministic_status"], "pass")
        self.assertEqual(report["evidence"]["category"], "harness_self_test_only")
        self.assertIsNone(report["evidence"]["overall_skill_pass"])
        self.assertEqual(report["manual_checks"][0]["status"], "pending")
        self.assertEqual(h.verify_run(self.root / "run")["replay"], "pass")

    def test_captured_output_and_manifest_tampering_detected(self):
        self.run_import()
        (self.root / "run/captures/01-output.txt").write_text("改为图片1", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "asset changed"):
            h.verify_run(self.root / "run")

    def test_case_tampering_detected(self):
        self.run_import()
        (self.root / "run/case.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "manifest changed"):
            h.verify_run(self.root / "run")

    def test_pending_fixture_blocks_import_evidence(self):
        self.case["fixtures"] = [{"id": "missing", "kind": "image", "role": "source", "required": True, "path": None, "sha256": None}]
        self.assertEqual(self.run_import()["deterministic_status"], "blocked")

    def test_fixture_hash_and_presentation_are_separate(self):
        fixture = self.root / "fixture.bin"
        fixture.write_bytes(b"synthetic fixture bytes; not an image")
        self.case["fixtures"] = [{"id": "f1", "kind": "image", "role": "source", "required": True, "path": "fixture.bin", "sha256": h.digest(fixture)}]
        self.assertEqual(self.run_import()["fixtures"][0]["status"], "presentation_not_declared")

    def test_hash_mismatch_rejected(self):
        fixture = self.root / "fixture.bin"
        fixture.write_bytes(b"synthetic")
        self.case["fixtures"] = [{"id": "f1", "kind": "image", "role": "source", "required": True, "path": "fixture.bin", "sha256": "0" * 64}]
        with self.assertRaisesRegex(ValueError, "fixture hash mismatch"):
            self.run_import()

    def test_media_archived_but_not_verified(self):
        (self.root / "media.bin").write_bytes(b"synthetic output bytes; no actual pixels")
        self.sub["media_outputs"] = [{"path": "media.bin", "role": "edited-result", "provider": "none", "model": "none", "settings": {}, "prompt_turn_id": "t1"}]
        report = self.run_import()
        self.assertEqual(report["evidence"]["media_output_status"], "captured_pending_review")
        self.assertEqual(h.verify_run(self.root / "run")["integrity"], "pass")

    def test_transcript_mismatch_rejected(self):
        self.sub["transcript_path"] = "transcript.json"
        h.dump_json(self.root / "transcript.json", [{"role": "user", "id": "u1", "content": "different input"}, {"role": "assistant", "turn_id": "t1", "content": "保留@图1。"}])
        with self.assertRaisesRegex(ValueError, "user messages differ"):
            self.run_import()

    def test_no_assertions_is_not_pass(self):
        self.case["assertions"] = []
        self.assertEqual(self.run_import()["deterministic_status"], "not_assessed")

    def test_no_skill_requires_null_revision(self):
        self.sub["variant"] = "no-skill"
        with self.assertRaisesRegex(ValueError, "null skill_revision"):
            self.run_import()

    def test_replay_rejects_inconsistent_aggregate(self):
        (self.root / "output.txt").write_text("参考图片1", encoding="utf-8")
        report = self.run_import()
        self.assertEqual(report["deterministic_status"], "fail")
        self.assertEqual(h.verify_run(self.root / "run")["deterministic_status"], "fail")
        report["deterministic_status"] = "pass"
        h.dump_json(self.root / "run/report.json", report)
        with self.assertRaisesRegex(ValueError, "aggregate status"):
            h.verify_run(self.root / "run")

    def add_fixture(self):
        fixture = self.root / "fixture.bin"
        fixture.write_bytes(b"synthetic fixture; not actual image data")
        self.case["fixtures"] = [{"id": "f1", "kind": "image", "role": "source", "required": True,
                                  "path": "fixture.bin", "sha256": h.digest(fixture)}]
        self.sub["fixture_inputs"] = [{"id": "f1", "sha256": h.digest(fixture), "presented_as": "synthetic declaration"}]

    def test_replay_requires_complete_inventory_and_bound_fixture_hash(self):
        self.add_fixture()
        self.run_import()
        # Replay is portable and must not read the original external fixture.
        (self.root / "fixture.bin").unlink()
        self.assertEqual(h.verify_run(self.root / "run")["integrity"], "pass")
        assets = h.read_json(self.root / "run/assets.json")
        kept = [a for a in assets if a["kind"] != "input_fixture"]
        h.dump_json(self.root / "run/assets.json", kept)
        with self.assertRaisesRegex(ValueError, "asset coverage"):
            h.verify_run(self.root / "run")
        item = next(a for a in assets if a["kind"] == "input_fixture")
        path = self.root / "run" / item["path"]
        path.write_bytes(b"different fixture")
        item["sha256"] = h.digest(path)
        h.dump_json(self.root / "run/assets.json", assets)
        with self.assertRaisesRegex(ValueError, "fixture/skill binding"):
            h.verify_run(self.root / "run")

    def test_replay_checks_all_declared_asset_types(self):
        self.add_fixture()
        (self.root / "media.bin").write_bytes(b"synthetic media")
        (self.root / "skill.md").write_text("synthetic skill")
        h.dump_json(self.root / "trace.json", [])
        self.sub["outputs"][0]["trace_path"] = "trace.json"
        self.sub["media_outputs"] = [{"path": "media.bin", "role": "result", "provider": "none", "model": "none",
                                      "settings": {}, "prompt_turn_id": "t1", "prompt_path": "output.txt"}]
        self.sub["skill_files"] = [{"path": "skill.md", "sha256": h.digest(self.root / "skill.md")}]
        self.sub["transcript_path"] = "transcript.json"
        h.dump_json(self.root / "transcript.json", [{"role": "user", "id": "u1", "content": "保留@图1"},
                    {"role": "assistant", "turn_id": "t1", "content": "保留@图1。"}])
        self.run_import()
        self.assertEqual(h.verify_run(self.root / "run")["integrity"], "pass")
        assets = h.read_json(self.root / "run/assets.json")
        for removed in assets:
            with self.subTest(kind=removed["kind"]):
                h.dump_json(self.root / "run/assets.json", [a for a in assets if a != removed])
                with self.assertRaisesRegex(ValueError, "asset coverage"):
                    h.verify_run(self.root / "run")
        h.dump_json(self.root / "run/assets.json", assets)

    def test_replay_recomputes_fixture_presentation_and_pending_status(self):
        self.add_fixture()
        self.sub["fixture_inputs"] = []
        report = self.run_import()
        self.assertEqual(h.verify_run(self.root / "run")["deterministic_status"], "blocked")
        report["fixtures"][0]["status"] = "hash_verified_presentation_declared"
        h.dump_json(self.root / "run/report.json", report)
        with self.assertRaisesRegex(ValueError, "fixture status"):
            h.verify_run(self.root / "run")

    def test_symlink_alias_names_replay_without_originals(self):
        self.add_fixture()
        alias = self.root / "input.alias"
        alias.symlink_to(self.root / "fixture.bin")
        self.case["fixtures"][0]["path"] = "input.alias"
        self.sub["media_outputs"] = [{"path": "input.alias", "role": "result", "provider": "none", "model": "none",
                                      "settings": {}, "prompt_turn_id": "t1"}]
        self.sub["skill_files"] = [{"path": "input.alias", "sha256": h.digest(alias)}]
        self.run_import()
        alias.unlink()
        (self.root / "fixture.bin").unlink()
        self.assertEqual(h.verify_run(self.root / "run")["integrity"], "pass")


if __name__ == "__main__":
    unittest.main()
