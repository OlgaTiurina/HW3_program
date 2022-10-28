# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import *
list = []
n = int(input('Введите число: '))
summ = 0
for _ in range(n):
     list.append(randint(1, n))
print(list)
for i in range(0, n):
     if i % 2 == 0:
         i += 1
     else:
         summ = summ + list[i]
         i += 1
print(summ)