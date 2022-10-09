# задача 4. Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def find_multiple(a, b):
    max = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    max = max // (a+b)    
    return max

number1 = int(input("Введите 1 число: "))
number2 = int(input("Введите 2 число: "))
max1 = find_multiple(number1, number2)
print("НОК = ", max1)


# Решение только для частных случаев:
# def simple_mult(n):
#     lst = []
#     for i in range(2, n+1):
#         while n % i == 0:
#             lst.append(i)
#             n = n/i
#     return lst


# def find_multiple(lst1, lst2):
#     for i in lst2:
#         if i not in lst1:
#             lst1.append(i)
#     res = 1
#     for i in lst1:
#         res = res * i
#     return res


# A = int(input("Введите первое число: "))
# B = int(input("Введите второе число: "))
# if A > B:
#     lst1 = simple_mult(A)
#     lst2 = simple_mult(B)
# else:
#     lst1 = simple_mult(B)
#     lst2 = simple_mult(A)
# print(lst1)
# print(lst2)
# result = (find_multiple(lst1, lst2))
# print("НОК =", result)
