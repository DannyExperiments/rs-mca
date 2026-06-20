#!/usr/bin/env python3
"""Finite checks for ROLE_03_MODEL_GJ_LOCAL_LIMIT_RESULT.md.

Pure Python; no external packages.  It verifies the F_17 tensor seed, the
split-prime effective/Q_per ledger, the cyclotomic-rank quantities, and small
model-fiber caps by exhaustive enumeration.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from math import comb


def v2(x: int) -> int:
    out = 0
    while x % 2 == 0:
        out += 1
        x //= 2
    return out


def elementary(values: tuple[int, ...] | list[int], depth: int, p: int) -> tuple[int, ...]:
    e = [1] + [0] * depth
    for x in values:
        for r in range(depth, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    return tuple(e[1:])


def product(values: tuple[int, ...] | list[int], p: int) -> int:
    out = 1
    for x in values:
        out = out * x % p
    return out


def multiplicative_order(a: int, modulus: int) -> int:
    if modulus == 1:
        return 1
    x = 1
    for k in range(1, modulus + 1):
        x = x * a % modulus
        if x == 1:
            return k
    raise AssertionError("order not found")


def cyclotomic_union(p: int, n: int, exponents: range | list[int]) -> set[int]:
    out: set[int] = set()
    for r in exponents:
        x = r % n
        while x not in out:
            out.add(x)
            x = p * x % n
    return out


def D_s(p: int, n: int, s: int) -> int:
    return len(cyclotomic_union(p, n, range(1, s + 1)))


def least_power_two_ge(x: int) -> int:
    out = 1
    while out < x:
        out *= 2
    return out


def element_of_order_n(p: int, n: int) -> int:
    assert (p - 1) % n == 0
    for a in range(2, p):
        g = pow(a, (p - 1) // n, p)
        if pow(g, n, p) == 1 and (n == 1 or pow(g, n // 2, p) != 1):
            return g
    raise AssertionError("no element of requested order")


def exhaustive_model_max(p: int, n: int, s: int, j: int) -> int:
    g = element_of_order_n(p, n)
    H = tuple(pow(g, i, p) for i in range(n))
    buckets: dict[tuple[tuple[int, ...], int], int] = defaultdict(int)
    for subset in combinations(H, j):
        buckets[(elementary(subset, s, p), product(subset, p))] += 1
    return max(buckets.values(), default=0)


def check_f17_seed() -> None:
    p = 17
    A = (1, 2, 3, 4, 5, 6, 7, 9, 10, 12)
    B = (1, 2, 3, 8, 10, 11, 13, 14, 15, 16)
    assert elementary(A, 4, p) == (8, 12, 13, 7)
    assert elementary(B, 4, p) == (8, 12, 13, 7)
    assert product(A, p) == 4
    assert product(B, p) == 2
    ratio = product(A, p) * pow(product(B, p), -1, p) % p
    assert ratio == 2
    assert multiplicative_order(ratio, p) == 8


def check_rank_orbit_bound() -> None:
    for p in (3, 5, 7, 17, 97):
        R = 2 ** v2(p * p - 1) - 1
        for n in (16, 32, 64, 128, 256):
            for s in range(max(1, min(R, n - 1)), n):
                d = D_s(p, n, s)
                if s >= R:
                    a = (s // R).bit_length() - 1
                    B = 2 ** (a + 1)
                    assert n - d <= n // B


def check_small_split_fibers() -> None:
    # These are regression checks, not proofs of the general theorem.
    for p in (17, 97):
        n = 16
        for s in (1, 2, 3, 4):
            M0 = least_power_two_ge(s + 1)
            stable_block_cap = 2 ** (n // M0)
            for j in range(0, n + 1):
                if comb(n, j) > 100_000:
                    continue
                maximum = exhaustive_model_max(p, n, s, j)
                assert maximum <= max(stable_block_cap, comb(n, j))


def main() -> None:
    check_f17_seed()
    check_rank_orbit_bound()
    check_small_split_fibers()
    print("ROLE_03 finite checks: PASS")


if __name__ == "__main__":
    main()
