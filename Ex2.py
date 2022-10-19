# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# lst = [3, 4, 5, 7, 12, 4, 8, 2, 6]
# lst2 = []
# n = len(lst)
# count_ = 0
# print(len(lst))

# while count_ < n/2:
#     multiply_of_couples = lst[0+count_] * lst[-1-count_]
#     print(f"{multiply_of_couples} = {lst[0+count_]} * {lst[-1-count_]}")
#     lst2.append(multiply_of_couples)
#     count_ += 1
# print(lst2)

def multiply_of_couples_elements(spisok):
    lst2 = []
    n = len(spisok)
    count_ = 0
    
    while count_ < n/2:
        multiply_of_couples = spisok[0+count_] * spisok[-1-count_]
        print(f"{multiply_of_couples} = {spisok[0+count_]} * {spisok[-1-count_]}")
        lst2.append(multiply_of_couples)
        count_ += 1
    print(lst2)
    return(lst2)


lst = [3, 4, 5, 7, 12, 4, 8, 2, 6]
multiply_of_couples_elements(lst)

