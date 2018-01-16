# Napisz algorytm, który na wejście przyjmie listę zawierającą tylko stringi i integery.
# Zwróci listą zawierającą tylko powtarzające się wartości, nie zmieniając ich kolejności.
# Przykład: [1, 2, 3, 1, 3] 1 i 3 nie są unikalne, więc wynikiem będzie [1, 3, 1, 3].


def notunique(my_list):
    unique_list = []
    nonunique_list = []
    for item in my_list:
        if my_list.count(item) == 1:
            unique_list.append(item)
        else:
            nonunique_list.append(item)
    return nonunique_list


print(notunique([1, 2, 3, 1, 3, 2, "w", "kkk", 1, 17, "kkk"]))
