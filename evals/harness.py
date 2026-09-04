#!/usr/bin/env python3
"""Offline import and deterministic checks. Never invokes a model or provider."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VARIANTS = {"baseline", "current", "candidate", "no-skill"}
ACTORS = {"user", "assistant_reported", "tool", "harness", "reviewer"}
KINDS = {"literal", "dialogue", "interval", "forbid", "ordered", "timeline", "trace_fields", "state_consistency", "permission_scope"}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def need(condition, message):
    if not condition:
        raise ValueError(message)


def unique(values, label):
    need(len(values) == len(set(values)), f"duplicate {label}")


def validate_case(case, rules):
    need(case.get("schema_version") == 1, "case schema_version must be 1")
    for key in ("id", "title", "family", "rule_ids", "messages", "assertions", "manual_checks"):
        need(key in case, f"case missing {key}")
    need(bool(re.fullmatch(r"[a-z0-9][a-z0-9-]*", case["id"])), "invalid case id")
    known = {rule["id"] for rule in rules["rules"]}
    need(set(case["rule_ids"]) <= known, "case refers to unknown rule id")
    need(bool(case["messages"]), "case needs messages")
    unique([m["id"] for m in case["messages"]], "message id")
    turns = []
    for message in case["messages"]:
        need(message.get("role") == "user", "case messages are input user messages only")
        need(isinstance(message.get("content"), str) and message["content"], "empty user content")
        need(message.get("request_id"), "message needs logical request_id")
        need(message.get("output_turn"), "message needs output_turn")
        turns.append(message["output_turn"])
    unique(turns, "output turn")
    all_ids = []
    for assertion in case["assertions"]:
        all_ids.append(assertion["id"])
        need(assertion.get("kind") in KINDS, f"unknown assertion kind: {assertion.get('kind')}")
        need(assertion.get("turn_id") in turns, "assertion references unknown output turn")
        need(set(assertion.get("rule_ids", [])) <= set(case["rule_ids"]), "assertion rule not in case")
        kind = assertion["kind"]
        if kind in {"literal", "dialogue", "forbid"}:
            need(isinstance(assertion.get("text"), str) and assertion["text"], "literal text missing")
        if kind == "literal":
            need(isinstance(assertion.get("count", 1), int) and assertion.get("count", 1) > 0,
                 "literal count must be a positive integer")
        if kind == "ordered":
            need(len(assertion.get("texts", [])) >= 2 and all(assertion["texts"]), "ordered needs 2+ strings")
        if kind == "timeline":
            need(isinstance(assertion.get("duration"), (int, float)) and assertion["duration"] > 0,
                 "timeline needs positive duration")
            need(isinstance(assertion.get("shot_count"), int) and assertion["shot_count"] > 0,
                 "timeline needs positive shot_count")
        if kind == "interval":
            need(isinstance(assertion.get("start"), (int, float)) and isinstance(assertion.get("end"), (int, float))
                 and 0 <= assertion["start"] < assertion["end"], "interval needs nonnegative start before end")
        if kind == "trace_fields":
            need(isinstance(assertion.get("selector"), dict) and assertion["selector"], "trace selector missing")
            need(isinstance(assertion.get("fields"), dict) and assertion["fields"], "trace fields missing")
        if kind == "state_consistency":
            need(isinstance(assertion.get("structure_fields"), list) and assertion["structure_fields"],
                 "state_consistency needs explicit structure field names; no natural-language field guessing")
    for check in case["manual_checks"]:
        all_ids.append(check["id"])
        need(check.get("question"), "manual check needs question")
        need(check.get("evidence_kind") in {"prompt", "trace", "media"}, "invalid manual evidence_kind")
        need(set(check.get("rule_ids", [])) <= set(case["rule_ids"]), "manual rule not in case")
    unique(all_ids, "check id")
    msg = {m["id"]: m for m in case["messages"]}
    for auth in case.get("authorizations", []):
        need(auth.get("message_id") in msg, "authorization must cite an input user message")
        need(auth.get("request_id") == msg[auth["message_id"]]["request_id"], "authorization request mismatch")
        need(bool(auth.get("units")) and bool(auth.get("actions")), "authorization needs scoped units/actions")
    for acceptance in case.get("acceptances", []):
        need(acceptance.get("message_id") in msg and acceptance.get("unit_id")
             and isinstance(acceptance.get("structure_version"), int), "acceptance needs input message, unit and version")
        if "covers_structure_changes" in acceptance:
            coverage = acceptance["covers_structure_changes"]
            need(isinstance(coverage, list) and all(isinstance(v, str) and v for v in coverage),
                 "acceptance covers_structure_changes must be a string array from input authority")
            unique(coverage, "acceptance structure change")
    unique([f["id"] for f in case.get("fixtures", [])], "fixture id")
    for fixture in case.get("fixtures", []):
        need(isinstance(fixture.get("required"), bool), "fixture needs required boolean")
        need(bool(fixture.get("role")), "fixture needs role")
        need((fixture.get("path") is None) == (fixture.get("sha256") is None), "fixture path/hash must both be set or pending")
        if fixture.get("sha256"):
            need(bool(re.fullmatch(r"[a-f0-9]{64}", fixture["sha256"])), "invalid fixture sha256")


def validate_trace(events):
    need(isinstance(events, list), "trace must be a JSON event array")
    unique([event.get("event_id") for event in events], "trace event id")
    for event in events:
        need(isinstance(event.get("event_id"), str) and event["event_id"], "trace event_id missing")
        need(event.get("type") in {"state_snapshot", "authorization", "tool_call", "artifact", "operation_planned", "condition_inspected"}, "unknown trace type")
        need(event.get("actor") in ACTORS, "invalid trace actor")
        need(isinstance(event.get("fields"), dict), "trace fields must be object")
        need(isinstance(event.get("evidence"), list), "trace evidence must be array")


def validate_submission(submission, case):
    need(submission.get("schema_version") == 1, "submission schema_version must be 1")
    for key in ("run_id", "case_id", "source_kind", "variant", "provider", "model", "settings", "skill_revision", "captured_at", "provenance", "outputs"):
        need(key in submission, f"submission missing {key}")
    need(submission["case_id"] == case["id"], "submission/case id mismatch")
    need(submission["variant"] in VARIANTS, "invalid variant")
    need(submission["source_kind"] in {"imported_forward", "synthetic_self_test"}, "invalid source_kind")
    need(isinstance(submission["settings"], dict), "settings must be an object; unknown values must be explicit")
    need(submission["provider"] and submission["model"], "provider/model must be recorded")
    need(submission["variant"] != "no-skill" or submission["skill_revision"] is None,
         "no-skill requires null skill_revision")
    need(submission["variant"] == "no-skill" or submission["skill_revision"], "skill variant needs revision/snapshot identifier")
    try:
        timestamp = dt.datetime.fromisoformat(submission["captured_at"].replace("Z", "+00:00"))
        need(timestamp.tzinfo is not None, "captured_at needs timezone")
    except (TypeError, AttributeError, ValueError) as exc:
        raise ValueError("captured_at must be ISO timestamp with timezone") from exc
    need(submission["provenance"].get("capture_method") and submission["provenance"].get("source_ref"), "provenance needs capture_method and source_ref")
    expected = {m["output_turn"] for m in case["messages"]}
    actual = [o["turn_id"] for o in submission["outputs"]]
    unique(actual, "submitted output turn")
    need(set(actual) == expected, f"outputs must cover exactly {sorted(expected)}")
    need(all(o.get("text_path") for o in submission["outputs"]), "every output needs raw text_path")


def result(assertion, status, detail, evidence=None):
    return {"id": assertion["id"], "kind": assertion["kind"], "status": status,
            "detail": detail, "evidence": evidence or [], "rule_ids": assertion.get("rule_ids", [])}


def matches(event, selector):
    return all(event.get(key) == value for key, value in selector.items())


def check_assertion(assertion, output, case):
    text, events = output["text"], output.get("events", [])
    kind = assertion["kind"]
    if kind == "literal":
        count = text.count(assertion["text"])
        ok = count == assertion.get("count", 1)
        detail = f"literal count {count}; expected {assertion.get('count', 1)}"
    elif kind == "dialogue":
        quoted = [a or b for a, b in re.findall(r'“([^”]*)”|"([^"]*)"', text)]
        if assertion.get("allow_terminal_punctuation", False):
            quoted = [line.rstrip("。！？.!?") for line in quoted]
        count = quoted.count(assertion["text"])
        ok = count == assertion.get("count", 1)
        detail = {"quoted_lines": quoted, "exact_line_count": count,
                  "limit": "Quoted text only; speaker, sound delivery and lip-sync require separate review."}
    elif kind == "forbid":
        count = text.count(assertion["text"])
        ok, detail = count == 0, f"forbidden literal count {count}"
    elif kind == "interval":
        found = [(float(a), float(b)) for a, b in re.findall(r"(\d+(?:\.\d+)?)\s*(?:[-–—]|到|至)\s*(\d+(?:\.\d+)?)\s*秒", text)]
        count = found.count((float(assertion["start"]), float(assertion["end"])))
        ok, detail = count == assertion.get("count", 1), {"intervals": found, "matching_count": count}
    elif kind == "ordered":
        position, positions = 0, []
        for token in assertion["texts"]:
            found = text.find(token, position)
            positions.append(found)
            if found < 0:
                break
            position = found + len(token)
        ok = len(positions) == len(assertion["texts"]) and all(p >= 0 for p in positions)
        detail = f"literal occurrence offsets: {positions}; not a semantic action-order judgment"
    elif kind == "timeline":
        # Only heading grammar is inspected. Video timing is never inferred from prompt text.
        pattern = r"镜头\s*(\d+)\s*[（(]\s*(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)\s*秒\s*[）)]\s*[：:]"
        ranges = [(int(n), float(a), float(b)) for n, a, b in re.findall(pattern, text)]
        ok = len(ranges) == assertion["shot_count"]
        end = 0.0
        for index, (number, start, finish) in enumerate(ranges, 1):
            ok = ok and number == index and abs(start - end) < 1e-8 and finish > start
            end = finish
        ok = ok and abs(end - assertion["duration"]) < 1e-8
        detail = f"parsed shot headings: {ranges}; expected contiguous 0–{assertion['duration']}"
    elif kind == "trace_fields":
        selected = [e for e in events if matches(e, assertion["selector"])]
        if not selected:
            return result(assertion, "blocked", "required trace event was not captured")
        need(len(selected) == 1, f"{assertion['id']}: trace selector must match exactly one event")
        event = selected[0]
        mismatches = {k: {"expected": v, "actual": event["fields"].get(k, "<missing>")}
                      for k, v in assertion["fields"].items() if k not in event["fields"] or event["fields"][k] != v}
        return result(assertion, "fail" if mismatches else "pass",
                      {"mismatches": mismatches, "actor": event["actor"],
                       "limit": "Checks captured state claims only; not proof of hidden reasoning or successful media execution."},
                      [event["event_id"]])
    elif kind == "permission_scope":
        deliveries = [e for e in events if e["type"] == "artifact"]
        if not deliveries:
            return result(assertion, "blocked", "artifact trace missing; cannot infer authorization from prose")
        errors, missing = [], []
        current = next(m for m in case["messages"] if m["output_turn"] == assertion["turn_id"])
        visible_ids = {m["id"] for m in case["messages"][:case["messages"].index(current) + 1]}
        for event in deliveries:
            fields = event["fields"]
            if fields.get("admission_basis") not in {"direct_authorized", "confirmed_version", "source_preserved", "language_only", "unresolved"}:
                missing.append(event["event_id"])
                continue
            if fields.get("admission_basis") != "direct_authorized":
                continue
            grant = [a for a in case.get("authorizations", [])
                     if fields.get("request_id") == current["request_id"] and a["message_id"] in visible_ids
                     and a["request_id"] == fields.get("request_id")
                     and (event.get("unit_id") in a["units"] or "*" in a["units"])
                     and "skip_structure_review" in a["actions"]
                     and a["message_id"] in event["evidence"]]
            if not grant:
                errors.append(event["event_id"])
        return result(assertion, "fail" if errors else "blocked" if missing else "pass",
                      {"unauthorized_artifact_events": errors,
                       "missing_or_unknown_admission_basis": missing,
                       "limit": "Checks reported direct-authorized deliveries against explicit case grants; semantic omission and tool truth need review."},
                      [e["event_id"] for e in deliveries])
    elif kind == "state_consistency":
        states = [e for e in events if e["type"] == "state_snapshot"]
        if not states:
            return result(assertion, "blocked", "state trace not captured")
        errors, missing = [], []
        current = next(m for m in case["messages"] if m["output_turn"] == assertion["turn_id"])
        visible_ids = {m["id"] for m in case["messages"][:case["messages"].index(current) + 1]}
        for event in states:
            f, eid = event["fields"], event["event_id"]
            required = {"task_kind", "structure_status", "delivery_decision", "changed_fields",
                        "invalidated_fields", "rechecked_fields", "light_composite_applicability", "light_composite_review"}
            absent = sorted(required - f.keys())
            if absent:
                missing.append({"event": eid, "fields": absent})
                continue
            for key in ("changed_fields", "invalidated_fields", "rechecked_fields"):
                need(isinstance(f[key], list) and all(isinstance(v, str) for v in f[key]), f"{eid}: {key} must be string array")
            language_only = f.get("operation") == "language_only"
            if f["structure_status"] not in {"source_preserved", "pending", "confirmed"} and not (language_only and f["structure_status"] is None):
                errors.append({"event": eid, "violation": "invalid or unexplained structure status"})
            if language_only and set(f["changed_fields"]) & set(assertion["structure_fields"]):
                errors.append({"event": eid, "violation": "language_only changes an explicitly named structure field"})
            if f["structure_status"] == "source_preserved":
                null_keys = {"structure_version", "structure_review_mode", "acceptance_ref"}
                if not null_keys <= f.keys():
                    missing.append({"event": eid, "fields": sorted(null_keys - f.keys())})
                elif f["task_kind"] != "edit" or any(f[k] is not None for k in null_keys):
                    errors.append({"event": eid, "violation": "source_preserved is edit-only with null version/review/acceptance"})
                if set(f["changed_fields"]) & set(assertion["structure_fields"]):
                    errors.append({"event": eid, "violation": "source_preserved changes an explicitly named structure field"})
            if f["structure_status"] == "confirmed":
                changed_structure = set(f["changed_fields"]) & set(assertion["structure_fields"])
                matching_acceptances = [a for a in case.get("acceptances", [])
                    if f.get("acceptance_ref") in {a["message_id"], a.get("id", a["message_id"])}
                    and a["message_id"] in visible_ids and a["unit_id"] == event.get("unit_id")
                    and a["structure_version"] == f.get("structure_version")]
                if "acceptance_ref" not in f or "structure_version" not in f:
                    missing.append({"event": eid, "fields": ["acceptance_ref", "structure_version"]})
                elif not matching_acceptances:
                    errors.append({"event": eid, "violation": "confirmed lacks matching available case acceptance evidence"})
                elif changed_structure and not any(a["message_id"] == current["id"]
                         and changed_structure <= set(a.get("covers_structure_changes", []))
                         for a in matching_acceptances):
                    errors.append({"event": eid, "violation": "current structure changes are not explicitly covered by a current-turn case acceptance"})
            if f["light_composite_applicability"] == "physical" and f["light_composite_review"] == "not_applicable":
                errors.append({"event": eid, "violation": "physical light cannot be not_applicable"})
            if f["delivery_decision"] == "deliver" and not language_only:
                # An explicit pending claim is unfinished work. Untouched source
                # fields may remain inherited/null; do not invent a new review.
                for review in ("light_composite_review", "world_dynamics_review"):
                    if f.get(review) == "pending":
                        errors.append({"event": eid, "violation": f"delivery has unresolved {review}"})
                light_roots = {"light", "lighting", "light_composite", "light_composite_applicability", "light_composite_review"}
                light_touched = any(field.split(".")[0] in light_roots
                                    for field in f["changed_fields"] + f["invalidated_fields"])
                if (f["task_kind"] != "edit" or light_touched) and f["light_composite_applicability"] == "physical" and f["light_composite_review"] is None:
                    missing.append({"event": eid, "fields": ["resolved light_composite_review"]})
                world_roots = {"world", "world_dynamics", "world_dynamics_review", "world_dynamics_mode"}
                world_touched = any(field.split(".")[0] in world_roots
                                    for field in f["changed_fields"] + f["invalidated_fields"])
                if world_touched and f.get("world_dynamics_review") is None:
                    missing.append({"event": eid, "fields": ["resolved world_dynamics_review"]})
            if f["delivery_decision"] == "deliver" and set(f["invalidated_fields"]) - set(f["rechecked_fields"]):
                errors.append({"event": eid, "violation": "delivery has invalidated dependencies not rechecked"})
            if f["delivery_decision"] == "deliver" and f["structure_status"] == "pending" and not language_only:
                if "admission_basis" not in f:
                    missing.append({"event": eid, "fields": ["admission_basis"]})
                elif f["admission_basis"] != "direct_authorized":
                    errors.append({"event": eid, "violation": "pending delivery lacks direct authorization basis"})
        return result(assertion, "fail" if errors else "blocked" if missing else "pass",
                      {"violations": errors, "missing": missing,
                       "limit": "Consistency of captured claims and case authority only; completeness of changed fields and visual facts needs review."},
                      [e["event_id"] for e in states])
    else:
        raise ValueError(f"unsupported assertion kind: {kind}")
    return result(assertion, "pass" if ok else "fail", detail, [assertion["turn_id"]])


def verify_transcript(transcript, case, outputs):
    """Exact input/output matching is capture integrity, not proof of execution origin."""
    need(isinstance(transcript, list), "transcript must be array of role/id/content entries")
    users = [m for m in transcript if m.get("role") == "user"]
    need([(m.get("id"), m.get("content")) for m in users] ==
         [(m["id"], m["content"]) for m in case["messages"]], "transcript user messages differ from case")
    assistants = [m for m in transcript if m.get("role") == "assistant"]
    need([(m.get("turn_id"), m.get("content")) for m in assistants] ==
         [(m["output_turn"], outputs[m["output_turn"]]["text"]) for m in case["messages"]],
         "transcript assistant text differs from raw captures")
    expected_roles = [role for _ in case["messages"] for role in ("user", "assistant")]
    need([m.get("role") for m in transcript if m.get("role") in {"user", "assistant"}] == expected_roles,
         "transcript must preserve user/assistant turn order")


def fixture_states(case, submission):
    """Presentation declarations are not proof that a model saw the fixture."""
    declarations = submission.get("fixture_inputs", [])
    unique([f["id"] for f in declarations], "fixture exposure declaration")
    known = {f["id"] for f in case.get("fixtures", [])}
    need(all(f["id"] in known for f in declarations), "exposure refers to unknown fixture")
    statuses = []
    for fixture in case.get("fixtures", []):
        status = {"id": fixture["id"], "required": fixture["required"], "status": "pending", "sha256": fixture.get("sha256")}
        exposed = next((f for f in declarations if f["id"] == fixture["id"]), None)
        if exposed:
            need(fixture.get("path") and exposed.get("sha256") == fixture["sha256"] and exposed.get("presented_as"),
                 f"fixture exposure hash/method missing or mismatched: {fixture['id']}")
        if fixture.get("path"):
            status["status"] = "hash_verified_presentation_declared" if exposed else "presentation_not_declared"
        statuses.append(status)
    return statuses


def aggregate_status(checks, fixture_status):
    blocked = [f["id"] for f in fixture_status if f["required"] and f["status"] != "hash_verified_presentation_declared"]
    statuses = [c["status"] for c in checks]
    status = "fail" if "fail" in statuses else "blocked" if "blocked" in statuses or blocked else "pass" if checks else "not_assessed"
    return status, blocked


def import_run(case_path, submission_path, destination, rules_path=ROOT / "rules.json"):
    case_path, submission_path, destination = map(Path, (case_path, submission_path, destination))
    case, submission, rules = read_json(case_path), read_json(submission_path), read_json(rules_path)
    validate_case(case, rules)
    validate_submission(submission, case)
    if submission.get("case_sha256"):
        need(submission["case_sha256"] == digest(case_path), "submission was captured against a different case hash")
    need(not destination.exists(), "run destination already exists; use a new run directory")
    base = submission_path.resolve().parent
    captures, files = {}, []

    def source(path):
        resolved = (base / path).resolve()
        need(resolved.is_file(), f"capture missing: {resolved}")
        return resolved

    # Validate all sources before making a run directory.
    for index, item in enumerate(submission["outputs"]):
        raw_path = source(item["text_path"])
        output = {"text": raw_path.read_text(encoding="utf-8"), "events": []}
        files.append((raw_path, f"captures/{index + 1:02d}-output.txt", "prompt_output", item["turn_id"]))
        if item.get("trace_path"):
            trace_path = source(item["trace_path"])
            output["events"] = read_json(trace_path)
            validate_trace(output["events"])
            files.append((trace_path, f"captures/{index + 1:02d}-trace.json", "reported_trace", item["turn_id"]))
        captures[item["turn_id"]] = output
    transcript_verified = False
    if submission.get("transcript_path"):
        transcript_path = source(submission["transcript_path"])
        verify_transcript(read_json(transcript_path), case, captures)
        files.append((transcript_path, "captures/transcript.json", "transcript", None))
        transcript_verified = True
    for index, media in enumerate(submission.get("media_outputs", [])):
        need(all(key in media for key in ("path", "role", "provider", "model", "settings", "prompt_turn_id")),
             "media output needs path/role/provider/model/settings/prompt_turn_id")
        need(media["prompt_turn_id"] in captures and isinstance(media["settings"], dict), "invalid media prompt turn/settings")
        media_path = source(media["path"])
        files.append((media_path, f"media/{index + 1:02d}{Path(media['path']).suffix}", "media_output", media["prompt_turn_id"]))
        if media.get("prompt_path"):
            files.append((source(media["prompt_path"]), f"media/{index + 1:02d}-provider-prompt.txt", "provider_prompt", media["prompt_turn_id"]))
    need(submission["variant"] != "no-skill" or not submission.get("skill_files"), "no-skill cannot declare loaded skill files")
    for index, skill_file in enumerate(submission.get("skill_files", [])):
        skill_path = source(skill_file["path"])
        need(digest(skill_path) == skill_file.get("sha256"), f"loaded skill file hash mismatch: {skill_path}")
        files.append((skill_path, f"skills/{index + 1:03d}-{Path(skill_file['path']).name}", "declared_loaded_skill", str(skill_path)))
    fixture_status = fixture_states(case, submission)
    for index, fixture in enumerate(case.get("fixtures", [])):
        if fixture.get("path"):
            fixture_path = (case_path.resolve().parent / fixture["path"]).resolve()
            need(fixture_path.is_file(), f"fixture missing: {fixture_path}")
            need(digest(fixture_path) == fixture["sha256"], f"fixture hash mismatch: {fixture['id']}")
            files.append((fixture_path, f"fixtures/{index + 1:02d}{Path(fixture['path']).suffix}", "input_fixture", fixture["id"]))
    checks = [check_assertion(a, captures[a["turn_id"]], case) for a in case["assertions"]]
    deterministic, blocked_fixtures = aggregate_status(checks, fixture_status)
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    report = {
        "schema_version": 1, "run_id": submission["run_id"], "case_id": case["id"],
        "source_kind": submission["source_kind"], "variant": submission["variant"], "imported_at": now,
        "deterministic_status": deterministic, "assertions": checks,
        "fixtures": fixture_status, "blocked_fixtures": blocked_fixtures,
        "manual_checks": [{**c, "status": "pending"} for c in case["manual_checks"]],
        "evidence": {
            "category": "harness_self_test_only" if submission["source_kind"] == "synthetic_self_test" else "imported_forward_output",
            "transcript_matches_case_and_captures": transcript_verified,
            "execution_origin": "declared_by_importer_not_independently_verified",
            "skill_snapshot_status": "declared_files_hash_verified" if submission.get("skill_files") else "not_applicable" if submission["variant"] == "no-skill" else "not_recorded",
            "semantic_status": "pending" if case["manual_checks"] else "not_assessed",
            "media_output_status": "captured_pending_review" if submission.get("media_outputs") else "not_assessed", "overall_skill_pass": None,
            "limits": ["Deterministic passes do not prove semantic correctness or generated-media quality.",
                       "A model-reported state trace does not establish that a tool action occurred.",
                       "Synthetic self-tests never count as model forward tests."]},
        "integrity": {"case_sha256": digest(case_path), "submission_sha256": digest(submission_path),
                      "rules_sha256": digest(rules_path), "harness_sha256": digest(__file__)},
    }
    destination.mkdir(parents=True)
    shutil.copyfile(case_path, destination / "case.json")
    shutil.copyfile(submission_path, destination / "submission.json")
    shutil.copyfile(rules_path, destination / "rules.json")
    assets = []
    for original, relative, kind, ref in files:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
        assets.append({"path": relative, "sha256": digest(target), "kind": kind, "ref": ref})
    dump_json(destination / "assets.json", assets)
    dump_json(destination / "report.json", report)
    return report


def verify_run(run_path):
    run = Path(run_path)
    report = read_json(run / "report.json")
    for filename, key in (("case.json", "case_sha256"), ("submission.json", "submission_sha256"), ("rules.json", "rules_sha256")):
        need(digest(run / filename) == report["integrity"][key], f"captured manifest changed: {filename}")
    case, rules, submission = read_json(run / "case.json"), read_json(run / "rules.json"), read_json(run / "submission.json")
    validate_case(case, rules)
    validate_submission(submission, case)
    # Derive the complete archive inventory from the frozen input manifests,
    # not from the possibly incomplete assets list. No original source access.
    expected = {}
    def expect(path, kind, ref, sha=None):
        need(path not in expected, "duplicate expected archive path")
        expected[path] = (kind, ref, sha)
    for index, item in enumerate(submission["outputs"], 1):
        expect(f"captures/{index:02d}-output.txt", "prompt_output", item["turn_id"])
        if item.get("trace_path"):
            expect(f"captures/{index:02d}-trace.json", "reported_trace", item["turn_id"])
    if submission.get("transcript_path"):
        expect("captures/transcript.json", "transcript", None)
    for index, item in enumerate(submission.get("media_outputs", []), 1):
        expect(f"media/{index:02d}{Path(item['path']).suffix}", "media_output", item["prompt_turn_id"])
        if item.get("prompt_path"):
            expect(f"media/{index:02d}-provider-prompt.txt", "provider_prompt", item["prompt_turn_id"])
    for index, item in enumerate(submission.get("skill_files", []), 1):
        # Original absolute paths are provenance, not inputs to offline replay.
        expect(f"skills/{index:03d}-{Path(item['path']).name}", "declared_loaded_skill", None, item["sha256"])
    for index, item in enumerate(case.get("fixtures", []), 1):
        if item.get("path"):
            expect(f"fixtures/{index:02d}{Path(item['path']).suffix}", "input_fixture", item["id"], item["sha256"])
    assets = read_json(run / "assets.json")
    unique([a["path"] for a in assets], "archived asset path")
    need({a["path"] for a in assets} == set(expected), "archive asset coverage differs from frozen case/submission")
    outputs = {}
    transcript = None
    for item in assets:
        kind, ref, sha = expected[item["path"]]
        need(item["kind"] == kind and (kind == "declared_loaded_skill" or item["ref"] == ref), "archive asset role/ref mismatch")
        need(sha is None or item["sha256"] == sha, "archive asset hash differs from fixture/skill binding")
        path = (run / item["path"]).resolve()
        need(path.is_relative_to(run.resolve()), "run asset path escapes run directory")
        need(path.is_file() and digest(path) == item["sha256"], f"run asset changed: {item['path']}")
        if item["kind"] == "prompt_output":
            outputs.setdefault(item["ref"], {})["text"] = path.read_text(encoding="utf-8")
        elif item["kind"] == "reported_trace":
            events = read_json(path)
            validate_trace(events)
            outputs.setdefault(item["ref"], {})["events"] = events
        elif item["kind"] == "transcript":
            transcript = read_json(path)
    if transcript is not None:
        verify_transcript(transcript, case, outputs)
    fixtures = fixture_states(case, submission)
    checks = [check_assertion(a, outputs[a["turn_id"]], case) for a in case["assertions"]]
    need(checks == report["assertions"], "replayed assertion results differ from saved report")
    deterministic, blocked = aggregate_status(checks, fixtures)
    need(fixtures == report["fixtures"] and blocked == report["blocked_fixtures"], "replayed fixture status differs from saved report")
    need(deterministic == report["deterministic_status"], "replayed aggregate status differs from saved report")
    return {"integrity": "pass", "replay": "pass", "deterministic_status": deterministic,
            "limit": "Checks offline artifacts and deterministic replay only; does not re-run a model."}


def import_review(run_path, review_path):
    run, review_path = Path(run_path), Path(review_path)
    verify_run(run)
    review, report = read_json(review_path), read_json(run / "report.json")
    need(review.get("schema_version") == 1, "review schema_version must be 1")
    need(review.get("run_id") == report["run_id"], "review/run id mismatch")
    need(review.get("reviewer") and review.get("reviewer_kind") in {"human", "model"}, "identify reviewer and kind")
    need(isinstance(review.get("blind_to_variant"), bool), "review must record blinding")
    known = {c["id"]: c for c in report["manual_checks"]}
    assets = {a["path"]: a for a in read_json(run / "assets.json")}
    unique([c["id"] for c in review.get("checks", [])], "review check id")
    for check in review.get("checks", []):
        need(check["id"] in known, "review refers to unknown check")
        need(check.get("status") in {"pass", "fail", "uncertain", "not_applicable"}, "invalid review status")
        need(check.get("reason") and check.get("evidence"), "each judgment needs reason and evidence locations")
        for evidence in check["evidence"]:
            need(isinstance(evidence, dict) and evidence.get("path") in assets and evidence.get("location"),
                 "review evidence needs a captured asset path and a line/frame/time location")
            if known[check["id"]]["evidence_kind"] == "media":
                need(assets[evidence["path"]]["kind"] == "media_output", "media judgment must cite actual captured media output")
    folder = run / "reviews"
    folder.mkdir(exist_ok=True)
    target = folder / f"{digest(review_path)}.json"
    need(not target.exists(), "identical review already imported")
    shutil.copyfile(review_path, target)
    # Never overwrite deterministic evidence or manufacture a global score.
    return {"stored": str(target), "reviewer_kind": review["reviewer_kind"],
            "overall_skill_pass": None, "limit": "Review is attributed evidence; it does not upgrade the original capture provenance."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="validate case/rule manifests and fixture bindings")
    validate.add_argument("--cases", type=Path, default=ROOT / "cases")
    validate.add_argument("--rules", type=Path, default=ROOT / "rules.json")
    imp = sub.add_parser("import-run", help="import existing captures; never generates model output")
    imp.add_argument("--case", required=True, type=Path)
    imp.add_argument("--submission", required=True, type=Path)
    imp.add_argument("--out", required=True, type=Path)
    replay = sub.add_parser("verify-run", help="check hashes and replay deterministic assertions offline")
    replay.add_argument("run", type=Path)
    review = sub.add_parser("import-review", help="append an attributed manual/model semantic review")
    review.add_argument("run", type=Path)
    review.add_argument("review", type=Path)
    packet = sub.add_parser("packet", help="export only requests and input attachments, without expected results")
    packet.add_argument("--case", required=True, type=Path)
    packet.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            rules = read_json(args.rules)
            need(rules.get("schema_version") == 1, "rules schema_version must be 1")
            unique([r["id"] for r in rules["rules"]], "rule id")
            for rule in rules["rules"]:
                need((ROOT.parent / rule["owner"]).is_file(), f"rule owner missing: {rule['owner']}")
                need(rule["id"] in (ROOT.parent / rule["owner"]).read_text(encoding="utf-8"),
                     f"rule id not found in declared owner: {rule['id']}")
            paths = sorted(args.cases.glob("*.json"))
            need(bool(paths), "no case files")
            cases = [read_json(p) for p in paths]
            unique([c["id"] for c in cases], "case id")
            pending = []
            for path, case in zip(paths, cases):
                validate_case(case, rules)
                for fixture in case.get("fixtures", []):
                    if fixture.get("path"):
                        bound = (path.parent / fixture["path"]).resolve()
                        need(bound.is_file() and digest(bound) == fixture["sha256"], f"fixture hash mismatch: {case['id']}/{fixture['id']}")
                    elif fixture["required"]:
                        pending.append(f"{case['id']}/{fixture['id']}")
            value = {"manifest_status": "pass", "cases": len(cases), "families": len(set(c["family"] for c in cases)),
                     "pending_required_fixtures": pending, "model_tests_run": 0}
        elif args.command == "import-run":
            value = import_run(args.case, args.submission, args.out)
        elif args.command == "verify-run":
            value = verify_run(args.run)
        elif args.command == "packet":
            case = read_json(args.case)
            validate_case(case, read_json(ROOT / "rules.json"))
            value = {"schema_version": 1, "case_id": case["id"], "case_sha256": digest(args.case),
                     "messages": case["messages"], "fixtures": [{**f, "path": str((args.case.resolve().parent / f["path"]).resolve()) if f.get("path") else None}
                                                                  for f in case.get("fixtures", [])]}
            need(not args.out.exists(), "packet output already exists")
            args.out.parent.mkdir(parents=True, exist_ok=True)
            dump_json(args.out, value)
            value = {"packet": str(args.out), "contains_expected_results": False,
                     "pending_fixtures": [f["id"] for f in case.get("fixtures", []) if f["required"] and not f.get("path")]}
        else:
            value = import_review(args.run, args.review)
        print(json.dumps(value, ensure_ascii=False, indent=2))
        if args.command == "import-run" and value["deterministic_status"] in {"fail", "blocked"}:
            return 1
        return 0
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
