from random import randint


def my_sort(input_list: list, ascending: bool = True):
    sorted_list = input_list.copy()
    for i in range(0, len(sorted_list)):
        for j in range(i, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    if not ascending:
        sorted_list = sorted_list[::-1]

    return sorted_list


# Тестирование на заданных значениях из примера
input_list = [-3, 1, 1, 2, 8, 5]
print(my_sort(input_list, ascending=False))


# Тестирование на сгенерированных произвольно значениях
def random_list():
    list = []
    for i in range(1, 10):
        numbers = randint(-100, 100)
        list.append(numbers)
    return list


print(my_sort(random_list(), ascending=True))
