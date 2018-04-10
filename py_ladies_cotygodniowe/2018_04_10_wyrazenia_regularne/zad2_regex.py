import re
encoding="utf8"

with open('program_pylove.txt', 'r') as file:
    tekst = file.read()


date_list = re.findall(r'\d{4}\.\d{2}\.\d{2}', tekst)
print(date_list)