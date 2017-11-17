# string[poczatek:koniec:krok]

x = 'text'
print(x[1:])
print(x[:3])
print(x[1:2])

text_1 = "Ala ma kota a kot ma Ale"
text_2 = "PyLadies.start() ma przerwę obiadową o 14:00"
lt1 = len(text_1)
lt2 = len(text_2)
print(text_1[:lt1//2])
print(text_2[:lt2//2])
print(text_1[lt1//2:])