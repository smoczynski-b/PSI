# Experiments

Controlled PSI experiments and falsification runs.

## PSI–Jev

- [PSI–JEV RUN-01 — separating-test selection](PSI-JEV-RUN-01.md)
- [Machine-readable RUN-01 fixture](psi-jev-run-01-fixture.json)

RUN-01 is pre-registered before any Jev output is recorded. The PSI oracle is fixed in advance: `T1` is the unique test that guarantees task-level decidability after one result.

The live Jev call is intentionally separated from the oracle construction. This prevents post-hoc changes to the task partition, admissible tests, or success criterion.

Official TypeSafe API documentation currently exposes `POST /v1/systemone` for typed decision queries and `GET /v1/models` for model discovery. Authentication uses a Bearer API key. A Jev output must be recorded verbatim before the RUN-01 result is scored.
