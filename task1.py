# задача 1. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def simple_mult(n):
    lst = []
    for i in range(2, n+1):
        while n % i == 0:
            lst.append(i)
            n = n/i
    return lst


N = int(input("Введите натуральное число N: "))
lst = simple_mult(N)
print("Простыми множителями числа", N, "являются", lst)
