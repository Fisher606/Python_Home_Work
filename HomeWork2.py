# # Задача 1.  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# # Пример:

# # - 6782 -> 23
# # - 0,56 -> 11


# str1=str(input())
# print(str1)
# k=0
# for elem in str1:
#     if elem.isdigit():
#         k += int(elem)
#         print(elem)
# print(f' - {str1} ->' ,k)


# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input('input N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' ')




