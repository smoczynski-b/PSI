#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Iterable, Mapping, Any


@dataclass(frozen=True)
class InvalidationResult:
    changed_dependencies: tuple[str, ...]
    stale_records: tuple[str, ...]
    visited_tokens: tuple[str, ...]
    examined_links: int


class DependencyIndex:
    """Reverse dependency index for selective invalidation of derived records.

    Records are addressed by stable record_id. A dependency token may be a
    source, edge, contract, object, or another derived record expressed as
    ``record:<record_id>``. Invalidation is transitive over derived records but
    does not scan unrelated records after the index has been built.
    """

    def __init__(self):
        self._record_dependencies: dict[str, frozenset[str]] = {}
        self._reverse: dict[str, set[str]] = defaultdict(set)
        self._status: dict[str, str] = {}

    def register(self, record_id: str, dependencies: Iterable[str], *, status: str = "VALID") -> None:
        rid = str(record_id).strip()
        if not rid:
            raise ValueError("record_id is required")
        deps = frozenset(str(dep).strip() for dep in dependencies if str(dep).strip())
        if not deps:
            raise ValueError("derived record requires at least one dependency")
        if f"record:{rid}" in deps:
            raise ValueError("record cannot depend directly on itself")
        if rid in self._record_dependencies:
            raise ValueError(f"record already registered: {rid}")
        self._record_dependencies[rid] = deps
        self._status[rid] = str(status).strip() or "VALID"
        for dep in deps:
            self._reverse[dep].add(rid)

    def register_record(self, record: Mapping[str, Any]) -> None:
        rid = str(record.get("id", "")).strip()
        dependencies = record.get("dependencies", ())
        if isinstance(dependencies, (str, bytes)):
            raise ValueError("dependencies must be an iterable of tokens, not a string")
        self.register(rid, dependencies, status=str(record.get("status", "VALID")))

    def status(self, record_id: str) -> str:
        return self._status[record_id]

    def dependencies(self, record_id: str) -> frozenset[str]:
        return self._record_dependencies[record_id]

    @property
    def record_count(self) -> int:
        return len(self._record_dependencies)

    @property
    def dependency_link_count(self) -> int:
        return sum(len(v) for v in self._record_dependencies.values())

    def invalidate(self, changed_dependencies: Iterable[str]) -> InvalidationResult:
        initial = tuple(sorted({str(dep).strip() for dep in changed_dependencies if str(dep).strip()}))
        queue = deque(initial)
        visited_tokens: set[str] = set()
        stale: set[str] = set()
        examined_links = 0

        while queue:
            token = queue.popleft()
            if token in visited_tokens:
                continue
            visited_tokens.add(token)

            dependents = self._reverse.get(token, ())
            examined_links += len(dependents)
            for rid in sorted(dependents):
                if rid in stale:
                    continue
                stale.add(rid)
                self._status[rid] = "STALE"
                queue.append(f"record:{rid}")

        return InvalidationResult(
            changed_dependencies=initial,
            stale_records=tuple(sorted(stale)),
            visited_tokens=tuple(sorted(visited_tokens)),
            examined_links=examined_links,
        )


def full_scan_invalidated(records: Mapping[str, Iterable[str]], changed_dependencies: Iterable[str]) -> tuple[str, ...]:
    """Reference oracle: repeatedly scan every record until a fixed point."""
    active_tokens = {str(dep).strip() for dep in changed_dependencies if str(dep).strip()}
    stale: set[str] = set()
    changed = True
    while changed:
        changed = False
        for rid, dependencies in records.items():
            if rid in stale:
                continue
            deps = set(dependencies)
            if deps & active_tokens:
                stale.add(rid)
                active_tokens.add(f"record:{rid}")
                changed = True
    return tuple(sorted(stale))
