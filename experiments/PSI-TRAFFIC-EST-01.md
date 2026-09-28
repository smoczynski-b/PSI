# PSI-TRAFFIC-EST-01

## Status

`DESIGN / PRE-REGISTRATION / G0A ACTIVE`

This experiment treats public communication as a PSI observation problem rather than as a branding exercise.

The immediate target variable is **traffic to the Ψ Omni public website**. The experiment asks which representations of the same research program produce measurable movement from an external channel into deeper public layers of the project.

The protocol was fixed before adaptive optimization began.

---

## 1. Object

Let each public item be a treatment-like perturbation

\[
p_i=(C_i,F_i,L_i,T_i,A_i,E_i),
\]

where:

- `C` — content class: formal mathematics, lineage, experiment, poetry, film, agent/FORUM, cultural laboratory;
- `F` — representation: text, formula, diagram, image, video, mixed;
- `L` — length / density class;
- `T` — publication time;
- `A` — call-to-action / destination structure;
- `E` — epistemic stage: problem, hypothesis, test, result, lineage, unresolved.

A publication is not assumed to be successful because it receives reactions on the platform.

---

## 2. Primary observation

For a window \(t\), the desired observation is

\[
Y_t=(V_t,U_t,S_t,R_t),
\]

with:

- \(V_t\) — page views / visits;
- \(U_t\) — users or sessions when distinguishable;
- \(S_t\) — source / referral class;
- \(R_t\) — deeper transitions: GitHub, Zenodo, PSI-FORUM or another declared research destination.

The first experiment optimizes neither reactions nor follower count.

Primary quantity:

\[
\Delta_i = A_i-\widehat B_i,
\]

where \(A_i\) is observed post-publication traffic in a fixed response window and \(\widehat B_i\) is the estimated no-publication baseline for the corresponding time regime.

No causal interpretation is permitted unless attribution and baseline conditions are explicitly satisfied.

---

## 3. Instrumentation gate

`G0 — TELEMETRY`

Before an item may be used as a quantitative observation, the public site must expose enough telemetry to distinguish at least:

1. traffic magnitude,
2. time,
3. referral/source when available,
4. destination transitions when available.

### G0A — first-party browser pageviews

Deployed on 2026-09-28. The site records one anonymous first-party event per browser page load with only:

- UTC hour bucket;
- public view (`home`, `lineage`, or `other`);
- coarse source class (`direct`, `internal`, `facebook`, `google`, `github`, `chatgpt`, `other`);
- sanitized explicit campaign tag.

The implementation stores **no IP address, cookie, persistent visitor identifier, or raw referrer URL**.

The summary endpoint explicitly reports:

- `observable = first_party_browser_pageviews`;
- `uniqueUsers = null` and `uniqueUsersStatus = UNOBSERVED_NO_PERSISTENT_VISITOR_ID`;
- `rawServerRequestsStatus = UNOBSERVED`.

Daily reads are deliberately bounded. If the safe one-page read is exceeded, the result is marked `censored=true` and no exact pageview total is asserted. A breakout must therefore trigger a telemetry upgrade rather than silent truncation.

### G0 boundary

Current state:

\[
\boxed{
G0_A(\text{browser pageviews/time/source/campaign})=PASS
}
\]

\[
G0_B(\text{unique users/sessions})=UNOBSERVED,
\qquad
G0_C(\text{raw server requests})=UNOBSERVED,
\qquad
G0_D(\text{outbound destination transitions})=OPEN.
\]

Therefore **browser-pageview claims from the deployment boundary onward are legal**. Claims about unique people, sessions, raw server traffic or deeper transitions are not.

Social-platform reactions remain contextual observations only. They are not a substitute for any of the unobserved quantities above.

---

## 4. Baseline

For each publication time \(t_i\), estimate a baseline from comparable untreated periods.

Minimal baseline:

\[
\widehat B_i = \operatorname{median}\{V_t: t \in W_i^{\mathrm{control}}\}.
\]

The control window should preserve, as far as data allow, comparable weekday and clock-time structure.

The exact baseline model may become more sophisticated after enough observations exist, but the model version used for every estimate must be recorded.

Because G0A began only on 2026-09-28, no browser-pageview baseline may be reconstructed for earlier periods from social reactions or memory.

