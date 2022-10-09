# задача 3. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def random_coefficient(k):
    lst = []
    for i in range(k+1):
        i = randint(0, 100)
        lst.append(i)
    return lst


def equation(k, lst):
    x = "*x**"
    new_lst = []
    for i in lst:
        if k != 0:
            x = str(i) + x + str(k)
            new_lst.append(x)
            x = "*x**"
            k = k - 1
        else:
            x = str(i)
            new_lst.append(x)
    return new_lst


K = int(input('Введите значение степени K: '))
lst1 = random_coefficient(K)
print(lst1)
lst2 = equation(K, lst1)
print(lst2)
result = "+".join(lst2)
print("Пулученный результат: ", result)
