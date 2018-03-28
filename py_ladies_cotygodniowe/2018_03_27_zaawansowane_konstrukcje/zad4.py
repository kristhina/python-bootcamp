#
# Pobierz losowe dane z https://pylove.org/exercise/1_19_2 i
# znajdź hasło, na które złoży się 6 najpopularniejszych
# liter w kolejności malejącej według wystąpień.
# Wykonaj zadanie 2. z wykorzystaniem konstruktu Counter z biblioteki collections.

import requests
from collections import Counter

tekst = requests.get("https://pylove.org/exercise/1_19_2").text
c = Counter(tekst)
mc = c.most_common(6)
word = ''
for k, v in mc:
    word += k
print(word)

