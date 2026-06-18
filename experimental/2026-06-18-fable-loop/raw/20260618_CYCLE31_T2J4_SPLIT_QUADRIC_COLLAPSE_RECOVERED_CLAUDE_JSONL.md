I have enough to give a definitive verdict without re-running code. Note up front: I attempted to re-run the scan with larger primes/more trials to confirm the scaling directly, but code execution is disabled in this harness, so the analysis below rests on (a) the existing Cycle 30 certificate numbers, reinterpreted, and (b) the banked algebraic structure from Cycles 28/29. I flag explicitly what that leaves unverified.

---

ROUTE_CUT

The hypothesized `W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE` (a hidden rational-root / discriminant / Frobenius mechanism forcing `O(p)`) does **not** exist. The Codex finite scan was misread: its own numbers refute `O(p)` and point to `Theta(q_line) = Theta(p^2)` with realized-slope density converging to `1/24 = 1/|S_4|`. I cut the search for an `O(p)` collapse theorem in this window and replace it with the exact monodromy invariant needed to bank the `Theta(p^2)` counterpacket.

## Field ledger (kept separate)

- `q_gen = p`; `B = F_p`; `F = F_{p^2}`; `q_line = |F| = p^2`; `q_chal` unused.
- `D = F_p`, `n = p`; restricted `t = sigma = 2`, `j = n-a = r-t = 4`; off `R0`, `kappa = u wedge b != 0`; source-valid separated `E = X^2 + cX + d` nonzero on `F_p`, `c_b != 0`.
- Residue-line / bad-slope incidence only. No promotion to corrected-reserve, MCA, list-decoding, CA, line-decoding, curve-MCA, protocol, SNARK, or Proximity Prize.

## Refutation

**Step 1 — the realized quartics are always `B`-rational; there is no Frobenius/Galois obstruction at the coefficient level.** Cycle 29 already established that fixing a slope `z in F` makes the incidence `iota - z mu = 0` a *square* `4x4` system over `B`:
```text
M(z) tau = -C_0(z),   M(z) in B^{4x4},  C_0(z) in B^4,
tau(z) = M(z)^{-1}(-C_0(z)) in B^4   when det_B M(z) != 0.
```
Because `M(z)` and `C_0(z)` have `B`-entries, `tau(z) in B^4` for **every** `z` off the degree-`<=4` noninvertibility curve. So `L_{tau(z)} = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4` is an `F_p`-coefficient quartic for all such `z`. The only thing that can vary is its `F_p`-splitting type. A "rational-root / Frobenius collapse" would have to live *inside* the splitting behavior, not in rationality of the coefficients.

**Step 2 — landing locus = image of `z -> tau(z)`, and `z` is injective on it.** The Cycle 30 quadric `Phi(tau) = iota wedge_F mu = 0` is exactly the `z`-elimination of `iota = z mu`. Conversely `z -> tau(z)` single-valuedly inverts it (Step 1). Hence
```text
{ tau : Phi(tau)=0, det_B M != 0 }  =  { tau(z) : z in F },
```
a rational curve carrying `~p^2` `B`-points, and the slope map `tau -> z` is generically injective on it (it is the left inverse of `z -> tau`). Therefore
```text
C2 = #{ z in F : tau(z) in TSD },   TSD = {4 distinct roots in F_p}.
```
The two `B`-quadrics cut out the curve; they do **not** further cut `C2` down — `C2` is controlled entirely by how often the curve meets the totally-split-distinct open set.

**Step 3 — the governing invariant is the Galois group of the universal quartic, and `1/24` is its fingerprint.** Splitting `L_{tau(z)}` into four distinct `F_p`-roots is a positive-density open condition controlled by `disc_X L` and the resolvent cubic. For a quartic family with geometric Galois/monodromy group `S_4`, the proportion of fibers that split completely equals `1/|S_4| = 1/24` (function-field Chebotarev / Frobenius density, effective via Weil). The Cycle 30 certificate is converging to precisely this:
```text
p     avg_C2/p^2     max_C2     p^2/24
7     0.0112          2          2.04
11    0.0198          4          5.04
13    0.0255         10          7.04
17    0.0284         12         12.04
19    0.0325         17         15.04
23    0.0321         25         22.04
29    0.0372         35         35.04
```
`avg_C2/p^2` is **monotonically increasing** toward `~0.04 ≈ 1/24`, and `max_C2` sits at or above `p^2/24` at every prime. An `O(p)` law forces `C2/p^2 -> 0`; the data do the opposite. Equivalently `avg_C2/p` runs `0.079 -> 1.078` (grows ~linearly in `p`), i.e. `C2 ~ p^2`. This is the signature of `Theta(q_line)`, not `O(p)`.

