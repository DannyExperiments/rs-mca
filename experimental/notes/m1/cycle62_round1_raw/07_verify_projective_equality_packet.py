#!/usr/bin/env python3
"""Exact verifier for the Cycle 60 projective equality-scale packet.

The script verifies all finite arithmetic and the symbolic coefficient identities
used in the existence proof.  It does not enumerate GF(p^8); the admissible
parameter is certified by an exact forbidden-value count strictly below p^8.
"""
from __future__ import annotations

import json
from math import comb, gcd, isqrt
from pathlib import Path

try:
    import sympy as sp
except ImportError as exc:  # pragma: no cover
    raise SystemExit("sympy is required for the symbolic identity check") from exc


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def multiplicative_order(a: int, modulus: int) -> int:
    assert gcd(a, modulus) == 1
    x = 1
    for order in range(1, modulus):
        x = (x * a) % modulus
        if x == 1:
            return order
    raise AssertionError("order not found")


p = 2**19 - 1
n = 2**19
k = 2**17
M = sigma = 2**14
a = k + sigma
j = n - a
r = n - k
q_gen = p**2
q_line = q_chal = p**8
T_F = q_line // 2**128
omega_size = n // M
slope_count = comb(omega_size, a // M)

# Field and divisibility ledger.
assert is_prime_trial(p)
assert n == p + 1
assert k == n // 4
assert M == sigma == n // 32
assert a == 9 * M
assert j == 23 * M
assert r == 24 * M
assert gcd(M, p) == 1
assert q_line < 2**256
assert k <= 2**40

# The element 2 has exact order 19 modulo p.  Consequently 2^M != +/-1,
# which proves 1-y*2^M != 0 for y in H^M.
ord_2 = multiplicative_order(2, p)
assert ord_2 == 19
assert gcd(ord_2, 2 * M) == 1
assert pow(2, M, p) not in (1, p - 1)

# Exact block and slope counts.
assert omega_size == 32
assert a // M == 9
assert slope_count == 28_048_800

# Pairwise slope-collision union bound: each nonzero collision polynomial has
# degree at most 9.
slope_collision_upper = 9 * comb(slope_count, 2)
assert slope_collision_upper == 3_540_308_190_260_400
assert slope_collision_upper < 2**52  # stronger than the source's < 2^53

# Symbolic action-collision equation:
# psi(hX)=zeta psi(X) iff
# (hX+2)(2X+1)-zeta(X+2)(2hX+1)=0.
X, h, zeta = sp.symbols("X h zeta")
action_poly = sp.expand((h * X + 2) * (2 * X + 1) - zeta * (X + 2) * (2 * h * X + 1))
expected = 2 * h * (1 - zeta) * X**2 + (h + 4 - zeta * (1 + 4 * h)) * X + 2 * (1 - zeta)
assert sp.expand(action_poly - expected) == 0
# Since p != 2,3, all three coefficients vanish only for zeta=1 and h=1.
assert p % 2 != 0 and p % 3 != 0

action_collision_upper = 2 * k * M
assert action_collision_upper == 2**32

# Base exclusions: Omega (32 values), theta=0, theta=2^M, theta=2^{-M}.
base_exclusion_upper = omega_size + 3
forbidden_upper = slope_collision_upper + action_collision_upper + base_exclusion_upper
admissible_theta_lower = q_line - forbidden_upper
assert forbidden_upper == 3_540_312_485_227_731
assert admissible_theta_lower > 0
assert q_line > 2**144

# Exact target.  Record the binary-division remainder as an additional check.
target_remainder = q_line - T_F * 2**128
assert T_F == 2**24 - 256 == 16_776_960
assert 0 <= target_remainder < 2**128
assert slope_count > T_F

# Tangent and inherited monomial-profile ledgers.
assert j == 376_832 < T_F
profile_terms = [comb(31, 8), comb(15, 4), comb(7, 2), comb(3, 1)]
profile_sum = sum(profile_terms)
assert profile_terms == [7_888_725, 1_365, 21, 3]
assert profile_sum == 7_890_114 < T_F

# Exact integer certificates for occupancy and generated-field entropy.
# binom(n,a) < 2^n.  q_line > 2^144, so q_line^(sigma-1) > 2^(144(sigma-1)).
occupancy_denominator_bit_lower = 144 * (sigma - 1)
assert occupancy_denominator_bit_lower > n
# q_gen > 2^36 and binom(n,a) < 2^n imply a strict surplus > 36*sigma-n.
entropy_surplus_lower = 36 * sigma - n
assert q_gen > 2**36
assert entropy_surplus_lower == 65_536

certificate = {
    "verdict": "AUDIT_PASS",
    "parameters": {
        "p": p,
        "n": n,
        "k": k,
        "M": M,
        "sigma": sigma,
        "a": a,
        "j": j,
        "q_gen": q_gen,
        "q_line": q_line,
    },
    "field_checks": {
        "p_prime": True,
        "ord_p_2": ord_2,
        "two_to_M_mod_p": pow(2, M, p),
        "omega_size": omega_size,
    },
    "theta_existence": {
        "slope_collision_upper": slope_collision_upper,
        "action_collision_upper": action_collision_upper,
        "base_exclusion_upper": base_exclusion_upper,
        "total_forbidden_upper": forbidden_upper,
        "field_size": q_line,
        "admissible_theta_lower_bound": admissible_theta_lower,
    },
    "packet_counts": {
        "distinct_slopes": slope_count,
        "target_T_F": T_F,
        "target_remainder": target_remainder,
        "excess_over_target": slope_count - T_F,
        "tangent_j": j,
        "monomial_profile_terms": profile_terms,
        "monomial_profile_sum": profile_sum,
    },
    "entropy_occupancy": {
        "occupancy_denominator_bit_lower": occupancy_denominator_bit_lower,
        "binomial_bit_upper": n,
        "generated_entropy_surplus_strictly_greater_than": entropy_surplus_lower,
    },
    "symbolic_action_polynomial": str(action_poly),
    "formal_lemmas_used": [
        "Finite-field multiplicative groups are cyclic.",
        "For squarefree E, the minimal polynomial degree of [X^D] equals the number of distinct geometric D-th-power values on roots of E.",
        "A nonzero degree-d polynomial has at most d roots.",
        "An RS syndrome lies in V_T iff the word agrees with a degree-<k polynomial off T.",
    ],
}

out = Path("/mnt/data/projective_equality_packet_certificate.json")
out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(certificate, indent=2, sort_keys=True))
print(f"WROTE {out}")
