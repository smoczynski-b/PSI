#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

import durable_shared_memory as durable_module
from access_steward_runtime import AccessChronicle
from durable_shared_memory import JSONLWAL, WALCorruption
from servant_runtime import ServantChronicle, ServantCommand
from test_active_memory_wal import make_runtime, upsert


def inject_torn_tail(path: Path) -> None:
    with path.open("ab") as fh:
        fh.write(b'{"seq":')


def generic_tail_recovery() -> None:
    with TemporaryDirectory() as td:
        path = Path(td) / "generic.wal"
        wal = JSONLWAL(path)
        wal.append("ONE", "T1", {"n": 1})
        inject_torn_tail(path)

        recovered = JSONLWAL(path)
        assert not recovered.read_valid_prefix().tail_truncated
        assert [r["kind"] for r in recovered.read_valid_prefix().records] == ["ONE"]
        recovered.append("TWO", "T2", {"n": 2})
        recovered.append("THREE", "T3", {"n": 3})

        restarted = JSONLWAL(path)
        records = restarted.read_valid_prefix().records
        assert [r["kind"] for r in records] == ["ONE", "TWO", "THREE"]
        assert [r["payload"]["n"] for r in records] == [1, 2, 3]


def complete_invalid_record_fails_closed() -> None:
    with TemporaryDirectory() as td:
        path = Path(td) / "invalid-complete.wal"
        JSONLWAL(path).append("ONE", "T1", {"n": 1})
        with path.open("ab") as fh:
            fh.write(b'{"broken":}\n')
        try:
            JSONLWAL(path)
            raise AssertionError("newline-terminated invalid JSON was treated as a crash tail")
        except WALCorruption:
            pass


def interrupted_repair_preserves_verified_prefix() -> None:
    with TemporaryDirectory() as td:
        path = Path(td) / "repair-interrupt.wal"
        wal = JSONLWAL(path)
        wal.append("ONE", "T1", {"n": 1})
        wal.append("TWO", "T2", {"n": 2})
        inject_torn_tail(path)

        real_fsync = durable_module.os.fsync
        armed = {"value": True}

        def fail_once(fd: int) -> None:
            if armed["value"]:
                armed["value"] = False
                raise OSError("simulated interruption after prefix truncation")
            real_fsync(fd)

        durable_module.os.fsync = fail_once
        try:
            try:
                JSONLWAL(path)
                raise AssertionError("repair interruption did not fire")
            except OSError:
                pass
        finally:
            durable_module.os.fsync = real_fsync

        # ftruncate touched only bytes after the verified prefix. A second
        # restart must still see both acknowledged records, then accept two more.
        restarted = JSONLWAL(path)
        assert [r["kind"] for r in restarted.read_valid_prefix().records] == ["ONE", "TWO"]
        restarted.append("THREE", "T3", {"n": 3})
        restarted.append("FOUR", "T4", {"n": 4})
        final = JSONLWAL(path)
        assert [r["kind"] for r in final.read_valid_prefix().records] == ["ONE", "TWO", "THREE", "FOUR"]


def short_write_is_completed_before_ack() -> None:
    with TemporaryDirectory() as td:
        path = Path(td) / "short-write.wal"
        wal = JSONLWAL(path)
        real_write = durable_module.os.write

        def short_write(fd: int, data) -> int:
            width = min(7, len(data))
            return real_write(fd, data[:width])

        durable_module.os.write = short_write
        try:
            wal.append("SHORT", "TS", {"payload": "x" * 80})
        finally:
            durable_module.os.write = real_write

        restarted = JSONLWAL(path)
        records = restarted.read_valid_prefix().records
        assert len(records) == 1
        assert records[0]["kind"] == "SHORT"


