AUDIT

# RS-PRIZE-FRONTIER-V1 — exact finite prize-frontier checker

## 1. Executive verdict

**Verdict.** The repository contains enough exact finite definitions to specify the checker unambiguously. This wall closes as an accounting and certificate-verification wall. It does **not** close the scalar/GJ or MCA upper-bound theorem.

**Confidence.** High for the specification and the soundness theorem below. High that, with the presently banked mathematics, the checker will identify many failing reserves and a usually much later certified-safe reserve, leaving an explicit nonempty unknown interval.

The checker has five jobs:

1. preserve `q_gen`, `q_line`, `q_code`, and `q_chal` as different fields;
2. evaluate only finite, theorem-backed integer bounds;
3. propagate lower and upper certificates in the correct reserve directions;
4. report the first reserve not already killed and the exact unresolved upper-budget constraints there;
5. decide whether a projective, Lattès, quotient, or other packet actually moves the certified prize frontier.

It is forbidden to turn `n^{1+o(1)}`, a floating-point estimate, an unregistered theorem, or a field substitution into `SAFE`.

## 2. Required normalization correction

There are two distinct finite prize numerators in the repository.

| Objective | Native sample/parameter field | Native target |
|---|---:|---:|
| MCA bad slopes | `q_line` | `T_line = floor(q_line / 2^128)` |
| scalar/interleaved lists | `q_code` | `T_code = floor(q_code / 2^128)` |

The Cycle 62 role also explicitly requires the field

\[
T_q:=\left\lfloor\frac{q_{\rm code}}{2^{128}}\right\rfloor.
\]

Therefore every result emits `T_q_code` exactly. For a list run, `T_decision=T_q_code`. For an MCA run, the native decision target is `T_q_line`; `T_q_code` may be used instead **only** when either

- `q_line == q_code`, or
- a registered exact normalization bridge proves that comparison with `T_q_code` is equivalent to the native MCA probability comparison.

A larger `q_chal` never changes either target. A larger `q_line` never pays a `q_gen` entropy or projection bill. This explicit objective-dependent rule is necessary; silently setting all four fields equal would make the checker unsound outside the same-field regime.

## 3. Exact finite objects

Let

\[
C=\operatorname{RS}[F_{\rm code},L,k],\qquad n=|L|,\qquad r=n-k,
\]

and let the integer reserve be

\[
0\le \sigma\le r,\qquad a_\sigma=k+\sigma,\qquad
j_\sigma=n-a_\sigma=r-\sigma.
\]

The grid radius at reserve \(\sigma\) is

\[
\delta_{\rm grid}(\sigma)=\frac{j_\sigma}{n}
=1-\frac{k}{n}-\frac{\sigma}{n}.
\]

### 3.1 MCA numerator

After any declared scalar extension from `q_code` to `q_line`, take a parity-check matrix
\(H\) over the line field, with columns \(h_x\), and put

\[
V_T=\operatorname{span}\{h_x:x\in T\}.
\]

For a nonconstant affine syndrome line

\[
\ell(z)=u+zv,\qquad z\in F_{\rm line},\quad v\ne0,
\]

define

\[
\operatorname{Bad}_{\le j}(u,v)=
\left\{
 z\in F_{\rm line}:
 \exists T\subseteq L,\ |T|\le j,
 \ u+zv\in V_T,\ v\notin V_T
\right\}.
\]

The exact support-wise MCA numerator is

\[
M_C(\sigma)=\max_{u,v\ne0}|\operatorname{Bad}_{\le j_\sigma}(u,v)|.
\]

For \(\sigma\ge1\), the banked MDS padding theorem permits replacement of
\(|T|\le j_\sigma\) by \(|T|=j_\sigma\). The checker must not make that replacement at \(\sigma=0\).

### 3.2 Scalar and interleaved list numerator

For interleaving arity \(m\ge1\), let \(\mathcal E_{m,\le j}\) be the
\(m\times n\) arrays with at most \(j\) nonzero columns. If
\(E=(e_1,\ldots,e_m)\), put

\[
\Psi_m(E)=(He_1^{\mathsf T},\ldots,He_m^{\mathsf T}).
\]

The exact list numerator is

\[
L_{C,m}(\sigma)=
\max_s\left|\Psi_m^{-1}(s)\cap\mathcal E_{m,\le j_\sigma}\right|.
\]

The scalar case is \(m=1\). All error weights \(e\le j_\sigma\) are part of this numerator. A boundary-only, raw feasible-support, or minimum-stratum count is not a complete list upper bound.

### 3.3 Monotonicity and zero radius

For either objective, write \(N(\sigma)\) for the relevant numerator. Then

\[
N(\sigma+1)\le N(\sigma),\qquad N(r)=1.
\]

For the objective-dependent exact target \(T\), define

\[
\operatorname{SAFE}(\sigma)\iff N(\sigma)\le T,
\qquad
\operatorname{FAIL}(\sigma)\iff N(\sigma)>T.
\]

If \(T=0\), no reserve is safe. If \(T\ge1\), reserve \(r\) is safe, so the first safe reserve exists.

## 4. Banked core bounds injected by the checker

These are the only non-input mathematical bounds hard-coded into v1.

### 4.1 Both objectives

\[
N(\sigma)\ge1\quad(0\le\sigma\le r),
\qquad N(r)=1.
\]

The first fact follows by propagating the exact zero-radius value backward.

### 4.2 MCA core bounds

The tangent construction gives

\[
M_C(\sigma)\ge j_\sigma.
\]

At the capacity endpoint \(\sigma=0\), where some source statements use the open condition \(\delta<1-\rho\), the same construction still works: the complement of an \(r\)-set has exactly \(k\) points, and any degree-\(<k\) difference vanishing on those \(k\) points is zero; the added point then gives the contradiction required for transversality. The domain checks ensure \(r\le q_{\rm line}\), so the \(r\) tangent parameters can be chosen distinctly.

