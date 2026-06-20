#!/usr/bin/env python3
"""Cycle 76 fast right-half product-injectivity check.

This is a local follow-up to the Cycle 76 Fable answer.  It tests the open
right half {4,5,6,7} using the exact Cycle 68 slot table, but replaces the
generic polynomial division multiplier by direct reduction modulo

    X^16 + X^8 + 3.

Equality key is packed field product only.  Colors are intentionally ignored
for product-injectivity.
"""

from __future__ import annotations

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
            # X^16 = -X^8 - 3, so X^d = -X^(d-8) - 3 X^(d-16).
            tmp[d - 8] = (tmp[d - 8] - c) % P
            tmp[d - 16] = (tmp[d - 16] - 3 * c) % P
    return tuple(tmp[:16])


def pack(v):
    key = 0
    for c in reversed(v):
        key = key * P + c
    return key


def pair_products(table, slots):
    assert len(slots) == 2
    products = []
    seen = {}
    for k0, k1 in itertools.product(range(48), repeat=2):
        p = fmul_fast(table[(slots[0], k0)], table[(slots[1], k1)])
        key = pack(p)
        if key in seen:
            return products, {
                "product_injective": False,
                "slots": list(slots),
                "keys_a": list(seen[key]),
                "keys_b": [k0, k1],
                "collision_value": key,
            }
        seen[key] = (k0, k1)
        products.append((p, (k0, k1)))
    return products, {
        "product_injective": True,
        "slots": list(slots),
        "tuple_count": 48 ** 2,
        "distinct_products": len(seen),
    }


def right_half_check(table):
    left, left_result = pair_products(table, (4, 5))
    right, right_result = pair_products(table, (6, 7))
    if not left_result["product_injective"] or not right_result["product_injective"]:
        return {
            "right_45": left_result,
            "right_67": right_result,
            "right_4567": "not_run_pair_collision_found",
            "decision": "RIGHT_HALF_COLLISION_FOUND",
        }

    seen = {}
    for lp, lk in left:
        for rp, rk in right:
            key = pack(fmul_fast(lp, rp))
            if key in seen:
                return {
                    "right_45": left_result,
                    "right_67": right_result,
                    "right_4567": {
                        "product_injective": False,
                        "slots": [4, 5, 6, 7],
                        "keys_a": list(seen[key]),
                        "keys_b": list(lk + rk),
                        "collision_value": key,
                    },
                    "decision": "RIGHT_HALF_COLLISION_FOUND",
                }
            seen[key] = lk + rk
    return {
        "right_45": left_result,
        "right_67": right_result,
        "right_4567": {
            "product_injective": True,
            "slots": [4, 5, 6, 7],
            "tuple_count": 48 ** 4,
            "distinct_products": len(seen),
        },
        "decision": "RIGHT_HALF_PRODUCT_INJECTIVE",
    }


def main():
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
    result = {
        "model": {
            "field_poly": list(f),
            "eta": list(eta),
            "beta": list(beta),
        },
        "key": "packed_product_only",
        "modulus_specialization": "X^16 + X^8 + 3",
    }
    result.update(right_half_check(table))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
