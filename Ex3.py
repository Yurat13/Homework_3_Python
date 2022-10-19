# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Example - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# a = [1.1, 1.2, 3.1, 5, 10.01]

def difference_max_and_min_fractional_part_elements (spisok):
# a = [1.1, 1.2, 3.1, 5, 10.01]
    lst = []
    for i in spisok:
        b = round(i % 1, 2)
        if b != 0:
            lst.append(b)
    print(lst)
    max_value = max(lst)
    min_value = min(lst)
    print (f'{max_value} - {min_value}  = {max_value - min_value}')
    # min_value = lst[0]
    # max_value = lst[0]
    # for elem in lst:
    #     if min_value > elem:
    #         min_value = elem
    #     elif max_value < elem:
    #         max_value = elem
    # print (f'{max_value} - {min_value}  = {max_value - min_value}')
    # return max_value, min_value

a = [1.1, 1.2, 3.1, 5, 10.01]
difference_max_and_min_fractional_part_elements(a)