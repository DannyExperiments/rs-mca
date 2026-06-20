#!/usr/bin/env python3
"""Exact verifier for the Cycle 62 ROLE_04 model-GJ counterpacket.

No external packages are used.  The script checks:
  * the Pocklington certificate for the 133-bit prime q;
  * the order-256 domain generator;
  * the exact fixed-product bucket count;
  * an explicit base support and a second support in the same bucket;
  * the model-modulus restriction congruences for those support locators;
  * the exact target and Q_per/occupancy inequalities.

The universal full-coordinate and all-members restriction assertions are proved
symbolically in the accompanying report; this script verifies their finite
arithmetic inputs.
"""

from math import comb, gcd, isqrt

Q = 21 * (1 << 128) + 1
N = 256
K_DIM = 128
R = 128
SIGMA = 4
J = 124
TARGET = Q // (1 << 128)


def mul_poly(a: list[int], b: list[int], mod: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % mod
    return out


def locator_coefficients(omega: int, labels: set[int]) -> list[int]:
    """Coefficients of P(1,t), ascending in t."""
    roots = [pow(omega, e, Q) for e in (0, 64, 1, 65)]
    p = [1]
    for root in roots:
        p = mul_poly(p, [1, -root % Q], Q)
    for a in sorted(labels):
        p = mul_poly(p, [1, 0, 0, 0, -pow(omega, 4 * a, Q) % Q], Q)
    return p


def bucket_counts() -> list[int]:
    # 30-subsets of Z/64Z avoiding labels 0 and 1, classified by exponent sum.
    dp = [[0] * 64 for _ in range(31)]
    dp[0][0] = 1
    for a in range(2, 64):
        for ell in range(30, 0, -1):
            for s, value in enumerate(dp[ell - 1]):
                if value:
                    dp[ell][(s + a) % 64] += value
    return dp[30]


def main() -> None:
    # Complete factorization Q-1 = 2^128 * 3 * 7 and Pocklington witness 5.
    assert Q - 1 == (1 << 128) * 3 * 7
    assert Q - 1 > isqrt(Q)
    assert pow(5, Q - 1, Q) == 1
    expected_residues = {
        2: 7145929705339707732730866756067132440576,
        3: 6926644114561205365636538732032677850943,
        7: 819384134099699443468573954699378903498,
    }
    for prime_factor, expected in expected_residues.items():
        residue = pow(5, (Q - 1) // prime_factor, Q)
        assert residue == expected
        assert gcd(residue - 1, Q) == 1

    omega = pow(5, (Q - 1) // N, Q)
    assert omega == 3280346933828309263869282213710358210492
    assert pow(omega, N, Q) == 1
    assert pow(omega, N // 2, Q) == Q - 1

    # Exact bucket and explicit supports.
    counts = bucket_counts()
    assert sum(counts) == comb(62, 30)
    assert max(counts) == 7045058086196679
    assert counts[15] == 7045058086196679

    labels0 = set(range(3, 31)) | {32, 33}
    labels1 = (labels0 - {3, 33}) | {2, 34}
    assert len(labels0) == len(labels1) == 30
    assert sum(labels0) % 64 == sum(labels1) % 64 == 15
    assert labels0 != labels1
    assert labels0 <= set(range(2, 64))
    assert labels1 <= set(range(2, 64))

    # P_A-P_B is divisible by X Z^4: in P(1,t), coefficients t^0..t^3
    # and t^124 agree.  (All intermediate terms automatically represent the
    # quotient by Z^4; equality of top coefficient supplies the X factor.)
    p0 = locator_coefficients(omega, labels0)
    p1 = locator_coefficients(omega, labels1)
    assert len(p0) == len(p1) == J + 1
    assert p0[:4] == p1[:4]
    assert p0[J] == p1[J]
    assert p0 != p1
    assert p0[J] == pow(omega, 190, Q)

    # Parameter ledger and finite target.
    assert N - K_DIM == R
    assert J == R - SIGMA
    assert 5 + J == R + 1
    assert Q.bit_length() == 133
    assert Q < 1 << 256
    assert K_DIM <= 1 << 40
    assert TARGET == 21
    assert counts[15] > TARGET

    total_supports = comb(N, J)
    geff = N * Q**3
    qper_kernel = 2 * Q**2
    assert 882 * total_supports < qper_kernel
    # Equivalently N_Qper(pi b)/|ker pi| < 1/882 for every target b.
    assert total_supports * 882 < 2 * Q**2
    # The raw occupancy is below 1/(21^3*2^136).
    assert total_supports * (21**3) * (1 << 136) < geff

    print("ROLE_04 counterpacket verification: PASS")
    print(f"q = {Q}")
    print(f"omega = {omega}")
    print(f"bucket size = {counts[15]:,}")
    print(f"T_q = {TARGET}")
    print(f"|G_eff| = 256*q^3 = {geff}")
    print(f"|ker(pi_per)| = 2*q^2 = {qper_kernel}")
    print(f"binom(256,124) = {total_supports}")


if __name__ == "__main__":
    main()
