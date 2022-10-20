# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Enter numner N = '))
# a = n
# while a > 0:
#     b = a % 2
#     print (b, end ="")
#     a = a // 2


n = int(input('Enter numner N = '))
a = n
lst = []
while a > 0:
    b = a % 2
    lst.append(b)
    a = a // 2
s = ''.join(str(i) for i in lst)
print (s[::-1])