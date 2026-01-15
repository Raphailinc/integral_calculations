from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable, Optional

import numpy as np


DEFAULT_SEED = 0.84616823
DEFAULT_K = 8


def middle_square_uniform(n: int, seed: float = DEFAULT_SEED, k: int = DEFAULT_K) -> np.ndarray:
    """
    Generate `n` pseudo-uniform numbers on [0, 1) using middle-square method.
    k — even number of digits kept.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    if not (0 < seed < 1):
        raise ValueError("seed must be in (0,1)")
    if k <= 0 or k % 2 != 0:
        raise ValueError("k must be a positive even integer")

    seq = np.empty(n, dtype=float)
    seq[0] = seed
    scale_half = 10 ** (k // 2)
    scale = 10**k
    for i in range(1, n):
        val = seq[i - 1] ** 2
        fractional = math.modf(val * scale_half)[0]
        seq[i] = int(fractional * scale) / scale
    return seq


def sample_transforms(uniforms: Iterable[float]) -> tuple[np.ndarray, np.ndarray]:
    """Return two transformed sample arrays for demo integrals."""
    u = np.asarray(list(uniforms), dtype=float)
    x1 = np.sqrt(2 * u)  # for I1
    x2 = 2 * u           # for I2
    return x1, x2


@dataclass
class IntegralEstimate:
    estimate: float
    variance: float
    stderr: float


def _mc_estimate(values: np.ndarray, weight: float = 1.0) -> IntegralEstimate:
    est = weight * float(np.mean(values))
    var = float(np.var(values, ddof=0))
    stderr = weight * math.sqrt(var / len(values))
    return IntegralEstimate(est, var, stderr)


def estimate_integrals(
    n: int = 5000,
    *,
    method: str = "middle-square",
    seed: Optional[float | int] = None,
    k: int = DEFAULT_K,
) -> dict[str, IntegralEstimate]:
    """
    Compute two integrals via Monte Carlo:
    I1 = E[x^-1/4] where x = sqrt(2u)
    I2 = 2 * E[x^3/4] where x = 2u
    """
    if method == "numpy":
        rng = np.random.default_rng(seed if seed is None or not float(seed).is_integer() else int(seed))
        u = rng.random(n)
    else:
        u = middle_square_uniform(n, seed=seed or DEFAULT_SEED, k=k)

    x1, x2 = sample_transforms(u)

    i1 = _mc_estimate(x1 ** (-0.25))
    i2 = _mc_estimate((x2 ** 0.75), weight=2.0)
    return {"I1": i1, "I2": i2}


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Monte Carlo estimates for two integrals.")
    parser.add_argument("-n", type=int, default=5000, help="Number of samples.")
    parser.add_argument("--method", choices=["middle-square", "numpy"], default="middle-square")
    parser.add_argument("--seed", type=float, default=DEFAULT_SEED, help="Seed for generator.")
    parser.add_argument("-k", type=int, default=DEFAULT_K, help="Digits for middle-square (even).")
    args = parser.parse_args(argv)

    results = estimate_integrals(n=args.n, method=args.method, seed=args.seed, k=args.k)
    for name, est in results.items():
        print(f"{name}: {est.estimate:.6f} (var={est.variance:.6f}, stderr={est.stderr:.6f})")


if __name__ == "__main__":  # pragma: no cover
    main()
