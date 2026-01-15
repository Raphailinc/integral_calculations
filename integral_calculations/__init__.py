"""
Monte Carlo helpers for simple integrals with custom pseudo-random generators.

Exposes:
- middle_square_uniform(n, seed, k): uniform [0,1) via middle-square method.
- sample_transforms(y): map uniforms to x1, x2 for two demo integrals.
- estimate_integrals(...): compute estimates, variance, stderr for I1/I2.
"""

from .core import (
    IntegralEstimate,
    estimate_integrals,
    middle_square_uniform,
    sample_transforms,
)

__all__ = [
    "IntegralEstimate",
    "estimate_integrals",
    "middle_square_uniform",
    "sample_transforms",
]
