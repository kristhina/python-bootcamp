def policz_slowa(zdanie):
    print(len(zdanie.split()))

def policz_samogloski(zdanie):
#liczy liczbę samogłosek w podanym zdaniu (niezależnie od wielkości liter)
    liczba_samoglosek = 0
    samogloska = ["a", "e", "i", "o", "u", "y", "ó", "ą", "ę"]
    for litera in zdanie:
        if litera.lower() in samogloska:
            liczba_samoglosek +=1
    print(liczba_samoglosek)


def xo_checker(ciag_znakow):
    # porównuje liczbę znaków "x" oraz "o" w ciągu znaków
    # return: True or False

    liczba_x = 0
    liczba_o = 0
    for znak in ciag_znakow:
        if znak == "x":
            liczba_x += 1
        elif znak == "o":
            liczba_o +=1
        else:
            print("Illegal letters in text")
            exit()
    if liczba_o == liczba_x:
        return True
    else:
        return False

# print(xo_checker("xoxoxoxoxoxo"))
# print(xo_checker("xxxoooxxxxxxxo"))
# print(xo_checker("xpd"))

def cenzura_cyfr(zdanie):
    cyfry = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    zdanie_lista = list(zdanie)
    for i in range(len(zdanie_lista)):
        if zdanie_lista[i] in cyfry:
            zdanie_lista[i] = "#"
    print("".join(zdanie_lista))



cenzura_cyfr('aa123')
cenzura_cyfr("a1a ma k0ta")