---

## 5. Attribution

Where possible, public links should carry source/content identifiers, for example:

`source = facebook`

`campaign = open-psi`

`content = <stable publication id>`

The current G0A receiver records a sanitized campaign tag and coarse source class. An identifier is metadata, not evidence; it becomes evidence only if the receiving telemetry records it.

---

## 6. Initial natural sequence

The first public sequence already contains heterogeneous representations:

1. PSI formal core,
2. observation versus hidden object,
3. Manski / compatible fiber,
4. task-relative decidability,
5. Ślebodziński / lineage,
6. Sierpiński / lineage.

These items are not to be rewritten retrospectively to improve the experiment after observing reactions.

Items published before G0A are part of the communication history but cannot acquire first-party pageview observations retrospectively.

Later probes may deliberately introduce other classes such as:

- a real experimental result,
- poetry,
- film analysis,
- agent/FORUM interaction,
- geometric visualization.

---

## 7. Breakout condition

The experiment is interested not only in marginal uplift but in a possible regime change.

Define

\[
Q_i = \frac{V_i}{\widehat V_i^{0}}.
\]

A `BREAKOUT` candidate requires:

1. \(Q_i \gg 1\) relative to the established baseline,
2. persistence beyond the first short-lived impulse,
3. evidence that traffic is not explained by one actor or mechanical refresh behavior when this can be distinguished,
4. preferably evidence of movement into deeper research layers.

No fixed numeric breakout threshold is frozen before baseline variance is known.

Under current G0A, condition 3 is only partially observable because no persistent visitor identity is collected. That limitation must be carried into any verdict.

---

## 8. Agent policy

The agent operates under

\[
\mathrm{ESTIMATE}\rightarrow\mathrm{BREAKOUT}\rightarrow\mathrm{EXPAND}.
\]

### ESTIMATE

- preserve the scheduled sequence;
- collect observations;
- do not optimize from one noisy result;
- distinguish browser pageviews, platform reactions, people/sessions and server requests;
- keep uncertainty explicit.

### BREAKOUT

A candidate regime change triggers immediate re-estimation and source classification, not automatic content imitation.

### EXPAND

Only after a supported breakout may publication frequency or breadth increase. Expansion draws from existing real research objects: Principia, experiments, formal results, failures, cultural laboratories, lineage and PSI-FORUM.

The agent must not manufacture filler merely to maintain cadence.

---

## 9. Exploration versus exploitation

For representation class \(a\), maintain at minimum

\[
(\widehat\mu_a,\widehat\sigma_a,n_a).
\]

A high response from \(n_a=1\) is not evidence that class \(a\) is globally superior.

Adaptive selection must preserve exploration of poorly sampled representation classes rather than collapsing into the first locally successful format.

---

## 10. Interpretation rule

If a representation attracts a new population, the correct conclusion is not automatically

`publish more of that format`.

The stronger hypothesis is that the representation may function as an **interface between populations**.

The next test is then whether visitors traverse the chain

\[
\text{representation}\rightarrow\text{Ψ Omni}\rightarrow\text{formal/public research layer}.
\]

That transition is not yet directly measured by G0A and belongs to the next instrumentation layer.

---

## 11. Visual constraint

Public representations should preferentially use real research objects rather than scenographic substitutes:

- real equations,
- real diagrams,
- real experimental outputs,
- real quotations with provenance,
- real text/film/poetry objects when culturally analysed.

The experiment may later compare these against more synthetic representations, but no aesthetic superiority is assumed in advance.

---

## 12. Current verdict

`G0A FIRST-PARTY BROWSER TELEMETRY = PASS`

`G0B UNIQUE USERS / SESSIONS = UNOBSERVED`

`G0C RAW SERVER REQUESTS = UNOBSERVED`

`G0D OUTBOUND RESEARCH TRANSITIONS = OPEN`

Therefore:

- the public sequence should continue unchanged;
- quantitative browser-pageview observations may now be accumulated prospectively;
- unique-person, session, raw-server-traffic and transition claims remain blocked;
- the next instrumentation task is to measure **outbound research transitions** without introducing persistent personal tracking.

This preserves the requested measurement discipline instead of replacing an unavailable quantity with an easier proxy after the fact.
