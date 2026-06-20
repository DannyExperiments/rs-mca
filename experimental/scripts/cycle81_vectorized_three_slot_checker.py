#!/usr/bin/env python3
"""Cycle 81 vectorized three-slot product-injectivity checker.

This decides all 35 three-slot product maps in the Cycle 68 finite model using
exact arithmetic in F_17[X]/(X^16 + X^8 + 3). Equality keys are packed field
products only; color is recorded only if a collision packet is found.

Run with the Codex bundled Python if system Python lacks NumPy:

    /Users/danielcabezas/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
      experimental/scripts/cycle81_vectorized_three_slot_checker.py
"""

from __future__ import annotations

import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


P = 17
NDEG = 16
SCRIPT_DIR = Path(__file__).resolve().parent
CYCLE68_PATH = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"
CYCLE80_PATH = SCRIPT_DIR / "cycle80_three_slot_injectivity_checker.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def dense_tuple(v):
    out = [0] * NDEG
    for i, x in enumerate(v[:NDEG]):
        out[i] = x % P
    return tuple(out)


def dense_arr(vals):
    arr = np.zeros((len(vals), NDEG), dtype=np.int64)
    for r, v in enumerate(vals):
        for i, c in enumerate(v[:NDEG]):
            arr[r, i] = c % P
    return arr


def fold_reduce(conv):
    tmp = conv.copy() % P
    for d in range(30, NDEG - 1, -1):
        coeff = tmp[:, d] % P
        tmp[:, d - 8] = (tmp[:, d - 8] - coeff) % P
        tmp[:, d - 16] = (tmp[:, d - 16] - 3 * coeff) % P
        tmp[:, d] = 0
    return tmp[:, :NDEG] % P


def batch_mul(a, b):
    n = a.shape[0]
    conv = np.zeros((n, 2 * NDEG - 1), dtype=np.int64)
    for i in range(NDEG):
        conv[:, i : i + NDEG] += a[:, i][:, None] * b
    return fold_reduce(conv)


def all_combos_mul(a, b):
    n_a, n_b = a.shape[0], b.shape[0]
    a2 = np.repeat(a, n_b, axis=0)
    b2 = np.tile(b, (n_a, 1))
    return batch_mul(a2, b2)


def keys_of(matrix):
    compact = np.ascontiguousarray(matrix.astype(np.uint8))
    return compact.view(np.dtype((np.void, NDEG))).reshape(-1)


def main() -> None:
    c68 = load_module(CYCLE68_PATH, "cycle68_checker")
    c80 = load_module(CYCLE80_PATH, "cycle80_checker")
    f = c68.find_field_poly()
    eta = c68.find_eta(f)
    beta = c68.find_beta(f)
    raw = c68.build_u(f, eta, beta)

    slot_tuples = {}
    slot = {}
    key_of_k = {}
    for t in range(1, 8):
        vals = []
        for k in range(48):
            i, a = k // 16 + 1, k % 16
            vals.append(dense_tuple(raw[(t, i, a)]))
            key_of_k[k] = (i, a)
        slot_tuples[t] = vals
        slot[t] = dense_arr(vals)

    # Exact scalar-vs-vector self-test on all products for the first pair.
    scalar_pair = []
    for a in slot_tuples[1]:
        for b in slot_tuples[2]:
            scalar_pair.append(c80.fmul_fast(a, b))
    vector_pair = all_combos_mul(slot[1], slot[2])
    assert [tuple(map(int, row)) for row in vector_pair] == scalar_pair

    color = {
        k: (c68.S_COLOR[k // 16 + 1] + 8 * ((k % 16) % 2)) % 16
        for k in range(48)
    }

    results = []
    all_ok = True
    collision = None
    for t1, t2, t3 in itertools.combinations(range(1, 8), 3):
        pair = all_combos_mul(slot[t1], slot[t2])
        full = all_combos_mul(pair, slot[t3])
        keys = keys_of(full)
        uniq, idx, counts = np.unique(keys, return_index=True, return_counts=True)
        max_count = int(counts.max()) if len(counts) else 0
        if max_count > 1:
            key = uniq[int(np.argmax(counts))]
            dup = np.where(keys == key)[0]
            r_a, r_b = int(dup[0]), int(dup[1])

            def decode(row: int) -> tuple[int, int, int]:
                k3 = row % 48
                pp = row // 48
                k2 = pp % 48
                k1 = pp // 48
                return k1, k2, k3

            k_a, k_b = decode(r_a), decode(r_b)
            slots = (t1, t2, t3)
            collision = {
                "slots": list(slots),
                "assignment_A": [
                    {
                        "slot": t,
                        "k": k,
                        "ia": list(key_of_k[k]),
                        "color": color[k],
                    }
                    for t, k in zip(slots, k_a)
                ],
                "assignment_B": [
                    {
                        "slot": t,
                        "k": k,
                        "ia": list(key_of_k[k]),
                        "color": color[k],
                    }
                    for t, k in zip(slots, k_b)
                ],
                "packed_product_coeffs": [int(x) for x in full[r_a]],
                "colorsum_A": sum(color[k] for k in k_a) % 16,
                "colorsum_B": sum(color[k] for k in k_b) % 16,
            }
            results.append(
                {
                    "slots": list(slots),
                    "product_injective": False,
                    "max_multiplicity": max_count,
                }
            )
            all_ok = False
            break

        results.append(
            {
                "slots": [t1, t2, t3],
                "product_injective": True,
                "tuple_count": 48**3,
                "distinct_products": int(uniq.size),
                "max_multiplicity": max_count,
            }
        )

    out = {
        "model": {"field_poly": list(f), "eta": list(eta), "beta": list(beta)},
        "key": "packed_product_only",
        "subset_size": 3,
        "subsets_checked": len(results),
        "all_checked_product_injective": all_ok,
        "self_test": "scalar_pair_12_matches_vectorized",
        "results": results,
    }
    if all_ok:
        out["decision"] = "ALL_3_SUBSETS_PRODUCT_INJECTIVE"
        out["fiber_min_distance_lower_bound"] = 4
    else:
        out["decision"] = "PRODUCT_COLLISION_FOUND"
        out["collision_packet"] = collision
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
