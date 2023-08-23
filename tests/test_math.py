import pytest

from scalib import math


def test_geometric_sequence_n_at_least_0():
    with pytest.raises(ValueError):
        math.geometric_sequence(1, 2, -1)
