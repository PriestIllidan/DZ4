# задача 1. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def simple_mult(n):
    lst = []
    for i in range(1, n+1):
        if n%i == 0:
            lst.append(i)
    return lst

N = int(input("Введите натуральное число N: "))
lst = simple_mult(N)
print(lst)

