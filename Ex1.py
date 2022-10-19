# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from operator import index


lst = [2, 3, 5, 7, 4, 9, 8, 24]
lst2 = []
sum_odd_elements = 0
for i in lst:
    if lst.index(i) % 2 > 0:
        sum_odd_elements = i + sum_odd_elements
        lst2.append(i)
print(sum_odd_elements)
print(lst2)