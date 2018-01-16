# Napisz prosty konwerter walut, który na wejściu przyjmie stringa składającego się z:
# kwoty, waluty wejściowej, słówka kluczowego "to" i kwoty wyjściowej.
# Użyj następujących kursów: 1 PLN to 1000 USD, 1 PLN to 4505 EURO, 1 PLN to 100 JPY
# Załóż, że konwersje są wykonywane tylko z lub do PLNów.
# Dla zaawansowanych: przeliczaj wszystkie waluty między sobą (PLN, USD, EURO, JPY)
# Przykład:
# input: "2 PLN to USD" output: "2000 USD"
# input "15 USD to PLN" output: "0.015 PLN"

kursUSD = 1000
kursEURO = 4505
kursJPY = 100


def konwerter(my_string):
    cut_string = my_string.split()
    if cut_string[1] == "PLN":
        waluta = cut_string[3]
        if waluta == "USD":
            pln = float(cut_string[0]) * kursUSD
        elif waluta == "EURO":
            pln = float(cut_string[0]) * kursEURO
        elif waluta == "JPY":
            pln = float(cut_string[0]) * kursJPY
        else:
            return "Błędne dane wejściowe"
        return "{} {}".format(pln, waluta)
    else:
        waluta = cut_string[1]
        if waluta == "USD":
            pln = float(cut_string[0]) / kursUSD
        elif waluta == "EURO":
            pln = float(cut_string[0]) / kursEURO
        elif waluta == "JPY":
            pln = float(cut_string[0]) / kursJPY
        else:
            return "Błędne dane wejściowe"
        return "{} PLN".format(pln)


print(konwerter("2 PLN to USD"))
print(konwerter("15 USD to PLN"))
print(konwerter("15 JPY to PLN"))

