#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import hashlib
import json

from durable_shared_memory import DurableSharedMemoryRuntime, JSONLWAL
from mvcc_workspace import MVCCProposal


def _canon(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _fingerprint(value) -> str:
    return hashlib.sha256(_canon(value).encode("utf-8")).hexdigest()


LEGAL_KINDS = {"TRANSACT", "COMPENSATE", "RECOVER"}
BLOCKED_KINDS = {
    "REWRITE_DURABLE_HISTORY",
    "DELETE_COMMITTED_HISTORY",
    "DIRECT_WORKSPACE_MUTATION",
    "SEMANTIC_VERDICT",
}
STOP_KINDS = {"CHANGE_CONSTITUTION", "CONSTITUTION_CONFLICT"}


@dataclass(frozen=True)
class ServantCommand:
    command_id: str
    kind: str
    txid: str = ""
    proposals: tuple[MVCCProposal, ...] = ()
    runbook_id: str = ""
    compensates_txid: str = ""

    def __post_init__(self):
        command_id = str(self.command_id).strip()
        kind = str(self.kind).strip().upper()
        txid = str(self.txid).strip()
        runbook_id = str(self.runbook_id).strip()
        compensates = str(self.compensates_txid).strip()
        if not command_id:
            raise ValueError("command_id is required")
        if not kind:
            raise ValueError("kind is required")
        object.__setattr__(self, "command_id", command_id)
        object.__setattr__(self, "kind", kind)
        object.__setattr__(self, "txid", txid)
        object.__setattr__(self, "runbook_id", runbook_id)
        object.__setattr__(self, "compensates_txid", compensates)
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

    def records(self):
        return self.wal.read_valid_prefix().records


class ServantRuntime:
    """Deterministic procedural servant over durable shared memory.

    No natural-language input is accepted. The servant does not decide domain
    truth, mutate the constitution, rewrite durable history or bypass MVCC/WAL.
    It only classifies typed transition commands and executes pre-authorized
    local protocol operations.
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
            if cid and fp and disposition:
                completed[cid] = CompletedCommand(
                    fingerprint=fp,
                    disposition=disposition,
                    reason_code=reason,
                    txid=str(payload.get("txid", "")),
                    durable_state=str(payload.get("durable_state", "")),
                )
        return completed

    def _chronicle_observed(self, command: ServantCommand, revision: int) -> None:
        self.chronicle.append("OBSERVED", command, {"revision": revision})

    def _finish(
        self,
        command: ServantCommand,
        *,
        disposition: str,
        reason_code: str,
        revision_before: int,
        durable_state: str = "",
        remember: bool = True,
    ) -> ServantDecision:
        decision = ServantDecision(
            command_id=command.command_id,
            disposition=disposition,
            reason_code=reason_code,
            revision_before=revision_before,
            revision_after=self.durable.revision,
            txid=command.txid,
            durable_state=durable_state,
        )
        self.chronicle.append("RESULT", command, {
            "disposition": disposition,
            "reason_code": reason_code,
            "revision_before": revision_before,
            "revision_after": decision.revision_after,
            "txid": command.txid,
            "durable_state": durable_state,
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
        if command.kind == "RECOVER" and (command.txid or command.proposals):
            return "RECOVER_HAS_WRITE_PAYLOAD"
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
            )

        return self._finish(
            command,
            disposition="BLOCK_ILLEGAL_TRANSITION",
            reason_code=f"MVCC:{durable_result.result.status}",
            revision_before=before,
            durable_state=durable_result.wal_state,
        )
