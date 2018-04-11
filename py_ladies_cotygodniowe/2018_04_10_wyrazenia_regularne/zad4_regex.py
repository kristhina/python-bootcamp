#
# Otwórz przykładową listę celebrytów z pliku txt (użyj encoding="utf8")
# i zamień pierwszą literę imienia z pierwszą literą nazwiska.
# Przykład: Magda Gessler - Gagda Messler

import re

with open('celebrities.txt', 'r', encoding="utf8") as file:
    celebrieties_list = file.readlines()

changed_celebrietes = []
for celeb in celebrieties_list:
    celeb_changed = re.sub(r'(\w)(\w+) (\w)(\w+)', r'\3\2 \1\4', celeb)
    changed_celebrietes.append(celeb_changed[0:(len(celeb_changed)-1)])

print(changed_celebrietes)
