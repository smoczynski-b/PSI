# PSI-TRAFFIC-EST-01

## Status

`DESIGN / PRE-REGISTRATION / G0A+G0D ACTIVE`

This experiment treats public communication as a PSI observation problem rather than as a branding exercise.

The immediate measured variables are **traffic to the Ψ Omni public website and aggregate outbound research clicks**. The protocol was fixed before adaptive optimization began.

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

A publication is not assumed successful because it receives reactions on the platform.

---

## 2. Desired observation

For a window \(t\), the desired observation is

\[
Y_t=(V_t,U_t,S_t,R_t),
\]

with:

- \(V_t\) — page views / visits;
- \(U_t\) — users or sessions when distinguishable;
- \(S_t\) — source / referral class;
- \(R_t\) — deeper destination arrival / transition when it is actually observable.

Under the present instrumentation, \(R_t\) itself is **not** observed. Instead we observe an outbound-click variable

\[
C_t^{\rm out}=\text{clicks on declared GitHub / Zenodo / PSI-FORUM links}.
\]

Primary quantity after a baseline exists:

\[
\Delta_i=A_i-\widehat B_i.
\]

No causal interpretation is permitted unless attribution and baseline conditions are explicitly satisfied.

---

## 3. Instrumentation gate

### G0A — first-party browser pageviews

Deployed on 2026-09-28. The site records one anonymous first-party event per browser page load with only:

- UTC hour bucket;
- public view (`home`, `lineage`, or `other`);
- coarse source class (`direct`, `internal`, `facebook`, `google`, `github`, `chatgpt`, `other`);
- sanitized explicit campaign tag.

### G0D — outbound research clicks

Deployed on 2026-09-28 and semantically corrected on the same day. The site records anonymous aggregate **click events** on links from Ψ Omni to exactly three research-destination classes:

- `github`;
- `zenodo` (including DOI links);
- `forum` (PSI-FORUM).

Each click event carries only:

- UTC hour bucket;
- current public view;
- destination class;
- the same sanitized campaign tag, if one was supplied at entry.

The event is recorded at click time. It does **not** confirm that the destination loaded, that the visitor read it, or that any scientific contribution occurred.

\[
\boxed{\text{outbound click}\neq\text{confirmed transition / arrival}.}
\]

No user/session/person identifier is created. Campaign-level outbound-click counts can be associated with campaign tags, but individual journeys cannot be reconstructed.

### Privacy boundary

The implementation stores **no IP address, cookie, persistent visitor identifier, raw referrer URL, or person-level journey**.

The summary endpoint explicitly reports:

- `observable = first_party_browser_pageviews`;
- `outboundObservable = aggregate_outbound_research_clicks`;
- `uniqueUsers = null`;
- `uniqueUsersStatus = UNOBSERVED_NO_PERSISTENT_VISITOR_ID`;
- `rawServerRequestsStatus = UNOBSERVED`;
- `journeyIdentityStatus = UNOBSERVED_NO_SESSION_OR_PERSON_IDENTIFIER`.

Daily reads are deliberately bounded. If the safe one-page read is exceeded, the result is marked `censored=true`; no exact pageview or outbound-click total is asserted. A breakout must then trigger a telemetry upgrade rather than silent truncation.

### Current G0 state

\[
\boxed{G0_A(\text{browser pageviews/time/source/campaign})=PASS}
\]

\[
\boxed{G0_D(\text{aggregate outbound research clicks})=PASS}
\]

\[
G0_B(\text{unique users/sessions})=UNOBSERVED,
\qquad
G0_C(\text{raw server requests})=UNOBSERVED,
\qquad
G0_E(\text{confirmed destination arrivals})=UNOBSERVED.
\]

Therefore browser-pageview and aggregate outbound-click claims from the deployment boundary onward are legal. Claims about unique people, sessions, raw server traffic, confirmed arrivals or person-level paths are not.

Social-platform reactions remain contextual observations only.

---

## 4. Baseline

For each publication time \(t_i\), estimate a baseline from comparable untreated periods.

Minimal baseline:

\[
\widehat B_i=\operatorname{median}\{V_t:t\in W_i^{\mathrm{control}}\}.
\]

The control window should preserve, as far as data allow, comparable weekday and clock-time structure. The model version used for every estimate must be recorded.

Because G0A/G0D began only on 2026-09-28, no first-party pageview or outbound-click baseline may be reconstructed for earlier periods from reactions, memory or platform impressions.

---

## 5. Attribution

