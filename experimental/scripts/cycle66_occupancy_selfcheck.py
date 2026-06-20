#!/usr/bin/env python3
"""Cycle 66 sevenfold occupancy setup self-check.

This is not the full 52,747,567,104-product occupancy count.  It verifies the
finite-field setup and Cycle 65 factorization identities used by the Cycle 66
worker answer:

* constructs an explicit F_17^16 model;
* finds eta of order 256 with eta^16 = 3;
* chooses beta outside mu_256;
* verifies the three degree-8 gadget polynomials and color constants;
* verifies c_7(4)=25152 and |P_0|=393*2^27;
* spot-checks the locator factorization rho_beta(T)=C prod_t u_t.
"""

from __future__ import annotations

import json
import random
from typing import Dict, Iterable, List, Sequence, Tuple

P = 17
N_DEG = 16
GROUP_ORDER = P**N_DEG - 1
ONE = (1,)


def trim(a: Sequence[int]) -> Tuple[int, ...]:
    b = list(a)
    while b and b[-1] == 0:
        b.pop()
    return tuple(x % P for x in b)


def padd(a: Sequence[int], b: Sequence[int]) -> Tuple[int, ...]:
    r = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        r[i] = x % P
    for i, x in enumerate(b):
        r[i] = (r[i] + x) % P
    return trim(r)


def psub(a: Sequence[int], b: Sequence[int]) -> Tuple[int, ...]:
    r = [x % P for x in a] + [0] * max(0, len(b) - len(a))
    for i, x in enumerate(b):
        r[i] = (r[i] - x) % P
    return trim(r)


def pmul(a: Sequence[int], b: Sequence[int]) -> Tuple[int, ...]:
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % P
    return trim(r)


def pdivmod(a: Sequence[int], b: Sequence[int]) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    aa = [x % P for x in a]
    bb = list(trim(b))
    if not bb:
        raise ZeroDivisionError("polynomial division by zero")
    q = [0] * max(1, len(aa) - len(bb) + 1)
    inv_lc = pow(bb[-1], P - 2, P)
    while True:
        aa = list(trim(aa))
        if not aa or len(aa) < len(bb):
            break
        d = len(aa) - len(bb)
        c = aa[-1] * inv_lc % P
        q[d] = c
        for i, y in enumerate(bb):
            aa[d + i] = (aa[d + i] - c * y) % P
    return trim(q), trim(aa)


def pmod(a: Sequence[int], b: Sequence[int]) -> Tuple[int, ...]:
    return pdivmod(a, b)[1]


def pgcd(a: Sequence[int], b: Sequence[int]) -> Tuple[int, ...]:
    aa = trim(a)
    bb = trim(b)
    while bb:
        aa, bb = bb, pmod(aa, bb)
    if aa:
        inv_lc = pow(aa[-1], P - 2, P)
        aa = tuple(x * inv_lc % P for x in aa)
    return aa


def fmul(a: Sequence[int], b: Sequence[int], f: Sequence[int]) -> Tuple[int, ...]:
    return pmod(pmul(a, b), f)


def fpow(a: Sequence[int], e: int, f: Sequence[int]) -> Tuple[int, ...]:
    r = ONE
    base = pmod(a, f)
    while e > 0:
        if e & 1:
            r = fmul(r, base, f)
        base = fmul(base, base, f)
        e >>= 1
    return trim(r)


def emb(c: int) -> Tuple[int, ...]:
    c %= P
    return (c,) if c else ()


def is_irreducible_degree_16(f: Sequence[int]) -> bool:
    x = (0, 1)
    if pgcd(psub(fpow(x, P**8, f), x), f) != ONE:
        return False
    return psub(fpow(x, P**16, f), x) == ()


def find_field_poly() -> Tuple[int, ...]:
    for c in range(1, P):
        for k in range(1, N_DEG):
            f = [0] * (N_DEG + 1)
            f[N_DEG] = 1
            f[k] = 1
            f[0] = c
            tf = tuple(f)
            if is_irreducible_degree_16(tf):
                return tf
    raise RuntimeError("no irreducible degree-16 trinomial/binomial-plus-term found")


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


def prod_linear(roots: Iterable[int]) -> Tuple[int, ...]:
    r = ONE
    for x in roots:
        r = pmul(r, ((-x) % P, 1))
    return r


def c7_target() -> int:
    residues = [1, 4, 7, 9, 12, 15]
    dp = [0] * 16
    dp[0] = 1
    for _ in range(7):
        nd = [0] * 16
        for r, val in enumerate(dp):
            if val:
                for u in residues:
                    nd[(r + u) % 16] += val
        dp = nd
    return dp[4]


