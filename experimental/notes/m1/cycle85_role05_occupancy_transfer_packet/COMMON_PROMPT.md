# COMMON PROMPT FOR CYCLE 85

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

You are working on the RS-MCA / proximity-prize finite obstruction route. You
are not brainstorming from scratch. You are adjudicating the exact transfer
wall after Cycle84.

Read the attached context first, especially:

```text
CYCLE85_CURRENT_STATE.md
cycle84_github_replay_receipt.md
m1_cycle84_wallbreaker_returns_audit.md
m1_cycle68_collision_multiplicity_audit.md
m1_cycle67_cross_color_injectivity_audit.md
m1_cycle66_sevenfold_product_occupancy_audit.md
m1_cycle65_thickened_gadget_color_audit.md
cycle62_round1_raw/05_role05_t1_mca_gj_color_result.md
cycle62_round1_raw/06_role06_frontier_checker_ledger.md
cycle63_round2_raw/06_role06_frontier_checker_implementation.md
```

## Current Target

The active target is:

```text
L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER
```

The public Cycle84 replay proves, for the explicit seven-slot model:

```text
m_max(beta)=2
Occ(beta)=52,747,567,092
D=24
```

The question is no longer whether the finite product count is large. It is.
The question is what exact theorem, ledger entry, or counterpacket follows from
that count.

## Non-Negotiable Distinctions

Keep separate:

```text
finite model certificate
official prize counterpacket
MCA numerator lower certificate
scalar-list numerator
q_gen / q_line / q_code / q_chal
T_line = floor(q_line / 2^128)
T_code = floor(q_code / 2^128)
the informal comparison Occ(beta)>2^32
```

Do not claim a prize-level result unless all finite-frontier normalization,
field, reserve, and transfer hypotheses are proved.

## Output Rules

Start your answer with one label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. executive verdict and confidence;
2. exact theorem/counterpacket/checker statement;
3. proof or construction;
4. verification requirements;
5. next exact lemma or construction.

Do not return broad strategy without an exact target. Do not rerun the old
MITM wall unless your role explicitly requires auditing the public replay.

If you write code, it must be self-contained, deterministic, and accompanied by
the exact certificate it should emit. If you cannot run code, mark it `UNRUN`.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
