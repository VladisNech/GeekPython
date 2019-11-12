"""""
Задание №2
Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
Если список пустой функция должна вернуть None. 
Проверьте работу функций в этом же модуле.
Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
"""""

import random


def get_number_random_list():
    my_list = []
    for i in range(1, 10):
        numbers = random.randint(1, 20)
        my_list.append(numbers)
    print(my_list)
    if my_list is not None:
        print(random.choice(my_list))
    else:
        print('None')


get_number_random_list()
