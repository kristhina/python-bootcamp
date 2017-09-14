from klasowo import Person
from average_class import ListStats

# from my_package.my_stats import Vector as MyVector
# from my_package.better_stats import Vector as BetterVector

import my_package.my_stats
import my_package.better_stats as bs


def find_max(list_of_numbers):
    v = bs.Vector()
    li = []
    child = Person()
    mother = Person()
    mother.get
    return max(list_of_numbers)


def sort_list(list_of_numbers):
    sorted_list = []
    l = len(list_of_numbers)
    for i in range(l):
        x = min(list_of_numbers)
        sorted_list.append(x)
        list_of_numbers.remove(x)
    return sorted_list


def is_prime(number_to_check):
    if number_to_check in [0, 1]:
        return False
    if number_to_check == 2:
        return True
    for i in range(2, number_to_check - 1):
        if number_to_check % i == 0:
            return False
    return True


def is_prime_for_list(list_to_check):
    list_of_bools = []
    for element in list_to_check:
        list_of_bools.append(is_prime(element))
    return list_of_bools


# print("Hello world!")
# print(find_max([1, 3, 5]))
# print(sort_list([1, 5, 7, 3, 9, 4]))
# print(sort_list([1, 3, 0, 6, 7, 13]))
# if is_prime(1):
#     print("is prime")
# else:
#     print("not prime")

jac = Person("Jacek")
pio = Person("Łukasz")
kry = Person("Krysia", surname="Piątkowska")
jac.mother = kry
jac.father = pio

jac.say_hello()
jac.father.say_hello()
jac.mother.say_hello()

print(jac.get_name())

jac.set_age(3)
print(jac.get_age())

list_to_average = ListStats([2, 5, 6])
print(list_to_average.get_list_average())
