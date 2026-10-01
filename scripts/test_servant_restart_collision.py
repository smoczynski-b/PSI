#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from servant_runtime import ServantCommand, ServantRuntime
from test_servant_runtime import make_durable


def main() -> None:
    with TemporaryDirectory() as td:
        root = Path(td)
        memory = root / "memory.wal"
        chronicle = root / "servant.wal"

        durable = make_durable(memory)
        servant = ServantRuntime(durable, chronicle)

        original = ServantCommand("C", "SEMANTIC_VERDICT")
        first = servant.handle(original)
        assert first.disposition == "BLOCK_ILLEGAL_TRANSITION"
        assert first.reason_code == "SEMANTIC_VERDICT"

        collision = servant.handle(ServantCommand("C", "RECOVER"))
        assert collision.disposition == "STOP_ESCALATE_CHRONICLE"
        assert collision.reason_code == "COMMAND_ID_COLLISION"

        # Restart must recover the first completed verdict, not the later
        # collision RESULT that was chronicled with remember=False.
        restarted = ServantRuntime(durable, chronicle)
        replay = restarted.handle(original)
        assert replay.disposition == "BLOCK_ILLEGAL_TRANSITION"
        assert replay.reason_code == "IDEMPOTENT_REPLAY:SEMANTIC_VERDICT"

        # No authoritative memory transaction was executed by either command.
        assert durable.revision == 0
        assert durable.wal.read_valid_prefix().records == ()

        results = [
            r for r in restarted.chronicle.records()
            if r.get("kind") == "SERVANT_RESULT"
            and r.get("payload", {}).get("command_id") == "C"
        ]
        assert results[0]["payload"]["disposition"] == "BLOCK_ILLEGAL_TRANSITION"
        assert results[1]["payload"]["reason_code"] == "COMMAND_ID_COLLISION"

    print("PSI-MEMORY-SERVANT-F0.1 PASS")
    print("first_completed_verdict_survives_collision_restart=PASS")
    print("collision_remains_chronicled=PASS")
    print("authoritative_memory_side_effect=NONE")


if __name__ == "__main__":
    main()
