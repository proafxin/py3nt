"""Totient functions"""

from typing import Optional

from py3nt.core.factorize import FactorizationFactory


def jordan(n: int, k: int, factorizer: Optional[FactorizationFactory]) -> int:
    if not factorizer:
        raise ValueError("`factorizer` cannot be None")

    phi = pow(n, k)

    factorization = factorizer.factorize(n=n)

    for prime in factorization:
        p_k = pow(prime, k)
        phi //= p_k
        phi *= p_k - 1

    return phi


def carmichael(n: int, factorizer: Optional[FactorizationFactory]) -> int:
    if not factorizer:
        raise ValueError("`factorizer` cannot be None")

    universal_exponent = 1

    if (n & 1) == 0:
        multiplicity = 0
        while (n & 1) == 0:
            n >>= 1
            multiplicity += 1

        if multiplicity > 1:
            universal_exponent *= 1 << (multiplicity - 2)

    if n == 1:
        return universal_exponent

    factorization = factorizer.factorize(n=n)

    for prime, multiplicity in factorization.items():
        universal_exponent *= pow(prime, multiplicity - 1)
        universal_exponent *= prime - 1
        print(universal_exponent, prime, multiplicity)

    return universal_exponent
