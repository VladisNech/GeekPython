# Урок 4
"""""
Задание №1
"""""

a, b = int(input()), int(input())
my_list = []

for i in range(a, b + 1):
    if i % 3 == 0:
        my_list.append(i)
c = len(my_list)

print(sum(my_list) / int(c))
