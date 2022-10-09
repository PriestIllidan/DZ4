# задача 2 . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint


def fill_list(n):
    lst = []
    for i in range(n):
        i = randint(-5, 5)
        lst.append(i)
    return lst


def uniq_list(lst):
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return lst1


N = int(input("Введите число N: "))
lst = fill_list(N)
print(lst)
lst1 = uniq_list(lst)
print("Через цикл:")
print(lst1)
print("Через функцию:")
lst1 = set(lst)
print(lst1)