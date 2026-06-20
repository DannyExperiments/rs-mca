# ROLE 06 - Exact Frontier And Certificate Ledger

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
RS-PRIZE-FRONTIER-V1
```

## Objective

Design the exact code-specific finite scanner. Do not prove a theorem; define
the checker precisely enough that it can be implemented without ambiguity.

It must keep separate:

```text
q_gen
q_line
q_code
q_chal
```

and it must refuse to mark any radius safe from asymptotic language such as
`n^{1+o(1)}`.

## Required Input Contract

Specify JSON input containing at least:

```json
{
  "code_id": "...",
  "n": "...",
  "k": "...",
  "domain_descriptor": "...",
  "q_gen": "...",
  "q_line": "...",
  "q_code": "...",
  "q_chal": "...",
  "reserve_range": ["..."],
  "certified_lower_terms": ["..."],
  "certified_upper_terms": ["..."],
  "conditional_terms": ["..."]
}
```

## Required Output Contract

For each reserve output:

- `j`;
- exact target `T_q=floor(q_code/2^128)`;
- exact lower maximum;
- exact proved upper total;
- unresolved budget;
- safe/fail/unknown;
- assumption flags;
- both radius conventions.

## Success Criteria

Output `AUDIT` with a complete spec and pseudocode strong enough for a direct
implementation.

## Failure Criteria

Output `ROUTE_CUT` if the current repo lacks enough finite definitions to make
the checker meaningful.

