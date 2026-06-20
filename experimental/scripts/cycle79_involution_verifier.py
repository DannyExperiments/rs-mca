#!/usr/bin/env python3
"""Cycle 79 complement-involution verifier.

This is a bounded local check for the structure returned by Cycle 79:

* the 48 legal 8-subsets of Z/16Z are closed under complement;
* the induced involution tau has a constant per-slot product pairing;
* the global seven-slot product satisfies Phi(tau(T)) = K / Phi(T);
* tau preserves the color shell P_0.

It does not prove m_max(beta) <= 12.
"""

from __future__ import annotations

import importlib.util
import json
import random
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
CYCLE68_PATH = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"


def load_cycle68():
    spec = importlib.util.spec_from_file_location("cycle68_checker", CYCLE68_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def tau(i: int, a: int) -> tuple[int, int]:
    if i == 1:
        return 2, (a + 6) % 16
    if i == 2:
        return 1, (a + 10) % 16
    if i == 3:
        return 3, (a + 8) % 16
    raise ValueError(i)


def main() -> None:
    c68 = load_cycle68()
    f = c68.find_field_poly()
    eta = c68.find_eta(f)
    beta = c68.find_beta(f)
    table = c68.build_u(f, eta, beta)

    def u(t: int, i: int, a: int):
        return table[(t, i, a)]

    complement_checks = []
    for i in (1, 2, 3):
        for a in range(16):
            bset = {(a + e) % 16 for e in c68.E_SETS[i]}
            j, b = tau(i, a)
            tau_set = {(b + e) % 16 for e in c68.E_SETS[j]}
            assert tau_set == (set(range(16)) - bset)
            assert tau(*tau(i, a)) == (i, a)
            complement_checks.append((i, a, j, b))

    def emb(c: int):
        return c68.emb(c)

    slot_constants = {}
    for t in range(1, 8):
        const = c68.fmul(
            c68.fpow(emb(pow(3, 2 * t, 17)), c68.N - 1, f),
            c68.psub(c68.fpow(beta, 32, f), emb(pow(9, t, 17))),
            f,
        )
        slot_constants[t] = list(const)
        for i in (1, 2, 3):
            for a in range(16):
                j, b = tau(i, a)
                assert c68.fmul(u(t, i, a), u(t, j, b), f) == const

    global_k = c68.ONE
    for t in range(1, 8):
        const = c68.fmul(
            c68.fpow(emb(pow(3, 2 * t, 17)), c68.N - 1, f),
            c68.psub(c68.fpow(beta, 32, f), emb(pow(9, t, 17))),
            f,
        )
        global_k = c68.fmul(global_k, const, f)

    def color(i: int, a: int) -> int:
        return (c68.S_COLOR[i] + 8 * (a % 2)) % 16

    shell_samples = 0
    rng = random.Random(79)
    for _ in range(512):
        choices = [(rng.randint(1, 3), rng.randint(0, 15)) for _ in range(7)]
        if sum(color(i, a) for i, a in choices) % 16 != 4:
            continue
        tau_choices = [tau(i, a) for i, a in choices]
        assert sum(color(i, a) for i, a in tau_choices) % 16 == 4
        prod_a = c68.ONE
        prod_b = c68.ONE
        for t, (i, a) in enumerate(choices, 1):
            prod_a = c68.fmul(prod_a, u(t, i, a), f)
        for t, (i, a) in enumerate(tau_choices, 1):
            prod_b = c68.fmul(prod_b, u(t, i, a), f)
        assert c68.fmul(prod_a, prod_b, f) == global_k
        shell_samples += 1

    out = {
        "decision": "CYCLE79_INVOLUTION_OK",
        "model": {
            "field_poly": list(f),
            "eta": list(eta),
            "beta": list(beta),
        },
        "tau": {
            "1,a": "2,a+6",
            "2,a": "1,a+10",
            "3,a": "3,a+8",
            "modulus": 16,
        },
        "complement_checks": len(complement_checks),
        "slot_pairing_constants": slot_constants,
        "global_pairing_constant_K": list(global_k),
        "p0_shell_samples_checked": shell_samples,
        "scope": "verifies Cycle 79 involution structure only; no m_max bound",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
