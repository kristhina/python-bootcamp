# m = float(input("Podaj swoją wagę"))
# h = float(input("Podaj swój wzrost"))
# BMI = m/(h*h)
# print("Twoje BMI wynosi {}".format (BMI))
#
# def bmi_func(m,h):
#     return m/h**2
#
# print(bmi_func(50, 156))
#
# print('Twoje BMI wynosi' + str((float(input("podaj swoją wagę"))/float(input('podaj swój wzrost'))**2)))
#


# def bmi_func1(h, m):
#     bmi = round(m/h**2, 2)
#     print("Twoje BMI wynosi {} ".format(bmi))
#     if bmi < 20:
#         print("Masz niedowagę")
#     elif 20 <= bmi < 25:
#         print("Twoja waga jest prawidłowa")
#     else:
#         print("Masz nadwagę")
#
#
# koniec = False
# while not koniec:
#     while True:
#         try:
#             h = float(input("Podaj swój wzrost - w metrach"))
#             m = float(input("Podaj swoją wagę"))
#             break
#         except ValueError:
#             print("Zła wartość")
#     bmi_func1(h, m)
#     decyzja = input('Czy policzyć BMI dla kolejnej osoby? Y/N')
#     if decyzja == "Y":
#         koniec = False
#     elif decyzja == "N":
#         koniec = True
#     else:
#         print('Musisz napisać Y lub N')
#
# #
# class Osoba:
#
#     def __init__(self, imie, waga, wzrost):
#         self.imie = imie
#         self.waga = waga
#         self.wzrost = wzrost
#
# class ListaOsob:
#     def __init__(self):
#
#
#     def create_list(self):
#         lista_osob = []
#         while True:
#
#
#
#
# def pobierz_dane():
#     lista_osob = []
#     while True:
#         imie = input('Podaj swoje imię: ')
#         wzrost = input('Podaj wzrost w cm: ')
#         waga = input('Podaj wagę w kg: ')
#         osoba = [imie, int(wzrost), int(waga)]
#         lista_osob.append(osoba)
#         decyzja = input('Czy chcesz dodać kolejną osobę? (y/n)')
#         if decyzja == 'n':
#             break
#
# pobierz_dane()
#
#
def bmi_func1(h, m, p):
    bmi = round(m/h**2, 2)
    if p == "K":
        print("Kobieto!")
    elif p == "M":
        print("Mężczyzno!")
    else:
        print("Nieprawidłowo podana płeć")
    print("Twoje BMI wynosi {} ".format(bmi))
    if bmi < 18.5:
        print("Masz niedowagę")
    elif 18.5 <= bmi < 25:
        print("Twoja waga jest prawidłowa")
    elif 25 <= bmi < 30:
        print("Masz nadwagę")
    else:
        print("Jesteś otyły")


koniec = False
while not koniec:
    while True:
        try:
            h = float(input("Podaj swój wzrost - w metrach"))
            m = float(input("Podaj swoją wagę"))
            p = input("jesteś kobietą czy mężczyzną (K/M)? ")
            break
        except ValueError:
            print("Zła wartość")
    bmi_func1(h, m, p)
    decyzja = input('Czy policzyć BMI dla kolejnej osoby? Y/N')
    if decyzja == "Y":
        koniec = False
    elif decyzja == "N":
        koniec = True
    else:
        print('Musisz napisać Y lub N')