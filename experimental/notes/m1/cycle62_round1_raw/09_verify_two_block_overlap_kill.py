#!/usr/bin/env python3
"""Exact finite verifier for the M=2, N=3, c=8, h=5 counterpacket.

The extension-field element theta is represented abstractly by an irreducible
polynomial of degree 6 over F_97.  Since every slope polynomial has degree 5,
coefficient-tuple distinctness proves distinct evaluation at theta.
"""
from __future__ import annotations

import itertools
import json
from collections import defaultdict, deque
from math import comb

from sympy import primitive_root
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_irreducible_p

P = 97
M = 2
N = 3
MN = M * N
C = 8
H = 5
N_CODE = C * MN
SIGMA = MN
K = (H - 1) * MN
R = N_CODE - K
J = R - SIGMA


def poly_mul(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return tuple(out)


def subset_polynomial(roots: tuple[int, ...]) -> tuple[int, ...]:
    # Ascending coefficient order, product (T-root).
    out = (1,)
    for root in roots:
        out = poly_mul(out, ((-root) % P, 1), P)
    return out


def graph_components(edges: list[tuple[tuple[str, int], tuple[str, int], int]]):
    adjacency: dict[tuple[str, int], set[tuple[str, int]]] = defaultdict(set)
    edge_by_pair: dict[frozenset[tuple[str, int]], int] = {}
    for left, right, x in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
        edge_by_pair[frozenset((left, right))] = x
    seen = set()
    comps = []
    for v in adjacency:
        if v in seen:
            continue
        q = deque([v])
        seen.add(v)
        vertices = set()
        while q:
            u = q.popleft()
            vertices.add(u)
            for w in adjacency[u]:
                if w not in seen:
                    seen.add(w)
                    q.append(w)
        lefts = {u for u in vertices if u[0] == "R"}
        rights = {u for u in vertices if u[0] == "S"}
        xs = {
            x
            for pair, x in edge_by_pair.items()
            if pair.issubset(vertices)
        }
        comps.append((lefts, rights, xs))
    return comps


def main() -> None:
    assert N_CODE == 48 and K == 24 and SIGMA == 6 and J == 18
    gen = int(primitive_root(P))
    # F_97^* has order 96; <gen^2> has order 48.
    lgen = pow(gen, 2, P)
    L = [pow(lgen, i, P) for i in range(N_CODE)]
    assert len(set(L)) == N_CODE

    r_blocks: dict[int, set[int]] = defaultdict(set)
    s_blocks: dict[int, set[int]] = defaultdict(set)
    edges = []
    for x in L:
        rv = pow(x, M, P)
        sv = pow(x, N, P)
        r_blocks[rv].add(x)
        s_blocks[sv].add(x)
        edges.append((("R", rv), ("S", sv), x))

    assert len(r_blocks) == C * N
    assert len(s_blocks) == C * M
    assert all(len(b) == M for b in r_blocks.values())
    assert all(len(b) == N for b in s_blocks.values())

    comps = graph_components(edges)
    assert len(comps) == C
    for lefts, rights, xs in comps:
        assert len(lefts) == N
        assert len(rights) == M
        assert len(xs) == MN
        # Complete bipartite: MN vertex pairs and MN edges.
        assert len(lefts) * len(rights) == len(xs)

    labels = sorted({pow(x, MN, P) for x in L})
    assert len(labels) == C
    component_by_label = {
        t: {x for x in L if pow(x, MN, P) == t}
        for t in labels
    }
    assert all(len(comp) == MN for comp in component_by_label.values())

    support_records = []
    slope_polys = set()
    for A in itertools.combinations(labels, H):
        support = set().union(*(component_by_label[t] for t in A))
        assert len(support) == H * MN == K + SIGMA
        # It is exactly a union of complete R- and S-blocks.
        assert all((block <= support) or block.isdisjoint(support) for block in r_blocks.values())
        assert all((block <= support) or block.isdisjoint(support) for block in s_blocks.values())
        coeffs = subset_polynomial(A)
        assert len(coeffs) == H + 1
        # Locator P_A(X)=F_A(X^6) has precisely this support on L.
        for x in L:
            value = 1
            y = pow(x, MN, P)
            for t in A:
                value = (value * (y - t)) % P
            assert (value == 0) == (x in support)
        # Divided difference (F_A(Y)-F_A(T))/(Y-T) is monic of
        # Y-degree H-1, so subtracting it from Y^(H-1) has degree < H-1.
        # This is the exact degree check for Q_A.
        dd_y_coeffs = [[0] for _ in range(H)]  # polynomial-in-T coefficients
        for i, ai in enumerate(coeffs):
            if i == 0:
                continue
            for r in range(i):
                ydeg = i - 1 - r
                while len(dd_y_coeffs[ydeg]) <= r:
                    dd_y_coeffs[ydeg].append(0)
                dd_y_coeffs[ydeg][r] = (dd_y_coeffs[ydeg][r] + ai) % P
        assert dd_y_coeffs[H - 1] == [1]
        q_y_coeffs = [row[:] for row in dd_y_coeffs]
        q_y_coeffs[H - 1][0] = (q_y_coeffs[H - 1][0] - 1) % P
        assert all(v == 0 for v in q_y_coeffs[H - 1])
        slope_polys.add(coeffs)
        support_records.append((A, support, coeffs))

    assert len(support_records) == comb(C, H) == 56
    assert len(slope_polys) == comb(C, H)  # theta has degree 6 > 5
    assert set.intersection(*(rec[1] for rec in support_records)) == set()

    # Exhibit three non-collinear locator polynomials in Y=X^6.
    B = tuple(labels[: H - 2])
    a, b, d = labels[H - 2 : H + 1]
    p_ab = subset_polynomial(tuple(sorted(B + (a, b))))
    p_ad = subset_polynomial(tuple(sorted(B + (a, d))))
    p_bd = subset_polynomial(tuple(sorted(B + (b, d))))
    v1 = tuple((x - y) % P for x, y in zip(p_ab, p_ad))
    v2 = tuple((x - y) % P for x, y in zip(p_ab, p_bd))
    # Check no scalar lambda satisfies v1=lambda*v2.
    collinear = False
    for lam in range(P):
        if all(x == (lam * y) % P for x, y in zip(v1, v2)):
            collinear = True
            break
    assert not collinear

    # An explicit irreducible degree-6 polynomial certifies an element theta
    # of degree 6 over F_97. gf_irreducible uses descending coefficient order.
    irr = [1, 70, 53, 81, 58, 6, 3]
    assert gf_irreducible_p(irr, P, ZZ)

    max_supports_per_k_core = C - H + 1
    kappa_lower_num = comb(C, H)
    weighted_cover = min(
        comb(C, H),
        (R // SIGMA) * ((kappa_lower_num + max_supports_per_k_core - 1) // max_supports_per_k_core),
    )
    assert R // SIGMA == C - H + 1
    assert weighted_cover == comb(C, H)

    result = {
        "field_base": P,
        "extension_degree": 6,
        "irreducible_polynomial_descending": irr,
        "map_degrees": [M, N],
        "code": {"n": N_CODE, "k": K, "sigma": SIGMA, "j": J, "rate": "1/2"},
        "R_blocks": len(r_blocks),
        "S_blocks": len(s_blocks),
        "incidence_components": len(comps),
        "component_graph_type": f"K_{{{N},{M}}}",
        "all_common_unions": 2 ** C,
        "nontrivial_common_unions": 2 ** C - 2,
        "fixed_size_common_supports": comb(C, H),
        "distinct_slopes": len(slope_polys),
        "common_core_size": 0,
        "weighted_cover": weighted_cover,
        "locator_family_collinear": collinear,
        "degree_checks": {
            "agreement": H * MN,
            "k_plus_sigma": K + SIGMA,
            "direction_zero_bound": K + SIGMA - 1,
            "anchor_root_bound": K,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
