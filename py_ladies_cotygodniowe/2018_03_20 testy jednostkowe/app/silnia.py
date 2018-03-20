def silnia(n):
    if n < 0:
        raise ValueError("should not be negatice")
    if n < 2:
        return n

    return n * silnia(n - 1)