#!/usr/bin/env python3
"""Cycle 70 slot-value normalization checker.

This imports the Cycle 68 checker, tests the Cycle 70 normalization claims,
and optionally reruns the product-injectivity ladder. The worker's strongest
claimed collapse

    u_t(i,a) = prod_{c in 3^a D_i}(beta^2-c)

is false; the script records the first counterexample. The surviving corrected
identity is the Cycle 68 t-dependent polynomial-evaluation formula.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--kmax", type=int, default=2)
    args = parser.parse_args()
    if args.kmax < 1 or args.kmax > 4:
        raise SystemExit("--kmax must be between 1 and 4")

    c68 = load_cycle68()
    f = c68.find_field_poly()
    eta = c68.find_eta(f)
    beta = c68.find_beta(f)
    table = c68.build_u(f, eta, beta)
    xi = c68.fpow(beta, 2, f)

    def emb(c: int):
        return c68.emb(c % c68.P)

    false_collapse_counterexample = None
    false_collapse_checks_before_failure = 0
    corrected_identity_checks = 0
    einv = c68.fpow(eta, c68.N - 1, f)
    for t in range(1, 8):
        for i in (1, 2, 3):
            for a in range(16):
                prod = c68.ONE
                for e in E_SETS[i]:
                    scalar = pow(3, (a + e) % 16, c68.P)
                    prod = c68.fmul(prod, c68.psub(xi, emb(scalar)), f)
                if prod != table[(t, i, a)] and false_collapse_counterexample is None:
                    false_collapse_counterexample = {
                        "t": t,
                        "i": i,
                        "a": a,
                        "claimed_value": list(prod),
                        "actual_table_value": list(table[(t, i, a)]),
                    }
                if false_collapse_counterexample is None:
                    false_collapse_checks_before_failure += 1

                arg = c68.fmul(
                    c68.fmul(xi, emb(pow(3, (-a) % 16, c68.P)), f),
                    c68.fpow(einv, 2 * t, f),
                    f,
                )
                corrected = c68.peval(i, arg, f)
                if a & 1:
                    corrected = c68.psub((), corrected)
                assert corrected == table[(t, i, a)], (t, i, a, corrected, table[(t, i, a)])
                corrected_identity_checks += 1

    def u_value(t, key):
        i = key // 16 + 1
        a = key % 16
        return table[(t, i, a)]

    ladder = []
    first_collision = None
    for k in range(1, args.kmax + 1):
        ok = True
        for slots in itertools.combinations(range(1, 8), k):
            seen = {}
            for keys in itertools.product(range(48), repeat=k):
                prod = c68.ONE
                for t, key in zip(slots, keys):
                    prod = c68.fmul(prod, u_value(t, key), f)
                if prod in seen:
                    ok = False
                    first_collision = {
                        "k": k,
                        "slots": list(slots),
                        "keys_a": list(seen[prod]),
                        "keys_b": list(keys),
                        "value": list(prod),
                    }
                    break
                seen[prod] = keys
            if not ok:
                break
        ladder.append({"k": k, "product_injective": ok})
        if not ok:
            break

    max_good = 0
    for row in ladder:
        if row["product_injective"]:
            max_good = row["k"]

    cert = {
        "model": {
            "field_poly": list(f),
            "eta": list(eta),
            "beta": list(beta),
        },
        "false_collapse_counterexample": false_collapse_counterexample,
        "false_collapse_checks_before_failure": false_collapse_checks_before_failure,
        "false_claim": "u_t(i,a)=prod_{c in 3^a D_i}(beta^2-c)",
        "corrected_identity_checks": corrected_identity_checks,
        "corrected_identity": "u_t(i,a)=(-1)^a Q_i(beta^2 eta^(-2t) 3^(-a))",
        "ladder": ladder,
        "max_good_k": max_good,
        "min_collision_support_if_no_failure": max_good + 1,
        "first_collision": first_collision,
        "decision": (
            "CORRECTED_IDENTITY_AND_LADDER_PROBE_PASSED_TO_KMAX"
            if first_collision is None
            else "PARTIAL_COLLISION_FOUND"
        ),
    }
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
