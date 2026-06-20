#!/usr/bin/env python3
"""Cycle 73 prime-field slot polynomial and norm-bucket self-check.

This is deliberately bounded: it checks the new Cycle 73 algebraic identities
against the already banked Cycle 68 arithmetic table on all 336 slot values,
but it does not attempt the expensive k=3/k=4 ladder.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
CYCLE68_PATH = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"

E_SETS = {
    1: {0, 1, 2, 3, 5, 11, 12, 13},
    2: {0, 1, 2, 3, 4, 8, 9, 14},
    3: {0, 1, 2, 4, 5, 7, 11, 14},
}


def load_cycle68():
    spec = importlib.util.spec_from_file_location("cycle68_checker", CYCLE68_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    c68 = load_cycle68()
    f = c68.find_field_poly()
    eta = c68.find_eta(f)
    beta = c68.find_beta(f)
    xi = c68.fpow(beta, 2, f)
    einv = c68.fpow(eta, c68.N - 1, f)
    table = c68.build_u(f, eta, beta)

    assert c68.fpow(eta, 16, f) == c68.emb(3)

    first_false_collapse = None
    prime_identity_checked = 0
    false_collapse_mismatch_count = 0
    for t in range(1, 8):
        yt = c68.fmul(xi, c68.fpow(einv, 2 * t, f), f)
        for i in (1, 2, 3):
            for a in range(16):
                prime_form = c68.ONE
                false_form = c68.ONE
                for e in E_SETS[i]:
                    c = c68.emb(pow(3, (a + e) % 16, c68.P))
                    prime_form = c68.fmul(prime_form, c68.psub(yt, c), f)
                    false_form = c68.fmul(false_form, c68.psub(xi, c), f)
                assert prime_form == table[(t, i, a)], (t, i, a)
                prime_identity_checked += 1
                if false_form != prime_form:
                    false_collapse_mismatch_count += 1
                    if first_false_collapse is None:
                        first_false_collapse = {"t": t, "i": i, "a": a}

    assert first_false_collapse == {"t": 1, "i": 1, "a": 0}

    norm_exp = c68.N // 16

    def norm17(v):
        nv = c68.fpow(v, norm_exp, f)
        return nv[0] if nv else 0

    # Bounded homomorphism spot-check across all adjacent slot pairs.
    norm_pairs_checked = 0
    for t in range(1, 7):
        for key in range(48):
            v = table[(t, key // 16 + 1, key % 16)]
            w = table[(t + 1, key // 16 + 1, key % 16)]
            prod = c68.fmul(v, w, f)
            assert norm17(prod) == (norm17(v) * norm17(w)) % c68.P
            norm_pairs_checked += 1

    cert = {
        "model": {
            "field_poly": list(f),
            "eta": list(eta),
            "beta": list(beta),
        },
        "eta16_equals_3": True,
        "prime_field_slot_identity_all_336": True,
        "prime_identity_checked": prime_identity_checked,
        "false_collapse_fails_at": first_false_collapse,
        "false_collapse_mismatch_count": false_collapse_mismatch_count,
        "norm17_homomorphism_adjacent_pair_checks": norm_pairs_checked,
        "decision": "CYCLE73_PRIME_SLOT_NORM_SELFCHECK_PASS",
    }
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

