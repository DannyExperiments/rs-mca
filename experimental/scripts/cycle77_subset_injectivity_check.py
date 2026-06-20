#!/usr/bin/env python3
"""Cycle 77 subset product-injectivity checker.

This bounded local follow-up verifies all product maps on selected slot subsets
using the exact Cycle 68 table.  Equality keys are packed field products only.

Default: check all slot subsets up to size 3.  This is small enough for a
heartbeat follow-up and supports the Cycle 77 fiber-as-code lemma.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path


P = 17
NDEG = 16
SCRIPT_DIR = Path(__file__).resolve().parent
CYCLE68_PATH = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"


def load_cycle68():
    spec = importlib.util.spec_from_file_location("cycle68_checker", CYCLE68_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def dense(v):
    out = [0] * NDEG
    for i, x in enumerate(v[:NDEG]):
        out[i] = x % P
    return tuple(out)


def fmul_fast(a, b):
    tmp = [0] * 31
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    tmp[i + j] = (tmp[i + j] + x * y) % P
    for d in range(30, 15, -1):
        c = tmp[d] % P
        if c:
            tmp[d - 8] = (tmp[d - 8] - c) % P
            tmp[d - 16] = (tmp[d - 16] - 3 * c) % P
    return tuple(tmp[:16])


def pack(v):
    key = 0
    for c in reversed(v):
        key = key * P + c
    return key


def check_subset(table, slots):
    seen = {}
    for keys in itertools.product(range(48), repeat=len(slots)):
        prod = (1,) + (0,) * (NDEG - 1)
        for t, k in zip(slots, keys):
            prod = fmul_fast(prod, table[(t, k)])
        key = pack(prod)
        if key in seen:
            return {
                "product_injective": False,
                "slots": list(slots),
                "keys_a": list(seen[key]),
                "keys_b": list(keys),
                "collision_value": key,
                "tuple_count_checked_until_collision": None,
            }
        seen[key] = keys
    return {
        "product_injective": True,
        "slots": list(slots),
        "tuple_count": 48 ** len(slots),
        "distinct_products": len(seen),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, default=3)
    parser.add_argument(
        "--include-four",
        action="store_true",
        help="also check all 4-subsets; expensive in Python",
    )
    args = parser.parse_args()
    max_size = max(args.max_size, 4 if args.include_four else args.max_size)

    c68 = load_cycle68()
    f = c68.find_field_poly()
    eta = c68.find_eta(f)
    beta = c68.find_beta(f)
    raw_table = c68.build_u(f, eta, beta)
    table = {}
    for t in range(1, 8):
        for k in range(48):
            i = k // 16 + 1
            a = k % 16
            table[(t, k)] = dense(raw_table[(t, i, a)])

    results = []
    all_ok = True
    for size in range(1, max_size + 1):
        if size == 4 and not args.include_four:
            continue
        for slots in itertools.combinations(range(1, 8), size):
            res = check_subset(table, slots)
            results.append(res)
            all_ok = all_ok and res["product_injective"]
            if not res["product_injective"]:
                break
        if not all_ok:
            break

    out = {
        "model": {
            "field_poly": list(f),
            "eta": list(eta),
            "beta": list(beta),
        },
        "key": "packed_product_only",
        "max_size_requested": max_size,
        "include_four": args.include_four,
        "subsets_checked": len(results),
        "all_checked_product_injective": all_ok,
        "results": results,
    }
    if all_ok:
        max_checked = max(len(r["slots"]) for r in results) if results else 0
        out["fiber_min_distance_lower_bound"] = max_checked + 1
        out["decision"] = f"ALL_SUBSETS_UP_TO_{max_checked}_PRODUCT_INJECTIVE"
    else:
        out["decision"] = "SUBSET_PRODUCT_COLLISION_FOUND"
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
