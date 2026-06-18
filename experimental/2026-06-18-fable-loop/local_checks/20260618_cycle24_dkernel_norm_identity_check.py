#!/usr/bin/env python3
"""Cycle 24 D-kernel norm identity checker.

Experimental consistency only, not a proof.  Checks the restricted
B=F_p, F=F_{p^2}, D=F_p, t=2, j=3 identities:

  ell=[X^p-X]_E=mu*(xi+c/2)+delta_c
  D=N(ell)*kappa
  N(ell)=prod_{a in F_p}E(a)=delta_c^2-mu^2*(c^2/4-d)

It also samples off-R0 pairs and verifies that source-valid denominators
nonzero on D=F_p never give D=0.
"""

from __future__ import annotations


def find_nonresidue(p):
    squares = {(i * i) % p for i in range(p)}
    for a in range(2, p):
        if a not in squares:
            return a
    raise ValueError(p)


def fadd(p, x, y):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def fsub(p, x, y):
    return ((x[0] - y[0]) % p, (x[1] - y[1]) % p)


def fmul(p, nr, x, y):
    return (
        (x[0] * y[0] + nr * x[1] * y[1]) % p,
        (x[0] * y[1] + x[1] * y[0]) % p,
    )


def fpow(p, nr, x, e):
    out = (1, 0)
    while e:
        if e & 1:
            out = fmul(p, nr, out, x)
        x = fmul(p, nr, x, x)
        e >>= 1
    return out


def ftau(p, x):
    return (x[0] % p, (-x[1]) % p)


def finv(p, nr, x):
    norm = (x[0] * x[0] - nr * x[1] * x[1]) % p
    inv_norm = pow(norm, p - 2, p)
    return ((x[0] * inv_norm) % p, ((-x[1]) * inv_norm) % p)


def amul(p, nr, c, d, x, y):
    m = lambda a, b: fmul(p, nr, a, b)
    z0 = fsub(p, m(x[0], y[0]), m(d, m(x[1], y[1])))
    z1 = fsub(p, fadd(p, m(x[0], y[1]), m(x[1], y[0])), m(c, m(x[1], y[1])))
    return (z0, z1)


def axipow(p, nr, c, d, e):
    out = ((1, 0), (0, 0))
    base = ((0, 0), (1, 0))
    while e:
        if e & 1:
            out = amul(p, nr, c, d, out, base)
        base = amul(p, nr, c, d, base, base)
        e >>= 1
    return out


def wedge(p, nr, x, y):
    return fsub(p, fmul(p, nr, x[0], y[1]), fmul(p, nr, x[1], y[0]))


def pe(p, nr, c, d, x, y):
    m = lambda a, b: fmul(p, nr, a, b)
    return fadd(p, fsub(p, m(x[0], y[0]), m(c, m(x[0], y[1]))), m(d, m(x[1], y[1])))


def eval_e(p, nr, c, d, a):
    aa = (a, 0)
    return fadd(p, fadd(p, fmul(p, nr, aa, aa), fmul(p, nr, c, aa)), d)


def has_base_root(p, nr, c, d):
    return any(eval_e(p, nr, c, d, a) == (0, 0) for a in range(p))


def separated_from_frobenius(p, nr, c, d):
    """Return gcd(E,E^tau)=1 for quadratic E=X^2+cX+d."""
    c_tau, d_tau = ftau(p, c), ftau(p, d)
    if c == c_tau and d == d_tau:
        return False
    if c == c_tau:
        return True
    root = fmul(p, nr, fsub(p, d_tau, d), finv(p, nr, fsub(p, c, c_tau)))
    return fadd(p, fadd(p, fmul(p, nr, root, root), fmul(p, nr, c, root)), d) != (0, 0)


