"""Test totient functions"""

import pytest

from py3nt.core.factorize import FactorizationFactory
from py3nt.functions.unary.totient import carmichael, jordan


def test_totient() -> None:
    """Test Jordan function."""

    factorizer = FactorizationFactory(N=1000)
    assert jordan(n=6, k=1, factorizer=factorizer) == 2

    with pytest.raises(ValueError):
        jordan(n=6, k=1, factorizer=None)


def test_carmichael() -> None:
    factorizer = FactorizationFactory(N=1000)
    assert carmichael(n=4, factorizer=factorizer) == 1
    assert carmichael(n=12, factorizer=factorizer) == 2

    with pytest.raises(ValueError):
        assert carmichael(n=10, factorizer=None)
