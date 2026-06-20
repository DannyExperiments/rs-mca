#!/usr/bin/env python3
"""Cycle 69 injectivity-ladder probe.

This reuses the Cycle 68 slot-factorization checker to test the product
injectivity ladder suggested by Cycle 69. The default kmax is 2, which is a
small local proof-of-pipeline run. k=3 is already slow in pure Python on this
machine, and k=4 should be run only in compiled or specially optimized form.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
CYCLE68_PATH = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"


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
        raise SystemExit("--kmax must be between 1 and 4 for this Python probe")

    c68 = load_cycle68()
    f = c68.find_field_poly()
    eta = c68.find_eta(f)
    beta = c68.find_beta(f)
    table = c68.build_u(f, eta, beta)
    xi = c68.fpow(beta, 2, f)
    eta_pows = [c68.fpow(eta, j, f) for j in range(256)]

    def bset(i, a):
        return frozenset((a + e) % 16 for e in c68.E_SETS[i])

    def slot_product(t, b_set):
        r = c68.ONE
        for b in b_set:
            r = c68.fmul(r, c68.psub(xi, eta_pows[(2 * t + 16 * b) % 256]), f)
        return r

    # Complement oracle on all 48 table sets in each slot.
    complement_checks = 0
    all_b = frozenset(range(16))
    for t in range(1, 8):
        full = c68.psub(c68.fpow(beta, 32, f), c68.emb(pow(3, 2 * t, c68.P)))
        for i in (1, 2, 3):
            for a in range(16):
                b = bset(i, a)
                bc = frozenset(all_b - b)
                assert c68.fmul(slot_product(t, b), slot_product(t, bc), f) == full
                complement_checks += 1

    def u_value(t, k):
        i = k // 16 + 1
        a = k % 16
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
        "complement_oracle_checks": complement_checks,
        "ladder": ladder,
        "max_good_k": max_good,
        "min_collision_support_if_no_failure": max_good + 1,
        "first_collision": first_collision,
        "decision": (
            "LADDER_PROBE_PASSED_TO_KMAX"
            if first_collision is None
            else "PARTIAL_COLLISION_FOUND"
        ),
    }
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