Thus the injected direct lower bound is

\[
L_{\rm tan}(\sigma)=\max\{1,j_\sigma\}.
\]

In native MCA mode with \(T\ge1\), the tangent term alone kills every
\(\sigma<r-T\). Its greatest failing reserve is \(r-T-1\) when that
integer is nonnegative, so every true first safe reserve obeys

\[
\sigma_*\ge\max\{0,r-T\}.
\]

Every transverse support span meets a fixed affine line in at most one parameter. Hence

\[
M_C(\sigma)\le q_{\rm line}
\]

and, without padding,

\[
M_C(\sigma)\le
\sum_{e=0}^{j_\sigma}\binom ne.
\]

Using exact-\(j\) padding when \(\sigma\ge1\), the sharper core program is

\[
U_{\rm MCA,core}(\sigma)=
\begin{cases}
\min\left\{q_{\rm line},\displaystyle\sum_{e=0}^{r}\binom ne\right\},
&\sigma=0,\\[2mm]
\min\left\{q_{\rm line},\binom n{j_\sigma}\right\},
&1\le\sigma\le r.
\end{cases}
\]

The `min` is represented canonically as two alternative complete upper programs; see Section 10.

### 4.3 List core bounds

Because every set of at most \(r\) parity-check columns is independent, a fixed support carries at most one error array with a fixed syndrome tuple. Therefore

\[
L_{C,m}(\sigma)\le
U_{\rm supp}(\sigma):=
\sum_{e=0}^{j_\sigma}\binom ne.
\]

The interleaved code has column minimum distance \(r+1\). Therefore

\[
2j_\sigma<r+1
\quad\Longrightarrow\quad
L_{C,m}(\sigma)=1.
\]

Consequently, whenever the list target is at least one, the core checker already certifies

\[
\sigma_*\le\left\lceil\frac r2\right\rceil.
\]

These are complete finite upper programs, not heuristic estimates.

## 5. Soundness theorem for the certificate ledger

### Theorem `RS-PRIZE-FRONTIER-V1-SOUNDNESS`

Fix one valid code instance and one objective. Assume every item accepted as certified is backed by the trusted theorem registry or by a registered certificate producer whose hypotheses, source digest, producer digest, code fingerprint, objective, scope, reserve, and field ledger all verify.

For every reserve \(\sigma\), let

\[
L_{\rm dir}(\sigma)=\max_i \ell_i(\sigma)
\]

be the maximum direct certified lower bound, including the core bounds, and let

\[
U_{\rm dir}(\sigma)=\min_p U_p(\sigma)
\]

be the minimum value among complete certified whole-numerator upper programs at that reserve. A missing minimum is recorded as absent, not as infinity in the output.

Define the monotone closures over the full reserve lattice \(\{0,\ldots,r\}\):

\[
L(\sigma)=\max_{\tau\ge\sigma}L_{\rm dir}(\tau),
\qquad
U(\sigma)=\min_{\tau\le\sigma}U_{\rm dir}(\tau),
\]

again treating a missing upper value as absent.

The checker assigns

\[
\begin{array}{ll}
\texttt{FAIL} &\Longleftrightarrow L(\sigma)>T,\\
\texttt{SAFE} &\Longleftrightarrow U(\sigma)\text{ exists and }U(\sigma)\le T,\\
\texttt{UNKNOWN} &\Longleftrightarrow\text{neither condition holds}.
\end{array}
\]

Before assignment it rejects any instance for which \(L(\sigma)>U(\sigma)\) at a reserve where both sides exist.

Then:

1. `FAIL` implies the actual numerator exceeds \(T\).
2. `SAFE` implies the actual numerator is at most \(T\).
3. `UNKNOWN` makes no mathematical assertion beyond absence of a supplied certificate.
4. Let
   \[
   f=\max\{\sigma:L(\sigma)>T\},
   \]
   with sentinel \(f=-1\) if there is no certified failing reserve, and let
   \[
   s=\min\{\sigma:U(\sigma)\le T\}
   \]
   when one exists. If \(T\ge1\), the core zero-radius certificate ensures \(s\le r\), and the true first safe reserve \(\sigma_*\) satisfies
   \[
   f+1\le\sigma_*\le s.
   \]
5. The first reserve not already killed is
   \[
   c=f+1.
   \]
6. The frontier is exact iff \(s=f+1\). In that case \(\sigma_*=s\).

### Proof

A direct lower bound at \(\tau\) also holds at every \(\sigma\le\tau\) because \(N\) is nonincreasing in reserve. This proves the suffix-maximum formula for \(L\). A direct upper bound at \(\tau\) also holds at every \(\sigma\ge\tau\), proving the prefix-minimum formula for \(U\). Threshold comparison gives Items 1–3. Any true first safe reserve must lie strictly after every certified failure and no later than every certified safety point, proving Items 4–6. ∎

## 6. Exact radius and endpoint conventions

For a real radius \(\delta\) in the prize domain \(0\le\delta\le r/n\), the active agreement is

\[
a(\delta)=\left\lceil(1-\delta)n\right\rceil.
\]

For \(1\le\sigma\le r\), reserve \(\sigma\) is active on

\[
\frac{r-\sigma}{n}\le\delta<\frac{r-\sigma+1}{n}.
\]

Reserve \(0\) is active at the capacity endpoint \(\delta=r/n\) after clipping to the prize domain.

If the exact first safe reserve is \(s>0\), then

\[
\delta^{\rm grid}_{\max}=\frac{r-s}{n},
\qquad
\delta^{\rm sup}=\frac{r-s+1}{n},
\]

