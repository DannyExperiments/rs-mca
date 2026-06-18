#!/usr/bin/env python3
"""Verify Cycle 39 locator collapse in the explicit restricted family.

This is a finite sanity check for the hand proof, not a proof by itself.
Ledger: q_gen=p, B=F_p, F=F_{p^2}=F_p(alpha), alpha^2=-1, q_line=p^2.
"""

import json


PRIMES = [7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83]


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def locator_residue(p):
    nr = -1 % p
    zf = (0, 0)
    of = (1, 0)
    alpha = (0, 1)

    def fadd(x, y):
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def fneg(x):
        return ((-x[0]) % p, (-x[1]) % p)

    def fsub(x, y):
        return fadd(x, fneg(y))

    def fmul(x, y):
        return ((x[0] * y[0] + nr * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)

    def fpow(x, n):
        out = of
        b = x
        while n:
            if n & 1:
                out = fmul(out, b)
            b = fmul(b, b)
            n >>= 1
        return out

    def finv(x):
        return fpow(x, p * p - 2)

    def trim(poly):
        poly = list(poly)
        while len(poly) > 1 and poly[-1] == zf:
            poly.pop()
        return poly

    def coeff(poly, i):
        return poly[i] if i < len(poly) else zf

    def deg(poly):
        poly = trim(poly)
        return -1 if poly == [zf] else len(poly) - 1

    def pscale(poly, c):
        return trim([fmul(x, c) for x in poly])

    def padd(a, b):
        m = max(len(a), len(b))
        return trim([fadd(coeff(a, i), coeff(b, i)) for i in range(m)])

    def psub(a, b):
        return padd(a, [fneg(c) for c in b])

    def pdivmod(a, mod):
        a = trim(a)
        mod = trim(mod)
        q = [zf] * max(1, deg(a) - deg(mod) + 1)
        r = a[:]
        inv = finv(mod[-1])
        while deg(r) >= deg(mod) and r != [zf]:
            shift = deg(r) - deg(mod)
            c = fmul(r[-1], inv)
            q[shift] = c
            r = psub(r, [zf] * shift + pscale(mod, c))
        return trim(q), trim(r)

    # E = X^2 + alpha X + 1, stored as [1, alpha, 1].
    E = [of, alpha, of]
    locator = [zf] * (p + 1)
    locator[p] = of
    locator[1] = fsub(locator[1], of)
    residue = pdivmod(locator, E)[1]
    ell = (coeff(residue, 0), coeff(residue, 1))

    chi = legendre(-5, p)
    if chi == 1:
        expected = (alpha, zf)
        subcase = "A"
    else:
        expected = (zf, ((-2) % p, 0))
        subcase = "B"

    return {
        "p": p,
        "p_mod_20": p % 20,
        "legendre_minus_5": chi,
        "subcase": subcase,
        "ell": ell,
        "expected": expected,
        "ok": ell == expected,
    }


def main():
    rows = []
    for p in PRIMES:
        assert p % 4 == 3 and p != 5
        rows.append(locator_residue(p))
    print(json.dumps({"all_ok": all(row["ok"] for row in rows), "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
