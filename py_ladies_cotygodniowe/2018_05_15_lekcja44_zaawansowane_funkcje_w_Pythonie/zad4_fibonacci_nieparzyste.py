# Napisz algorytm,
# który wyświetli wszystkie nieparzyste liczby w pierwszych 100 elementach ciągu Fibonaciego.


def fibonaci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


nieparzyste = filter(lambda x: x % 2 != 0, list(fibonaci(100)))
print(list(nieparzyste))
