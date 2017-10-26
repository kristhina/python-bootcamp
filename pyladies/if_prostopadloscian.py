while True:
    try:
        a = int(input("podaj długość pierwszego boku"))
        b = int(input("podaj długość drugiego boku"))
        h = int(input("podaj wysokość"))
        break
    except ValueError:
        print("Podaj liczbę całkowitą")

v = a*b*h

print("Objętość prostopadłościanu wynosi {}".format(v))

if a == b:
    print("Pole podstawy jest kwadratem")
    if a == b == h:
        print("Mamy do czynienia z sześcianem")