and the supremal endpoint is unsafe because it activates reserve \(s-1\). If \(s=0\), then

\[
\delta^{\rm grid}_{\max}=
\delta^{\rm sup}=\frac rn,
\]

and the capacity endpoint is safe.

For a nonexact bracket \(f+1\le\sigma_*\le s\), the checker emits both certified radius intervals:

\[
\frac{r-s}{n}
\le \delta^{\rm grid}_{\max}
\le \frac{r-f-1}{n},
\]

and

\[
\operatorname{clip}\!\left(\frac{r-s+1}{n}\right)
\le \delta^{\rm sup}
\le
\operatorname{clip}\!\left(\frac{r-f}{n}\right),
\]

where `clip(x)=min(x,r/n)`. The upper endpoint supplied by a certified failure is unsafe; the lower endpoint need not be attained unless the bracket is exact.

## 7. Canonical input contract

Every proof-relevant integer is a canonical nonnegative decimal string matching

```text
0|[1-9][0-9]*
```

JSON numeric literals, binary floating point, signed zero, leading zeros, `NaN`, and infinities are forbidden in proof-relevant fields. IDs are printable ASCII. Duplicate object keys and duplicate IDs are invalid. Lists declared as sets are lexicographically sorted. The input digest is SHA-256 of UTF-8 RFC-8785-style canonical JSON after duplicate-key rejection.

The minimum complete input is:

```json
{
  "schema": "rs-prize-frontier-v1",
  "certificate_id": "...",
  "code_id": "...",
  "objective": {
    "kind": "mca | scalar_list | interleaved_list",
    "interleaving_arity": "1",
    "decision_denominator": "native | q_code_with_bridge",
    "normalization_bridge_ref": null
  },
  "profile": {
    "id": "proximity-prize-2026-v1",
    "official": true,
    "enforce_rate_set": true,
    "enforce_k_le_2^40": true,
    "enforce_q_code_lt_2^256": true,
    "enforce_q_line_lt_2^256": true
  },
  "n": "...",
  "k": "...",
  "domain_descriptor": {
    "schema": "rs-domain-descriptor-v1",
    "kind": "multiplicative_subgroup | multiplicative_coset | projective_subline | explicit",
    "size": "...",
    "ambient_field": "q_code",
    "generated_field": "q_gen",
    "ordered_points_sha256": "...",
    "order_factorization": [],
    "certificate_ref": "..."
  },
  "q_gen": "...",
  "q_line": "...",
  "q_code": "...",
  "q_chal": "...",
  "field_ledger": {
    "characteristic": "...",
    "fields": {
      "q_gen":  {"degree": "...", "field_certificate_ref": "..."},
      "q_line": {"degree": "...", "field_certificate_ref": "..."},
      "q_code": {"degree": "...", "field_certificate_ref": "..."},
      "q_chal": {"degree": "...", "field_certificate_ref": "..."}
    },
    "embeddings": [],
    "generated_field_minimality_ref": "..."
  },
  "reserve_range": ["sigma_min", "sigma_max"],
  "certified_lower_terms": [],
  "certified_upper_terms": [],
  "conditional_terms": [],
  "upper_programs": [],
  "budget_programs": [],
  "theorem_manifest": [],
  "options": {
    "emit_dense_rows": true,
    "emit_leave_one_out_relevance": true,
    "maximum_output_rows": "1000000",
    "maximum_budget_branches": "4096"
  }
}
```

`reserve_range` controls the rows requested in the report. Monotone propagation and frontier extraction use **all** certified reserve events, including events outside that output range and the core anchors at \(0\) and \(r\).

## 8. Field, code, and domain validation

The checker validates by exact arithmetic:

1. `0 < k < n`, `r=n-k`, and `0 <= sigma_min <= sigma_max <= r`.
2. `domain_descriptor.size == n`.
3. For every field role, if the common characteristic is \(p\) and the declared degree is \(d\), then the declared order is exactly \(p^d\).
4. The characteristic has a registered primality certificate. A probable-prime test is insufficient.
5. Every claimed embedding has equal characteristic and divisible extension degrees; witness-verifying mode additionally checks the explicit embedding map.
6. The code field embeds into the line field whenever MCA is evaluated over an extension line field.
7. A multiplicative subgroup or coset satisfies \(n\mid(q_{\rm ambient}-1)\), with exact-order evidence tied to the supplied factorization.
8. An affine explicit domain has at most its ambient field size; a projective domain has at most one more point than its ambient field size.
9. The ordered-domain digest and the domain certificate agree with `code_id`.
10. In the official profile,
    \[
    \frac kn\in\left\{\frac12,\frac14,\frac18,\frac1{16}\right\},
    \qquad k\le2^{40},
    \]
    checked by cross multiplication, and the declared strict field caps hold.
11. For a list objective, the decision denominator is `q_code`.
12. For native MCA, the decision denominator is `q_line`.
13. MCA comparison against `q_code` requires `q_line==q_code` or a registered exact bridge.
14. No term may substitute `q_chal` for a generated-, line-, or code-field quantity.

The result always reports

