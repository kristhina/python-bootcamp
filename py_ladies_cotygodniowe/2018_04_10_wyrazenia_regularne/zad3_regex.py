# Korzystając z pliku z poprzedniego zadania, stwórz słownik warsztatów w formacie - przykład:
# workshops = {22: {date: "2018.04.10", title: "Wyrażenie regularne", leading_mentor: "Zuzanna Kunik"}.
# "BRAK ZAJĘĆ" potraktuj jako tytuł, przypisz wtedy pusty string jako leading_mentor.
# Numeruj lekcje wg daty (2017.10.17 to pierwsze zajęcia, 2018.06.19 to ostatnie).
# Podpowiedź: użyj znaku nowej linii.

import re
encoding = "utf8"

with open('program_pylove.txt', 'r') as file:
    tekst = file.read()


workshop_list = re.findall(r'(\d{4}\.\d{2}\.\d{2})\s-\s(.+)', tekst)

workshops = {}
for workshop_number, (data, info) in enumerate(workshop_list, 1):
    info = re.split(r' - ', info)
    workshops[workshop_number] = {
        'date' : data,
        'title' : ' - '.join(info[0:-1]),
        'mentor' : info [-1] if len (info) != 1 else ''
    }
print(workshops)