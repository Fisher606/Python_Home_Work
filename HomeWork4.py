# Задача 1. Вычислить число c заданной точностью d
# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi

# d =  int(input("Какую точность числа Пи Вы хотите увидеть?\n"))
# print(f'Заданная точность числа ПИ {d} равна {round(pi, d)}')


# Задача 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# number=int(input("Введите число: "))
# for i in range(1, number+1):
#     if(number%i==0):
#         print(i)

# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list((int, input("Введите числа через пробел:\n").split()))

unique_numbers = list(set(lst))

print(unique_numbers)