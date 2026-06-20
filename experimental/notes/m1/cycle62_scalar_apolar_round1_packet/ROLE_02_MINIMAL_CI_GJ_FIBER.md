# ROLE 02 - Minimal Scalar Generalized-Jacobian Formalizer

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
L-LIST-MINIMAL-CI-GJ-FIBER
```

## Objective

Prove or kill the next exact lemma selected by the Master Referee.

Let

```text
C = RS[F,L,k],   r=n-k,   j=r-sigma,
I_s=(A,B),
deg A=sigma+1,
deg B=j>sigma+1,
gcd(A,B)=1,
Delta=V(A).
```

Choose a linear form `L_*` nonvanishing on `Delta`, define

```text
G_Delta = H^0(Delta,O_Delta)^*/F^*,
alpha_Delta(x) = [(L_x/L_*)|_Delta],
b_Delta = [(B/L_*^j)|_Delta],
```

and prove the exact equivalence:

```text
T in binom(L,j) is a full-coordinate representation of s
iff
T cap Supp(Delta)=empty
and product_{x in T} alpha_Delta(x)=b_Delta in G_Delta.
```

Also prove:

- the only full-coordinate listed locator of degree `< j` is `A`, when `A`
  is monic, squarefree, and fully `L`-split;
- the exact count
  `N_s(sigma)=1_{A squarefree L-split}+N_{Delta,j}(b_Delta)`;
- the effective subgroup `G_eff` and exact finite Fourier expansion over it;
- independence of `L_*`;
- invariance under admissible generator shear `B -> cB + AC`.

## Success Criteria

Output `BANKABLE_LEMMA` with a complete proof and exact finite formulas.

## Failure Criteria

Output `COUNTERPACKET` if an explicit complete intersection has a list count
different from the generalized-Jacobian fiber count.

