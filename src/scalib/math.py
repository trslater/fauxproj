def geometric_sequence(a_0: float, r: float, n: int) -> float:
    if n < 0:
        raise ValueError("n must be at least 0")

    return a_0*r**n
