# Rozszerz generator o limit określający ostatni kolejny element.


def fibonaci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonaci(17)))