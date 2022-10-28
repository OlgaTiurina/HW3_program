# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке.

n = int(input('Введите число: '))
f1 = 1
f2 = 1
print(f1, f2, end=' ')

for i in range(2, n):
    nun = f1 + f2
    f1 = f2
    f2 = nun
    print(f2, end=' ')