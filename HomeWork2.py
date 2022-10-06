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


# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')


# Задача 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму (1+(1/n))^n

# n = int(input('Введите n '))
# list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
# print(f'Последовательность: {list}\nСумма: {sum(list)}')


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# Я не смог(

# import random
# n=int(input('input number '))
# list=[]
# for i in range(n):                      # генератор случайных чисел
#     a=random.randint(-n, n)
#     list.append(a)   
# print (list)
# index_list = input(f'введите позиции элементов от 1 до {n} через пробел').split()
# result=1
# for j in range(len(index_list)):        # перебор элементов с номерами позиций
#     a=int(index_list[j])-1
#     print (f'{result}*{int(list[a])}', end=' ')
#     result*=int(list[a])    
# print (f'= {result}')



# Задача 5. Реализуйте алгоритм перемешивания списка


# list = ['Высокогорный водолаз', 'RevenHolm', 4, 900, 'Neo prosnis, ty obosralsya!!!']
# print(list) 
# import random
# random.shuffle(list)
# print('->', list) 