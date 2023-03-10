"""Test sieve"""

import numpy as np

from py3nt.core.base import BaseSieve
from py3nt.core.sieve import SieveOfEratosthenes, SieveOfEratosthenesOptimized
from py3nt.defaults import LOGN_PRIME_FACTOR_FIELD


def test_sieve_normal():
    """Test normal prime generation"""

    sieve = SieveOfEratosthenes(limit=1)

    assert isinstance(sieve, BaseSieve)
    sieve.generate_primes()

    assert isinstance(sieve.primes_, np.ndarray)
    assert sieve.num_primes == 0

    sieve = SieveOfEratosthenes(limit=10)
    sieve.generate_primes()

    primes = sieve.primes_

    assert isinstance(primes, np.ndarray)
    assert sieve.num_primes == 4
    assert primes.tolist() == [2, 3, 5, 7]

    sieve = SieveOfEratosthenes(limit=30)
    sieve.generate_primes()
    primes = sieve.primes_

    assert len(primes) == 10
    assert primes.tolist() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_sieve_optimized():
    """Test smallest prime factor sieve"""

    sieve = SieveOfEratosthenesOptimized(limit=1)
    assert isinstance(sieve, BaseSieve)
    sieve.generate_primes()

    assert isinstance(sieve.primes_, np.ndarray)
    assert sieve.num_primes == 0

    sieve = SieveOfEratosthenesOptimized(limit=100)
    sieve.generate_primes()

    assert hasattr(sieve, "primes_")

    assert isinstance(sieve.primes_, np.ndarray)
    assert sieve.num_primes == 25

    assert hasattr(sieve, LOGN_PRIME_FACTOR_FIELD)
    smallest_factors = getattr(sieve, LOGN_PRIME_FACTOR_FIELD)

    assert isinstance(smallest_factors, np.ndarray)
    assert smallest_factors.shape[0] == 100 + 1
    assert smallest_factors[45] == 5
