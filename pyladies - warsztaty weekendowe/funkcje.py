# def moje_dodawanie(a,b):
#     c = a+b
#     print('Twoim wynikiem jest liczba ' + str(c))
#
# moje_dodawanie(2,5)
# moje_dodawanie(4,8)
# moje_dodawanie(-4, -5)

def moje_dzialanie(a, b, dzialanie='dodawanie'):
    if dzialanie == 'dodawanie':
        wynik = a+b
    elif dzialanie == 'odejmowanie':
        wynik = a-b
    elif dzialanie == 'mnozenie':
        wynik = a*b
    elif dzialanie == 'dzielenie':
        if b == 0:
            print("nie dziel przez 0")
            wynik = 'Błąd'
        else:
            wynik = a/b
    print(wynik)

moje_dzialanie(2, 5)
moje_dzialanie(3, 4, "odejmowanie")
moje_dzialanie(2,4, "dzielenie")
moje_dzialanie(1, 3, "mnozenie")
moje_dzialanie(3, 0, "dzielenie")