# Cycle 85 Local Director Rubric

This note is for auditing the nine Cycle85 returns. It is not part of the
prompt packet sent to models.

## Immediate Arithmetic Guardrail

For the literal Cycle84 product field:

```text
q = 17^16 = 48,661,191,875,666,868,481
2^128 = 340,282,366,920,938,463,463,374,607,431,768,211,456
floor(17^16 / 2^128) = 0
```

The public Cycle84 replay gives:

```text
Occ(beta) = 52,747,567,092
Occ(beta) - 2^32 = 48,452,599,796
Occ(beta) / 2^32 = 12.281249997206032...
```

Therefore:

```text
Occ(beta)>2^32
```

is not automatically the native finite-prize comparison for the literal field
`F_17^16`. In native MCA mode over `q_line=17^16`, the target
`floor(q_line/2^128)` is zero. That is itself a finite-prize problem for small
fields, but it is not the intended `2^32` threshold comparison.

Any returned answer that treats `2^32` as the native prize threshold must
explain the field normalization or tensor/block construction that makes it so.

## Grading Priorities

### Bankable

Bank an answer if it gives one of:

```text
PROOF: exact transfer from rho_beta occupancy to MCA bad-slope numerator,
       with field and transversality hypotheses stated.

BANKABLE_LEMMA: exact registry/ledger entry that is soundly model-level.

AUDIT: exact field-threshold normalization that prevents overclaiming.

COUNTERPACKET / ROUTE_CUT: precise failed implication in the Cycle62->85 chain.
```

### Not Bankable

Do not bank as theorem-level:

```text
full prize solved
official counterpacket
delta_C^* determined
safe-side upper theorem advanced
```

unless the answer gives exact `q_line`, reserve, support domain, transverse
syndrome line, and native `floor(q_line/2^128)` comparison.

### Likely Correct High-Level Outcome

Current best expectation before the returns:

```text
Cycle84 is a strong finite-model obstruction certificate.
It likely banks a Role05 thickened-color / product-occupancy lower certificate.
Official prize relevance still depends on field normalization and tensor/frontier placement.
```

The most useful next theorem would be:

```text
L-CYCLE85-TRANSFER-WITH-FIELD-LEDGER
```

stating exactly what the public replay certifies and exactly which extra
hypotheses turn it into an official MCA lower/failure certificate.

## Return Intake Checklist

For each of the nine answers, record:

```text
label:
confidence:
does it accept Cycle84 replay? yes/no/with caveat
does it prove rho_beta -> slope injection? yes/no/conditional
does it handle noncontainment/transversality? yes/no/conditional
does it compute q_line and target correctly? yes/no
does it claim official prize relevance? yes/no/conditional
bankable result:
failure point:
next exact lemma:
```

After banking raw answers, synthesize:

```text
1. Consensus.
2. Conflicts.
3. Actual theorem-level progress.
4. Wishful or overclaimed parts.
5. New prompt if needed.
```
