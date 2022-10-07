# задача 2 . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint


def fill_list(n):
    lst = []
    for i in range(n):
        i = randint(-5, 5)
        lst.append(i)
    return lst

def unique_list(lst):
    lst1 = []
    for i in lst:
        if i in lst1:
            continue
        else:
            lst1.append(i)
    return lst1



N = int(input("Введите число N: "))
lst = fill_list(N)
print(lst)
lst1 = unique_list(lst)
print(lst1)
