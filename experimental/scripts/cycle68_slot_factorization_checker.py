#!/usr/bin/env python3
"""Cycle 68 slot-factorization checker.

This validates the disjoint-coset factorization from the Cycle 68 response on
the explicit Cycle 66 model:

    F = F_17[X] / (X^16 + X^8 + 3)
    eta = 6 X^9
    beta = X + 2

It is not a proof of m_max(beta) <= 12. It verifies the reduced 336-entry
slot table, exact color/set-sum bookkeeping, slot full-product oracle, and
runs a small certified lower-bound multiplicity probe.
"""

from __future__ import annotations

import json
import random


P = 17
NDEG = 16
N = P**NDEG - 1
ONE = (1,)

E_SETS = {
    1: {0, 1, 2, 3, 5, 11, 12, 13},
    2: {0, 1, 2, 3, 4, 8, 9, 14},
    3: {0, 1, 2, 4, 5, 7, 11, 14},
}
P_COEFFS = {
    1: (6, 4, 4, 10, 5, 4, 0, 0, 1),
    2: (14, 13, 14, 12, 5, 9, 0, 0, 1),
    3: (4, 12, 1, 5, 0, 11, 0, 0, 1),
}
S_COLOR = {1: 15, 2: 9, 3: 12}


def trim(a):
    b = list(a)
    while b and b[-1] == 0:
        b.pop()
    return tuple(x % P for x in b)


def padd(a, b):
    r = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        r[i] = x % P
    for i, x in enumerate(b):
        r[i] = (r[i] + x) % P
    return trim(r)


def psub(a, b):
    r = [x % P for x in a] + [0] * max(0, len(b) - len(a))
    for i, x in enumerate(b):
        r[i] = (r[i] - x) % P
    return trim(r)


def pmul(a, b):
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % P
    return trim(r)


def pdivmod(a, b):
    aa = [x % P for x in a]
    bb = list(trim(b))
    q = [0] * max(1, len(aa) - len(bb) + 1)
    inv = pow(bb[-1], P - 2, P)
    while True:
        aa = list(trim(aa))
        if not aa or len(aa) < len(bb):
            break
        d = len(aa) - len(bb)
        c = aa[-1] * inv % P
        q[d] = c
        for i, y in enumerate(bb):
            aa[d + i] = (aa[d + i] - c * y) % P
    return trim(q), trim(aa)


def pmod(a, b):
    return pdivmod(a, b)[1]


def pgcd(a, b):
    aa, bb = trim(a), trim(b)
    while bb:
        aa, bb = bb, pmod(aa, bb)
    if aa:
        inv = pow(aa[-1], P - 2, P)
        aa = tuple(x * inv % P for x in aa)
    return aa


def fmul(a, b, f):
    return pmod(pmul(a, b), f)


def fpow(a, e, f):
    r = ONE
    base = pmod(a, f)
    while e > 0:
        if e & 1:
            r = fmul(r, base, f)
        base = fmul(base, base, f)
        e >>= 1
    return trim(r)


def emb(c):
    c %= P
    return (c,) if c else ()


def irred16(f):
    x = (0, 1)
    if pgcd(psub(fpow(x, P**8, f), x), f) != ONE:
        return False
    return psub(fpow(x, P**16, f), x) == ()


def find_field_poly():
    for c in range(1, P):
        for k in range(1, NDEG):
            f = [0] * (NDEG + 1)
            f[NDEG] = 1
            f[k] = 1
            f[0] = c
            if irred16(tuple(f)):
                return tuple(f)
    raise RuntimeError("no polynomial found")


