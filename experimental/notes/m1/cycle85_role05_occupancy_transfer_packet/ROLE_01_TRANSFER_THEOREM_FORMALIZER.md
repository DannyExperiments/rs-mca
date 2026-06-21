# ROLE 01: Transfer Theorem Formalizer

Your job is to prove or correct:

```text
L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER
```

Starting from the Cycle62 Role05 support-plus-color theorem and the Cycle65-68
factorization, state the exact theorem that converts:

```text
Occ(beta)=#{rho_beta(T): T in P_0}=52,747,567,092
```

into an MCA numerator lower certificate or thickened-color lower certificate.

Required:

1. Define the domain, code, reserve, `t=1` normal form, `Delta`, `Delta^+`,
   support family `P_0`, and color map.
2. Prove exactly when distinct occupied `rho_beta(T)` values give distinct MCA
   slopes.
3. State all side conditions: nonzero direction, transversality,
   full-coordinate supports, noncontainment, denominator/reducedness, quotient
   exceptions, and field of slopes.
4. Decide whether the theorem is already prize-relevant or only model-level.
5. Output the exact strongest bankable statement.

If the transfer theorem needs a correction, give the corrected theorem and the
minimal missing lemma.
