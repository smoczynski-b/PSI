# Minimal example — a separating test

This example isolates the basic PSI logic without importing a physical model.

## Candidate space

Let

\[
\Omega=\{a,b,c\}.
\]

The first observation map is

\[
\Psi_0(a)=0,\qquad
\Psi_0(b)=0,\qquad
\Psi_0(c)=1.
\]

Suppose we observe

\[
Y_0=0.
\]

Then the compatible fiber is

\[
F(Y_0)=\{a,b\}.
\]

The observation has ruled out \(c\), but it has not identified whether the underlying candidate is \(a\) or \(b\).

## Task A — distinguish all candidates

Let task \(\mathcal T_A\) require distinguishing \(a\), \(b\) and \(c\) individually.

Then

\[
q_{\mathcal T_A}(a)\neq q_{\mathcal T_A}(b).
\]

Therefore

\[
|q_{\mathcal T_A}(F(Y_0))|=2,
\]

so the task is **not exactly decidable** from \(Y_0\).

Choosing either \(a\) or \(b\) at this point would be reconstruction, not identification.

## A separating test

Introduce a second admissible observation

\[
\Psi_1(a)=0,\qquad
\Psi_1(b)=1.
\]

Applied only after \(Y_0=0\), this test separates the two remaining live candidates.

If

\[
Y_1=0,
\]

then

\[
F(Y_0,Y_1)=\{a\}.
\]

If

\[
Y_1=1,
\]

then

\[
F(Y_0,Y_1)=\{b\}.
\]

The new observation therefore converts an unresolved fiber into a singleton.

## Task B — only distinguish \(c\) from \(\{a,b\}\)

Now change the task.

Let \(\mathcal T_B\) care only whether the candidate belongs to

\[
\{a,b\}
\]

or is equal to \(c\).

Then \(a\) and \(b\) are task-equivalent:

\[
a\;E_{\mathcal T_B}\;b.
\]

For the same first observation \(Y_0=0\), we now have

\[
|q_{\mathcal T_B}(F(Y_0))|=1.
\]

So the very same observation is sufficient for task \(\mathcal T_B\), even though it is insufficient for task \(\mathcal T_A\).

## Point of the example

Identifiability is not an absolute property of the raw observation.

It is relative to the task-relevant quotient:

\[
\boxed{
\text{same data}
+\text{different task}
\Rightarrow
\text{different right to conclude}.
}
\]

And when the current fiber is too large, the correct next move is not to guess — it is to design a test that separates the remaining alternatives.