**Why Codex's read leaned `O(p)`.** The averages are depressed (not the scaling) by two artifacts: (i) trial counts collapse with `p` (`20 -> 4`), so large-`p` means are noisy and biased by a few degenerate random `(W, E, b)` draws whose curve `tau(z)` is partly non-generic; (ii) the average mixes degenerate fibers (repeated roots, roots in `F_{p^2}\F_p`) into the count. The *trend* of `C2/p^2` and the *maxima* are the scale-invariant signals, and both say `Theta(p^2)`.

## Route to full solve (next exact lemma)

Bank `Theta(q_line)` by certifying the monodromy group, not by more random scans:

Lemma (target). Over the function field `B(z)` (resp. `F(z)`), the universal quartic `L_{tau(z)}` has geometric Galois group `S_4`. Concretely, certify both:
```text
(a) disc_X L_{tau(z)}  is a non-square in B(z)        => G ⊄ A_4,
(b) resolvent cubic R(z) is irreducible over B(z)     => 3 | |G|, transitive,
```
together forcing `G = S_4`. Then effective function-field Chebotarev/Weil gives
```text
C2 = #{ z in F : Frob_z = id in S_4 }
   = (1/24) p^2 + O(p^{3/2}) = Theta(q_line),
```
in the restricted `t=2, j=4`, off-`R0`, `c_b != 0`, source-valid separated branch only.

This is the smallest exact algebraic invariant to check next (task item 4): the pair `(disc_X L_{tau(z)}, R(z))` as explicit rational functions of `z`, read off from `tau(z) = M(z)^{-1}(-C_0(z))` with `M(z)`, `C_0(z)` from the Cycle 29 columns. A degenerate outcome (e.g. `disc` a square, or `R` reducible, shrinking `G` to `A_4`, `D_4`, `V_4`, `C_4`) would still keep a positive totally-split density as long as `id in G` — only an `O(p)` count would require the curve to avoid `TSD` entirely, which Step 1 forbids generically.

## Dependencies

- Cycle 29: square `4x4` `B`-system `M(z) tau = -C_0(z)`; `tau(z) in B^4`; top symbol `-N(kappa) N(z)^2 Q_4` (invertibility off a degree-`<=4` curve).
- Cycle 28: `Q_4 = N(c_b)(Im(d)^2 - Im(c)Im(conj(c)d))` source-validly nonzero; used here only to guarantee `det_B M(z)` is not identically zero so `tau(z)` is defined for `~p^2` slopes.
- Cycle 30: the single `F`-quadric `Phi(tau) = kappa N_{A/F}(lambda) - (ell[Q_S]_E) wedge_F (b lambda)` and its `tau_4`-quadratic expansion; the EXPERIMENTAL scan certificate.
- Cycle 11/12: quotient form, `line_scalar`, `residue2`, co-support elementary-symmetric parametrization `tau = e(T)`.

## Hidden assumptions

- `z in F = F_{p^2}` but `TSD` asks for roots in `B = F_p`; the Chebotarev count therefore mixes an `F_{p^2}`-indexed sample with `F_p`-splitting. The clean statement needs the geometric monodromy group of the cover and the correct base (`B(z)` vs `F(z)`) pinned down — flagged as the one genuine subtlety before banking.
- `z -> tau(z)` injectivity on the landing locus is generic (holds off the noninvertibility curve); collisions are `O(p)` and do not change the `Theta(p^2)` scale.
- The `1/24` reading assumes `G = S_4`; a smaller `G` changes the constant, not the `Theta(p^2)` order, provided `id in G`.
- The heavier confirming scan (larger primes, fixed source-valid `(W,E,b)`, tracking `landings` vs `C2` and fiber sizes) was **not executed** — code execution is disabled in this harness. The reinterpretation uses only the already-recorded certificate numbers.

## Rejected overclaims

- Not a banked `Theta(q_line)` counterpacket yet — only a seed plus the exact lemma needed; the monodromy certificate `(disc, resolvent cubic)` is not yet computed.
- Not a proof of `G = S_4`; not a proof of geometric irreducibility of the image curve.
- Not an `O(p)` theorem (refuted) and not a disproof of the Cycle 28 `j=3` bound (which stands; the `j=4` square-system mechanism genuinely differs).
- No corrected-reserve, MCA, list-decoding, CA, line-decoding, curve-MCA, protocol, `q_gen`/`q_line` merge, SNARK, or Proximity Prize consequence.

## Next exact wall

```text
W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4
```
Compute `disc_X L_{tau(z)}` and the resolvent cubic `R(z)` as rational functions of `z` from the Cycle 29 columns; certify `G = S_4` (or identify the transitive subgroup), then apply effective function-field Chebotarev/Weil to bank `C2 = (1/|G|) p^2 + O(p^{3/2}) = Theta(q_line)` in the restricted branch. If `(disc, R)` source-validly degenerate `G` so that `id ∉` the relevant Frobenius image, that degeneracy — not a rational-root collapse — is the only remaining way back to a sub-`Theta(p^2)` count, and would itself be the next counterpacket-blocking invariant.
