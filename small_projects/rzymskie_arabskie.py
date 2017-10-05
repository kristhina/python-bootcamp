#sprawdzenie poprawności podanej liczby
def sprawdzenie_poprawnosci():
    while True:
        try:
            ldz = int(input("Jaką liczbę chcesz zmienić na rzymską?"))
            if ldz > 0:
                break
            else:
                print("podaj liczbę dodatnią")
        except ValueError:
            print("To nie jest liczba całkowita")


    return(ldz)

def przekształcenie(liczba):
    rzymskie = ''
    m = liczba // 1000
    if m > 0:
        rzymskie = m*"M"
    liczba = liczba - m*1000
    if liczba >=900:
        rzymskie = rzymskie + "CM"
        liczba = liczba - 900
    if liczba >= 500:
        rzymskie += "D"
        liczba -= 500
    if liczba >= 400:
        rzymskie += "CD"
        liczba -= 400
    c = liczba // 100
    if c > 0:
        rzymskie = rzymskie + c*"C"
        liczba = liczba - c*100
    if liczba >= 90:
        rzymskie += "XC"
        liczba -=90
    if liczba >= 50:
        rzymskie += "L"
        liczba -=50
    if liczba  >= 40:
        rzymskie += "XL"
        liczba -= 40
    x = liczba // 10
    if x > 0:
        rzymskie = rzymskie + x * "X"
        liczba = liczba - x*10
    if liczba == 9:
        rzymskie = rzymskie + "IX"
        liczba = liczba -9
    if liczba >=5:
        rzymskie += "V"
        liczba -=5
    if liczba == 4:
        rzymskie += "IV"
        liczba -=4
    rzymskie = rzymskie + liczba * "I"



    print(rzymskie)

przekształcenie(sprawdzenie_poprawnosci())
