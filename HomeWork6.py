# Задача 1. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))

# unique = list(set(lst))

# print(unique)


# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



# def twin_multiplication(list):
#     a = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
#     new_multiplication_list = [list[i]*list[len(list)-i-1] for i in range(a)]
#     print(f' {list} => {new_multiplication_list}')

# list = [22,31,67,8,45,567]
# twin_multiplication(list)

# 2 решение

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# a = len(li)//2 + 1 if len(li) % 2 != 0 else len(li)//2
# final_list = list(map(lambda x: [x]*[len()-x-1] , a))
# print(final_list)




# # Задача 3. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# # Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# from functools import reduce
  
# fibbo = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
#                                  range(n-2), [0, 1])
  
# print(fibbo(8))

# # Второй вариант

# def fibbo(count):
#     fib_list = [0, 1]
  
#     any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
#                                          range(2, count)))
  
#     return fib_list[:count]
  
# print(fibbo(8))