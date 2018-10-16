import pytest

from gcd import gcd


@pytest.mark.parametrize('a, b, gcd_number', [
    (1, 0, 1),
    (0, 1, 1),
    (1, 15, 1),
    (15, 1, 1),
    (6, 9, 3),
    (13, 11, 1),
    (15, 30, 15),
    (28, 7, 7),
    (0, 0, 0),
    (6, 8, 2)
])
def test_gcd(a, b, gcd_number):
    assert gcd(a, b) == gcd_number
