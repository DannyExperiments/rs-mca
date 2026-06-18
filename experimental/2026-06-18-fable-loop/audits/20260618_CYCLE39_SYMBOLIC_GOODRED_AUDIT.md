# Cycle 39 Symbolic Good-Reduction Audit

Status: PROOF / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Harness status: clean `artifact_stream` run. The mathematical answer is
preserved in `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RESPONSE.md`; raw
provider receipts are preserved separately and terminal/ad text is not involved.

Source artifacts:

- `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RESPONSE.md`
- `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RAW.json`
- `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RAW.jsonl`
- `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RUN_RESULT.json`
- `local_checks/20260618_cycle39_locator_collapse_verify.py`
- `local_checks/20260618_cycle39_locator_collapse_verify_result.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`, with `alpha^2 = -1`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n = p`.
- Restricted regime: `t = sigma = 2`, `j = n-a = r-t = 4`.
- Candidate family: primes `p = 3 mod 4`, `E=X^2+alpha X+1`, `b=X`,
  `u=[W]_E=1+X`, and top free data
  `W_{n-1..n-4}=1, alpha, 1+alpha, 1`.

This remains a restricted residue-line / surface-monodromy branch. It is not
a corrected-reserve theorem, MCA claim, list-decoding claim, CA claim,
line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, prize
solution, or `COUNTERPACKET`.

## Banked Locator-Collapse Lemma

Cycle 39 proves the following restricted lemma.

Let `p = 3 mod 4`, `p != 5`, `B=F_p`,
`F=F_{p^2}=B(alpha)` with `alpha^2=-1`, and
`E=X^2+alpha X+1`. In `A=F[X]/(E)`, put `b=[X]_E` and

```text
ell = [X^p - X]_E.
```

Then:

```text
ell = alpha*1_A    if (-5/p)=+1,
ell = -2*b         if (-5/p)=-1.
```

Equivalently, since `p=3 mod 4`:

```text
Subcase A: p = 2,3 mod 5, ell = alpha.
Subcase B: p = 1,4 mod 5, ell = -2X.
```

Proof sketch, audited by Codex:

1. `disc(E)=alpha^2-4=-5`. For `p != 5`, `E` is separable.
2. Every element of `F_p^*` is a square in `F_{p^2}^*`, so `E` splits in
   `F` and `A ~= F x F`.
3. At a root `rho`, `ell(rho)=rho^p-rho`.
4. Frobenius fixes `B=F_p` and sends `alpha` to `-alpha` because
   `p=3 mod 4`.
5. If `sqrt(-5) in F_p`, both roots have imaginary part `-1/2`, so
   `rho^p-rho=alpha`.
6. If `sqrt(-5) notin F_p`, each root is purely `alpha`-imaginary, so
   `rho^p-rho=-2rho`, hence `ell=-2b`.

Codex added a finite sanity checker, not as proof but as a regression guard,
and verified the formula on sample primes from both subcases:

```text
python3 experimental/2026-06-18-fable-loop/local_checks/20260618_cycle39_locator_collapse_verify.py
```

The output has `all_ok=true`.

## Route Consequence

Before Cycle 39, the obstruction was that `[X^p-X]_E` seemed to make the
quartic surface family genuinely `p`-dependent, so a finite `p=31` certificate
could not obviously globalize.

Cycle 39 removes that obstruction. Inside each subcase, `ell` is fixed:

- Subcase A uses `ell=alpha`.
- Subcase B uses `ell=-2X`.

Thus the equations

```text
G(z,tau)=(u-z*b)*lambda(tau)-ell*[Q_S(tau)]_E=0
```

define a fixed two-dimensional `B`-surface model per subcase. The remaining
good-reduction/monodromy question is no longer moving with `p`.

Cycle 39 also correctly observes that the existing `p=31` certificate lies
only in Subcase B, since `31 = 1 mod 5` and hence `(-5/31)=-1`. It gives no
direct certificate for Subcase A.

## Exact New Wall

The live wall is:

```text
W-F1-AA-RES-T2J4-A2B-S4-GOODRED-SUBCASE
```

The next theorem-sized target is to prove, separately for `ell=alpha` and
`ell=-2X`, at least one of:

1. a symbolic characteristic-zero certificate over `Q(i)(z0,z1)`:
   geometric irreducibility of the quartic, irreducibility of the cubic
   resolvent, and nonconstant squarefree discriminant part;
2. an explicit good-reduction certificate at one small prime per subcase,
   proving that the branch divisor remains etale, `Delta` keeps its degree,
   and the quartic cover remains separable;
3. a finite-place `S_4` certificate for Subcase A, analogous to the Cycle 38
   `p=31` Subcase B certificate;
4. a `ROUTE_CUT` showing that one subcase is reducible, trapped in `A_4`, or
   otherwise cannot yield the intended restricted seed.

If the good-reduction bridge is proved in each subcase, the finite-place
monodromy certificate can potentially globalize to all but finitely many good
primes in that subcase. That still would be only a restricted local
counterpacket seed until the source-to-prize implications are separately
proved.

## What Is Not Banked

Do not bank:

- a full solution or disproof of the Proximity Prize;
- a proof of corrected-reserve RS-MCA;
- a `COUNTERPACKET`;
- a uniform growing-prime `Theta(q_line)` theorem;
- Subcase A monodromy;
- good reduction at `p=31`;
- geometric `S_4` over `Q(i)(z0,z1)` for either subcase;
- an MCA, CA, list-decoding, line-decoding, curve-MCA, protocol, or SNARK
  statement;
- any merge of `q_gen=p` with `q_line=p^2`.

## Cycle 40 Direction

Ask the next worker to attack:

```text
W-F1-AA-RES-T2J4-A2B-S4-GOODRED-SUBCASE
```

The highest-value route is a subcase-separated certificate:

- prove/compute Subcase A (`ell=alpha`) at `p=7`, `23`, `43`, or `47`;
- prove/compute Subcase B (`ell=-2X`) at `p=11`, `19`, `31`, or `59`;
- write symbolic `Delta`/discriminant/resolvent data over `Q(i)(z0,z1)` if
  feasible;
- otherwise identify the exact obstruction below this wall.
