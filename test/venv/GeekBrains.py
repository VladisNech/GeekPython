# Урок №4
"""""
Задание №1
"""""


def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age='20', car='yes')
