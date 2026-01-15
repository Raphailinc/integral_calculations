import numpy as np

from integral_calculations.core import DEFAULT_SEED, estimate_integrals, middle_square_uniform, sample_transforms


def test_middle_square_deterministic():
    seq = middle_square_uniform(5, seed=DEFAULT_SEED, k=8)
    assert np.allclose(seq[:3], [0.84616823, 0.00673461, 0.45354971], atol=1e-8)
    assert (seq >= 0).all() and (seq < 1).all()


def test_sample_transforms_shapes():
    u = np.array([0.0, 0.5, 1.0])
    x1, x2 = sample_transforms(u)
    assert np.allclose(x1, np.sqrt(2 * u))
    assert np.allclose(x2, 2 * u)


def test_estimate_integrals_numpy_seed():
    results = estimate_integrals(n=1000, method="numpy", seed=42)
    assert "I1" in results and "I2" in results
    i1 = results["I1"].estimate
    i2 = results["I2"].estimate
    # Rough sanity bounds for deterministic seed
    assert 0.8 < i1 < 1.3
    assert 1.5 < i2 < 2.5
