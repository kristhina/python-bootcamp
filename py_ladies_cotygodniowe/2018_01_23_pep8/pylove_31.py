
"""Not Missing Docstring"""
import math
import random
import this


def nic_nie_robie():
    """
    funkcja kompletnie do niczego nie potrzebna
    :return:
    """
    our_pi = math.pi
    random.randint(0, int(our_pi))
    return this


def podzielna(liczba, podzielna_przez):
    """
    :param liczba:
    :param podzielna_przez:
    :return: True/False
    """
    return liczba % podzielna_przez == 0


def ugly(liczba):
    """
    funkcja brzydkiej liczby ;)
    :param liczba:
    :return: True/False
    """
    if liczba == 1:
        return True
    for i in [2, 3, 5]:
        if podzielna(liczba, i):
            return True
    return False


print(ugly(11))
print(ugly(12))


def time(czas, jednostka):
    """
    :param czas:
    :param jednostka:
    :return: coś tam z czasem
    """
    hour, minute, second = czas.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    if jednostka == 'second':
        return hour * 3600 + minute * 60 + second
    elif jednostka == 'minute':
        return hour * 60 + minute + round(second / 60, 2)
    else:
        return hour + round(minute / 60, 2) + round(second / 3600, 2)


print(time('01:15:59', 's'))
print(time('01:15:59', 'm'))
print(time('01:15:59', 'h'))

result = []
r2 = []


def flatten(arr):
    for el in arr:
        if isinstance(el, list):
            flatten(el)
        else:
            result.append(el)
    return result


def flatten_nr(arr):
    while True:
        el = arr.pop()
        if not isinstance(el, list):
            r2.append(el)
        else:
            arr = el
        if len(arr) == 0:
            break
    return r2[::-1]


print(flatten([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))
print(flatten_nr([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))


def weird_power(num):
    return num ** 2, num ** 3


def calculate(afun, data):
    return afun(weird_power(data))


CONSTANT_A = 3


def sum_a(whatever):
    return sum(whatever)


b = sum_a(CONSTANT_A)
c = calculate(b, CONSTANT_A)
print(c)


def sorted_a(whatever):
    return sorted(whatever)


d = sorted_a(CONSTANT_A)
f = calculate(d, CONSTANT_A)
print(f)


def power_2(a):
    return (a + 0.5 * a) ** 2


print(power_2(3))

x = lambda a: (a + 0.5 * a) ** 2
print(x(3))


data = [(9, 0), (1, 2), (3, 4)]
sorted_data = sorted(data, key=lambda a: a[0], reverse=False)
max_data = max(data, key=lambda a: max(a))
min_data = min(data, key=lambda a: max(a))
filtered_data = list(filter(lambda a: sum(a) > 5, data))

print({'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': 1}}}}}}}}}}}}}}}}}}}}}}})