#!/usr/bin/env python3
"""Exact verifier for the F_11 counterpacket in ROLE_05_T1_MCA_GJ_COLOR_RESULT.md."""

P = 11
D = tuple(range(7))
S = (9, 0, 0, 2)
R = 4


def mod(x: int) -> int:
    return x % P


def moments(T: tuple[int, ...], c: tuple[int, ...], top: int) -> tuple[int, ...]:
    return tuple(mod(sum(ci * pow(x, m, P) for x, ci in zip(T, c))) for m in range(top + 1))


def mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = mod(out[i + j] + ai * bj)
    return tuple(out)


def locator(T: tuple[int, ...]) -> tuple[int, ...]:
    out = (1,)
    for x in T:
        out = mul(out, (mod(-x), 1))
    return out


A = (0, 1, 0)       # homogeneous degree 2: X_0 X_1
B = (1, 0, 0, 1)    # homogeneous degree 3: X_0^3 + X_1^3
packets = (
    ((1, 2, 5), (6, 7, 7), (6, 3, 1)),
    ((4, 5, 6), (3, 4, 2), (8, 7, 1)),
)

# Apolar checks: A has shifts 0,1; B has shift 0.
assert mod(sum(A[i] * S[i] for i in range(3))) == 0
assert mod(sum(A[i] * S[i + 1] for i in range(3))) == 0
assert mod(sum(B[i] * S[i] for i in range(4))) == 0

colors = []
for T, c, (u0, u1, gamma) in packets:
    ms = moments(T, c, R)
    assert ms[:R] == S
    P_T = locator(T)
    expected = (
        mod(gamma * B[0]),
        mod(u0 + gamma * B[1]),
        mod(u1 + gamma * B[2]),
        mod(gamma * B[3]),
    )
    assert P_T == expected
    assert gamma == 1
    chi = mod(-ms[R])
    assert chi == mod(2 * u1)
    colors.append(chi)

assert colors == [6, 3]
assert len(set(colors)) == 2
print("verified: same old scalar lift gamma=1, distinct reduced colors 6 and 3")
