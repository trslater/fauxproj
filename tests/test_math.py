import pytest

from fauxproj import math


def test_geometric_sequence_n_at_least_0():
    with pytest.raises(ValueError):
        math.geometric_sequence(1, 2, -1)


@pytest.mark.parametrize("a_0, r, n, a_n", [
    (1, 2, 3, 8),
    (3, 2, 3, 24),
    (0, 2, 3, 0),
    (2, 0, 3, 0),
    (1, 3, 0, 1),
    (1, 0, 0, 1),
    (1, 0.5, 3, 0.125),
    (1, -1, 1, -1),
    (1, -1, 2, 1),
])
def test_geometric_sequence_output(a_0, r, n, a_n):
    assert math.geometric_sequence(a_0, r, n) == a_n