def find_eta(f):
    for c in range(P):
        h = fpow((c, 1), N // 256, f)
        if fpow(h, 128, f) == ONE:
            continue
        t16 = fpow(h, 16, f)
        for j in range(1, 16, 2):
            if t16 == emb(pow(3, j, P)):
                return fpow(h, pow(j, -1, 16), f)
    raise RuntimeError("eta not found")


def find_beta(f):
    for c in range(2, P + 40):
        beta = (c % P, 1)
        if fpow(beta, 256, f) != ONE:
            return beta
    raise RuntimeError("beta not found")


def peval(i, z, f):
    r = ()
    for c in reversed(P_COEFFS[i]):
        r = padd(fmul(r, z, f), emb(c))
    return r


def build_u(f, eta, beta):
    xi = fpow(beta, 2, f)
    einv = fpow(eta, N - 1, f)
    table = {}
    for t in range(1, 8):
        ef = fpow(einv, 2 * t, f)
        for i in (1, 2, 3):
            for a in range(16):
                arg = fmul(fmul(xi, emb(pow(3, (-a) % 16, P)), f), ef, f)
                u = peval(i, arg, f)
                if a & 1:
                    u = psub((), u)
                assert u != ()
                table[(t, i, a)] = u
    return table


def main():
    f = find_field_poly()
    eta = find_eta(f)
    beta = find_beta(f)
    xi = fpow(beta, 2, f)
    table = build_u(f, eta, beta)
    eta_pows = [fpow(eta, j, f) for j in range(256)]
    inv3t = {
        t: fpow(emb(pow(3, t, P)), P - 2, f)
        for t in range(1, 8)
    }

    def bset(i, a):
        return frozenset((a + e) % 16 for e in E_SETS[i])

    def slot_product(t, b_set):
        r = ONE
        for b in b_set:
            r = fmul(r, psub(xi, eta_pows[(2 * t + 16 * b) % 256]), f)
        return r

    # C1: all 336 slot factorizations.
    for t in range(1, 8):
        for i in (1, 2, 3):
            for a in range(16):
                assert fmul(inv3t[t], slot_product(t, bset(i, a)), f) == table[(t, i, a)]

    # C2: random brute-force support products match factorization.
    rng = random.Random(0)
    subgroup = [fpow(eta, 8 * m, f) for m in range(32)]

    def lift(i, a):
        target = {emb(pow(3, (a + e) % 16, P)) for e in E_SETS[i]}
        return [x for x in subgroup if fpow(x, 2, f) in target]

    for _ in range(16):
        choices = [(rng.randint(1, 3), rng.randint(0, 15)) for _ in range(7)]
        support = [ONE]
        for t, (i, a) in enumerate(choices, 1):
            et = fpow(eta, t, f)
            support.extend(fmul(et, y, f) for y in lift(i, a))
        rho = ONE
        for x in support:
            rho = fmul(rho, psub(beta, x), f)
        rhs = psub(beta, ONE)
        for t, (i, a) in enumerate(choices, 1):
            rhs = fmul(rhs, slot_product(t, bset(i, a)), f)
        assert rho == rhs

    # C3: 48 sets are distinct and color equals set-sum mod 16.
    seen = {}
    for i in (1, 2, 3):
        for a in range(16):
            b_set = bset(i, a)
            assert sum(b_set) % 16 == (S_COLOR[i] + 8 * (a % 2)) % 16
            assert b_set not in seen
            seen[b_set] = (i, a)
    assert len(seen) == 48

    # C4: full slot product oracle.
    for t in range(1, 8):
        full = slot_product(t, frozenset(range(16)))
        assert full == psub(fpow(beta, 32, f), emb(pow(3, 2 * t, P)))

    # C5: single-slot injectivity.
    for t in range(1, 8):
        vals = {table[(t, i, a)] for i in (1, 2, 3) for a in range(16)}
        assert len(vals) == 48

    def color_key(k):
        i = k // 16 + 1
        a = k % 16
        return (S_COLOR[i] + 8 * (a % 2)) % 16

    def u_value(t, k):
        i = k // 16 + 1
        a = k % 16
        return table[(t, i, a)]

    # C6: a small certified lower-bound probe for m_max.
    lb = 1
    # These fixed right tuples have compatible left colors for slots 1,2,3.
    right_tuples = [(0, 0, 0, 16), (0, 0, 0, 17), (5, 20, 40, 47)]
    for right in right_tuples:
        c_right = sum(color_key(k) for k in right) % 16
        needed = (4 - c_right) % 16
        buckets = {}
        for k1 in range(48):
            c1 = color_key(k1)
            u1 = u_value(1, k1)
            for k2 in range(48):
                c12 = (c1 + color_key(k2)) % 16
                p12 = fmul(u1, u_value(2, k2), f)
                for k3 in range(48):
                    if (c12 + color_key(k3)) % 16 != needed:
                        continue
                    p_left = fmul(p12, u_value(3, k3), f)
                    buckets[p_left] = buckets.get(p_left, 0) + 1
        assert buckets, (right, needed)
        lb = max(lb, max(buckets.values()))

    cert = {
        "model": {
            "field_poly": list(f),
            "eta": list(eta),
            "beta": list(beta),
        },
        "selfchecks": {
            "C1_factorization_all_336": True,
            "C2_rho_random": 16,
            "C3_48_sets_distinct_color_eq_sum": True,
            "C4_slot_full_product_oracle": True,
            "C5_single_slot_injective": True,
            "C6_right_tuple_probe_count": len(right_tuples),
        },
        "m_max_lower_bound_probe": lb,
        "P0": 52_747_567_104,
        "threshold": 2**32,
        "decision": "REDUCTION_VERIFIED__FULL_MMAX_REQUIRES_COMPILED_RUN",
    }
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
