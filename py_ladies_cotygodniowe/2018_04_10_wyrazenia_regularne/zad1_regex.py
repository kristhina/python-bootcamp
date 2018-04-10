import re
encoding="utf8"

with open('wikipedia_python.txt', 'r') as file:
    tekst = file.read()

lista_dopasowan = re.findall(r'[Pp]ython', tekst)

print(len(lista_dopasowan))
