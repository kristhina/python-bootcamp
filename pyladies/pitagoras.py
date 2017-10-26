from math import sqrt

# a = int(input("Podaj jeden bok trójkąta"))
# b = int(input("Podaj drugi bok trójkąta"))
# c = round(sqrt(a**2 + b**2), 2)
# print("Trzeci bok trójkąta ma długość {}".format(c))
#
#
# w = float(input("podaj swoją wagę"))
# h = float(input("podaj swój wzrost"))
# bmi = round(w/h**2, 2)
# print("Twoje bmi wynosi {}". format(bmi))

# l = [1, 2, 3]
# print(dir(l))
# print(dir(5))

def pitagoras():
    while True:
        try:
            a = int(input("Podaj długość pierwszego boku"))
            break
        except ValueError:
            print("Wpisz liczbę całkowitą")
    while True:
        try:
            b = int(input("Podaj długość drugiego boku"))
            break
        except ValueError:
            print("Wpisz liczbę całkowitą")
    c = round(sqrt(a ** 2 + b ** 2), 2)
    print("Trzeci bok trójkąta ma długość {}".format(c))

pitagoras()
