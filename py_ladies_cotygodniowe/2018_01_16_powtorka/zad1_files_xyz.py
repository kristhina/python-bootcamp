# Napisz program, który w zależności od opcji podanej przez użytkownika (1, 2 lub 3)
# odczyta odpowiednio plik x.txt, y.txt lub z.txt (zawartość dowolna)
# obsługa błędów powinna obejmować (co najmniej) komunikat o nieprawidłowej opcji,
# zaś wczytywanie treści pliku powinno znaleźć się w oddzielnej funkcji (wraz z obsługą błędów)

def read_file_xyz():
    while True:
        decision = input("Which file do you want to read 1, 2 or 3?")
        if decision == "1" or decision == "2" or decision == "3":
            break
        print("Write the correct number 1, 2 or 3")
    if decision == "1":
        file = open('x.txt')

    elif decision == "2":
        file = open('y.txt')
    else:
        file = open('z.txt')

    data = file.read()
    file.close()
    print(data)


read_file_xyz()
