# Cycle 37 Prompt: Single-Prime S4 Certificate For The Explicit A2_B Family

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA / Proximity Prize Fable loop as a skeptical
mathematical co-director. Work only from mounted repository/context files. Do
not use web access. Keep these ledgers separate:

- `q_gen = p`
- `B = F_p`
- `F = F_{p^2}=B(alpha)`
- `q_line = |F| = p^2`
- `q_chal` unused

Do not promote anything to corrected-reserve, MCA, CA, list-decoding,
line-decoding, curve-MCA, protocol, SNARK, or prize status.

## Current Wall

```text
W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT
```

Restricted branch:

- `D=F_p`, `n=p`;
- `t=sigma=2`, `j=n-a=r-t=4`;
- off `R0`;
- explicit Cycle 36 family:

```text
nr=-1
p = 3 mod 4
alpha^2=-1
E=X^2+alpha X+1
b=[Bnum]_E=X
```

Source-valid denominator checks are banked in Cycle 36: no roots on `F_p`,
separated from `E^tau`, and `c_b != 0`. The remaining free data must be chosen
so `kappa != 0`.

## Source Context To Read First

Read these files before answering:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_BASE_FIELD_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE35_A2B_GEOMETRIC_S4_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE36_A2B_UNIFORM_S4_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`

Use `.tex` files only if you need to check a source definition or hypothesis.

## Correction To Enforce

Do not use the invalid shortcut

```text
resolvent irreducible + nonsquare discriminant ==> S_4
```

unless quartic transitivity/geometric irreducibility is also certified. A
finite-place factorization type `"4"` is an acceptable transitivity witness;
types `"4"` and `"13"` together are ideal.

## The Task

Produce a reproducible single-prime certificate for the explicit family, or
explain exactly why it fails.

Preferred prime: `p0=31` or another small prime with `p0 = 3 mod 4`.

Preferred deliverables if tool access permits writing files:

- `output_files/cycle37_single_prime_s4_cert.py`
- `output_files/cycle37_single_prime_s4_cert.md`

Use pure Python if feasible. Do not install dependencies. If a dependency such
as Sage or Sympy would be needed, write a precise checker spec instead of
pretending it ran.

Certificate requirements:

1. Choose fixed remaining free data `(u,W_{n-1},...,W_{n-4})` with `kappa != 0`
   and state it explicitly.
2. Build the `B`-linear system `M(z) tau = -C_0(z)` for
   `z=z_0+alpha z_1` in the Cycle 29/30/32 notation.
3. Restrict to a generic line `z_1=m z_0+e` with fixed `m,e in B`.
4. Compute `Delta=det_B M(z)` and check it is nonzero with the expected
   source-valid top-symbol behavior.
5. Compute `tau(z)=M(z)^(-1)(-C_0(z))` and
   `L_tau(X)=X^4-tau_1 X^3+tau_2 X^2-tau_3 X+tau_4`.
6. Certify quartic transitivity/geometric irreducibility, preferably by an
   unramified finite-place factorization type `"4"`.
7. Certify the cubic resolvent is absolutely irreducible, or provide
   finite-place data that forces the same monodromy conclusion.
8. Certify the discriminant numerator has nonconstant squarefree part /
   nonsquare behavior.
9. Record every bad denominator, singular place, repeated-root exclusion, and
   source-validity gate.

Classification rules:

- If the certificate is complete and source-valid, label it `BANKABLE_LEMMA`
  or `PROOF` only for the restricted local certificate, not for MCA/protocol.
- If it gives an actual local positive-density restricted seed, label it a
  conditional `COUNTERPACKET` seed only if all dependencies are explicit.
- If it fails, label the precise failure `ROUTE_CUT` or `EXACT_NEW_WALL`.
- If it is only a checker specification or unrun code, label it `EXPERIMENTAL`
  / `AUDIT`.

End by answering:

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
