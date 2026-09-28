#!/usr/bin/env python3
"""Execute the pre-registered PSI-JEV-RUN-01 against TypeSafe Jev.

The fixture is immutable input. The script writes a separate JSON result so that
model output cannot silently rewrite the pre-registered oracle or task contract.

Requires:
    TYPESAFE_API_KEY
Optional:
    TYPESAFE_MODEL (default: jev-latest)
    PSI_JEV_RESULT_PATH
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "experiments" / "psi-jev-run-01-fixture.json"
RESULT_PATH = Path(
    os.environ.get(
        "PSI_JEV_RESULT_PATH",
        ROOT / "artifacts" / "PSI-JEV-RUN-01-result.json",
    )
)
ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MODEL = os.environ.get("TYPESAFE_MODEL", "jev-latest")


def load_fixture() -> dict[str, Any]:
    with FIXTURE_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def build_request(fixture: dict[str, Any]) -> dict[str, Any]:
    tests = fixture["tests"]
    state = {
        "candidate_states": fixture["candidate_states"],
        "initial_fiber": fixture["initial_fiber"],
        "task_classes": fixture["task_classes"],
        "available_tests": tests,
        "task": (
            "Select one available test whose every possible result leaves a non-empty "
            "surviving candidate set entirely within one task class."
        ),
    }

    def description(name: str) -> str:
        mapping = tests[name]
        groups: dict[str, list[str]] = {}
        for state_name, outcome in mapping.items():
            groups.setdefault(str(outcome), []).append(state_name)
        partitions = "; ".join(
            f"result {outcome}: {{{','.join(states)}}}"
            for outcome, states in sorted(groups.items())
        )
        return f"{name} partitions the current fiber as {partitions}."

    criteria = {name: description(name) for name in fixture["typed_question"]["choices"]}

    return {
        "model": MODEL,
        "state": state,
        "questions": {
            "separating_test": {
                "type": "choice",
                "instructions": fixture["typed_question"]["criterion"],
                "criteria": criteria,
            }
        },
    }


def call_jev(payload: dict[str, Any], api_key: str) -> tuple[dict[str, Any], float]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "PSI-JEV-RUN-01/1.0",
        },
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"TypeSafe HTTP {exc.code}: {raw}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"TypeSafe connection error: {exc}") from exc
    elapsed_ms = (time.perf_counter() - started) * 1000
    return json.loads(raw), elapsed_ms


def extract_choice(raw: dict[str, Any]) -> dict[str, Any]:
    answers = raw.get("answers")
    if not isinstance(answers, dict) or "separating_test" not in answers:
        raise RuntimeError(f"Unexpected response schema: {json.dumps(raw, ensure_ascii=False)}")
    answer = answers["separating_test"]
    if not isinstance(answer, dict):
        raise RuntimeError("Choice answer is not an object")
    return answer


def main() -> int:
    api_key = os.environ.get("TYPESAFE_API_KEY")
    if not api_key:
        print("BLOCKED: TYPESAFE_API_KEY is not set.", file=sys.stderr)
        return 2

    fixture = load_fixture()
    payload = build_request(fixture)
    raw, elapsed_ms = call_jev(payload, api_key)
    answer = extract_choice(raw)

    choice = answer.get("choice")
    oracle = fixture["psi_oracle"]["choice"]
    legal_choices = set(fixture["typed_question"]["choices"])

    violations: list[str] = []
    if choice not in legal_choices:
        violations.append(f"out-of-domain choice: {choice!r}")

    action_result = "PASS" if choice == oracle and not violations else "FAIL"

    result = {
        "run_id": fixture["run_id"],
        "fixture_version": fixture["fixture_version"],
        "endpoint": ENDPOINT,
        "requested_model": MODEL,
        "served_model": raw.get("model"),
        "jev_choice": choice,
        "jev_probabilities": answer.get("probabilities"),
        "jev_confidence": answer.get("confidence"),
        "psi_oracle": oracle,
        "action_selection_result": action_result,
        "constraint_violations": violations,
        "elapsed_ms_client": round(elapsed_ms, 3),
        "usage": raw.get("usage"),
        "raw_typed_output": raw,
    }

    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with RESULT_PATH.open("w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(json.dumps({
        "run_id": result["run_id"],
        "choice": choice,
        "oracle": oracle,
        "result": action_result,
        "confidence": result["jev_confidence"],
        "probabilities": result["jev_probabilities"],
        "elapsed_ms_client": result["elapsed_ms_client"],
        "result_path": str(RESULT_PATH),
    }, ensure_ascii=False, indent=2))
    return 0 if action_result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
