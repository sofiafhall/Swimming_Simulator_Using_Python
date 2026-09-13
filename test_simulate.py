import numpy as np
import pytest
from simulate import predict_dist, summarize

def test_sample_count():
    """Verifies R-06: at least 10,000 Monte Carlo samples."""
    samples = predict_dist(53.10, 1.5, 1.2, n=10_000, seed=1)
    assert len(samples) == 10_000

def test_seed_deter():
    """Verifies R-08: identical input and seed gives identical output"""
    first = predict_dist(53.10, 1.5, 1.2, seed=42)
    second = predict_dist(53.10, 1.5, 1.2, seed=42)
    assert np.array_equal(first, second)

def test_pos_rate():
    """A positive improvement rate should center the distribution below the third year"""
    samples = predict_dist(53.10, 1.5, 0.1, seed=7)
    assert np.median(samples) < 53.10