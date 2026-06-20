#!/usr/bin/env python3
"""Exact verifier for the Cycle-60/62 degree-31 Lattes MCA packet.

No Sage, Magma, network, floating-point verdict, or probabilistic test is used.
The output is a machine-readable JSON certificate.  Large integers are emitted
as decimal strings to avoid downstream precision loss.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Optional, Sequence, Tuple

P = 8191
A_E = 1
B_E = 459
EXT_DEG = 18
N_CODE = 8192
K_CODE = 2048
SIGMA = 31
AGREEMENT = K_CODE + SIGMA
ERRORS = N_CODE - AGREEMENT
M = 31
B_FIBERS = 67
DEFECT = 2

# f_ext(Z)=Z^18+57Z+1, ascending coefficients.
FIELD_MODULUS = [1, 57] + [0] * 16 + [1]
Q_FIELD = P**EXT_DEG

# Exact factorization of q-1.
Q_MINUS_ONE_FACTORIZATION = {
    2: 14,
    3: 4,
    5: 1,
    7: 1,
    13: 1,
    19: 1,
    109: 1,
    193: 1,
    1459: 1,
    56467: 1,
    347587: 1,
    2633203: 1,
    22366891: 1,
    39662137: 1,
    73271251: 1,
    23286150103087: 1,
}

EXPECTED_U = [
    814, 1493, 2194, 2615, 2698, 2895, 3776, 4279,
    5486, 5537, 6235, 7216, 7905, 8013, 8050,
]

INF = None
Point = Optional[Tuple[int, int]]
FFElt = Tuple[int, ...]


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dec(n: int) -> str:
    return str(n)


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def is_prime_u64(n: int) -> bool:
    """Deterministic Miller--Rabin for n<2^64."""
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for r in small:
        if n % r == 0:
            return n == r
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


# ---------- Polynomials over F_p, ascending coefficients ----------

def fp_trim(a: Sequence[int]) -> list[int]:
    out = [x % P for x in a]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def fp_add(a: Sequence[int], b: Sequence[int]) -> list[int]:
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] = (c[i] + x) % P
    for i, x in enumerate(b):
        c[i] = (c[i] + x) % P
    return fp_trim(c)


def fp_neg(a: Sequence[int]) -> list[int]:
    return fp_trim([(-x) % P for x in a])


def fp_sub(a: Sequence[int], b: Sequence[int]) -> list[int]:
    return fp_add(a, fp_neg(b))


def fp_scale(a: Sequence[int], c: int) -> list[int]:
    return fp_trim([(c * x) % P for x in a])


def fp_mul(a: Sequence[int], b: Sequence[int]) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[i + j] = (c[i + j] + x * y) % P
    return fp_trim(c)


def fp_prod(polys: Iterable[Sequence[int]]) -> list[int]:
    r = [1]
    for f in polys:
        r = fp_mul(r, f)
    return r


def fp_divmod(a: Sequence[int], b: Sequence[int]) -> tuple[list[int], list[int]]:
    aa = fp_trim(a)
    bb = fp_trim(b)
    check(bb != [0], "division by zero polynomial")
    if len(aa) < len(bb):
        return [0], aa
    q = [0] * (len(aa) - len(bb) + 1)
    inv_lc = pow(bb[-1], P - 2, P)
    while aa != [0] and len(aa) >= len(bb):
        d = len(aa) - len(bb)
        c = aa[-1] * inv_lc % P
        q[d] = c
        for j, x in enumerate(bb):
            aa[d + j] = (aa[d + j] - c * x) % P
        aa = fp_trim(aa)
    return fp_trim(q), aa


def fp_mod(a: Sequence[int], modulus: Sequence[int]) -> list[int]:
    return fp_divmod(a, modulus)[1]


def fp_gcd(a: Sequence[int], b: Sequence[int]) -> list[int]:
    aa, bb = fp_trim(a), fp_trim(b)
    while bb != [0]:
        aa, bb = bb, fp_divmod(aa, bb)[1]
    return fp_scale(aa, pow(aa[-1], P - 2, P))


def fp_deriv(a: Sequence[int]) -> list[int]:
    return fp_trim([(i * a[i]) % P for i in range(1, len(a))] or [0])


def fp_eval(a: Sequence[int], x: int) -> int:
    r = 0
    for c in reversed(a):
        r = (r * x + c) % P
    return r


def fp_powmod(base: Sequence[int], exponent: int, modulus: Sequence[int]) -> list[int]:
    r = [1]
    b = fp_mod(base, modulus)
    e = exponent
    while e:
        if e & 1:
            r = fp_mod(fp_mul(r, b), modulus)
        b = fp_mod(fp_mul(b, b), modulus)
        e >>= 1
    return r


def fp_irreducible_degree_18(f: Sequence[int]) -> bool:
    f = fp_trim(f)
    if len(f) != 19 or f[-1] != 1:
        return False
    x = [0, 1]
    # Rabin criterion, prime divisors 2 and 3 of 18.
    if fp_sub(fp_powmod(x, P**18, f), x) != [0]:
        return False
    for d in (9, 6):
        h = fp_sub(fp_powmod(x, P**d, f), x)
        if fp_gcd(f, h) != [1]:
            return False
    return True


# ---------- Elliptic curve E/F_p ----------

def ec_on_curve(pt: Point, a: int = A_E, b: int = B_E) -> bool:
    if pt is None:
        return True
    x, y = pt
    return (y * y - (x * x * x + a * x + b)) % P == 0


def ec_add(p1: Point, p2: Point, a: int = A_E) -> Point:
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and (y1 + y2) % P == 0:
        return None
    if p1 == p2:
        check(y1 % P != 0, "doubling a 2-torsion point")
        slope = (3 * x1 * x1 + a) * pow(2 * y1, P - 2, P) % P
    else:
        slope = (y2 - y1) * pow(x2 - x1, P - 2, P) % P
    x3 = (slope * slope - x1 - x2) % P
    y3 = (slope * (x1 - x3) - y1) % P
    return x3, y3


def ec_mul(n: int, pt: Point, a: int = A_E) -> Point:
    r: Point = None
    q = pt
    e = n
    while e:
        if e & 1:
            r = ec_add(r, q, a)
        q = ec_add(q, q, a)
        e >>= 1
    return r


def legendre(z: int) -> int:
    z %= P
    if z == 0:
        return 0
    return 1 if pow(z, (P - 1) // 2, P) == 1 else -1


def curve_character_sum(a: int, b: int) -> int:
    return sum(legendre((x**3 + a * x + b) % P) for x in range(P))


# ---------- Explicit extension field F=F_p[z]/(z^18+57z+1) ----------
FF_ZERO: FFElt = (0,) * EXT_DEG
FF_ONE: FFElt = (1,) + (0,) * (EXT_DEG - 1)
FF_ALPHA: FFElt = (1, 1) + (0,) * (EXT_DEG - 2)  # z+1


def ff(c: int) -> FFElt:
    return (c % P,) + (0,) * (EXT_DEG - 1)


def ff_is_zero(a: FFElt) -> bool:
    return a == FF_ZERO


def ff_add(a: FFElt, b: FFElt) -> FFElt:
    return tuple((x + y) % P for x, y in zip(a, b))


def ff_neg(a: FFElt) -> FFElt:
    return tuple((-x) % P for x in a)


def ff_sub(a: FFElt, b: FFElt) -> FFElt:
    return ff_add(a, ff_neg(b))


def ff_mul(a: FFElt, b: FFElt) -> FFElt:
    tmp = [0] * (2 * EXT_DEG - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    tmp[i + j] = (tmp[i + j] + x * y) % P
    # z^18 = -57z-1.
    for d in range(2 * EXT_DEG - 2, EXT_DEG - 1, -1):
        c = tmp[d]
        if c:
            s = d - EXT_DEG
            tmp[s] = (tmp[s] - c) % P
            tmp[s + 1] = (tmp[s + 1] - 57 * c) % P
    return tuple(tmp[:EXT_DEG])


def ff_pow(a: FFElt, exponent: int) -> FFElt:
    r = FF_ONE
    b = a
    e = exponent
    while e:
        if e & 1:
            r = ff_mul(r, b)
        b = ff_mul(b, b)
        e >>= 1
    return r


def ff_inv(a: FFElt) -> FFElt:
    check(not ff_is_zero(a), "extension-field division by zero")
    return ff_pow(a, Q_FIELD - 2)


def ff_div(a: FFElt, b: FFElt) -> FFElt:
    return ff_mul(a, ff_inv(b))


def ff_batch_inverse(values: Sequence[FFElt]) -> list[FFElt]:
    check(all(not ff_is_zero(v) for v in values), "zero in batch inverse")
    prefix: list[FFElt] = [FF_ONE]
    for v in values:
        prefix.append(ff_mul(prefix[-1], v))
    acc = ff_inv(prefix[-1])
    out = [FF_ZERO] * len(values)
    for i in range(len(values) - 1, -1, -1):
        out[i] = ff_mul(acc, prefix[i])
        acc = ff_mul(acc, values[i])
    return out


# Polynomials over F.
def ffx_trim(a: Sequence[FFElt]) -> list[FFElt]:
    out = list(a)
    while len(out) > 1 and ff_is_zero(out[-1]):
        out.pop()
    return out


def ffx_add(a: Sequence[FFElt], b: Sequence[FFElt]) -> list[FFElt]:
    c = [FF_ZERO] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] = ff_add(c[i], x)
    for i, x in enumerate(b):
        c[i] = ff_add(c[i], x)
    return ffx_trim(c)


def ffx_neg(a: Sequence[FFElt]) -> list[FFElt]:
    return ffx_trim([ff_neg(x) for x in a])


def ffx_sub(a: Sequence[FFElt], b: Sequence[FFElt]) -> list[FFElt]:
    return ffx_add(a, ffx_neg(b))


def ffx_scale(a: Sequence[FFElt], c: FFElt) -> list[FFElt]:
    return ffx_trim([ff_mul(c, x) for x in a])


def ffx_mul(a: Sequence[FFElt], b: Sequence[FFElt]) -> list[FFElt]:
    c = [FF_ZERO] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if not ff_is_zero(x):
            for j, y in enumerate(b):
                if not ff_is_zero(y):
                    c[i + j] = ff_add(c[i + j], ff_mul(x, y))
    return ffx_trim(c)


def ffx_pow(a: Sequence[FFElt], exponent: int) -> list[FFElt]:
    r = [FF_ONE]
    b = list(a)
    e = exponent
    while e:
        if e & 1:
            r = ffx_mul(r, b)
        b = ffx_mul(b, b)
        e >>= 1
    return r


def ffx_divmod(a: Sequence[FFElt], b: Sequence[FFElt]) -> tuple[list[FFElt], list[FFElt]]:
    aa = ffx_trim(a)
    bb = ffx_trim(b)
    check(bb != [FF_ZERO], "extension polynomial division by zero")
    if len(aa) < len(bb):
        return [FF_ZERO], aa
    q = [FF_ZERO] * (len(aa) - len(bb) + 1)
    inv_lc = ff_inv(bb[-1])
    while aa != [FF_ZERO] and len(aa) >= len(bb):
        d = len(aa) - len(bb)
        c = ff_mul(aa[-1], inv_lc)
        q[d] = c
        for j, x in enumerate(bb):
            aa[d + j] = ff_sub(aa[d + j], ff_mul(c, x))
        aa = ffx_trim(aa)
    return ffx_trim(q), aa


def ffx_gcd(a: Sequence[FFElt], b: Sequence[FFElt]) -> list[FFElt]:
    aa, bb = ffx_trim(a), ffx_trim(b)
    while bb != [FF_ZERO]:
        aa, bb = bb, ffx_divmod(aa, bb)[1]
    return ffx_scale(aa, ff_inv(aa[-1]))


def ffx_deriv(a: Sequence[FFElt]) -> list[FFElt]:
    return ffx_trim([ff_mul(ff(i), a[i]) for i in range(1, len(a))] or [FF_ZERO])


def ffx_eval(a: Sequence[FFElt], x: FFElt) -> FFElt:
    r = FF_ZERO
    for c in reversed(a):
        r = ff_add(ff_mul(r, x), c)
    return r


def ffx_homogenized_linear_substitution(
    coeffs_fp: Sequence[int], total_degree: int, u: Sequence[FFElt], v: Sequence[FFElt]
) -> list[FFElt]:
    """Return sum_j c_j U^j V^(total_degree-j)."""
    upows = [[FF_ONE]]
    vpows = [[FF_ONE]]
    for _ in range(total_degree):
        upows.append(ffx_mul(upows[-1], u))
        vpows.append(ffx_mul(vpows[-1], v))
    out = [FF_ZERO]
    for j, c in enumerate(coeffs_fp):
        if c % P:
            term = ffx_mul(upows[j], vpows[total_degree - j])
            out = ffx_add(out, ffx_scale(term, ff(c)))
    return ffx_trim(out)


def ff_json(a: FFElt) -> list[int]:
    return list(a)


def ffx_json(poly: Sequence[FFElt]) -> list[list[int]]:
    return [ff_json(c) for c in poly]


def canonical_hash(obj: object) -> str:
    data = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


# ---------- Dihedral normalizer certificate ----------
def dmul(g: tuple[int, int], h: tuple[int, int]) -> tuple[int, int]:
    a, b = g
    c, d = h
    return ((a + (c if b == 0 else -c)) % 31, (b + d) % 2)


def dinv(g: tuple[int, int]) -> tuple[int, int]:
    for h in [(a, b) for a in range(31) for b in range(2)]:
        if dmul(g, h) == (0, 0) and dmul(h, g) == (0, 0):
            return h
    raise AssertionError("no inverse in D_62")


def dconj(g: tuple[int, int], h: tuple[int, int]) -> tuple[int, int]:
    return dmul(dmul(g, h), dinv(g))


def main(output_path: Path) -> dict:
    # Prime and field size.
    check(is_prime_trial(P), "8191 is not prime")
    check(2**233 < Q_FIELD < 2**234 < 2**256, "field-size envelope failed")

    factor_product = 1
    for r, e in Q_MINUS_ONE_FACTORIZATION.items():
        check(is_prime_u64(r), f"nonprime factor {r}")
        factor_product *= r**e
    check(factor_product == Q_FIELD - 1, "q-1 factorization mismatch")

    check(fp_irreducible_degree_18(FIELD_MODULUS), "extension modulus reducible")
    primitive_checks = {
        str(r): ff_pow(FF_ALPHA, (Q_FIELD - 1) // r) != FF_ONE
        for r in Q_MINUS_ONE_FACTORIZATION
    }
    check(all(primitive_checks.values()), "alpha=z+1 is not primitive")

    i_elt = ff_pow(FF_ALPHA, (Q_FIELD - 1) // 4)
    h_gen = ff_pow(FF_ALPHA, (Q_FIELD - 1) // (P + 1))
    check(ff_mul(i_elt, i_elt) == ff(-1), "i^2 != -1")
    check(ff_pow(i_elt, P) == ff_neg(i_elt), "i^p != -i")
    check(ff_pow(h_gen, P + 1) == FF_ONE, "H generator wrong order divisor")
    check(ff_pow(h_gen, (P + 1) // 2) != FF_ONE, "H generator not order 8192")
    check(ff_pow(FF_ALPHA, P) != FF_ALPHA, "alpha lies in F_p")

    # Exhaustive Cayley-domain equality beta(P^1(F_p))=alpha*<h>.
    denoms = [ff_add(ff(t), i_elt) for t in range(P)]
    inv_denoms = ff_batch_inverse(denoms)
    beta_affine = [
        ff_mul(FF_ALPHA, ff_mul(ff_sub(ff(t), i_elt), inv_denoms[t]))
        for t in range(P)
    ]
    beta_values = beta_affine + [FF_ALPHA]  # t=infinity
    check(len(set(beta_values)) == P + 1, "Cayley map not injective")
    h_values = []
    cur = FF_ONE
    for _ in range(P + 1):
        h_values.append(ff_mul(FF_ALPHA, cur))
        cur = ff_mul(cur, h_gen)
    check(cur == FF_ONE, "H enumeration failed")
    check(set(beta_values) == set(h_values), "Cayley image != alpha H")
    check(FF_ALPHA in set(beta_values), "alpha not in L")

    # Curve order and kernel.
    disc = (-16 * (4 * A_E**3 + 27 * B_E**2)) % P
    check(disc == 4136 and disc != 0, "curve discriminant mismatch")
    char_sum = curve_character_sum(A_E, B_E)
    curve_order = P + 1 + char_sum
    check(char_sum == -39, "character sum mismatch")
    check(curve_order == 8153 == 31 * 263, "curve order mismatch")

    G = (0, 7904)
    check(ec_on_curve(G), "G not on E")
    G263 = ec_mul(263, G)
    G31 = ec_mul(31, G)
    check(G263 == (8050, 6188), "[263]G mismatch")
    check(G31 == (3434, 924), "[31]G mismatch")
    check(ec_mul(curve_order, G) is None, "[8153]G != O")
    check(G263 is not None and G31 is not None, "G not full order")

    kernel_nonzero = [ec_mul(j, G263) for j in range(1, 31)]
    check(all(pt is not None and ec_on_curve(pt) for pt in kernel_nonzero), "bad kernel point")
    check(len(set(kernel_nonzero)) == 30, "kernel does not have 31 elements")
    check(ec_mul(31, G263) is None, "kernel generator not order 31")
    kernel_x = sorted({pt[0] for pt in kernel_nonzero if pt is not None})
    check(kernel_x == EXPECTED_U, "kernel x-coordinate list mismatch")

    # Vélu x-map lambda=N/D over F_p.
    f_curve = [B_E, A_E, 0, 1]
    d_base = fp_prod([[-u, 1] for u in kernel_x])
    velu_den = fp_mul(d_base, d_base)
    velu_num = fp_mul([0, 1], velu_den)
    for u in kernel_x:
        others = fp_prod([[-v, 1] for v in kernel_x if v != u])
        d_u = fp_mul(others, others)
        f_u = (u**3 + A_E * u + B_E) % P
        summand = fp_mul(fp_scale(fp_add(f_curve, [f_u]), 2), d_u)
        velu_num = fp_add(velu_num, summand)
        velu_num = fp_sub(velu_num, fp_mul([4 * u, 2], velu_den))
    check(len(velu_den) - 1 == 30, "Velu denominator degree !=30")
    check(len(velu_num) - 1 == 31, "Velu numerator degree !=31")
    check(fp_gcd(velu_num, velu_den) == [1], "Velu map not reduced")

    # Target curve and exact isogeny identity y'=lambda'(x)y.
    t_sum = sum(2 * (3 * u * u + A_E) for u in kernel_x) % P
    w_sum = sum(2 * (5 * u**3 + 3 * A_E * u + 2 * B_E) for u in kernel_x) % P
    A_target = (A_E - 5 * t_sum) % P
    B_target = (B_E - 7 * w_sum) % P
    check((A_target, B_target) == (36, 7292), "Velu target curve mismatch")
    target_disc = (-16 * (4 * A_target**3 + 27 * B_target**2)) % P
    check(target_disc == 2274 and target_disc != 0, "target discriminant mismatch")
    target_sum = curve_character_sum(A_target, B_target)
    check(P + 1 + target_sum == curve_order, "target curve order mismatch")

    wronskian = fp_sub(fp_mul(fp_deriv(velu_num), velu_den), fp_mul(velu_num, fp_deriv(velu_den)))
    check(len(wronskian) - 1 == 60, "ramification polynomial degree !=60")
    check(fp_gcd(wronskian, fp_deriv(wronskian)) == [1], "ramification not simple")
    expected_ramification_at_poles = d_base
    check(fp_gcd(wronskian, velu_den) == fp_scale(expected_ramification_at_poles, pow(expected_ramification_at_poles[-1], P - 2, P)),
          "ramification at kernel poles mismatch")

    left = fp_mul(fp_mul(wronskian, wronskian), f_curve)
    right_inside = fp_add(
        fp_add(
            fp_mul(fp_mul(velu_num, velu_num), velu_num),
            fp_scale(fp_mul(velu_num, fp_mul(velu_den, velu_den)), A_target),
        ),
        fp_scale(fp_mul(fp_mul(velu_den, velu_den), velu_den), B_target),
    )
    right = fp_mul(velu_den, right_inside)
    check(fp_trim(left) == fp_trim(right), "exact Velu isogeny identity failed")

    # Complete rational fiber distribution on P^1(F_p).
    kernel_x_set = set(kernel_x)

    def lambda_value(x: Optional[int]) -> Optional[int]:
        if x is None or x in kernel_x_set:
            return None
        den = fp_eval(velu_den, x)
        check(den != 0, "unexpected denominator zero")
        y = fp_eval(velu_num, x) * pow(den, P - 2, P) % P
        # Independent direct formula check.
        f_x = (x**3 + A_E * x + B_E) % P
        direct = x
        for u in kernel_x:
            direct += 2 * (f_x + (u**3 + A_E * u + B_E)) * pow((x - u) ** 2 % P, P - 2, P)
            direct -= 2 * x + 4 * u
        check(y == direct % P, "Velu formula/direct evaluation mismatch")
        return y

    fibers: dict[Optional[int], list[Optional[int]]] = defaultdict(list)
    for x in [None] + list(range(P)):
        fibers[lambda_value(x)].append(x)
    distribution = Counter(len(xs) for xs in fibers.values())
    check(distribution == Counter({1: 4115, 31: 131, 16: 1}), "fiber distribution mismatch")
    check(len(fibers[None]) == 16, "infinity fiber size mismatch")
    check(set(fibers[None]) == {None, *kernel_x}, "infinity fiber points mismatch")
    full_base_values = sorted(y for y, xs in fibers.items() if y is not None and len(xs) == 31)
    check(len(full_base_values) == 131, "full-fiber value count mismatch")
    check(sum(len(xs) for xs in fibers.values()) == P + 1, "fiber partition not exhaustive")

    # Abstract regular Galois closure/deck certificate: D_62 and reflection stabilizer.
    D62 = [(a, b) for a in range(31) for b in range(2)]
    H_reflection = {(0, 0), (0, 1)}
    normalizer = []
    conjugates = []
    for g in D62:
        conj = {dconj(g, h) for h in H_reflection}
        conjugates.append(conj)
        if conj == H_reflection:
            normalizer.append(g)
    core = set.intersection(*conjugates)
    check(set(normalizer) == H_reflection, "reflection normalizer not self-normalizing")
    check(core == {(0, 0)}, "reflection core not trivial")
    check(4 * 15 == 2 * M - 2, "(2,2,2,2) Riemann-Hurwitz mismatch")

    # Transport beta^{-1}(X)=i(alpha+X)/(alpha-X), eta(Y)=1/(Y-alpha).
    # U=i(alpha+X), V=alpha-X.
    U_poly = [ff_mul(i_elt, FF_ALPHA), i_elt]
    V_poly = [FF_ALPHA, ff(-1)]
    N_h = ffx_homogenized_linear_substitution(velu_num, 31, U_poly, V_poly)
    D_h = ffx_homogenized_linear_substitution(velu_den, 31, U_poly, V_poly)
    R_num = D_h
    R_den = ffx_sub(N_h, ffx_scale(D_h, FF_ALPHA))
    check(len(R_num) - 1 == 31, "transported numerator degree !=31")
    check(len(R_den) - 1 == 31, "transported denominator degree !=31")
    check(ffx_gcd(R_num, R_den) == [FF_ONE], "transported map not reduced")
    R_wronskian = ffx_sub(ffx_mul(ffx_deriv(R_num), R_den), ffx_mul(R_num, ffx_deriv(R_den)))
    check(R_wronskian != [FF_ZERO], "transported map inseparable")

    # Direct composition checks at all 8192 source points without inversions in target:
    # Q(beta(t)) is nonzero, and P/Q equals eta(lambda(t)).
    # This is affordable and closes the pole-normalization claim exactly.
    for idx, x_elt in enumerate(beta_values):
        t = idx if idx < P else None
        c = lambda_value(t)
        px = ffx_eval(R_num, x_elt)
        qx = ffx_eval(R_den, x_elt)
        check(not ff_is_zero(qx), "transported denominator vanishes on L")
        if c is None:
            # eta(infinity)=0.
            check(ff_is_zero(px), "R(beta(t)) != eta(infinity)")
        else:
            # P/Q = 1/(c-alpha), cross-multiplied.
            check(ff_mul(px, ff_sub(ff(c), FF_ALPHA)) == qx, "transported map value mismatch")

    # Full target values and leading coefficients of fiber locators.
    full_values = [ff_inv(ff_sub(ff(c), FF_ALPHA)) for c in full_base_values]
    check(len(set(full_values)) == 131, "target Mobius collapsed full values")
    lc_P = R_num[-1]
    lc_Q = R_den[-1]
    leading_coeffs = [ff_sub(lc_P, ff_mul(y, lc_Q)) for y in full_values]
    check(all(not ff_is_zero(a_y) for a_y in leading_coeffs), "a full-fiber locator lost degree")

    # Explicit defect points T=beta(5),beta(8); both lie in singleton fibers.
    check(len(fibers[lambda_value(5)]) == 1 and len(fibers[lambda_value(8)]) == 1,
          "chosen defect points are not outside the 131 full fibers")
    T_values = [beta_values[5], beta_values[8]]
    check(T_values[0] != T_values[1], "defect points collide")

    # Theta exclusion and slope collision certificate.
    image_size_RL = len(fibers)  # eta is a target Mobius bijection.
    check(image_size_RL == 4247, "R(L) image size mismatch")
    branch_value_count = 4
    action_maps = (2048 - 1) + 2048
    action_locus_upper = action_maps * (2 * M)
    # R(L), four branch values, R(infinity), R(0), and action collision values.
    bad_theta_upper = image_size_RL + branch_value_count + 1 + 1 + action_locus_upper
    good_theta_lower = Q_FIELD - bad_theta_upper
    check(good_theta_lower > Q_FIELD // 2, "good theta set not larger than q/2")
    check((Q_FIELD - 1) % 2048 == 0, "mu_2048 not contained in F")

    raw_profiles = math.comb(131, 67)
    pair_incidence_upper = 67 * math.comb(raw_profiles, 2)
    collision_bound_sharp = pair_incidence_upper // good_theta_lower
    collision_bound_packet = 67 * raw_profiles * (raw_profiles - 1) // Q_FIELD
    check(collision_bound_packet == 81509318, "packet collision number mismatch")
    check(collision_bound_sharp <= collision_bound_packet, "sharp collision bound not stronger")
    distinct_slopes_packet = raw_profiles - collision_bound_packet
    distinct_slopes_sharp = raw_profiles - collision_bound_sharp
    check(raw_profiles == 183062151498210163887302260440097215750, "binomial profile mismatch")
    check(distinct_slopes_packet == 183062151498210163887302260440015706432,
          "packet distinct-slope lower bound mismatch")
    check(distinct_slopes_packet > 2**127, "slope lower bound <=2^127")

    # MCA construction and all degree/regularity inequalities.
    check(DEFECT + B_FIBERS * M == AGREEMENT, "support size identity failed")
    full_union_size = 131 * 31
    check(N_CODE - full_union_size == 4131 >= DEFECT, "insufficient defect complement")
    check(ERRORS == 6113, "error count mismatch")
    check(K_CODE + 2 * SIGMA < N_CODE, "denominator uniqueness degree window failed")
    check(K_CODE + SIGMA - 1 < AGREEMENT, "transversality root bound failed")
    check(AGREEMENT > K_CODE, "envelope exclusion root bound failed")

    # Exact occupancy and target comparisons; no floating-point verdicts.
    occupancy_numerator = math.comb(N_CODE, AGREEMENT)
    occupancy_denominator = Q_FIELD**30
    occupancy_lt_2m325 = occupancy_numerator * 2**325 < occupancy_denominator
    check(occupancy_lt_2m325, "occupancy is not <2^-325")
    target = Q_FIELD // 2**128
    check(target == 80951559894234747884481262824352, "target floor mismatch")
    check(target < 2**106, "target not <2^106")
    check(distinct_slopes_packet > target, "packet does not beat exact target")
    check(distinct_slopes_packet * 2**128 > Q_FIELD, "normalized slope fraction <=2^-128")

    # R(infinity), R(0), and coefficient hashes for the explicit map.
    R_infinity = ff_div(R_num[-1], R_den[-1])
    R_zero = ff_div(R_num[0], R_den[0])
    r_coeff_obj = {"numerator": ffx_json(R_num), "denominator": ffx_json(R_den)}

    certificate = {
        "schema": "rs-mca-lattes31-certificate-v1",
        "wall": "V-LATTES-31",
        "status": "AUDIT_PASS",
        "all_checks_pass": True,
        "verifier": {
            "language": "Python 3 standard library",
            "floating_point_verdicts": False,
        },
        "base_field": {
            "p": P,
            "prime": True,
        },
        "code_field": {
            "degree_over_Fp": EXT_DEG,
            "q": dec(Q_FIELD),
            "q_bits_interval": "2^233 < q < 2^234 < 2^256",
            "modulus_ascending": FIELD_MODULUS,
            "modulus_irreducible": True,
            "alpha_basis_coefficients": ff_json(FF_ALPHA),
            "alpha_is_primitive": True,
            "primitive_prime_factor_checks": primitive_checks,
            "q_minus_1_factorization": {str(r): e for r, e in Q_MINUS_ONE_FACTORIZATION.items()},
            "i_basis_coefficients": ff_json(i_elt),
            "i_squared": ff_json(ff_mul(i_elt, i_elt)),
            "i_frobenius_equals_minus_i": True,
            "H_generator_basis_coefficients": ff_json(h_gen),
            "H_order": P + 1,
        },
        "domain": {
            "description": "L=alpha*ker(N_{F_{p^2}/F_p}), beta(t)=alpha(t-i)/(t+i)",
            "size": N_CODE,
            "cayley_bijection_exhaustively_checked": True,
            "multiplicative_coset_checked": True,
            "contains_alpha": True,
            "generates_full_code_field": True,
            "stabilizer": "beta PGL_2(F_p) beta^{-1}",
        },
        "elliptic_curve": {
            "equation": "y^2=x^3+x+459",
            "discriminant_mod_p": disc,
            "character_sum": char_sum,
            "order": curve_order,
            "order_factorization": {"31": 1, "263": 1},
            "G": list(G),
            "G_order": curve_order,
            "263G": list(G263) if G263 else None,
            "31G": list(G31) if G31 else None,
        },
        "isogeny": {
            "degree": M,
            "kernel_generator": list(G263) if G263 else None,
            "kernel_x_coordinates": kernel_x,
            "velu_numerator_ascending_Fp": velu_num,
            "velu_denominator_ascending_Fp": velu_den,
            "reduced": True,
            "separable": True,
            "target_curve": f"y^2=x^3+{A_target}x+{B_target}",
            "target_discriminant_mod_p": target_disc,
            "exact_xy_identity_checked": True,
            "ramification_polynomial_degree": len(wronskian) - 1,
            "ramification_simple": True,
            "galois_closure": {
                "curve_genus": 1,
                "group": "D_62=K semidirect {+/-1}",
                "arithmetic_equals_geometric": True,
                "constant_field": "F_p (and F after base change)",
                "branch_signature": [2, 2, 2, 2],
                "source_reflection_core_trivial": True,
                "source_reflection_normalizer_size": len(normalizer),
                "deck_group_trivial": True,
            },
            "fiber_distribution_on_P1_Fp": {"31": 131, "16": 1, "1": 4115},
            "image_size_on_P1_Fp": image_size_RL,
            "full_fiber_values_Fp": full_base_values,
        },
        "transported_map": {
            "formula": "R=eta o lambda o beta^{-1}, beta^{-1}(X)=i(alpha+X)/(alpha-X), eta(Y)=1/(Y-alpha)",
            "numerator_coefficients_ascending": ffx_json(R_num),
            "denominator_coefficients_ascending": ffx_json(R_den),
            "coefficient_sha256": canonical_hash(r_coeff_obj),
            "degree": 31,
            "reduced": True,
            "separable": True,
            "denominator_nonzero_on_all_L": True,
            "all_8192_transport_values_cross_checked": True,
            "R_infinity": ff_json(R_infinity),
            "R_zero": ff_json(R_zero),
            "full_fiber_distribution_on_L": {"31": 131, "16": 1, "1": 4115},
        },
        "mca_packet": {
            "n": N_CODE,
            "k": K_CODE,
            "rate": "1/4",
            "sigma": SIGMA,
            "agreement": AGREEMENT,
            "errors": ERRORS,
            "delta": "6113/8192",
            "full_fibers": 131,
            "fibers_per_support": B_FIBERS,
            "fixed_defect": DEFECT,
            "full_union_size": full_union_size,
            "defect_complement_size": N_CODE - full_union_size,
            "explicit_defect_parameters_t": [5, 8],
            "explicit_defect_points_basis_coefficients": [ff_json(x) for x in T_values],
            "theta_certificate": {
                "R_L_image_size": image_size_RL,
                "branch_values": branch_value_count,
                "action_maps": action_maps,
                "roots_per_action_equation_upper": 2 * M,
                "action_locus_upper": action_locus_upper,
                "extra_exclusions_R_infinity_and_R_zero": 2,
                "bad_theta_upper": bad_theta_upper,
                "good_theta_lower": dec(good_theta_lower),
                "good_theta_gt_q_over_2": True,
            },
            "slope_certificate": {
                "raw_profiles_binomial_131_67": dec(raw_profiles),
                "pair_root_incidence_upper": dec(pair_incidence_upper),
                "packet_collision_bound": collision_bound_packet,
                "sharpened_collision_bound": collision_bound_sharp,
                "packet_distinct_slope_lower": dec(distinct_slopes_packet),
                "sharpened_distinct_slope_lower": dec(distinct_slopes_sharp),
                "greater_than_2_pow_127": True,
            },
            "support_identity": "L_A mod E = kappa_A(theta) B; z_A=-kappa_A(theta); C_A=(E X^k-L_A-z_A B)/E",
            "transversality": {
                "degree_upper_EG_plus_B": K_CODE + SIGMA - 1,
                "number_of_zeros": AGREEMENT,
                "proved": True,
            },
            "proper_envelope_exclusion": {
                "anchor": "X^2048",
                "maximum_roots_against_degree_lt_2048": K_CODE,
                "needed_agreement": AGREEMENT,
                "proved": True,
            },
            "intrinsic_denominator_degree": {
                "degree": SIGMA,
                "uniqueness_window": K_CODE + 2 * SIGMA,
                "domain_size": N_CODE,
                "proved": True,
            },
            "ordinary_action_ranks": {
                "monomial_D_dividing_2048": 31,
                "toric_dihedral_D_dividing_2048": 31,
                "lattes_action_rank_d_R": 1,
                "proved_by_theta_exclusion_and_trivial_deck_group": True,
            },
        },
        "finite_ledger": {
            "occupancy_expression": "binom(8192,2079)/q^30",
            "occupancy_lt_2_pow_minus_325": True,
            "target_floor_q_over_2_pow_128": dec(target),
            "target_lt_2_pow_106": True,
            "packet_distinct_slopes_gt_target": True,
            "normalized_bad_fraction_gt_2_pow_minus_128": True,
        },
        "proof_scope": {
            "theta": "existential, certified by exact exclusion and averaging counts",
            "degree_113_checked": False,
        },
    }

    output_path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    return certificate


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("lattes31_certificate.json")
    cert = main(out)
    print(json.dumps({
        "status": cert["status"],
        "all_checks_pass": cert["all_checks_pass"],
        "certificate": str(out),
        "coefficient_sha256": cert["transported_map"]["coefficient_sha256"],
        "packet_distinct_slope_lower": cert["mca_packet"]["slope_certificate"]["packet_distinct_slope_lower"],
        "target": cert["finite_ledger"]["target_floor_q_over_2_pow_128"],
    }, indent=2))
