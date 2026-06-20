#!/usr/bin/env python3
"""Exact Cycle 84 checker for the two tau-self-paired fibers.

Model:
  F = F_17[X]/(X^16 + X^8 + 3)
  eta = 6 X^9, beta = X+2
  48 legal symbols per slot, colors from Cycle 68.

The checker:
  1. constructs all 336 exact slot values;
  2. proves g=X+1 generates F^* using the complete factorization of 17^16-1;
  3. computes and verifies exact discrete logs of all slot values by BSGS/CRT;
  4. computes the global tau constant K and its two square roots;
  5. performs an exact color-filtered 3+4 MITM lookup for both roots.

It emits TAU_FIXED_FIBERS_EMPTY exactly when both self-paired fibers have
multiplicity zero.  No probabilistic hashing is used.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
import argparse

import numpy as np

P = 17
NDEG = 16
N = P**NDEG - 1
PRIME_POWERS = (256, 9, 5, 29, 18913, 41761, 184417)
PRIMES = (2, 3, 5, 29, 18913, 41761, 184417)
assert math.prod(PRIME_POWERS) == N

# X^16 + X^8 + 3
F = (3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
ONE = (1,)
ETA = (0, 0, 0, 0, 0, 0, 0, 0, 0, 6)  # 6 X^9
BETA = (2, 1)                              # X+2
GEN = (1, 1)                               # X+1

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


def is_prime(n):
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


def trim(a):
    b = list(a)
    while b and b[-1] % P == 0:
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
                if y:
                    r[i + j] = (r[i + j] + x * y) % P
    return trim(r)


def pdivmod(a, b):
    aa = [x % P for x in a]
    bb = list(trim(b))
    if not bb:
        raise ZeroDivisionError
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
        aa = tuple((x * inv) % P for x in aa)
    return aa


def fmul(a, b):
    return pmod(pmul(a, b), F)


def fpow(a, e):
    r = ONE
    base = pmod(a, F)
    while e:
        if e & 1:
            r = fmul(r, base)
        base = fmul(base, base)
        e >>= 1
    return trim(r)


def emb(c):
    c %= P
    return (c,) if c else ()


def peval(i, z):
    r = ()
    for c in reversed(P_COEFFS[i]):
        r = padd(fmul(r, z), emb(c))
    return r


def build_u():
    # Irreducibility criterion for degree 16=2^4 over F_17.
    x = (0, 1)
    assert psub(fpow(x, P**16), x) == ()
    assert pgcd(psub(fpow(x, P**8), x), F) == ONE
    assert fpow(ETA, 16) == emb(3)
    assert fpow(ETA, 128) != ONE and fpow(ETA, 256) == ONE
    assert fpow(BETA, 256) != ONE
    xi = fpow(BETA, 2)
    einv = fpow(ETA, N - 1)
    table = {}
    for t in range(1, 8):
        ef = fpow(einv, 2 * t)
        for i in (1, 2, 3):
            for a in range(16):
                arg = fmul(fmul(xi, emb(pow(3, (-a) % 16, P))), ef)
                u = peval(i, arg)
                if a & 1:
                    u = psub((), u)
                assert u
                table[(t, i, a)] = u
    return table


def tau(i, a):
    if i == 1:
        return 2, (a + 6) % 16
    if i == 2:
        return 1, (a + 10) % 16
    if i == 3:
        return 3, (a + 8) % 16
    raise ValueError(i)


def color(k):
    i, a = k // 16 + 1, k % 16
    return (S_COLOR[i] + 8 * (a & 1)) % 16


def bsgs_setup(gen, order):
    m = math.isqrt(order)
    if m * m < order:
        m += 1
    baby = {}
    cur = ONE
    for j in range(m):
        baby.setdefault(cur, j)
        cur = fmul(cur, gen)
    factor = fpow(gen, (-m) % order)
    return m, baby, factor


def crt(residues, moduli):
    M = math.prod(moduli)
    x = 0
    for a, m in zip(residues, moduli):
        Mi = M // m
        x = (x + a * Mi * pow(Mi, -1, m)) % M
    return x


def compute_logs(table):
    # Exact generator proof because N is completely factored.
    assert all(is_prime(p) for p in PRIMES)
    generator_checks = {str(p): fpow(GEN, N // p) != ONE for p in PRIMES}
    assert all(generator_checks.values())
    setups = {}
    for order in PRIME_POWERS:
        gm = fpow(GEN, N // order)
        assert fpow(gm, order) == ONE
        setups[order] = (gm, *bsgs_setup(gm, order))

    def dlog_sub(h, order):
        gm, m, baby, factor = setups[order]
        target = fpow(h, N // order)
        gamma = target
        for i in range(m + 1):
            j = baby.get(gamma)
            if j is not None:
                x = (i * m + j) % order
                if fpow(gm, x) == target:
                    return x
            gamma = fmul(gamma, factor)
        raise RuntimeError("subgroup dlog failed")

    logs = {}
    for key, h in table.items():
        residues = [dlog_sub(h, order) for order in PRIME_POWERS]
        x = crt(residues, PRIME_POWERS)
        assert fpow(GEN, x) == h
        logs[key] = x
    return logs, generator_checks


def subset_arrays(slots, slotA, slotB, slot_colors, A, B):
    sa = np.array([0], dtype=np.uint64)
    sb = np.array([0], dtype=np.uint64)
    cc = np.array([0], dtype=np.uint8)
    for t in slots:
        sa = ((sa[:, None] + slotA[t][None, :]) % A).ravel()
        sb = ((sb[:, None] + slotB[t][None, :]) % B).ravel()
        cc = ((cc[:, None] + slot_colors[None, :]) % 16).ravel()
    return sa, sb, cc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=None)
    args = ap.parse_args()

    table = build_u()
    logs, generator_checks = compute_logs(table)

    # Tau pairing constants and global K.
    klogs = {}
    for t in range(1, 8):
        vals = set()
        for i in (1, 2, 3):
            for a in range(16):
                j, b = tau(i, a)
                vals.add((logs[(t, i, a)] + logs[(t, j, b)]) % N)
        assert len(vals) == 1
        klogs[t] = vals.pop()
    Klog = sum(klogs.values()) % N
    K = fpow(GEN, Klog)
    assert Klog % 2 == 0
    root_logs = [Klog // 2, Klog // 2 + N // 2]
    roots = [fpow(GEN, s) for s in root_logs]
    assert roots[1] == psub((), roots[0])
    assert all(fmul(r, r) == K for r in roots)

    # Split N into two coprime factors that each fit uint64.
    A = 256 * 9 * 5 * 29
    B = 18913 * 41761 * 184417
    assert math.gcd(A, B) == 1 and A * B == N

    slotA = {
        t: np.array([logs[(t, k // 16 + 1, k % 16)] % A for k in range(48)],
                    dtype=np.uint64)
        for t in range(1, 8)
    }
    slotB = {
        t: np.array([logs[(t, k // 16 + 1, k % 16)] % B for k in range(48)],
                    dtype=np.uint64)
        for t in range(1, 8)
    }
    slot_colors = np.array([color(k) for k in range(48)], dtype=np.uint8)

    LA, LB, LC = subset_arrays((1, 2, 3), slotA, slotB, slot_colors, A, B)
    RA, RB, RC = subset_arrays((4, 5, 6, 7), slotA, slotB, slot_colors, A, B)
    assert len(LA) == 48**3 and len(RA) == 48**4

    # Exact lexicographic index by (right color, residue mod A, residue mod B).
    gid = (RC.astype(np.uint64) * A + RA).astype(np.uint64)
    order = np.lexsort((RB, gid))
    gid_sorted = gid[order]
    RB_sorted = RB[order]
    nbins = 16 * A
    counts = np.bincount(gid.astype(np.int64), minlength=nbins)
    starts = np.empty(nbins + 1, dtype=np.int64)
    starts[0] = 0
    np.cumsum(counts, out=starts[1:])
    assert np.all(gid_sorted[:-1] <= gid_sorted[1:])

    def count_target(target):
        ta, tb = target % A, target % B
        total = 0
        for idx in range(len(LA)):
            needed_color = (4 - int(LC[idx])) % 16
            qa = (ta - int(LA[idx])) % A
            qb = (tb - int(LB[idx])) % B
            group = needed_color * A + qa
            lo, hi = int(starts[group]), int(starts[group + 1])
            if lo == hi:
                continue
            pos = int(np.searchsorted(RB_sorted[lo:hi], qb, side="left"))
            j = lo + pos
            while j < hi and int(RB_sorted[j]) == qb:
                total += 1
                j += 1
        return total

    root_counts = [count_target(s) for s in root_logs]

    # Stable digest of exact slot logs in canonical key order.
    h = hashlib.sha256()
    for t in range(1, 8):
        for i in (1, 2, 3):
            for a in range(16):
                h.update(int(logs[(t, i, a)]).to_bytes(9, "little"))
    out = {
        "decision": (
            "TAU_FIXED_FIBERS_EMPTY"
            if root_counts == [0, 0]
            else "TAU_FIXED_FIBER_OCCUPIED"
        ),
        "model": {
            "field_poly_coeffs_low_to_high": list(F),
            "eta_coeffs_low_to_high": list(ETA),
            "beta_coeffs_low_to_high": list(BETA),
            "generator_coeffs_low_to_high": list(GEN),
            "group_order": N,
            "group_order_factorization": {
                "2": 8, "3": 2, "5": 1, "29": 1,
                "18913": 1, "41761": 1, "184417": 1
            },
        },
        "field_irreducibility_verified": True,
        "prime_factor_primality_verified": True,
        "generator_checks": generator_checks,
        "all_336_slot_dlogs_verified": True,
        "slot_log_table_sha256": h.hexdigest(),
        "tau_slot_constant_logs": {str(t): klogs[t] for t in range(1, 8)},
        "tau_global_K_log": Klog,
        "tau_global_K_coeffs_low_to_high": list(K),
        "self_paired_target_logs": root_logs,
        "self_paired_target_coeffs_low_to_high": [list(r) for r in roots],
        "self_paired_target_multiplicities": root_counts,
        "left_records": int(len(LA)),
        "right_records": int(len(RA)),
        "domain_filter": "left_color + right_color == 4 mod 16",
        "equality_key": "exact discrete log modulo 17^16-1, represented by CRT(A,B)",
        "crt_moduli": [A, B],
        "consequence_if_empty": (
            "all occupied tau-orbits have two distinct product values; "
            "therefore m_max>=13 forces ordered off-diagonal energy >=312, "
            "so energy<=311 implies m_max<=12"
        ),
    }
    text = json.dumps(out, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
