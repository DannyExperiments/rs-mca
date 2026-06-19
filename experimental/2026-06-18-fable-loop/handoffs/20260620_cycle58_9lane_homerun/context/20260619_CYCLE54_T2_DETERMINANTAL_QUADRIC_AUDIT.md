# Cycle 54 t=2 Determinantal Quadric Audit

Status: `BANKABLE_LEMMA / PROOF / ROUTE_CUT / EXACT_NEW_WALL / AUDIT`.

Raw run:

- `raw/cycle54_t2_slope_summed_cosupport_cancellation/response.md`
- `raw/cycle54_t2_slope_summed_cosupport_cancellation/raw_response.jsonl`
- `raw/cycle54_t2_slope_summed_cosupport_cancellation/raw_response.json`
- `raw/cycle54_t2_slope_summed_cosupport_cancellation/run_result.json`
- `raw/cycle54_t2_slope_summed_cosupport_cancellation/input_manifest.json`
- `raw/cycle54_t2_slope_summed_cosupport_cancellation/prompt_sent.md`

Harness note: `run_result.json` reports `OK`, no capture warning, and no
`output_files/`.

## Verdict

Cycle 54 does not prove the full `Err<=O(j)` cancellation theorem and does not
produce a counterpacket. It does bank a sharper `t=2` normal form and a complete
proof of the `j=1` subcase.

The worker's top-line classification is accepted conservatively:

```text
BANKABLE_LEMMA + PROOF(j=1 subcase) + ROUTE_CUT + EXACT_NEW_WALL
```

## Bankable Lemma: t=2 z-Eliminated Determinant

For `t=2`, the Hankel matrix is `2 x (j+1)`. With

```text
a(T)=H(u)ell_T,
b(T)=H(v)ell_T,
```

the transverse landing condition is exactly

```text
b(T) != 0,
D(T):=a_0(T)b_1(T)-a_1(T)b_0(T)=0.
```

Every such `T` lands at a unique slope, so

```text
R(u,v)=#{T split : D(T)=0, b(T)!=0}.
```

Expanding in locator coefficients gives the canonical quadratic form

```text
D(T)=sum_{l,l'=0}^j kappa_{l,l'} (ell_T)_l (ell_T)_{l'},
kappa_{l,l'}=u_l v_{l'+1}-u_{l+1}v_{l'}.
```

Thus in `t=2` the Cycle53 slope-summed character wall is equivalent to counting
fully `L`-split locators on one explicit determinantal quadric.

## Bankable Proof: j=1

For `j=1`, write `T={x}` and `ell_T=(-x,1)`. Then

```text
D(x)=M_01 x^2 - M_02 x + M_12,
M_ij=u_i v_j-u_j v_i.
```

Under transversality, not all `M_01,M_02,M_12` vanish, so `D` is a nonzero
polynomial of degree at most two. Hence

```text
R(u,v)<=2=2j=O(j).
```

This is a complete deterministic per-line landing bound in the first subcase,
without random anchors, L2 anticollision, or monodromy.

## Route Cut / Correction

Cycle53's closing simplification that the `t=2` phase is a single
elementary-symmetric `e_j` sum is not correct in general. The phase is

```text
<y,H(u+zv)ell_T>
= sum_{l=0}^j (y_0 w_l(z)+y_1 w_{l+1}(z))(ell_T)_l,
```

so it generally involves all elementary-symmetric coordinates
`e_1(T),...,e_j(T)`. A one-variable Gauss/Kloosterman reduction is available
only on degenerate slices or in the `j=1` case.

## Exact New Wall

Cycle54 refines the active subwall to:

```text
W-MCA-T2-DETERMINANTAL-QUADRIC-SPLIT-COUNT
```

Statement:

```text
For L=mu_n, transverse balanced (u,v), and no proper low d_M(E)
quotient-action-rank defect, prove

#{T in binom(L,j) : D(T)=0, b(T)!=0}
<= ceil(binomial(n,j)/Q)+O(j),

after removing mu_M-coset-union quotient packets.
```

This is proved for `j=1`; it remains open for `j>=2`.

## Next Exact Target

The smallest open case is:

```text
W-MCA-T2J2-DETERMINANTAL-CONIC-SPLIT-PAIR-COUNT
```

For `T={s,s'}`, `D(T)` becomes a quadratic form in

```text
e_1=s+s',
e_2=ss'.
```

The next lemma should prove or refute:

```text
#{ {s,s'} subset L : D(s+s',ss')=0 }
<= binomial(n,2)/Q + O(1)
```

after removing quotient/imprimitive pairs. This is the first genuinely open
deterministic cancellation problem below the Cycle53 wall.

## Audit Notes

The inline checker in the response is useful as a specification, but it was not
executed by the theorem worker and should not be treated as verified code. If
used later, it should be cleaned and run locally before becoming a banked
checker artifact.

Do not promote this cycle to:

- a full `Err<=O(j)` theorem;
- a full scalar MCA upper theorem;
- a prize-level threshold formula.