def failed_partial_write_blocks_same_process_and_repairs_on_restart() -> None:
    with TemporaryDirectory() as td:
        path = Path(td) / "failed-write.wal"
        wal = JSONLWAL(path)
        real_write = durable_module.os.write
        calls = {"n": 0}

        def torn_write(fd: int, data) -> int:
            if calls["n"] == 0:
                calls["n"] += 1
                return real_write(fd, data[:5])
            raise OSError("simulated write failure")

        durable_module.os.write = torn_write
        try:
            try:
                wal.append("BROKEN", "TB", {"n": 0})
                raise AssertionError("partial write failure did not fire")
            except OSError:
                pass
        finally:
            durable_module.os.write = real_write

        try:
            wal.append("ILLEGAL-CONTINUE", "TB2", {"n": 1})
            raise AssertionError("same-process append continued after ambiguous write")
        except WALCorruption:
            pass

        restarted = JSONLWAL(path)
        assert restarted.read_valid_prefix().records == ()
        restarted.append("ONE", "T1", {"n": 1})
        restarted.append("TWO", "T2", {"n": 2})
        assert [r["kind"] for r in JSONLWAL(path).read_valid_prefix().records] == ["ONE", "TWO"]


def wrapper_recovery() -> None:
    with TemporaryDirectory() as td:
        root = Path(td)

        command = ServantCommand(
            command_id="CMD-R1",
            kind="INSTITUTION_ACTION",
            institution_action="NOTICE",
            subject_id="SUBJECT-R1",
        )
        servant_path = root / "servant.wal"
        servant = ServantChronicle(servant_path)
        servant.append("OBSERVED", command, {"revision": 0})
        inject_torn_tail(servant_path)
        servant2 = ServantChronicle(servant_path)
        servant2.append("RESULT", command, {"disposition": "EXECUTED", "reason_code": "TEST"})
        servant3 = ServantChronicle(servant_path)
        assert [r["kind"] for r in servant3.records()] == ["SERVANT_OBSERVED", "SERVANT_RESULT"]

        access_path = root / "access.wal"
        access = AccessChronicle(access_path)
        access.append("OBSERVED", "REQ-R1", {"request_id": "REQ-R1"})
        inject_torn_tail(access_path)
        access2 = AccessChronicle(access_path)
        access2.append("RESULT", "REQ-R1", {"request_id": "REQ-R1", "disposition": "ALLOW"})
        access3 = AccessChronicle(access_path)
        assert [r["kind"] for r in access3.records()] == ["ACCESS_OBSERVED", "ACCESS_RESULT"]


def shared_writer_recovery_and_two_later_commits() -> None:
    with TemporaryDirectory() as td:
        path = Path(td) / "shared.wal"
        live = make_runtime(path)
        p1 = upsert("R1-P1", "agent:r1", 0, "A", "SUPPORTS", "R1-A", "test:R1-A")
        first = live.commit("R1-TX1", (p1,))
        assert first.wal_state == "ACK"
        assert live.revision == 1
        inject_torn_tail(path)

        recovered = make_runtime(path)
        assert recovered.revision == 1
        assert not recovered.wal.read_valid_prefix().tail_truncated

        p2 = upsert("R1-P2", "agent:r1", 1, "A", "SUPPORTS", "R1-B", "test:R1-B")
        second = recovered.commit("R1-TX2", (p2,))
        assert second.wal_state == "ACK"
        assert recovered.revision == 2

        p3 = upsert("R1-P3", "agent:r1", 2, "A", "SUPPORTS", "R1-C", "test:R1-C")
        third = recovered.commit("R1-TX3", (p3,))
        assert third.wal_state == "ACK"
        assert recovered.revision == 3

        final = make_runtime(path)
        assert final.revision == 3
        assert ("A", "SUPPORTS", "R1-A") in final.workspace("proof").edges
        assert ("A", "SUPPORTS", "R1-B") in final.workspace("proof").edges
        assert ("A", "SUPPORTS", "R1-C") in final.workspace("proof").edges
        assert not final.wal.read_valid_prefix().tail_truncated


def main() -> None:
    generic_tail_recovery()
    complete_invalid_record_fails_closed()
    interrupted_repair_preserves_verified_prefix()
    short_write_is_completed_before_ack()
    failed_partial_write_blocks_same_process_and_repairs_on_restart()
    wrapper_recovery()
    shared_writer_recovery_and_two_later_commits()
    print("PSI-MEMORY-R1-JOURNAL-RECOVERY-01 PASS")
    print("torn_tail_restart_two_appends_restart=PASS")
    print("interrupted_repair_verified_prefix=PASS")
    print("complete_invalid_record_fail_closed=PASS")
    print("short_write_loop=PASS")
    print("ambiguous_write_blocks_until_restart=PASS")
    print("servant_access_wrappers=PASS")
    print("shared_writer_two_later_commits=PASS")


if __name__ == "__main__":
    main()
