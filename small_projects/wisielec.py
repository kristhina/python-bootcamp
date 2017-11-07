from random import choice

lista_wyrazow = ["krowa", "krokodyl", "szklanka", "pisanka", "elementarz", "figurka", "truskawka", "malina"]


def losowanie_wyrazu(lista):
    return choice(lista)


def poczatek_gry():
    decyzja = None
    print("Cześć! Zapraszam Cię do gry w Wisielca!")
    print("Zdecyduj, co chcesz zrobić")
    print("a - zacznij nowa grę")
    print("b - koniec gry")
    while decyzja != 'a' and decyzja != 'b':
        decyzja = input("Jaka jest Twoja decyzja? a/b: ")
    if decyzja == 'b':
        koniec_gry()


def koniec_gry():
    exit()


def gra():
    poczatek_gry()
    errors = 0
    zgadywany_wyraz = losowanie_wyrazu(lista_wyrazow)
    lista_znakow = len(zgadywany_wyraz) * ['-']
    print(lista_znakow)
    while '-' in lista_znakow and errors < 10:
        litera = input("Podaj literę: ")
        n = 0
        found = False
        for znak in zgadywany_wyraz:
            if znak == litera:
                lista_znakow[n] = litera
                found = True
            n += 1
        if found == False:
            errors += 1
        print(lista_znakow)
    if errors == 10:
        print("Przykro mi! Nie zgadłeś!")
    else:
        print('Brawo! Zgadłeś!')
    print('Zgadywany wyraz to {}'.format(zgadywany_wyraz))
    gra()


gra()
