# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


n = int(input('Enter number n = '))
x = [0, 1]
for i in range(0, n-1):
    x.append(x[-1] + x[-2])
y = print(', '.join(str(y) for y in x))
x = [1, 0]
for i in range(0, n):
    x.append(x[-2] - x[-1])
z = print(', '.join(str(y) for y in x))

    
