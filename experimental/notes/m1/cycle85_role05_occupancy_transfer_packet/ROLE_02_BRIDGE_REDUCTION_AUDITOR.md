# ROLE 02: Bridge Reduction Auditor

Red-team the bridge:

```text
Cycle62 Role05 theorem
  -> Cycle65 thickened product model
  -> Cycle66 locator evaluation
  -> Cycle67 multiplicity lower bound
  -> Cycle84 public m_max=2 certificate
  -> Cycle85 occupancy transfer
```

Your job is to find the weakest link.

Check:

1. Does `rho_beta(T)` really coincide with the `Delta^+` lift/color used by
   Role05?
2. Does same `rho_beta(T)` exactly mean same slope, or only same reduced color
   up to affine normalization?
3. Are all supports full-coordinate and admissible?
4. Is noncontainment automatic or does it need a separate witness?
5. Is the external point `beta=X+2` outside the support/domain in the required
   sense?
6. Is the Cycle84 product set counted in the same field as the MCA slope line?
7. Does quotient/periodic structure absorb this packet into an exception
   rather than a new obstruction?

Return either:

```text
BANKABLE_LEMMA
```

with a clean audited bridge, or:

```text
COUNTERPACKET / ROUTE_CUT
```

with the exact failed implication.