\[
T_{\rm code}=q_{\rm code}\mathbin{//}2^{128},
\qquad
T_{\rm line}=q_{\rm line}\mathbin{//}2^{128},
\]

and identifies which one is `T_decision`.

## 9. Trusted theorem and term contract

The checker is a verifier, not a theorem-discovery engine. Prose in Markdown or TeX is not automatically trusted.

### 9.1 Trusted registry entry

A theorem may be used only if the immutable local registry contains an entry with:

```json
{
  "theorem_id": "...",
  "version": "...",
  "status": "PROVED_FINITE",
  "statement_sha256": "...",
  "source_sha256": "...",
  "hypothesis_evaluator_id": "...",
  "allowed_objectives": [],
  "allowed_directions": [],
  "allowed_scopes": [],
  "allowed_aggregation_roles": [],
  "registered_producers": [
    {"producer_id": "...", "version": "...", "code_sha256": "..."}
  ]
}
```

The registry hash is included in every result.

### 9.2 Certified term

Each term has the following canonical shape:

```json
{
  "id": "unique-term-id",
  "status": "PROVED_FINITE",
  "objective": "mca | scalar_list | interleaved_list",
  "direction": "lower | upper",
  "term_type": "registered-type-id",
  "scope": {
    "kind": "whole_numerator | component | case_branch",
    "id": "scope-id"
  },
  "aggregation_role": "standalone | sum_child | max_case | bridge_input",
  "reserve_data": {
    "kind": "table | registered_evaluator",
    "entries": [
      {"sigma": "...", "bound": "..."}
    ],
    "evaluator_id": null,
    "parameters": {}
  },
  "field_debits": {
    "entropy": "q_gen | unused",
    "line": "q_line | unused",
    "code": "q_code | unused",
    "challenge": "unused"
  },
  "theorem_id": "...",
  "hypothesis_evidence": [],
  "producer_certificate": {
    "producer_id": "...",
    "version": "...",
    "source_sha256": "...",
    "certificate_sha256": "...",
    "producer_code_sha256": "...",
    "code_fingerprint": "..."
  },
  "notes": "non-normative"
}
```

The code fingerprint is SHA-256 of the canonical tuple

```text
(code_id, objective, interleaving_arity, n, k,
 domain_descriptor_digest, q_gen, q_line, q_code, q_chal).
```

A table lower entry asserts \(N(\sigma)\ge b\). A table upper entry asserts that the declared scope is at most \(b\). A registered evaluator must expose exact operations

```text
value_at(sigma)
threshold_crossing_events(T, reserve_interval)
hypotheses(instance, sigma)
```

and is identified by a registry digest. Arbitrary executable formulas are forbidden.

### 9.3 Lower-term rule

Distinct lower mechanisms combine only by `max`. They are never summed by the checker. If a theorem proves a disjoint union of witnesses, its producer must emit the already-combined integer as one lower term.

A producer may emit `min(proved_lower,T_decision+1)`. This remains a valid lower bound and is sufficient for failure and frontier relevance.

### 9.4 Upper-term rule

A component or case-branch upper term is not a whole-numerator upper certificate until a valid upper program consumes it. Every upper leaf used for safety is an exact nonnegative integer bound.

If a numerical analytic tool produced an interval, the certificate must expose a rigorously rounded integer endpoint:

- a lower endpoint for a lower term;
- an upper endpoint for an upper term.

An interval straddling the needed integer comparison yields no certified decision.

### 9.5 Conditional term

A conditional term uses the same finite format, but at least one dependency is not `PROVED_FINITE`. It is evaluated in a separate hypothetical ledger. It never changes `SAFE` or `FAIL`.

A certified lower bound may refute a conditional upper claim at the same instance. The result then records `CONDITIONAL_CLAIM_REFUTED_AT_INSTANCE`; the certified data remain valid.

## 10. Supported term catalogue

V1 recognizes only registered types. The following IDs are reserved.

### 10.1 Injected core

```text
core.unit_lower
core.zero_radius_exact
mca.tangent_lower
mca.field_cap_upper
mca.support_union_upper
list.support_injective_upper
list.unique_decoding_upper
```

### 10.2 Registered lower producers

```text
mca.bessel_paley_lower
list.generated_field_entropy_lower
list.quotient_core_binomial_lower
packet.explicit_mca_slope_set
packet.explicit_list_fiber
enumeration.exact_mca_numerator
enumeration.exact_list_numerator
```

An explicit packet term must bind the packet verifier digest, reserve, code fingerprint, witness cardinality, transversality/noncontainment status when applicable, and objective field.

### 10.3 Registered upper producers

```text
list.scalar_apolar_gj_layer_upper
list.scalar_all_layer_upper
list.scalar_to_interleaved_projection
mca.occupancy_upper
mca.tangent_or_envelope_upper
mca.quotient_upper
mca.residual_upper
mca.high_denominator_upper
mca.aperiodic_upper
mca.direct_all_line_upper
generic.direct_whole_numerator_upper
```

A boundary-layer scalar/GJ term is a component until a coverage theorem proves that all error weights \(e\le j\) have been charged.

## 11. Upper-program language and exact aggregation

The canonical v1 AST has only `term`, `sum`, and `max` nodes.

```json
{
  "id": "mca-six-term-sharp",
  "objective": "mca",
  "evaluation_reserves": ["..."],
  "root_scope": "whole_numerator",
  "coverage_certificate_ref": "...",
  "expression": {
    "op": "max",
    "justification": {
      "kind": "exhaustive_case_partition",
      "certificate_ref": "..."
    },
    "args": [
      {"op": "term", "id": "U_res"},
      {"op": "term", "id": "U_high"},
      {
        "op": "sum",
        "justification": {
          "kind": "union_bound | disjoint_assignment",
          "certificate_ref": "..."
        },
        "args": [
          {"op": "term", "id": "N_occ"},
          {"op": "term", "id": "U_tan"},
          {"op": "term", "id": "U_quot"},
          {"op": "term", "id": "U_ap"}
        ]
      }
    ]
  }
}
```

The rules are:

1. `sum` requires a registered union-bound coverage theorem or a registered disjoint canonical assignment. Overlap is allowed under a union bound, but coverage must be proved.
2. `max` requires a registered exhaustive case partition of the ambient line, received-word, or syndrome class.
3. Every node is scope-typed. The root must have scope `whole_numerator`.
4. Every leaf is nonnegative. Duplicate use of a term in one additive branch is invalid unless a registered multiplicity theorem explicitly authorizes it.
5. A program is complete certified only when its root coverage, every leaf, every aggregation justification, and every hypothesis verify.
6. A conditional or missing leaf makes the program conditional/incomplete, never certified.
7. Alternative complete proofs are separate programs. Their values combine by a top-level minimum.
8. A source expression `min(A,B)` is canonically compiled into two alternative programs. There is no `min` AST node, avoiding ambiguity in unresolved-budget extraction.
9. A scalar-to-interleaved bridge is complete only after exact verification of
   \[
   \binom{U_B+1}{2}<q_{\rm gen}
   \]
   or of the field named by the registered projection theorem. A larger `q_chal` cannot satisfy this test.

The sharp six-term MCA certificate is therefore

\[
\max\{U_{\rm res},U_{\rm high},
N_{\rm occ}+U_{\rm tan}+U_{\rm quot}+U_{\rm ap}\},
\]

not an unjustified six-term sum. A conservative additive program may be supplied separately if its own coverage theorem is valid.

## 12. Exact unresolved-budget normal form

A budget program is an upper-program template in which unresolved nonnegative leaves are written as `hole:<id>`. It is never itself a certified upper program until all holes are filled by certified upper terms.

For a fixed reserve, replace every known leaf by its exact integer upper bound and every hole by a formal nonnegative integer variable. For an expression \(E\) using only `sum` and `max`, define `Expand(E)` recursively:

- `Expand(c)={(c,0)}` for a known integer leaf \(c\);
- `Expand(h_i)={(0,e_i)}` for a hole \(h_i\);
- `Expand(max(E_1,...,E_t))` is the union of the expansions;
- `Expand(sum(E_1,...,E_t))` is the Cartesian Minkowski sum.

Then identically

\[
E(h)=\max_{(c,m)\in\operatorname{Expand}(E)}
\left(c+\sum_i m_i h_i\right).
\]

Thus that program clears the target exactly when every branch inequality

\[
\sum_i m_i h_i\le T-c
\]

holds.

The checker:

1. emits all such inequalities with exact integer coefficients;
2. marks a branch `IMPOSSIBLE` if \(c>T\);
3. removes duplicate inequalities;
4. may remove an inequality \((m,b)\) only under the safe syntactic dominance rule: another inequality \((m',b')\) has \(m'_i\ge m_i\) for every \(i\) and \(b'\le b\);
5. refuses only the budget expansion, not the already established row verdict, if the exact branch count exceeds `maximum_budget_branches`.

For the sharp MCA program, the exact remaining budget is

```text
h_res <= T
h_high <= T
h_tan + h_quot + h_ap <= T - N_occ
```

not the generally incorrect single number `T - sum(all known terms)`.

Alternative budget programs are reported as a disjunction: satisfying any one complete program is enough for safety.

## 13. Exact arithmetic engine

All verdicts use integer or rational arithmetic only.

### 13.1 Target and strictness

```text
T_code = q_code // 2^128
T_line = q_line // 2^128
FAIL iff lower >= T_decision + 1
SAFE iff upper <= T_decision
```

Every strict/non-strict comparison is preserved exactly.

### 13.2 Fractions

Every radius is stored as an integer numerator and denominator and also emitted in reduced form using `gcd`. Decimal radii are non-normative diagnostics only.

### 13.3 Binomial comparisons under the official cap

Under the strict official field cap, \(T<2^{128}\). Let
\(m=\min\{b,n-b\}\). If \(m\ge128\), then

\[
\binom nb\ge\binom{2m}{m}\ge2^m\ge2^{128}>T.
\]

If \(m<128\), the checker computes \(\binom nb\) exactly by the multiplicative recurrence in at most 127 steps. Therefore every isolated binomial-versus-target comparison needed by quotient packets is exact without materializing challenge-size factorials.

For a binomial sum, the evaluator accumulates exact nonnegative terms and stops with the proved relation `>T` as soon as the partial sum exceeds \(T\). To certify `<=T`, all terms are computed exactly. A core upper formula whose value is proved `>T` is recorded as decision-inactive and need not be materialized; omitting an above-target upper bound cannot create a false `SAFE`. Whenever a core upper formula can certify safety, its value is at most \(T<2^{128}\) and is therefore emitted as an exact decimal integer. Registered entropy/Bessel formulas with much larger intermediate thresholds use registered exact evaluators or rigorously directed integer endpoints.

### 13.4 Forbidden arithmetic

No decision path may call or consume:

```text
float, math.log, lgamma, decimal approximations,
O(...), o(...), Theta(...), ~, approximately,
eventually, sufficiently large, unspecified constants,
n^{1+o(1)}, or an unspecified polynomial.
```

Such material may appear only in `notes` or the conditional ledger and is ignored by the certified evaluator.

## 14. Reserve evaluation and sparse monotone propagation

A certificate contains finitely many direct reserve events. Registered evaluators may generate additional exact events. The checker need not enumerate all \(r+1\) reserves to determine the frontier.

1. Resolve all term tables and registered evaluator events.
2. Inject the core formulas and anchors at \(0\) and \(r\).
3. At every direct event reserve, compute `L_dir` and every complete `U_program`.
4. Sort lower events by decreasing reserve and form a suffix maximum.
5. Sort complete upper events by increasing reserve and form a prefix minimum.
6. For any requested row \(\sigma\), binary-search those step functions to obtain \(L(\sigma)\) and \(U(\sigma)\).
7. The greatest certified failing reserve is equivalently the greatest direct-event reserve with a lower value greater than \(T\).
8. The least certified safe reserve is equivalently the least direct-event reserve with a complete upper value at most \(T\).
9. A registered evaluator that claims a bound on an interval must either expand the required row values or return a certified threshold-crossing event plus `value_at` support. It cannot return a floating estimate of the crossing.

Dense output is required for every integer in `reserve_range`. If the requested number of rows exceeds `maximum_output_rows`, the checker returns `RESOURCE_LIMIT` without changing certificate validity; a narrower range or a lossless run-length mode may then be requested.

## 15. Frontier and packet relevance

### 15.1 Frontier record

For \(T\ge1\), define

```text
f = greatest certified failing reserve, or -1
c = f + 1                         # first reserve not already killed
s = least certified safe reserve  # exists because sigma=r is safe
```

The checker reports:

- the strict previous-reserve lower witness at `f` when `f>=0`;
- the unknown/certified status at `c`;
- the exact budget-program constraints at `c`;
- the bracket `[c,s]` for the true first safe reserve;
- exact frontier and endpoint data when `c==s`.

If \(T=0\), it reports `NO_SAFE_RESERVE`, `f=r`, and no candidate `c` in the reserve lattice.

### 15.2 Leave-one-out relevance for lower packets

For each certified lower term \(P\), recompute the greatest certified failing reserve after removing that term:

\[
f_{-P}=\max\{\sigma:L_{-P}(\sigma)>T\},
\]

using \(-1\) if empty. Let \(\lambda_P(\sigma)\) be the propagated contribution of \(P\) alone.

Classify exactly:

- `MOVES_FAILURE_FRONTIER` if \(f>f_{-P}\);
- `TIES_FAILURE_FRONTIER` if \(f=f_{-P}\), \(\lambda_P(f)=L(f)>T\), and another term still certifies failure there;
- `SUBFRONTIER_REDUNDANT` if \(P\) exceeds the target somewhere but removal leaves the same frontier and \(P\) does not attain the frontier maximum;
- `NUMERICALLY_INACTIVE` if \(\lambda_P(\sigma)\le T\) for every reserve;
- `CONDITIONAL_ONLY` if the packet is not certified.

This is the exact stop rule for projective and Lattès work. A packet can falsify a taxonomy theorem while being prize-subfrontier.

### 15.3 Leave-one-out relevance for upper programs

Remove one complete upper program and recompute the least certified safe reserve \(s_{-P}\). Classify `MOVES_SAFE_FRONTIER` exactly when \(s<s_{-P}\); classify a tie only when the removed program attains the minimum at \(s\) and another program preserves it.

Removing an upper leaf invalidates every program that depends on it before recomputation.

## 16. Required output contract

```json
{
  "schema": "rs-prize-frontier-result-v1",
  "input_sha256": "...",
  "checker_sha256": "...",
  "trusted_registry_sha256": "...",
  "validation": {
    "status": "VALID_OFFICIAL | VALID_RESEARCH | INVALID_CERTIFICATE | RESOURCE_LIMIT",
    "errors": [],
    "warnings": []
  },
  "objective": {
    "kind": "...",
    "interleaving_arity": "...",
    "decision_denominator": "q_line | q_code",
    "normalization_bridge_used": false
  },
  "targets": {
    "two_to_128": "340282366920938463463374607431768211456",
    "q_code": "...",
    "T_q_code": "...",
    "q_line": "...",
    "T_q_line": "...",
    "T_decision": "..."
  },
  "rows": [
    {
      "sigma": "...",
      "a": "...",
      "j": "...",
      "target": "...",
      "lower": {
        "direct_max": "...",
        "propagated_max": "...",
        "direct_source_term_ids": [],
        "propagated_source_term_ids": []
      },
      "upper": {
        "direct_proved_total_exists": true,
        "direct_proved_total": "... or null",
        "direct_program_id": "... or null",
        "propagated_proved_total_exists": true,
        "propagated_proved_total": "... or null",
        "propagated_program_id": "... or null"
      },
      "unresolved_budget": {
        "program_alternatives": [
          {
            "program_id": "...",
            "constraints": [
              {
                "holes": {"hole-id": "1"},
                "budget": "signed decimal",
                "status": "OPEN | CLOSED | IMPOSSIBLE"
              }
            ]
          }
        ]
      },
      "comparison": {
        "lower_minus_target": "signed decimal",
        "target_minus_upper": "signed decimal or null"
      },
      "status": "SAFE | FAIL | UNKNOWN",
      "status_reason": "...",
      "assumption_flags": [],
      "field_debit_summary": [],
      "radius": {
        "grid": {"numerator": "j", "denominator": "n"},
        "raw_same_reserve_interval": {
          "left_closed": {"numerator": "j", "denominator": "n"},
          "right_open": {"numerator": "j+1", "denominator": "n"}
        },
        "prize_domain_clipped_interval": "exact structured interval",
        "transition_candidate": {"numerator": "j+1", "denominator": "n"}
      }
    }
  ],
  "frontier": {
    "no_safe_reserve": false,
    "greatest_certified_failing_reserve": "... or -1",
    "first_not_killed_reserve": "... or null",
    "least_certified_safe_reserve": "... or null",
    "sigma_star_interval": {"lower": "...", "upper": "..."},
    "exact": false,
    "sigma_star": null,
    "previous_reserve_failure": {},
    "candidate_status": "...",
    "candidate_unresolved_budget": {},
    "largest_safe_grid_radius": null,
    "supremal_safe_radius": null,
    "supremal_endpoint_safe": "true | false | unknown",
    "radius_intervals": {}
  },
  "term_relevance": [],
  "conditional_conflicts": [],
  "theorem_manifest": []
}
```

Every rational is emitted both in reserve form and reduced form. No decimal radius affects a verdict.

## 17. Invalid-certificate conditions

The top-level result is `INVALID_CERTIFICATE`, not `UNKNOWN`, if any of the following occurs:

1. malformed canonical JSON, duplicate key/ID, malformed integer, or out-of-range reserve;
2. failed prime-power, embedding, domain, code, official-rate, or strict field-cap check;
3. objective target selected from the wrong field without an accepted bridge;
4. `q_chal` used to pay a code, line, generated-field, or projection bill;
5. missing theorem-registry entry or any source/producer/code-fingerprint mismatch;
6. false or unverifiable certified hypothesis;
7. unsupported term type or arbitrary executable formula;
8. unsupported, scope-inconsistent, or ambiguous aggregation;
9. a component upper bound used as a whole-numerator bound without coverage;
10. a `max` without an exhaustive case partition;
11. a `sum` without union-bound or disjoint-assignment justification;
12. a conditional/asymptotic/floating term used in a certified decision;
13. exact-\(j\) MCA padding at \(\sigma=0\);
14. a claimed scalar-to-interleaved bridge whose collision inequality is false;
15. a boundary-only list term claimed as all-layer coverage without a theorem;
16. certified propagated lower and upper bounds crossing at any reserve;
17. a packet count, reserve, objective, or code digest inconsistent with its verifier certificate.

A valid but incomplete collection of terms returns `UNKNOWN` where appropriate. Failure to expand an oversized budget normal form returns a budget-specific resource flag, not a false safety verdict.

## 18. Reference pseudocode

```text
function CHECK_FRONTIER(input, registry):
    reject_duplicate_json_keys(input)
    canonical_validate_strings_ids_and_integers(input)
    I = parse_exact_integers(input)

    validate_fields_code_domain_profile(I, registry)
    r = I.n - I.k

    T_code = I.q_code // 2^128
    T_line = I.q_line // 2^128
    if I.objective is MCA:
        if I.decision_denominator == native:
            T = T_line
        else:
            verify_q_code_normalization_bridge(I, registry)
            T = T_code
    else:
        require I.decision_denominator in {native, q_code_with_bridge}
        T = T_code

    fingerprint = hash_code_tuple(I)
    terms = verify_and_resolve_terms(I, registry, fingerprint)
    inject_core_terms(terms, I, r, T)

    direct_event_reserves = {0, r}
    direct_event_reserves += every explicit term-table reserve
    direct_event_reserves += every registered evaluator crossing/value event
    direct_event_reserves += every core-formula threshold-crossing event
    direct_event_reserves += every upper-program evaluation reserve
    direct_event_reserves += every requested output reserve

    for sigma in sorted(direct_event_reserves):
        require 0 <= sigma <= r
        j = r - sigma
        a = I.k + sigma

        active_lower = certified_whole_lower_terms_at(terms, sigma)
        Ldir[sigma] = max(bound(t, sigma) for t in active_lower)
        Ldir_sources[sigma] = argmax_ids(...)

        complete = []
        for program in I.upper_programs plus core_programs:
            if sigma in program.evaluation_reserves or program is core_formula:
                result = typecheck_verify_and_evaluate(program, terms, sigma)
                if result.complete_certified:
                    complete.append(result)
        Udir[sigma] = minimum_value_or_absent(complete)
        Udir_source[sigma] = argmin_program_id(...)

        evaluate_conditional_programs_separately(...)
        expand_budget_programs_exactly_or_flag_resource_limit(...)

    lower_steps = suffix_max_step_function(Ldir)
    upper_steps = prefix_min_step_function(Udir)

    for every step breakpoint and every requested row sigma:
        L = lower_steps.value_at(sigma)
        U = upper_steps.value_at_or_absent(sigma)
        if U exists and L > U:
            return INVALID_CERTIFICATE("crossing certified bounds")

    if T == 0:
        frontier.no_safe_reserve = true
        frontier.f = r
        frontier.c = null
        frontier.s = null
    else:
        f = greatest direct reserve with Ldir[reserve] > T, else -1
        s = least direct reserve with Udir[reserve] exists and Udir[reserve] <= T
        require s exists              # zero-radius exact core certificate
        require f < s                 # otherwise certified contradiction
        c = f + 1
        frontier = derive_sigma_and_radius_brackets(f, c, s, r, I.n)

    for sigma in every integer of input.reserve_range:
        L = lower_steps.value_at(sigma)
        U = upper_steps.value_at_or_absent(sigma)
        if L > T:
            status = FAIL
        else if U exists and U <= T:
            status = SAFE
        else:
            status = UNKNOWN
        emit_exact_row(sigma, I.k + sigma, r - sigma,
                       T, L, U, status,
                       exact_budget_constraints(sigma),
                       exact_radius_data(sigma))

    relevance = leave_one_out_lower_and_upper_frontiers(...)
    conditional_conflicts = compare_certified_and_conditional_ledgers(...)
    return canonical_result_with_hashes(...)
```

## 19. Mandatory regression suite

A conforming implementation must pass all of the following.

1. **Target floor.** Test `q=2^128-1`, `2^128`, and `2^128+1` exactly.
2. **No-safe case.** If the decision field is below `2^128`, then `T=0`; the unit lower bound makes every reserve fail.
3. **Zero-radius endpoint.** If `T>=1`, reserve `r` is exactly safe with numerator one.
4. **Objective normalization split.** A list run uses `q_code`; an MCA run uses `q_line`. Changing `q_chal` changes neither. MCA use of `q_code` with unequal fields is rejected absent a bridge.
5. **Tangent floor.** Verify failure wherever `r-sigma>T_line` in native MCA mode.
6. **Core upper programs.** Verify the exact support-union, exact-`j` padding guard, list support bound, and unique-decoding value one.
7. **Projective equality packet arithmetic.** For
   \[
   p=2^{19}-1,
   \quad n=2^{19},\quad k=2^{17},\quad \sigma=2^{14},
   \quad q=p^8,
   \]
   verify
   \[
   q=5708903659119442793759136591282812149479505921,
   \]
   \[
   T=16776960,
   \qquad 28048800-T=11271840>0,
   \]
   and classify the certified packet as a failure event at reserve \(2^{14}\).
8. **Degree-31 Lattès arithmetic.** For `q=8191^18`, verify
   \[
   T=80951559894234747884481262824352.
   \]
   The integer lower bound `2^127+1 = 170141183460469231731687303715884105729` fails at reserve 31. If a separate certified reserve-32 packet has lower bound `2^122+1 = 5316911983139663491615228241121378305`, removing the reserve-31 term leaves the frontier at 32, so the degree-31 term is `SUBFRONTIER_REDUNDANT`.
9. **Max versus sum.** With `T=10` and two exhaustive exclusive case caps equal to 8, `max(8,8)` is safe; an additive 16 is not.
10. **Monotone closure.** A lower certificate at reserve 5 propagates to 0–5. An upper certificate at reserve 8 propagates to 8–r.
11. **Exact frontier.** Failure at `s-1` and safety at `s` produce `sigma_star=s`, grid radius `(r-s)/n`, supremum `(r-s+1)/n`, endpoint unsafe.
12. **Capacity edge.** Exact `sigma_star=0` clips the supremum to `r/n` and marks the capacity endpoint safe.
13. **Sigma-zero MCA guard.** Reject exact-`j` padding at reserve zero.
14. **Projection collision.** Accept a scalar-to-interleaved bridge iff the exact strict inequality `U_B(U_B+1)/2 < q_gen` holds.
15. **Boundary-only refusal.** A scalar minimum-stratum upper with no all-layer coverage cannot certify a list-safe row.
16. **Asymptotic refusal.** A term containing `n^{1+o(1)}` remains conditional/unusable.
17. **Rigorous interval.** An interval with upper endpoint at most the target can supply an upper integer cap; an interval straddling the target supplies no verdict.
18. **Contradictory certificates.** Lower 11 and upper 10 at the same propagated reserve return `INVALID_CERTIFICATE`.
19. **Strict official cap.** `q_code=2^256` is invalid under the declared strict official profile.
20. **Leave-one-out tie.** Two independent lower terms attaining the same failing frontier are both ties, not movers.

## 20. Parameter and finite-relevance ledger

| Symbol/field | Exact role |
|---|---|
| `q_gen` | generated-domain field; entropy, locator, GJ, and projection bills only where a theorem says so |
| `q_line` | actual MCA parameter/slope field and native MCA denominator |
| `q_code` | code alphabet and scalar/interleaved-list denominator; also the role-mandated `T_q_code` field |
| `q_chal` | external protocol challenge accounting only |
| `sigma` | integer agreement reserve above `k` |
| `a=k+sigma` | agreement threshold |
| `j=n-k-sigma` | error-column/support budget |
| `T_decision` | exact objective target |
| `f` | greatest certified failing reserve |
| `c=f+1` | first reserve not already killed |
| `s` | least certified safe reserve |

A lower packet is prize-frontier relevant only if its leave-one-out removal lowers \(f\). An upper theorem is frontier relevant only if its removal raises \(s\) or if it closes a currently open budget inequality at \(c\).

## 21. Bankable versus conditional

### Bankable

- exact MCA and list numerator definitions;
- objective-dependent denominator rule and mandatory `T_q_code` reporting;
- integer reserve, agreement, error-budget, and radius staircase;
- monotonic lower/upper propagation;
- the checker soundness theorem;
- core unit, zero-radius, tangent, support-union, support-injective, and unique-decoding bounds;
- typed `sum`/`max` aggregation and top-level alternative-program minimum;
- exact unresolved-budget normal form;
- leave-one-out frontier relevance;
- rejection of asymptotics, floating arithmetic, and field conflation.

### Conditional or externally supplied

- every nontrivial scalar apolar/GJ local-limit upper;
- every MCA occupancy, quotient, envelope, residual, high-denominator, or aperiodic upper;
- generated-field minimality for a concrete domain unless certified;
- extension-field normalization or projection bridges;
- projective and Lattès packet claims until their dedicated verifiers emit accepted certificates;
- any nontrivial exact first-safe reserve not already forced by the core programs.

## 22. Failure point and next exact construction

The checker wall closes. The prize wall does not.

The first mathematical failure point exposed by this checker will be the candidate reserve

\[
c=f+1,
\]

where all supplied lower mechanisms have stopped certifying failure but no complete finite upper program yet clears `T_decision`. The output at that row is an exact finite system of hole inequalities, not an asymptotic margin.

The implementation artifacts should be:

```text
experimental/scripts/rs_prize_frontier_v1.py
experimental/schemas/rs_prize_frontier_v1.schema.json
experimental/certificates/trusted_theorems_v1.json
```

with adapters for:

```text
L-LIST-MINIMAL-CI-GJ-FIBER
W-LIST-MODEL-GJ-QUOTIENT-CONDITIONED-LOCAL-LIMIT
L-JR-T1-GJ-FIBER-AND-COLOR
V-PROJECTIVE-SUBLINE-M-EQUAL-SIGMA
V-LATTES-31
```

## 23. Route to a full solve

Yes, there is a coherent route, but the checker is only the exact accounting layer. The next decisive lemma is a **finite quotient-conditioned generalized-Jacobian upper theorem for the full scalar sparse-syndrome fiber**, with explicit integer constants and all error-weight layers covered. Its output must be a registered table/program at the candidate reserve \(c\). Together with the already required strict lower witness at \(c-1\), the checker then converts the theorem mechanically into the exact first safe reserve, the largest safe grid radius, the supremal transition radius, and the correct endpoint convention.
