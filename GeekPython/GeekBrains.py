# Урок 7
"""""
Задание №1

"""""


def add_to_list(input_list=None):  # обычный способ
    if input_list is None:
        input_list = []
    input_list.append(2)
    return input_list


result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)


def add_to_list(input_list=None):  # ленивый способ через or
    input_list = input_list or []
    input_list.append(2)
    return input_list


result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)
