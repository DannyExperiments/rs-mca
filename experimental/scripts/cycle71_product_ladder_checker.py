#!/usr/bin/env python3
"""Cycle 71 product-only ladder checker.

This is a conservative local reference checker. Unlike the Cycle 71 returned
Python sketch, duplicate detection keys only the packed field product, not
`(color, product)`, because product-injectivity is the actual ladder condition.

The default `kmax=2` is intentionally bounded for heartbeat use. The `k=3` and
`k=4` rungs should be run with optimized or compiled code.
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


def pack(v):
    key = 0
    coeffs = tuple(v) + (0,) * (16 - len(v))
    for c in reversed(coeffs):
        key = key * 17 + c
    return key


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
                packed = pack(prod)
                if packed in seen:
                    ok = False
                    first_collision = {
                        "k": k,
                        "slots": list(slots),
                        "keys_a": list(seen[packed]),
                        "keys_b": list(keys),
                        "value": list(prod),
                    }
                    break
                seen[packed] = keys
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
        "key": "packed_product_only",
        "ladder": ladder,
        "max_good_k": max_good,
        "min_collision_support_if_no_failure": max_good + 1,
        "first_collision": first_collision,
        "decision": (
            "PRODUCT_ONLY_LADDER_PASSED_TO_KMAX"
            if first_collision is None
            else "PARTIAL_COLLISION_FOUND"
        ),
    }
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

