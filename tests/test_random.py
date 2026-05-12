import random
import pytest
import sys
import os

# Asigurăm că modulele pot fi importate indiferent de unde rulăm
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

from linear_search import linear_search
from oracle import oracle_search

# Seed fix pentru reproductibilitate
random.seed(42)

# Parametri experiment
N = 1000
INTERVAL = (-10, 10)


def generate_test_cases(n, interval, seed=42):
    """Generează n cazuri de test (v, key) aleatorii."""
    random.seed(seed)
    cases = []
    for _ in range(n):
        v = [random.randint(*interval) for _ in range(5)]
        key = random.randint(*interval)
        cases.append((v, key))
    return cases


TEST_CASES = generate_test_cases(N, INTERVAL)


@pytest.mark.parametrize("v, key", TEST_CASES)
def test_random_linear_search(v, key):
    """
    Pentru fiecare caz aleatoriu, verificăm că linear_search
    returnează același rezultat ca oracolul independent.
    """
    result = linear_search(v, key)
    expected = oracle_search(v, key)
    assert result == expected, (
        f"EROARE: linear_search({v}, {key}) = {result}, "
        f"dar oracolul returnează {expected}"
    )


# -------------------------------------------------------
# Rulare directă (fără pytest) — afișează statistici
# -------------------------------------------------------
if __name__ == "__main__":
    passed = 0
    failed = 0
    found_cases = 0
    not_found_cases = 0

    for v, key in TEST_CASES:
        expected = oracle_search(v, key)
        result = linear_search(v, key)

        if expected >= 0:
            found_cases += 1
        else:
            not_found_cases += 1

        if result == expected:
            passed += 1
        else:
            failed += 1
            print(f"FAIL: v={v}, key={key} → got {result}, expected {expected}")

    print(f"\n=== Rezultate pentru N={N} teste aleatorii (seed=42) ===")
    print(f"Trecute:       {passed}/{N}")
    print(f"Eșuate:        {failed}/{N}")
    print(f"Cazuri găsite (key în v):     {found_cases}")
    print(f"Cazuri negăsite (key absent): {not_found_cases}")
