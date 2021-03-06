# УРОК №1 --------------------------------------------------------------------------------------------------------------
"""""
Задание №1
Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
"""""

number = int(input())
number += 2
print(number)

"""""
Задание №2
Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. 
И просите ввести заново.
Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.
"""""

number = int(input())

while (number <= 0) or (number >= 10):
    print('False')
    number = int(input())
else:
    print(number ** 2)

"""""
Задание №3
Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
Выведите результат согласно которому:
Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.

(Формула не соответствует реальной действительности и здесь используется только ради примера)
Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.  
Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно. 
В случае ошибок, уточните условия для той или иной ситуации.
Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
Пример: Вася Пупкин, 41 год, вес 121 - следует обратиться к врачу!
Пример: Вася Пупкин, 41 год, вес 49 - следует обратиться к врачу!
"""""

name, surname, age, weight = input('Введите ваше имя '), input('Введите вашу фамилию '), \
                             int(input('Введите ваш возраст ')), int(input('Введите ваш вес '))

if (age < 30) and (50 < weight < 120):
    print(name + ' ' + surname, ' ' + str(age) + ' год', ' вес - ' + str(weight), '- хорошее состояние', sep=', ')
elif (30 <= age < 40) and (50 >= weight or weight >= 120):
    print(name + ' ' + surname, ' ' + str(age) + ' год', ' вес - ' + str(weight), '- заняться собой', sep=', ')
elif (age >= 40) and (50 >= weight or weight >= 120):
    print(name + ' ' + surname, ' ' + str(age) + ' год', ' вес - ' + str(weight), "- следует обратиться к врачу!",
          sep=', ')
else:
    print(name + ' ' + surname, ' ' + str(age) + ' год', ' вес - ' + str(weight), "- мутант", sep=', ')

# Урок №2 -------------------------------------------------------------------------------------------------------------
"""""
Задание №1
Даны два произвольных списка. Удалите из первого списка элементы присутствующие во втором списке.
Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
"""""
# Версия с set:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

my_list_1 = set(my_list_1)
my_list_2 = set(my_list_2)

my_list_1 = my_list_1 - my_list_2
print(my_list_1)

# Версия с for in:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for number in my_list_1:
    if number in my_list_2:
        my_list_1.remove(number)

for number in my_list_1:
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)

"""""
Задание №2
Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
Ваша задача — вывести дату в текстовом виде, например: 
второе ноября 2013 года. 
Склонением пренебречь (2000 года, 2010 года)
"""""

date = input()
a, b, c = date.split('.')

days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одинадцатое',
    '12': 'двенадцатое',
}

month = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'агуста',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря',
}

result = f'{days[a]} {month[b]} {c} года'
print(result)

"""""
Задание №3
Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]

В этом случае ответ будет:
[5, 8]
"""""

my_list_1 = [2, 3, 2, 5, 12, 8, 2, 12, 3, 7]

result = []

for number in my_list_1:
    if my_list_1.count(number) == 1:
        result.append(number)
print(result)

# Урок №3 ------------------------------------------------------------------------------------------------------------

# Игра угадай число

