def odwazniki(a,b):
    odwaznik1 = a
    odwaznik2 = b
    for i in range(1, round(min(odwaznik1, odwaznik2) + 1)):
        if odwaznik1 % i == 0 and odwaznik2 % i == 0:
            odwaznik1 /= i
            odwaznik2 /= i
    print(int(odwaznik2), int(odwaznik1))



def droga(czas, przyspieszenie, predkosc_poczatkowa=0):
    return predkosc_poczatkowa*czas + (przyspieszenie*czas**2)/2

def cezar(tekst, przesuniecie):
    lista = list(tekst)
    for i in range(len(lista)):
        if 65 <= ord(lista[i]) <= 90:
            new_ord = ord(lista[i])+przesuniecie
            if new_ord < 65:
                new_ord += 26
            elif new_ord > 90:
                new_ord -= 26
            lista[i] = chr(new_ord)
        if 97 <= ord(lista[i]) <= 122:
            new_ord = ord(lista[i]) + przesuniecie
            if new_ord < 97:
                new_ord += 26
            elif new_ord > 122:
                new_ord -= 26
            lista[i] = chr(new_ord)
    print("".join(lista))





# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))
#
cezar("nwdkę mqva k rua vgż, 123!!!", -2)
cezar("abc", 2)
# cezar("abc", -2)

def ugly(liczba):
    if liczba == 1:
        return True
    elif liczba % 2 == 0 or liczba % 3 == 0 or liczba % 5 == 0:
        return True
    else:
        return False

# print(ugly(15))
# print(ugly(1))
#
def get_time(czas, forma):
    if forma == 's':
        return int(czas[-2:]) + int(czas[-5:-3]) * 60 + int(czas[:-6]) * 3600
    elif forma == 'm':
        return int(czas[-2:]) / 60 + int(czas[-5:-3]) + int(czas[:-6]) * 60
    elif forma == 'h':
        return int(czas[-2:]) / 360 + int(czas[-5:-3]) / 60 + int(czas[:-6])

# strint = "krysiap"
# strint = "12:34:56"
# print(strint[0])
# print(strint[:-6])
# print(strint[2:])
# print(strint[-2:])
# print(strint[-5:-3])
# print(strint[:-6])

# print(get_time('2:00:00', 's'))
# print(get_time('12:00:00', 'm'))
# print(get_time('1:15:00', 'h'))

a = [[[[[[[[[["a"],"b"]]],"c"]]],"d"]],"e"]

def flatten(lista):
    pass