def find_eta(f: Sequence[int]) -> Tuple[int, ...]:
    for c in range(P):
        h = fpow((c, 1), GROUP_ORDER // 256, f)
        if fpow(h, 128, f) == ONE:
            continue
        t16 = fpow(h, 16, f)
        for j in range(1, 16, 2):
            if t16 == emb(pow(3, j, P)):
                return fpow(h, pow(j, -1, 16), f)
    raise RuntimeError("eta not found")


def find_beta(f: Sequence[int]) -> Tuple[int, ...]:
    for c in range(2, P + 40):
        beta = (c % P, 1)
        if fpow(beta, 256, f) != ONE:
            return beta
    raise RuntimeError("admissible beta not found")


def peval(i: int, z: Sequence[int], f: Sequence[int]) -> Tuple[int, ...]:
    r: Tuple[int, ...] = ()
    for c in reversed(P_COEFFS[i]):
        r = padd(fmul(r, z, f), emb(c))
    return r


def build_u_table(
    f: Sequence[int], eta: Sequence[int], beta: Sequence[int]
) -> Dict[Tuple[int, int, int], Tuple[int, ...]]:
    xi = fpow(beta, 2, f)
    eta_inv = fpow(eta, GROUP_ORDER - 1, f)
    u_table: Dict[Tuple[int, int, int], Tuple[int, ...]] = {}
    for t in range(1, 8):
        eta_factor = fpow(eta_inv, 2 * t, f)
        for i in (1, 2, 3):
            for a in range(16):
                arg = fmul(fmul(xi, emb(pow(3, (-a) % 16, P)), f), eta_factor, f)
                u = peval(i, arg, f)
                if a & 1:
                    u = psub((), u)
                if not u:
                    raise AssertionError("unexpected zero u_t(i,a)")
                u_table[(t, i, a)] = u
    return u_table


def check_factorization(
    f: Sequence[int],
    eta: Sequence[int],
    beta: Sequence[int],
    u_table: Dict[Tuple[int, int, int], Tuple[int, ...]],
) -> None:
    subgroup = [fpow(eta, 8 * m, f) for m in range(32)]

    def lift(i: int, a: int) -> List[Tuple[int, ...]]:
        target = {emb(pow(3, (a + e) % 16, P)) for e in E_SETS[i]}
        return [x for x in subgroup if fpow(x, 2, f) in target]

    rng = random.Random(0)
    for _ in range(32):
        choices = [(rng.randint(1, 3), rng.randint(0, 15)) for _ in range(7)]
        support = [ONE]
        for t, (i, a) in enumerate(choices, 1):
            eta_t = fpow(eta, t, f)
            support.extend(fmul(eta_t, y, f) for y in lift(i, a))

        rho = ONE
        for x in support:
            rho = fmul(rho, psub(beta, x), f)

        constant = fmul(psub(beta, ONE), emb(pow(3, 12, P)), f)
        rhs = constant
        for t, (i, a) in enumerate(choices, 1):
            rhs = fmul(rhs, u_table[(t, i, a)], f)

        if rho != rhs:
            raise AssertionError("Cycle65 rho_beta factorization failed")


def main() -> None:
    assert GROUP_ORDER % 256 == 0 and GROUP_ORDER % 512 != 0
    field_poly = find_field_poly()

    for i in (1, 2, 3):
        roots = [pow(3, e, P) for e in E_SETS[i]]
        assert prod_linear(roots) == P_COEFFS[i]
        assert P_COEFFS[i][7] == 0 and P_COEFFS[i][6] == 0
        assert sum(E_SETS[i]) % 16 == S_COLOR[i]

    assert c7_target() == 25152
    p0_count = 25152 * 8**7
    assert p0_count == 52747567104 == 393 * 2**27

    eta = find_eta(field_poly)
    assert fpow(eta, 16, field_poly) == emb(3)
    assert fpow(eta, 256, field_poly) == ONE
    assert fpow(eta, 128, field_poly) == emb(-1)

    beta = find_beta(field_poly)
    assert fpow(beta, 256, field_poly) != ONE

    u_table = build_u_table(field_poly, eta, beta)
    check_factorization(field_poly, eta, beta, u_table)

    certificate = {
        "field_poly": list(field_poly),
        "N": GROUP_ORDER,
        "v2_N": 8,
        "mu512_equals_mu256": True,
        "eta": list(eta),
        "beta": list(beta),
        "selfchecks": {
            "P_i_products": True,
            "e1_e2_zero": True,
            "colors": [S_COLOR[1], S_COLOR[2], S_COLOR[3]],
            "c7_4": 25152,
            "P0": p0_count,
            "factorization_oracle_spotchecks": 32,
        },
        "decision": "SELF_CHECK_ONLY",
        "threshold": 2**32,
    }
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
