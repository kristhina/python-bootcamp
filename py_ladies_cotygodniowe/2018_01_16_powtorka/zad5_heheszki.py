# Napisz aplikację, która w zależności od argumentu "file" (GET) odczyta plik "hehe.txt",
# "heheszki.json" lub "beczka_smiechu.txt"
# (zawartość dowolna, powinny znajdować się w katalogu z aplikacją).
# Obsłuż sytuację, w której plik nie będzie istniał.
# W aplikacji 5a. jeśli użytkownik odpowiednio zmodyfikuje argument "file"
# (zamiast "hehe.txt" poda np. "../../../../hehe.txt"
# [Linux] lub "..\..\..\..\hehe.txt" [Windows]),
# możliwe jest załadowanie dowolnego pliku (każde ../ lub ..\
# powoduje wejście do katalogu/folderu nadrzędnego).
# Napraw aplikację tak, aby pod uwagę brana była tylko nazwa pliku.
# Przydatny moduł: os.path
# (ciekawostka: jest to błąd "z życia wzięty" z pewnego większego projektu)
# Więcej informacji o podatności aplikacji z 5a:
# https://sekurak.pl/czym-jest-podatnosc-path-traversal/
# https://www.owasp.org/index.php/Path_Traversal