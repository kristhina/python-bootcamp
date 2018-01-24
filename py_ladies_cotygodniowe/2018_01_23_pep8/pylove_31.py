
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
    return hour + round(minute / 60, 2) + round(second / 3600, 2)


print(time('01:15:59', 's'))
print(time('01:15:59', 'm'))
print(time('01:15:59', 'h'))


def flatten(arr):
    """
    Docstring for function 'flatten'
    :param arr:
    :return:
    """
    result = []
    for element in arr:
        if isinstance(element, list):
            flatten(element)
        else:
            result.append(element)
    return result


def flatten_nr(arr):
    """
    Docstring for function 'flatten_nr'
    :param arr:
    :return:
    """
    rr2 = []
    while True:
        element = arr.pop()
        if not isinstance(element, list):
            rr2.append(element)
        else:
            arr = element
        if not arr:
            break
    return rr2[::-1]


print(flatten([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))
print(flatten_nr([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))


def weird_power(num):
    """
    Docstring for weird_power
    :param num:
    :return:
    """
    return num ** 2, num ** 3


def calculate(afun, data1):
    """
    Docstring for calculate
    :param afun:
    :param data1:
    :return:
    """
    return afun(weird_power(data1))


CONSTANT_A = [3]


def sum_a(whatever):
    """
    Docstring for sum_a
    :param whatever:
    :return: number
    """
    return sum(whatever)


MY_B = sum_a(CONSTANT_A)
MY_C = calculate(MY_B, CONSTANT_A)
print(MY_C)


def sorted_a(whatever):
    """
    Docstring for sorted_a
    :param whatever:
    :return: sorted whatever
    """
    return sorted(whatever)


MY_D = sorted_a(CONSTANT_A)
MY_F = calculate(MY_D, CONSTANT_A)
print(MY_F)


def power_2(number):
    """
    Docstring for power_2
    :param number:
    :return:
    """
    return (number + 0.5 * number) ** 2


print(power_2(3))
DATA = [(9, 0), (1, 2), (3, 4)]
SORTED_DATA = sorted(DATA, key=lambda a: a[0], reverse=False)
MAX_DATA = max(DATA)
MIN_DATA = min(DATA)
FILTERED_DATA = list(filter(lambda a: sum(a) > 5, DATA))

INSIDE = {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': {'a': 1}}}}}}}}}}
INSIDE2 = {'a': {'a': {'a': {'a': {'a': {'a': INSIDE}}}}}}
print({'a': {'a': {'a': {'a': {'a': {'a': {'a': INSIDE2}}}}}}})
