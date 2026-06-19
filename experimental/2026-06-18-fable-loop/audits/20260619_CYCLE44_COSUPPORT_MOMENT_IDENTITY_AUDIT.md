# Cycle 44 Cosupport Moment Identity Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT / EXPERIMENTAL.

Run:

```text
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45
```

Harness status: clean non-ad `artifact_stream` answer. `response.md` is the
only theorem text audited here. Raw JSON/JSONL, prompt, run result, status,
and input manifest are preserved as provenance under:

```text
experimental/2026-06-18-fable-loop/raw/cycle44_cosupport_subset_product_homerun/
```

No web search was used by the worker. The run reported zero web search and
web fetch requests.

## Ledger

Keep the ledgers separate:

```text
q_gen = p
B = F_p
F = F_{p^2}
q_line = p^2
q_chal = unused
D = F_p
n = p
deg E = t = sigma
A = F[X]/E
dim_F A = t
dim_{F_p} A = 2t
j = |T| = n-a
```

The audited branch assumes a source-valid residue-line datum with `E` nonzero
on `D=F_p`, `b=[Bnum]_E != 0`, and the usual noncontained residue-line
setting from `tex/slackMCA_v3.tex:def:residue`.

## Source Alignment

The source object is the residue-line datum and exact normal form in
`tex/slackMCA_v3.tex:1189` and `tex/slackMCA_v3.tex:1197`. Prior audited loop
identities used here:

- Cycle 9: `W=L_S Q_S+I_S`, with `I_S=interp_S(w)`, and bad-line landing
  `[I_S]_E=z[Bnum]_E`.
- Cycle 11/12: the restricted low-`j` line-incidence calculations use the same
  `I_S`/locator quotient object.
- Cycle 13: multiplying by `L_T` gives
  `[L_T]_E[I_S]_E=[W]_E[L_T]_E-[L_D]_E[Q_S]_E`.
- Cycle 43: reserve scaling is reduced to cosupport landings
  `rho(T)=[I_{D\T}]_E in F*b`.

Cycle 44 is source-aligned because it rewrites exactly this residue
`rho(T)=[I_S]_E` for `T=D\S`, not a new MCA object.

## Banked Lemma 1: Cosupport Moment Identity

Let

```text
xi = [X]_E in A
ell = [X^p-X]_E = [L_D]_E in A
Lambda(T) = [L_T]_E in A
M_i = sum_{d in D} w(d)d^i(xi-d)^(-1) in A
```

For `T subset D=F_p`, `|T|=j`, `S=D\T`, and
`I_S=interp_S(w)`, Cycle 44's identity is

```text
rho(T) = [I_S]_E = -ell * Lambda(T)^(-1) * N(T),
N(T) = sum_{d in D} w(d)L_T(d)(xi-d)^(-1).
```

Expanding

```text
L_T(X)=sum_{m=0}^j (-1)^m tau_m X^(j-m),
tau_m=e_m(T),
```

gives

```text
N(T) = sum_{m=0}^j (-1)^m tau_m M_{j-m},
Lambda(T)=sum_{m=0}^j (-1)^m tau_m xi^(j-m).
```

Audit verification:

Since `D=F_p`, `L_D=X^p-X` and `L_D'=-1`. For `s in S`,

```text
L_S'(s)L_T(s)=L_D'(s)=-1,
1/L_S'(s)=-L_T(s).
```

Lagrange interpolation gives

```text
I_S(X) = sum_{s in S} w(s)L_S(X)/(L_S'(s)(X-s))
       = -L_S(X) sum_{s in S} w(s)L_T(s)/(X-s).
```

Reducing mod `E`, `Lambda(T)` is a unit because `E` has no roots on `D` and
`T subset D`, and `[L_S]_E=[L_D]_E Lambda(T)^(-1)=ell Lambda(T)^(-1)`.
The sum extends from `S` to `D` because `L_T(d)=0` for `d in T`. This proves
the displayed identity. Bank this lemma.

## Banked Lemma 2: Landing Orthogonality Reduction

The landing condition is

```text
rho(T) in F*b.
```

Equivalently, for some unique `z in F` when `b Lambda(T) != 0`,

```text
-ell N(T) = z b Lambda(T).
```

Using additive-character orthogonality on the finite additive group `A`, Cycle
44 gives the exact landing identity:

```text
#Land = binom(p,j)/p^(2(t-1)) + E_error,
E_error = p^(-2t) sum_{z in F} sum_{eta != 0}
          psi(a0(eta,z)) S_j(c(eta,z)).
```

Here `S_j(c)` is the elementary-symmetric exponential sum over
`j`-subsets of `F_p`,

```text
S_j(c_1,...,c_j)
  = sum_{T in binom(F_p,j)} psi(sum_{m=1}^j c_m e_m(T)).
```

This is banked as an exact reduction, not as a proved asymptotic. If the
ordinary trace pairing on `A` is degenerate for a non-etale quotient, replace
it with any fixed nondegenerate `F_p`-linear pairing for the additive group.
The additive orthogonality reduction is the banked point; no separability
upgrade is needed for that finite-group identity.

## Conditional Slope-Count Reduction

Let

```text
nu(z)=#{T: rho(T)=z b},
N_split=#{z: nu(z)>0},
M_2=sum_z nu(z)^2.
```

Then Cauchy-Schwarz gives

```text
N_split >= #Land^2/M_2.
```

So a first-moment estimate for `#Land` plus a second-moment anticollision
estimate for `M_2` would imply the Cycle 43 skeleton

```text
N_split ~ min(q_line, binom(p,j)/p^(2(t-1))).
```

This implication is useful but conditional. Do not bank it as a reserve lift.

## Exact New Wall

Cycle 44 sharpens the live wall from

```text
W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION
```

to

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION
```

The preferred next subwall is the second-moment/anticollision form:

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION
```

Target inequality:

```text
M_2 <= #Land + (1+o(1)) #Land^2/q_line.
```

Equivalent falsifier target:

```text
Find a source-valid growing family with max_z nu(z) >= #Land/p^(1+epsilon),
forcing N_split = o(min(q_line, binom(p,j)/p^(2(t-1)))).
```

## What Is Not Banked

Do not bank:

- a proof of first-moment cancellation;
- a proof of the `L2` anticollision bound;
- positive reserve density;
- a corrected-reserve result;
- a generated-field statement;
- any MCA/list/line/curve-MCA consequence;
- a protocol, SNARK, prize, or final `COUNTERPACKET` statement.

Cycle 44 banks the exact residue/moment identity and the exact orthogonality
reduction. It does not close the reserve branch.

## Recommended External Packet

For the six external 5.5 Pro instances, do not send six identical prompts.
Role split:

1. prove the `L2` anticollision bound;
2. hunt a high-multiplicity slope falsifier;
3. source-audit the cosupport identity against `def:residue`;
4. design and/or run the finite checker for `t=2`, increasing `j`;
5. attempt a full homerun reserve lift from the identity;
6. independently reduce the symmetric-function cancellation wall to a smaller
   named theorem.

The next useful packet should include this audit, the Cycle 43 audit, and the
Cycle 44 clean response as provenance.
