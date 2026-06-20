#!/usr/bin/env python3
"""Cycle 78 LR incidence sanity check.

This does not compute m_max.  It verifies, on deterministic sampled tuples, that
the Cycle 78 left-right incidence identity uses packed products as equality
keys and color only as the P_0 filter.
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
S_COLOR = {1: 15, 2: 9, 3: 12}


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


def color_key(k):
    i = k // 16 + 1
    a = k % 16
    return (S_COLOR[i] + 8 * (a % 2)) % 16


def product(table, slots, keys):
    prod = (1,) + (0,) * (NDEG - 1)
    color = 0
    for t, k in zip(slots, keys):
        prod = fmul_fast(prod, table[(t, k)])
        color = (color + color_key(k)) % 16
    return prod, color


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

    sample_left = [
        (0, 1, 2),
        (3, 17, 31),
        (47, 46, 45),
        (5, 29, 41),
        (12, 24, 36),
    ]
    sample_right = [
        (0, 1, 2, 3),
        (4, 18, 32, 46),
        (47, 0, 16, 33),
        (11, 22, 35, 44),
        (7, 19, 28, 40),
    ]

    rows = []
    ok = True
    for lk, rk in itertools.product(sample_left, sample_right):
        lprod, lc = product(table, (1, 2, 3), lk)
        rprod, rc = product(table, (4, 5, 6, 7), rk)
        full_prod, full_color = product(table, (1, 2, 3, 4, 5, 6, 7), lk + rk)
        lr_prod = fmul_fast(lprod, rprod)
        same_product = pack(full_prod) == pack(lr_prod)
        same_color = full_color == ((lc + rc) % 16)
        in_p0 = full_color == 4
        ok = ok and same_product and same_color
        rows.append(
            {
                "left": list(lk),
                "right": list(rk),
                "product_identity": same_product,
                "color_identity": same_color,
                "p0_member": in_p0,
                "packed_product": pack(full_prod),
            }
        )

    print(
        json.dumps(
            {
                "decision": "LR_INCIDENCE_SAMPLE_PASS" if ok else "LR_INCIDENCE_SAMPLE_FAIL",
                "sample_pairs": len(rows),
                "key": "packed_product_only",
                "color_role": "domain_filter_only",
                "rows": rows,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