def run(p):
    nr = find_nonresidue(p)
    inv2 = pow(2, p - 2, p)
    inv4 = pow(4, p - 2, p)
    xi = ((0, 0), (1, 0))
    samples = [((1, 0), (0, 1)), ((1, 1), (2, 3)), ((2, 1), (1, 4)), ((3, 2), (5, 1))]
    checked = 0
    source_valid_checked = 0
    separated_checked = 0
    d0_off_r0 = 0
    d0_has_root = 0

    for c0 in range(p):
        for c1 in range(p):
            c = (c0, c1)
            half_c = fmul(p, nr, c, (inv2, 0))
            s = (half_c, (1, 0))
            delta_c = fmul(p, nr, fsub(p, c, ftau(p, c)), (inv2, 0))
            for d0 in range(p):
                for d1 in range(p):
                    d = (d0, d1)
                    w = fsub(p, fmul(p, nr, fmul(p, nr, c, c), (inv4, 0)), d)
                    nu = fpow(p, nr, w, (p - 1) // 2) if w != (0, 0) else (0, 0)
                    mu = fsub(p, nu, (1, 0))
                    ell_closed = (fadd(p, fmul(p, nr, mu, s[0]), delta_c), fmul(p, nr, mu, s[1]))
                    xip = axipow(p, nr, c, d, p)
                    ell = (fsub(p, xip[0], xi[0]), fsub(p, xip[1], xi[1]))
                    assert ell == ell_closed, (p, c, d, ell, ell_closed)

                    n_ell = pe(p, nr, c, d, ell, ell)
                    prod_e = (1, 0)
                    for a in range(p):
                        prod_e = fmul(p, nr, prod_e, eval_e(p, nr, c, d, a))
                    assert n_ell == prod_e, (p, c, d, n_ell, prod_e)

                    lam = fsub(p, fmul(p, nr, delta_c, delta_c), fmul(p, nr, fmul(p, nr, mu, mu), w))
                    assert lam == n_ell, (p, c, d, lam, n_ell)

                    source_valid = not has_base_root(p, nr, c, d)
                    separated = separated_from_frobenius(p, nr, c, d)
                    for (u0, u1), (b0, b1) in samples:
                        u = ((u0 % p, u1 % p), ((u0 + 2 * u1 + 1) % p, (u0 + 1) % p))
                        b = ((b0 % p, (b1 + 1) % p), ((b0 + b1 + 1) % p, b1 % p))
                        kappa = wedge(p, nr, u, b)
                        if kappa == (0, 0):
                            continue
                        g1 = wedge(p, nr, ell, b)
                        g2 = pe(p, nr, c, d, b, ell)
                        h1 = wedge(p, nr, u, ell)
                        h2 = pe(p, nr, c, d, u, ell)
                        d_gate = fadd(p, fmul(p, nr, g1, h2), fmul(p, nr, g2, h1))
                        assert d_gate == fmul(p, nr, n_ell, kappa), (p, c, d, u, b, d_gate, n_ell, kappa)
                        checked += 1
                        if source_valid:
                            assert d_gate != (0, 0), (p, c, d, u, b)
                            source_valid_checked += 1
                        if separated:
                            assert d_gate != (0, 0), (p, c, d, u, b)
                            separated_checked += 1
                        if d_gate == (0, 0):
                            d0_off_r0 += 1
                            if not source_valid:
                                d0_has_root += 1

    return {
        "p": p,
        "checked": checked,
        "source_valid_checked": source_valid_checked,
        "separated_checked": separated_checked,
        "D0_offR0": d0_off_r0,
        "D0_all_have_base_root": d0_off_r0 == d0_has_root,
    }


if __name__ == "__main__":
    for p in (3, 5, 7, 11):
        r = run(p)
        print(
            f"p={r['p']}: checked={r['checked']}, "
            f"source-valid off-R0 samples={r['source_valid_checked']}, "
            f"separated off-R0 samples={r['separated_checked']}, "
            f"D=0 off-R0 samples={r['D0_offR0']}, "
            f"every D=0 has base root={r['D0_all_have_base_root']}"
        )
    print("PASS: Cycle 24 ell, D=N(ell)kappa, and resultant identities verified.")
