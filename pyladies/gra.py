from random import randint

def podaj_liczbe():
    while True:
        try:
            liczba = int(input("Podaj liczbę od 1 do 100"))
            break
        except ValueError:
            print("Musisz podać liczbę całkowitą od 1 do 100")
    return liczba

def losuj_liczbe():
    zgadywana_liczba = randint(0,100)
    return zgadywana_liczba

def porownaj_liczby(a, b):
    if a == b:
        return "wygrana"
    elif a<b:
        return "mniejsza"
    else:
        return "wieksza"

def przebieg_gry():
    liczba_komputera = losuj_liczbe()
    for i in range(5):
        liczba_gracza = podaj_liczbe()
        porownanie = porownaj_liczby(liczba_gracza, liczba_komputera)
        if porownanie == "wygrana":
            print("Wygrałeś! To jest prawidłowa liczba")
            koniec()
        elif porownanie == "mniejsza":
            if i < 4:
                print("Twoja liczba jest mniejsza od mojej. Spróbuj jeszcze raz.")
        else:
            if i < 4:
                print("Twoja liczba jest zbyt wysoka. Spróbuj wymyślić coś mniejszego")
    print("Przegrałeś! Moja liczba to było {}".format(liczba_komputera))
    koniec()

def koniec():
    decyzja = input("Czy chcesz zagrać jeszcze raz? t/n")
    if decyzja == "t":
        przebieg_gry()
    elif decyzja == "n":
        exit()
    else:
        print('Musisz wpisać "t" lub "n"')
        koniec()

przebieg_gry()