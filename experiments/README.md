# Experiments

Controlled PSI experiments, conformance checks and falsification attempts are kept separate.

The label matters: a run that can only pass or fail an adapter does **not** falsify the PSI core.

## PSI–Jev

- [PSI–JEV RUN-01 — separating-test conformance check](PSI-JEV-RUN-01.md)
- [Machine-readable RUN-01 fixture](psi-jev-run-01-fixture.json)

RUN-01 is a deliberately trivial **conformance / smoke test** for the experimental Jev adapter. The PSI oracle is fixed in advance: `T1` is the unique test that guarantees task-level decidability after one result.

The run asks only whether Jev selects that known action while the wrapper preserves the distinction between model confidence and PSI identifiability.

A Jev success or failure in RUN-01 does not confirm or falsify PSI. It evaluates the adapter against a closed synthetic fixture.

The live Jev call is separated from the oracle construction to prevent post-hoc changes to the task partition, admissible tests or scoring rule. That is useful test hygiene, but should not be confused with evidence for the mathematical theory.

A genuine PSI falsification attempt must put a PSI-specific formal claim at risk: for example, a counterexample satisfying the stated hypotheses while violating the claimed conclusion.

## PSI–Traffic

- [PSI-TRAFFIC-EST-01 — public-traffic estimation protocol](PSI-TRAFFIC-EST-01.md)

PSI-TRAFFIC-EST-01 treats public communication as an observation problem. The primary measured object is traffic into the Ψ Omni public research surface, not reactions on the source platform.

The protocol is fixed before adaptive optimization. Its first gate is telemetry: until traffic magnitude, time and source attribution are sufficiently observable, quantitative claims about publication effectiveness remain blocked.
