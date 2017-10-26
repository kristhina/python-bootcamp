imie = input("podaj imię").title()
nazwisko = input("podaj nazwisko").title()
tytul = input("podaj tytuł").title()
przymiotnik = input("podaj przymiotnik").title()
smak = input("podaj ulubiony smak")

print("{t} {i} {n}, \n {p} przyjacielu, chciałbym zaprosić Cię na urodziny, na których będę serwować twój ulubiony {s} tort \n Krysia". format(t = tytul, i = imie, n = nazwisko, p = przymiotnik, s = smak))

list = ['Jan', 'Nowak', 'profesor', ]