Where possible, public links should carry a stable campaign/content identifier, e.g.

`utm_campaign=fb-p03-manski`

or

`src=fb-p03-manski`.

The receiver sanitizes and records the campaign tag. Session storage may retain that **tag only** while the visitor remains in the current browser tab/session so later aggregate outbound clicks can remain associated with the campaign. No session identifier is created or stored.

The campaign tag is metadata, not evidence; it becomes evidence only when recorded by the receiving telemetry.

---

## 6. Initial natural sequence

The first public sequence contains heterogeneous representations:

1. PSI formal core,
2. observation versus hidden object,
3. Manski / compatible fiber,
4. task-relative decidability,
5. Ślebodziński / lineage,
6. Sierpiński / lineage.

These items are not to be rewritten retrospectively after observing reactions.

Items published before G0A/G0D are part of communication history but cannot acquire first-party measurements retrospectively.

Later probes may deliberately introduce real experimental results, poetry, film analysis, agent/FORUM interaction or geometric visualization.

---

## 7. Breakout condition

Define

\[
Q_i=\frac{V_i}{\widehat V_i^0}.
\]

A `BREAKOUT` candidate requires:

1. \(Q_i\gg1\) relative to the established baseline;
2. persistence beyond the first short-lived impulse;
3. evidence against trivial mechanical-refresh explanation insofar as the available observables permit;
4. preferably increased aggregate outbound-click counts toward deeper research layers.

No fixed numeric breakout threshold is frozen before baseline variance is known.

Because no persistent visitor identity is collected, condition 3 remains only partially observable. That limitation must be carried into every verdict.

---

## 8. Agent policy

\[
\mathrm{ESTIMATE}\rightarrow\mathrm{BREAKOUT}\rightarrow\mathrm{EXPAND}.
\]

### ESTIMATE

- preserve the scheduled sequence;
- collect observations;
- do not optimize from one noisy result;
- distinguish browser pageviews, platform reactions, people/sessions, server requests, outbound clicks and confirmed arrivals;
- use outbound research clicks as a separate observable, not as proof of arrival or comprehension;
- keep uncertainty explicit.

### BREAKOUT

A candidate regime change triggers re-estimation and source/campaign classification, not automatic imitation of the triggering format.

### EXPAND

Only after a supported breakout may publication frequency or breadth increase. Expansion draws from existing research objects: Principia, experiments, formal results, failures, cultural laboratories, lineage and PSI-FORUM. No filler is manufactured merely to maintain cadence.

---

## 9. Exploration versus exploitation

For representation class \(a\), maintain at minimum

\[
(\widehat\mu_a,\widehat\sigma_a,n_a).
\]

A high response from \(n_a=1\) is not evidence that class \(a\) is globally superior. Adaptive selection must preserve exploration of poorly sampled representation classes.

---

## 10. Interpretation rule

If a representation attracts a new population, the correct conclusion is not automatically `publish more of that format`.

The stronger hypothesis is that the representation may function as an **interface between populations**.

Under current G0 we can observe the aggregate chain only up to

\[
\text{campaign/representation}
\rightarrow
\text{Ψ Omni pageviews}
\rightarrow
\text{outbound clicks toward }\{\text{GitHub},\text{Zenodo},\text{FORUM}\}.
\]

We cannot infer confirmed destination arrival, person-level traversal, comprehension, agreement or scientific contribution from a click event.

---

## 11. Visual constraint

Public representations should preferentially use real research objects rather than scenographic substitutes:

- real equations,
- real diagrams,
- real experimental outputs,
- real quotations with provenance,
- real text/film/poetry objects when culturally analysed.

No aesthetic superiority is assumed in advance; it is a testable representation choice.

---

## 12. Current verdict

`G0A FIRST-PARTY BROWSER TELEMETRY = PASS`

`G0D AGGREGATE OUTBOUND RESEARCH CLICKS = PASS`

`G0B UNIQUE USERS / SESSIONS = UNOBSERVED`

`G0C RAW SERVER REQUESTS = UNOBSERVED`

`G0E CONFIRMED DESTINATION ARRIVALS = UNOBSERVED`

Therefore:

- **instrumentation work stops here for the current experiment**;
- the public sequence continues unchanged;
- pageviews and aggregate outbound clicks are accumulated prospectively;
- no optimization is permitted until a baseline/sample exists;
- an observed censoring boundary or a genuine breakout is the trigger for revisiting telemetry.

This preserves the measurement discipline instead of replacing unavailable quantities with easier proxies after the fact.