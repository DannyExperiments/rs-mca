# Agents Log

This file is the working ledger for agent-created material in `experimental/`.
Use it to record every new note, script, scan, formalization stub, or audit before
the material is promoted into `tex/` or `scripts/`.

The log is not a proof-status authority. It is a coordination record: what was
added, why it might matter, and what a human or later agent should check next.
Keep entries concise and link to the relevant files.

## Entry Format

```markdown
### YYYY-MM-DD - Short title

- **Agent/model:** Name the agent or model, for example `GPT-5.5 Pro`,
  `Claude Fable 5`, or `Codex`.
- **Files added or changed:** List paths under `experimental/`, `tex/`,
  or `scripts/`.
- **Status:** PROVED / CONDITIONAL / CONJECTURAL / EXPERIMENTAL / AUDIT /
  COUNTEREXAMPLE.
- **What is being added:** State the claim, note, scan, script, or certificate
  in one or two sentences.
- **How it is useful:** Say which paper, theorem, problem, ledger, or toy case
  the material supports.
- **What to do next:** Give the next verification, cleanup, proof step,
  experiment, or promotion decision.
```

## Entries

### 2026-06-18 - Codex F1/L1 audit dump

- **Agent/model:** Codex, auditing 5.5 Pro and Opus 4.8 outputs.
- **Files added or changed:** `experimental/2026-06-17-codex-f1-l1-audit/`
  with `context/`, `audits/`, `raw/`, and `verifiers/`.
- **Status:** COUNTEREXAMPLE / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** A companion audit bundle for the RS-MCA / Proximity
  Prize project. It records: counterexamples to the unrestricted same-numerator
  extension-line MCA lift; the raw arbitrary `Fib_U` locator-fiber overcount;
  fixed-rate and residual-slack F1 reductions; balanced-denominator CRT/base-core
  reductions for monic-anchor data; and the still-conditional status of the
  Paper D universal cap import.
- **How it is useful:** Supports `snarks_v4.tex` `ass:extension-mca-lift` /
  `op:extension-mca`, `proximity_blueprint_v3.tex` `prob:F1`, and
  `slackMCA_v3.tex` `conj:arbitrary-local`, `conj:final-locator`, and
  `thm:normalform`. The verifiers reproduce the finite F1/L1 packets without
  external dependencies.
- **What to do next:** Human/agent review should first check the arbitrary-anchor
  balanced-denominator gap: decide whether arbitrary anchors in `def:residue`
  reduce to the `hatE=lcm(E,E^tau)` base-field readout, or produce a finite
  balanced extension counterexample. Separately, complete the Crites-Stewart /
  ABF import audit before promoting Paper D's cap from CONDITIONAL.
