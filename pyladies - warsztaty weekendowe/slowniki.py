# moj_pusty_slownik = {}
# print(moj_pusty_slownik)
# moj_nowy_slownik = {'klucz':'wartosc'}
# print(moj_nowy_slownik)
#
# moj_slownik = {'klucz':'wartosc', 'klucz1':'wartosc1', 1:'jeden'}
# print(moj_slownik['klucz'])

# del usuwanie w słownikach

baza_danych = {
    'KP': {
        'imie': 'Krystyna',
        'nazwisko': 'Piątkowska',
        'data_urodzenia': '08.07.1981',
        'zawod': 'brak',
        'zainteresowania': ['gry planszowe', 'statystyka'],
        'stan_konta': 10000000
    },
    'AZ': {
        'imie': 'Agnieszka',
        'nazwisko': 'Ż',
        'data_urodzenia': '01.01.2000',
        'zawod': 'tester',
        'zainteresowania': ['programowanie'],
        'stan_konta': 999999999
    }
}

print(baza_danych)
print(baza_danych['KP']['imie'])
baza_danych['AZ']['zainteresowania'].append('jedzenie')
print(baza_danych['AZ'])
baza_danych['KP']['imie'] = 'Krysia'
print(baza_danych['KP'])
baza_danych['KP']['zainteresowania'] += ['spanie', 'czytanie']
print(baza_danych['KP']['zainteresowania'])
print(baza_danych.items())
print(baza_danych.keys())
print(baza_danych['KP'].values())
baza_danych['KP']['stan_konta'] *= 2
print(baza_danych['KP']['stan_konta'])
baza_danych['AZ']['nazwisko']='Kowalska'
baza_danych['KP']['drugie_imie'] = 'Maria'
baza_danych['AZ']['drugie_imie'] = 'Drugie Imie'
baza_danych['KP']['wiek'] = 18
baza_danych['AZ']['wiek'] = 18
baza_danych['KP']['wyksztalcenie'] = 'wyższe'
baza_danych['AZ']['wyksztalcenie'] = 'wyższe'
del baza_danych['KP']['data_urodzenia']
del baza_danych['AZ']['data_urodzenia']
print(baza_danych)
for key in baza_danych:
    baza_danych[key].update({'zwierze':'kot'})
print(baza_danych)

osoby = ['KP', 'AZ']
liczba_dzieci = [3, 5]
i = 0
for osoba in osoby:
    baza_danych[osoba]['liczba dzieci'] = liczba_dzieci[i]
    i+=1


print(baza_danych)

dane = {'KP': {'sen': '7 godzin'}, 'AZ': {'sen': '8 godzin'}}


baza_danych['KP']['wiek']+=5

print(baza_danych)



