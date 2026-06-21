# ROLE 06: Transverse Slope Auditor

Audit the final MCA interpretation.

The finite count is about occupied products:

```text
rho_beta(T)=prod_{x in T}(beta-x).
```

The MCA numerator counts bad slopes on an affine syndrome line, excluding
contained incidences.

Your job:

1. Construct the explicit syndrome line or t=1 residue line associated with
   the Role05 packet.
2. For every occupied color/product, identify the corresponding slope.
3. Prove the slope map is injective on occupied products, or give the exact
   multiplicity loss.
4. Prove transversality/noncontainment for these witnesses.
5. Prove there is no hidden same-witness or common-envelope collapse that
   reduces the slope numerator.
6. State the exact MCA lower numerator obtained.

If the count only gives thickened-color occupancy but not slopes, state the
missing lemma precisely.
