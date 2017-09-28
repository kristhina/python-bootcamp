from random import choice

lista_wyrazow = ["krowa", "krokodyl", "szklanka", "pisanka", "elementarz", "figurka", "truskawka", "malina"]

def losowanie_wyrazu(lista):
    wyraz = choice(lista)
    return wyraz

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
    zgadywany_wyraz = losowanie_wyrazu(lista_wyrazow)
    l = len(zgadywany_wyraz)
    print(l*'-')

gra()