import random
number = random.randint(1, 100)
# print(number)
# задаем переменные и создаем список
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
max_count = levels[int(input('Введите уровень сложности от 1 до 3 - '))]
# Вводим пользователей
user_count = int(input('Введите количество пользователей - '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i + 1} - ')
    users.append(user_name)

is_winner = False
winner_name = None
# начинаем цикл
while not is_winner:
    # Считаем попытки
    count += 1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    # Логика подбора чисел
    print(f'Попытка № {count}')
    for number_enum, user in enumerate(users, 1):
        print(f'Ход пользователя №{number_enum} {user}')
        user_number = int(input('Введите число - '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif user_number > number:
            print('Загаданное число меньше')
        else:
            print('Загаданное число больше')
else:
    print(f'Пользователь {winner_name} выиграл')

"""""
Задание №1
В этой игре человек загадывает число, а компьютер пытается его угадать.
В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. 
Компьютер начинает его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, игрок выбирает “победа”. 
Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”. 
Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”. 
Игра продолжается до тех пор пока компьютер не отгадает число.
Пример игры:
Допустим, пользователь загадал число 42
"""""

import random

min_number = 1
max_number = 100
user_mind = None

while user_mind != '=':
    number = random.randint(min_number, max_number)
    print(number)
    user_mind = input('Это число вы загадали? Введите подсказку - ')
    if user_mind == '<':
        max_number = number - 1
    elif user_mind == '>':
        min_number = number + 1
print("Число угадано")

# Урок №4 -------------------------------------------------------------------------------------------------------------
"""""
Задание №1
Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
"""""


def user(name, age, city):
    result = f'{name}, {age} год(а), проживает в городе {city}'
    return result


print(user(name=input(), age=int(input()), city=input()))

"""""
Задание №2
Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""""


def user(a, b, c):
    result = max(a, b, c)
    return result


print(user(a=int(input()), b=int(input()), c=int(input())))

"""""
Задание №3
Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. 
### Поэкспериментируйте со значениями урона и жизней по желанию. 
### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. 
### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
Функция должна сама работать со словарями и изменять их значения.
"""""

player = {'name': input(),
          'health': 100,
          'damage': 50}

enemy = {'name': input(),
         'health': 200,
         'damage': 40}


def attack(person1):
    if person1 == enemy['name']:
        player['health'] = player['health'] - enemy['damage']
        return player['health']
    elif person1 == player['name']:
        enemy['health'] = enemy['health'] - player['damage']
        return enemy['health']


print(attack(person1=input()))

"""""
Задание №3
Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. 
### Поэкспериментируйте со значениями урона и жизней по желанию. 
### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. 
### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
Функция должна сама работать со словарями и изменять их значения.
Задание №4
Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.
"""""

player = {'name': input(),
          'health': 100,
          'damage': 50,
          'armor': 10}

enemy = {'name': input(),
         'health': 200,
         'damage': 40,
         'armor': 2}


def get_damage(damage, armor):
    return damage / armor


def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage


attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)
# Урок №5 -------------------------------------------------------------------------------------------------------------

"""""
Задание №1
Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. 
Затем создайте вторую функцию удаляющую эти папки. 
Проверьте работу функций в этом же модуле.
"""""

import os


def mkdir():
    for i in range(1, 10):
        name = 'dir'
        new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.mkdir(new_path)


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


"""""
Задание №3
Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. 
Вызовите каждую функцию в main.py и проверьте что все работает как надо.
Примечание: 
Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
"""""
from LowPython.Test.mkdir import *
from LowPython.Test.mkdir import mkdir
from LowPython.Test.random import get_number_random_list
import LowPython.Test.random as my_random

mkdir()
get_number_random_list()

my_random.get_number_random_list()

# Урок №6 -------------------------------------------------------------------------------------------------------------

"""""
Задание №1
1: Создать модуль music_serialize.py. 
В этом модуле определить словарь для вашей любимой музыкальной группы, например:
my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал. 
Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
"""""
import pickle
import json

my_favourite_group = {
    'name': 'Г.М.О.', 'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]}

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
print(f)

with open('group.json', 'w', encoding='utf-8') as g:
    json.dump(my_favourite_group, g)
print(g)

print('Объект записан')

"""""
Задание №2
2: Создать модуль music_deserialize.py. 
В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. 
И получить объект: словарь из предыдущего задания.
"""""

with open('group.pickle', 'rb') as r:
    pickle.load(r)
print(my_favourite_group)

with open('group.json', 'r', encoding='utf-8') as q:
    json.load(q)
print(my_favourite_group)

print('Получен словарь -', my_favourite_group)
# Урок №7 -------------------------------------------------------------------------------------------------------------
"""""
Задание №1 (Решить с помощью генераторов списка)
Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
Примечание: Списки фруктов создайте вручную в начале файла.
"""""

fruit_list1 = ['Яблоки', 'Груши', 'Апельсины', 'Мандарины', 'Киви', 'Лимоны']
fruit_list2 = ['Яблоки', 'Инжир', 'Авокадо', 'Мандарины', 'Фейхуа', 'Лайм']
# Обычный способ
result = []
for fruit in fruit_list1:
    if fruit_list2.count(fruit) > 0:
        result.append(fruit)
print(result)
# Генератор
result = [fruit for fruit in fruit_list1 if fruit_list2.count(fruit) > 0]
print(result)

"""""
Задание №2 (Решить с помощью генераторов списка)
Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
Элемент кратен 3,
Элемент положительный,
Элемент не кратен 4.
Элемент не повторяется в изначальном списке.
"""""

import random

numbers = [random.randint(-10, 20) for number in range(20)]
print(numbers)

result = [number for number in numbers if
          number % 3 == 0 and number > 0 and number % 4 != 0 and numbers.count(numbers) == 0]
print(result)

"""""
Задание №3 (Решить с помощью генераторов списка)
Напишите функцию которая принимает на вход список. 
Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
и самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор
и тернарный оператор при необходимости). 
В результате работы функции исходный список не должен измениться.
Например:
old_list = [1, -3, 4]
result = [1, -3, 2]
"""""
import math

numbers = [1, -3, 4]


def new_sqrt_func(old_list):  # Смесь тернального оператора с генератором
    result = [round(math.sqrt(number)) if number > 0 else number for number in old_list]
    return result


print(numbers)
print(new_sqrt_func(numbers))

"""""
Задание №4
Написать функцию которая принимает на вход число от 1 до 100. 
Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, 
возведенное в квадрат.
Далее написать основной код программы. Пользователь вводит число. 
Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция. 
Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.
"""""


def exception(number):  # Вариант №1
    try:
        if number == 13:
            raise ValueError()
    except ValueError:
        print('Ошибка, введено число 13')
    else:
        print(number ** 2)


exception(number=int(input('Введите число - ')))


def exception(number):  # Вариант №2
    if number == 13:
        raise ValueError()
    else:
        return number ** 2


number = int(input())

try:
    result = exception(number)
except ValueError:
    print('Введено число 13')
else:
    print(result)
# Урок №8 -------------------------------------------------------------------------------------------------------------
"""""
Задание №1
1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами 
(на уроке разбирали на примере одной функции).
2. Добавить возможность изменения текущей рабочей директории.
3. Добавить возможность развлечения в процессе работы с менеджером. 
Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.
"""""
# Блок функций
# Функиция для создания файла
import os
import shutil  # позволяет копировать папки и файлы
import datetime


# Функиция для создания файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# Функиция для создания папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Файл уже создан')


# Функиция для проверки данных в дериктории
def get_list(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# Удаление папок и файлов
def delete_all(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# копирование папок и файлов
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Копируемая папка уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(massage):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {massage}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


# Встроенная игра
def get_game():
    os.getcwd()
    from Data.game import game
    game()


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())


# вызов других функций
if __name__ == '__main__':
    create_file('test.dat', 'some text')
    create_folder('new_folder')
    get_list()
    get_list(True)
    delete_all('new_folder')
    copy_file('new_folder', 'new_f')
    get_game()
    save_info('abc')

# блок вызова функций
from GeekBrains import create_file, create_folder, get_list, delete_all, copy_file, save_info, get_game, change_dir
import sys

save_info('start')

try:
    command = sys.argv[1]
except IndexError:
    print('Используйте терминал')
if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название удаляемого файла')
    else:
        delete_all(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Введите название файла и новое название')
    else:
        copy_file(name, new_name)
elif command == 'help':
    print('Помощь')
elif command == 'game':
    get_game()

elif command == 'ch':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название папки')
    else:
        change_dir(name)

save_info('finish')
# Урок №9 -------------------------------------------------------------------------------------------------------------
