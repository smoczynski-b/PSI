#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import hashlib
import json

from durable_shared_memory import DurableSharedMemoryRuntime, JSONLWAL
from mvcc_workspace import MVCCProposal
from shared_memory_runtime import SharedCommitResult


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _fingerprint(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


LEGAL_KINDS = {"TRANSACT", "COMPENSATE", "RECOVER", "INSTITUTION_ACTION"}
BLOCKED_KINDS = {
    "REWRITE_DURABLE_HISTORY",
    "DELETE_COMMITTED_HISTORY",
    "DIRECT_WORKSPACE_MUTATION",
    "SEMANTIC_VERDICT",
}
STOP_KINDS = {"CHANGE_CONSTITUTION", "CONSTITUTION_CONFLICT"}
INSTITUTION_ACTIONS = {
    "NOTICE",
    "POST_QUARANTINE",
    "REQUEST_RECHECK",
    "CLEAR_ANOMALY",
}


@dataclass(frozen=True)
class ServantCommand:
    command_id: str
    kind: str
    txid: str = ""
    proposals: tuple[MVCCProposal, ...] = ()
    runbook_id: str = ""
    compensates_txid: str = ""
    institution_action: str = ""
    subject_id: str = ""

    def __post_init__(self):
        command_id = str(self.command_id).strip()
        kind = str(self.kind).strip().upper()
        txid = str(self.txid).strip()
        runbook_id = str(self.runbook_id).strip()
        compensates = str(self.compensates_txid).strip()
        institution_action = str(self.institution_action).strip().upper()
        subject_id = str(self.subject_id).strip()
        if not command_id:
            raise ValueError("command_id is required")
        if not kind:
            raise ValueError("kind is required")
        object.__setattr__(self, "command_id", command_id)
        object.__setattr__(self, "kind", kind)
        object.__setattr__(self, "txid", txid)
        object.__setattr__(self, "runbook_id", runbook_id)
        object.__setattr__(self, "compensates_txid", compensates)
        object.__setattr__(self, "institution_action", institution_action)
        object.__setattr__(self, "subject_id", subject_id)
        object.__setattr__(self, "proposals", tuple(self.proposals))

    def fingerprint(self) -> str:
        proposals = [
            {
                "proposal_id": p.proposal_id,
                "actor_id": p.actor_id,
                "base_revision": p.base_revision,
                "read_set": list(p.read_set),
                "event_id": p.event.event_id,
                "event_kind": p.event.kind,
                "payload": dict(p.event.payload),
            }
            for p in self.proposals
        ]
        return _fingerprint({
            "kind": self.kind,
            "txid": self.txid,
            "proposals": proposals,
            "runbook_id": self.runbook_id,
            "compensates_txid": self.compensates_txid,
            "institution_action": self.institution_action,
            "subject_id": self.subject_id,
        })


@dataclass(frozen=True)
class ServantDecision:
    command_id: str
    disposition: str
    reason_code: str
    revision_before: int
    revision_after: int
    txid: str = ""
    durable_state: str = ""
    examined_versions: int = 0
    examined_workspaces: int = 0
    examined_dependency_links: int = 0
    examined_events: int = 0
    history_items_copied: int = 0
    history_items_appended: int = 0
    index_refresh_edge_visits: int = 0
    index_membership_updates: int = 0


@dataclass(frozen=True)
class CompletedCommand:
    fingerprint: str
    disposition: str
    reason_code: str
    txid: str
    durable_state: str


class ServantChronicle:
    """Append-only, fsync-backed procedural chronicle with hash-chain integrity."""

    def __init__(self, path: str | Path):
        self.wal = JSONLWAL(path)

    @property
    def path(self) -> Path:
        return self.wal.path

    def append(self, phase: str, command: ServantCommand, payload: dict) -> None:
        self.wal.append(
            f"SERVANT_{phase}",
            f"{command.command_id}:{phase}",
            {
                "command_id": command.command_id,
                "command_kind": command.kind,
                "command_fingerprint": command.fingerprint(),
                **payload,
            },
        )

    def append_reconciled_result(
        self,
        *,
        command_id: str,
        command_kind: str,
        command_fingerprint: str,
        txid: str,
        disposition: str,
        reason_code: str,
        revision_before: int,
        revision_after: int,
        durable_state: str,
    ) -> None:
        self.wal.append(
            "SERVANT_RESULT",
            f"{command_id}:RESULT:RECOVERED",
            {
                "command_id": command_id,
                "command_kind": command_kind,
                "command_fingerprint": command_fingerprint,
                "disposition": disposition,
                "reason_code": reason_code,
                "revision_before": revision_before,
                "revision_after": revision_after,
                "txid": txid,
                "durable_state": durable_state,
                "recovered": True,
                "examined_versions": 0,
                "examined_workspaces": 0,
                "examined_dependency_links": 0,
                "examined_events": 0,
                "history_items_copied": 0,
                "history_items_appended": 0,
                "index_refresh_edge_visits": 0,
                "index_membership_updates": 0,
            },
        )

    def records(self):
        return self.wal.read_valid_prefix().records


class ServantRuntime:
    """Deterministic procedural servant over durable shared memory.

    No natural-language input is accepted. The servant does not decide domain
    truth, mutate the constitution, rewrite durable history or bypass MVCC/WAL.
    It only classifies typed transition commands and executes pre-authorized
    local protocol operations.

    Work counters in `ServantDecision` are observational telemetry copied from
    the executed `SharedCommitResult`. They do not participate in authorization,
    disposition, or epistemic status.
    """

    def __init__(
        self,
        durable: DurableSharedMemoryRuntime,
        chronicle_path: str | Path,
        *,
        authorized_runbooks: Iterable[str] = (),
    ):
        self.durable = durable
        self.chronicle = ServantChronicle(chronicle_path)
        self.authorized_runbooks = frozenset(
            str(x).strip() for x in authorized_runbooks if str(x).strip()
        )
        self._committed_txids = self._load_committed_txids()
        self._completed_commands = self._load_completed_commands()
        self._reconcile_committed_commands()

    def _load_committed_txids(self) -> set[str]:
        return {
            str(r["txid"])
            for r in self.durable.wal.read_valid_prefix().records
            if r.get("kind") == "COMMIT"
        }

    def _load_completed_commands(self) -> dict[str, CompletedCommand]:
        completed: dict[str, CompletedCommand] = {}
        for record in self.chronicle.records():
            if record.get("kind") != "SERVANT_RESULT":
                continue
            payload = record.get("payload", {})
            cid = str(payload.get("command_id", ""))
            fp = str(payload.get("command_fingerprint", ""))
            disposition = str(payload.get("disposition", ""))
            reason = str(payload.get("reason_code", ""))
            # The first completed verdict for a command_id is authoritative.
            # Later RESULT records are idempotent replays or collision outcomes
            # and remain part of the chronicle, but must not rewrite recovery.
            if cid and fp and disposition and cid not in completed:
                completed[cid] = CompletedCommand(
                    fingerprint=fp,
                    disposition=disposition,
                    reason_code=reason,
                    txid=str(payload.get("txid", "")),
                    durable_state=str(payload.get("durable_state", "")),
                )
        return completed

    def _reconcile_committed_commands(self) -> None:
        durable_records = self.durable.wal.read_valid_prefix().records
        commits = {
            str(r["txid"]): r
            for r in durable_records
            if r.get("kind") == "COMMIT"
        }
        acked = {
            str(r["txid"])
            for r in durable_records
            if r.get("kind") == "ACK"
        }
        observed: dict[str, dict] = {}
        for record in self.chronicle.records():
            if record.get("kind") != "SERVANT_OBSERVED":
                continue
            payload = record.get("payload", {})
            cid = str(payload.get("command_id", ""))
            if cid and cid not in observed:
                observed[cid] = payload

        for cid, payload in observed.items():
            if cid in self._completed_commands:
                continue
            txid = str(payload.get("txid", ""))
            if not txid or txid not in commits:
                continue
            kind = str(payload.get("command_kind", ""))
            if kind not in {"TRANSACT", "COMPENSATE"}:
                continue
            fp = str(payload.get("command_fingerprint", ""))
            if not fp:
                continue
            disposition = "ACK_TRANSITION"
            reason = "COMPENSATING_COMMIT_ACCEPTED" if kind == "COMPENSATE" else "COMMIT_ACCEPTED"
            commit_payload = commits[txid].get("payload", {})
            revision_before = int(payload.get("revision", 0))
            revision_after = int(commit_payload.get("new_revision", self.durable.revision))
            durable_state = "ACK" if txid in acked else "COMMIT"
            self.chronicle.append_reconciled_result(
                command_id=cid,
                command_kind=kind,
                command_fingerprint=fp,
                txid=txid,
                disposition=disposition,
                reason_code=reason,
                revision_before=revision_before,
                revision_after=revision_after,
                durable_state=durable_state,
            )
            self._completed_commands[cid] = CompletedCommand(
                fingerprint=fp,
                disposition=disposition,
                reason_code=reason,
                txid=txid,
                durable_state=durable_state,
            )

    def completed_command(self, command_id: str) -> CompletedCommand | None:
        return self._completed_commands.get(str(command_id).strip())

    def _chronicle_observed(self, command: ServantCommand, revision: int) -> None:
        self.chronicle.append("OBSERVED", command, {
            "revision": revision,
            "txid": command.txid,
        })

    @staticmethod
    def _work_payload(work: SharedCommitResult | None) -> dict[str, int]:
        if work is None:
            return {
                "examined_versions": 0,
                "examined_workspaces": 0,
                "examined_dependency_links": 0,
                "examined_events": 0,
                "history_items_copied": 0,
                "history_items_appended": 0,
                "index_refresh_edge_visits": 0,
                "index_membership_updates": 0,
            }
        return {
            "examined_versions": work.examined_versions,
            "examined_workspaces": work.examined_workspaces,
            "examined_dependency_links": work.examined_dependency_links,
            "examined_events": work.examined_events,
            "history_items_copied": work.history_items_copied,
            "history_items_appended": work.history_items_appended,
            "index_refresh_edge_visits": work.index_refresh_edge_visits,
            "index_membership_updates": work.index_membership_updates,
        }

    def _finish(
        self,
        command: ServantCommand,
        *,
        disposition: str,
        reason_code: str,
        revision_before: int,
        durable_state: str = "",
        remember: bool = True,
        work: SharedCommitResult | None = None,
    ) -> ServantDecision:
        counters = self._work_payload(work)
        decision = ServantDecision(
            command_id=command.command_id,
            disposition=disposition,
            reason_code=reason_code,
            revision_before=revision_before,
            revision_after=self.durable.revision,
            txid=command.txid,
            durable_state=durable_state,
            **counters,
        )
        self.chronicle.append("RESULT", command, {
            "disposition": disposition,
            "reason_code": reason_code,
            "revision_before": revision_before,
            "revision_after": decision.revision_after,
            "txid": command.txid,
            "durable_state": durable_state,
            **counters,
        })
        if remember:
            self._completed_commands[command.command_id] = CompletedCommand(
                fingerprint=command.fingerprint(),
                disposition=disposition,
                reason_code=reason_code,
                txid=command.txid,
                durable_state=durable_state,
            )
        return decision

    def _stop(
        self,
        command: ServantCommand,
        revision: int,
        reason: str,
        *,
        remember: bool = True,
    ) -> ServantDecision:
        self.chronicle.append("ESCALATE", command, {
            "reason_code": reason,
            "revision": revision,
        })
        return self._finish(
            command,
            disposition="STOP_ESCALATE_CHRONICLE",
            reason_code=reason,
            revision_before=revision,
            remember=remember,
        )

    def _validate_typed_command(self, command: ServantCommand) -> str | None:
        if command.kind in {"TRANSACT", "COMPENSATE"}:
            if not command.txid:
                return "MISSING_TXID"
            if not command.proposals:
                return "EMPTY_PROPOSAL_BATCH"
        if command.kind == "RECOVER" and (
            command.txid or command.proposals or command.institution_action or command.subject_id
        ):
            return "RECOVER_HAS_WRITE_PAYLOAD"
        if command.kind == "INSTITUTION_ACTION":
            if command.txid or command.proposals or command.compensates_txid:
                return "INSTITUTION_ACTION_HAS_MEMORY_WRITE_PAYLOAD"
            if not command.runbook_id:
                return "MISSING_RUNBOOK"
            if not command.institution_action:
                return "MISSING_INSTITUTION_ACTION"
            if not command.subject_id:
                return "MISSING_SUBJECT_ID"
        return None

    def handle(self, command: ServantCommand) -> ServantDecision:
        if not isinstance(command, ServantCommand):
            raise TypeError("SERVANT accepts ServantCommand only")

        before = self.durable.revision
        fp = command.fingerprint()
        prior = self._completed_commands.get(command.command_id)
        if prior is not None:
            self._chronicle_observed(command, before)
            if prior.fingerprint == fp:
                return self._finish(
                    command,
                    disposition=prior.disposition,
                    reason_code=f"IDEMPOTENT_REPLAY:{prior.reason_code}",
                    revision_before=before,
                    durable_state=prior.durable_state,
                    remember=False,
                )
            return self._stop(
                command,
                before,
                "COMMAND_ID_COLLISION",
                remember=False,
            )

        self._chronicle_observed(command, before)

        if command.kind in STOP_KINDS:
            return self._stop(command, before, command.kind)

        if command.kind in BLOCKED_KINDS:
            return self._finish(
                command,
                disposition="BLOCK_ILLEGAL_TRANSITION",
                reason_code=command.kind,
                revision_before=before,
            )

        if command.kind not in LEGAL_KINDS:
            return self._stop(command, before, "UNKNOWN_TRANSITION_KIND")

        shape_fault = self._validate_typed_command(command)
        if shape_fault:
            return self._finish(
                command,
                disposition="BLOCK_ILLEGAL_TRANSITION",
                reason_code=shape_fault,
                revision_before=before,
            )

        if command.kind == "INSTITUTION_ACTION":
            if command.runbook_id not in self.authorized_runbooks:
                return self._finish(
                    command,
                    disposition="BLOCK_ILLEGAL_TRANSITION",
                    reason_code="RUNBOOK_NOT_AUTHORIZED",
                    revision_before=before,
                )
            if command.institution_action not in INSTITUTION_ACTIONS:
                return self._finish(
                    command,
                    disposition="BLOCK_ILLEGAL_TRANSITION",
                    reason_code="INSTITUTION_ACTION_NOT_AUTHORIZED",
                    revision_before=before,
                )
            return self._finish(
                command,
                disposition="ACK_TRANSITION",
                reason_code=f"INSTITUTION_ACTION_ACCEPTED:{command.institution_action}",
                revision_before=before,
            )

        if command.kind == "RECOVER":
            self.durable.recover()
            self._committed_txids = self._load_committed_txids()
            return self._finish(
                command,
                disposition="ACK_TRANSITION",
                reason_code="RECOVERY_COMPLETED",
                revision_before=before,
            )

        if command.kind == "COMPENSATE":
            if command.runbook_id not in self.authorized_runbooks:
                return self._finish(
                    command,
                    disposition="BLOCK_ILLEGAL_TRANSITION",
                    reason_code="RUNBOOK_NOT_AUTHORIZED",
                    revision_before=before,
                )
            if not command.compensates_txid:
                return self._finish(
                    command,
                    disposition="BLOCK_ILLEGAL_TRANSITION",
                    reason_code="MISSING_COMPENSATED_TXID",
                    revision_before=before,
                )
            if command.compensates_txid not in self._committed_txids:
                return self._finish(
                    command,
                    disposition="BLOCK_ILLEGAL_TRANSITION",
                    reason_code="COMPENSATED_TX_NOT_COMMITTED",
                    revision_before=before,
                )
            if command.txid == command.compensates_txid:
                return self._finish(
                    command,
                    disposition="BLOCK_ILLEGAL_TRANSITION",
                    reason_code="COMPENSATION_MUST_USE_NEW_TXID",
                    revision_before=before,
                )

        try:
            durable_result = self.durable.commit(command.txid, command.proposals)
        except ValueError as exc:
            return self._finish(
                command,
                disposition="BLOCK_ILLEGAL_TRANSITION",
                reason_code=f"DURABLE_PROTOCOL:{type(exc).__name__}",
                revision_before=before,
            )

        if durable_result.result.status == "COMMITTED":
            self._committed_txids.add(command.txid)
            return self._finish(
                command,
                disposition="ACK_TRANSITION",
                reason_code=(
                    "COMPENSATING_COMMIT_ACCEPTED"
                    if command.kind == "COMPENSATE"
                    else "COMMIT_ACCEPTED"
                ),
                revision_before=before,
                durable_state=durable_result.wal_state,
                work=durable_result.result,
            )

        return self._finish(
            command,
            disposition="BLOCK_ILLEGAL_TRANSITION",
            reason_code=f"MVCC:{durable_result.result.status}",
            revision_before=before,
            durable_state=durable_result.wal_state,
            work=durable_result.result,
        )
