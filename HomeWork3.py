# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# a = [22,31,67,8,4,567]

# print(f' {a} -> на нечётных позициях элементы {a[1::2]}, ответ: {sum(a[1::2])} ')


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


# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(round (max-min, 3))

