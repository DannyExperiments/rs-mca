#!/usr/bin/env python3
"""Deterministic precheck for the Cycle84 dlog/tau quotient census.

This script does NOT run the 26,373,783,552-record threshold census. It emits
all exact arithmetic data needed by that external run and verifies:
  * F_17[X]/(X^16+X^8+3) is a field;
  * eta=6X^9 has order 256 and eta^16=3;
  * beta=X+2 is admissible;
  * g=X+1 generates F^*;
  * all 336 slot values have certified discrete logs to base g;
  * the Cycle79 tau involution is exact in log coordinates;
  * q=29*18913*184417 is a divisor of |F^*| and the tau quotient data is exact.

The emitted JSON is a reproducible certificate/precomputation file, not a
certificate that m_max <= 12.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

P = 17
D = 16
N = P**D - 1
FACTOR = {2: 8, 3: 2, 5: 1, 29: 1, 18913: 1, 41761: 1, 184417: 1}
PRIME_POWERS = [p**e for p, e in FACTOR.items()]
MODULUS = (3,) + (0,) * 7 + (1,) + (0,) * 7 + (1,)  # X^16+X^8+3
ONE = (1,) + (0,) * 15
ZERO = (0,) * 16
ETA = (0,) * 9 + (6,) + (0,) * 6
BETA = (2, 1) + (0,) * 14
GENERATOR = (1, 1) + (0,) * 14
Q = 29 * 18913 * 184417

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


def mul(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    tmp = [0] * 31
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    tmp[i + j] = (tmp[i + j] + x * y) % P
    for degree in range(30, 15, -1):
        z = tmp[degree] % P
        if z:
            tmp[degree - 8] = (tmp[degree - 8] - z) % P
            tmp[degree - 16] = (tmp[degree - 16] - 3 * z) % P
    return tuple(x % P for x in tmp[:16])


def power(a: Tuple[int, ...], exponent: int) -> Tuple[int, ...]:
    result = ONE
    base = a
    while exponent:
        if exponent & 1:
            result = mul(result, base)
        base = mul(base, base)
        exponent >>= 1
    return result


def add(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple((x + y) % P for x, y in zip(a, b))


def neg(a: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple((-x) % P for x in a)


def scalar(c: int) -> Tuple[int, ...]:
    return (c % P,) + (0,) * 15


def evaluate(coeffs: Iterable[int], x: Tuple[int, ...]) -> Tuple[int, ...]:
    result = ZERO
    for c in reversed(tuple(coeffs)):
        result = add(mul(result, x), scalar(c))
    return result


def pack(a: Tuple[int, ...]) -> int:
    value = 0
    for c in reversed(a):
        value = value * P + c
    return value


def poly_trim(a: List[int]) -> List[int]:
    while a and a[-1] % P == 0:
        a.pop()
    return [x % P for x in a]


def poly_sub(a: List[int], b: List[int]) -> List[int]:
    out = [0] * max(len(a), len(b))
    for i in range(len(a)):
        out[i] = a[i]
    for i in range(len(b)):
        out[i] = (out[i] - b[i]) % P
    return poly_trim(out)


def poly_divmod(a: List[int], b: List[int]) -> Tuple[List[int], List[int]]:
    aa = poly_trim(a[:])
    bb = poly_trim(b[:])
    quotient = [0] * max(1, len(aa) - len(bb) + 1)
    inv_lead = pow(bb[-1], P - 2, P)
    while aa and len(aa) >= len(bb):
        shift = len(aa) - len(bb)
        c = aa[-1] * inv_lead % P
        quotient[shift] = c
        for i, y in enumerate(bb):
            aa[shift + i] = (aa[shift + i] - c * y) % P
        aa = poly_trim(aa)
    return poly_trim(quotient), aa


def poly_gcd(a: List[int], b: List[int]) -> List[int]:
    aa, bb = poly_trim(a), poly_trim(b)
    while bb:
        _, rem = poly_divmod(aa, bb)
        aa, bb = bb, rem
    if aa:
        inv = pow(aa[-1], P - 2, P)
        aa = [(x * inv) % P for x in aa]
    return aa


def build_slot_values() -> Dict[Tuple[int, int, int], Tuple[int, ...]]:
    xi = power(BETA, 2)
    eta_inv = power(ETA, N - 1)
    table: Dict[Tuple[int, int, int], Tuple[int, ...]] = {}
    for t in range(1, 8):
        eta_factor = power(eta_inv, 2 * t)
        for i in (1, 2, 3):
            for a in range(16):
                arg = mul(mul(xi, scalar(pow(3, (-a) % 16, P))), eta_factor)
                value = evaluate(P_COEFFS[i], arg)
                if a & 1:
                    value = neg(value)
                assert value != ZERO
                table[(t, i, a)] = value
    return table


def subgroup_log_tables() -> List[Dict[int, int]]:
    tables: List[Dict[int, int]] = []
    for order in PRIME_POWERS:
        step = power(GENERATOR, N // order)
        current = ONE
        lookup: Dict[int, int] = {}
        for exponent in range(order):
            key = pack(current)
            assert key not in lookup
            lookup[key] = exponent
            current = mul(current, step)
        assert current == ONE and len(lookup) == order
        tables.append(lookup)
    return tables


def crt_terms() -> List[int]:
    terms = []
    for modulus in PRIME_POWERS:
        cofactor = N // modulus
        terms.append((cofactor * pow(cofactor, -1, modulus)) % N)
    return terms


def discrete_log(h: Tuple[int, ...], tables: List[Dict[int, int]], terms: List[int]) -> int:
    residues = []
    for order, lookup in zip(PRIME_POWERS, tables):
        projected = power(h, N // order)
        residues.append(lookup[pack(projected)])
    exponent = sum(r * term for r, term in zip(residues, terms)) % N
    assert power(GENERATOR, exponent) == h
    return exponent


def tau(i: int, a: int) -> Tuple[int, int]:
    if i == 1:
        return 2, (a + 6) % 16
    if i == 2:
        return 1, (a + 10) % 16
    return 3, (a + 8) % 16


def color(i: int, a: int) -> int:
    return (S_COLOR[i] + 8 * (a & 1)) % 16


def main() -> None:
    # Irreducibility criterion for degree 16 (only prime divisor of 16 is 2).
    x = (0, 1) + (0,) * 14
    assert power(x, P**16) == x
    x8_minus_x = list(add(power(x, P**8), neg(x)))
    assert poly_gcd(list(MODULUS), x8_minus_x) == [1]

    assert power(ETA, 16) == scalar(3)
    assert power(ETA, 256) == ONE and power(ETA, 128) != ONE
    assert power(BETA, 256) != ONE
    assert Q == 101_148_482_909 and N % Q == 0

    # Primitive generator certificate.
    for prime in FACTOR:
        assert power(GENERATOR, N // prime) != ONE

    table = build_slot_values()
    log_tables = subgroup_log_tables()
    terms = crt_terms()
    logs = {key: discrete_log(value, log_tables, terms) for key, value in table.items()}
    assert len(set(logs.values())) == 336

    slot_constants = []
    for t in range(1, 8):
        constants = set()
        for i in (1, 2, 3):
            for a in range(16):
                j, b = tau(i, a)
                constants.add((logs[(t, i, a)] + logs[(t, j, b)]) % N)
                assert color(j, b) == (8 - color(i, a)) % 16
        assert len(constants) == 1
        slot_constants.append(next(iter(constants)))
    kappa = sum(slot_constants) % N
    assert kappa == 28_612_129_440_766_144_972

    # One representative per global tau orbit is selected by slot 1 alone.
    representatives = []
    for k in range(48):
        i, a = k // 16 + 1, k % 16
        j, b = tau(i, a)
        tau_k = (j - 1) * 16 + b
        if k < tau_k:
            representatives.append(k)
    assert representatives == list(range(16)) + list(range(32, 40))

    kappa_q = kappa % Q
    fixed_q = (kappa_q * pow(2, -1, Q)) % Q
    assert kappa_q == 50_517_414_113
    assert fixed_q == 75_832_948_511

    # Count the color shell and its tau-orbit representatives exactly.
    dp = [0] * 16
    dp[0] = 1
    for _ in range(7):
        nxt = [0] * 16
        for total in range(16):
            for i in (1, 2, 3):
                for a in range(16):
                    nxt[(total + color(i, a)) % 16] += dp[total]
        dp = nxt
    p0 = dp[4]
    assert p0 == 52_747_567_104
    assert p0 % 2 == 0

    records = []
    for t in range(1, 8):
        for i in (1, 2, 3):
            for a in range(16):
                records.append(
                    {
                        "t": t,
                        "i": i,
                        "a": a,
                        "k": (i - 1) * 16 + a,
                        "color": color(i, a),
                        "log_g": logs[(t, i, a)],
                        "log_mod_q": logs[(t, i, a)] % Q,
                    }
                )
    canonical_blob = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()

    certificate = {
        "decision": "DLOG_TAU_QUOTIENT_PRECHECK_PASS__FULL_CENSUS_UNRUN",
        "model": {
            "p": P,
            "degree": D,
            "field_polynomial_coefficients_low_to_high": list(MODULUS),
            "eta_coefficients": list(ETA),
            "beta_coefficients": list(BETA),
            "generator_coefficients": list(GENERATOR),
        },
        "group": {
            "order": N,
            "factorization": {str(p): e for p, e in FACTOR.items()},
            "generator_primitive_prime_divisor_tests": sorted(FACTOR),
        },
        "tau": {
            "slot_log_constants": slot_constants,
            "kappa_log_g": kappa,
            "slot1_orbit_representatives_k": representatives,
            "domain_orbits": p0 // 2,
        },
        "quotient": {
            "q": Q,
            "factorization": {"29": 1, "18913": 1, "184417": 1},
            "kernel_order": N // Q,
            "kappa_mod_q": kappa_q,
            "unique_fixed_residue": fixed_q,
            "nonfixed_tau_orbits": (Q - 1) // 2,
            "saturated_counter_bits": 4,
            "packed_counter_bytes": (Q - 1) // 4,
        },
        "shell": {"target_color": 4, "P0": p0, "tau_orbit_representatives": p0 // 2},
        "slot_log_records_sha256": hashlib.sha256(canonical_blob).hexdigest(),
        "slot_log_records": records,
        "external_checker_contract": {
            "pass1": "enumerate k1 in H and all compatible k2..k7; for nonfixed q-orbits saturate a 4-bit counter at 13; record every orbit first reaching 13; route the unique fixed q-residue to exact recount",
            "pass2": "re-enumerate only recorded q-orbits plus the fixed q-residue; count exact canonical logs e~kappa-e in Z/N; threshold 13 for nonselfdual keys and 7 tau-orbits for selfdual keys",
            "pass": "no exact key reaches its threshold",
            "fail": "emit 13 oriented tuples with one exact common log/product",
        },
    }

    out = Path("/mnt/data/cycle84_dlog_tau_quotient_precheck_certificate.json")
    out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: certificate[k] for k in ("decision", "group", "tau", "quotient", "shell", "slot_log_records_sha256")}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
