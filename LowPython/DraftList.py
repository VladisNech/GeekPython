import random

my_list = []
i = 0

for i in range(10):
    number = random.randint(1, 100)
    my_list.append(number)
print(sum(my_list), max(my_list), min(my_list))

# -------------------------------------------------------------------------------------------------------------------


def print_sep(my_sep, sep_len):
    return my_sep * sep_len


sep = print_sep('-', 10)
text = f'Hello {sep} fans {sep}'

print(text)

# -------------------------------------------------------------------------------------------------------------------

def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age='20', car='yes')
# -------------------------------------------------------------------------------------------------------------------

a, b = int(input()), int(input())
my_list = []

for i in range(a, b + 1):
    if i % 3 == 0:
        my_list.append(i)
c = len(my_list)

print(sum(my_list) / int(c))
# -------------------------------------------------------------------------------------------------------------------

# передача функции в другую функцию
import random

my_list = []
for i in range(1, 20):
    numbers = random.randint(1, 20)
    my_list.append(numbers)


def my_filter(function):
    result = []
    for number in my_list:
        if function(number):
            if my_list.count(number) == 1:
                result.append(number)
    return result


def is_even(number):
    return number % 2 == 0


def is_not_even(number):
    return number % 2 != 0


def max_num(number):
    return number > 4


print(my_filter(is_even), my_filter(is_not_even), my_filter(max_num), sep='\n')

# -------------------------------------------------------------------------------------------------------------------

# lambda-функции
import random
my_list = []
for i in range(1, 20):
    numbers = random.randint(1, 20)
    my_list.append(numbers)


def my_filter(function):
    result = []
    for number in my_list:
        if function(number):
            if my_list.count(number) == 1:
                result.append(number)
    return result


print(my_filter(lambda number: number % 2 == 0), my_filter(lambda number: number % 2 != 0),
      my_filter(lambda number: number > 4), sep='\n')

# -------------------------------------------------------------------------------------------------------------------

# lambda-функции без дубликатов в списке
import random
my_list = []
other_list = []
for i in range(1, 20):
    numbers = random.randint(1, 20)
    my_list.append(numbers)
print(my_list)


def my_filter(function):
    result = []
    for number in my_list:
        if function(number):
            if my_list.count(number) == 1:
                result.append(number)
            else:
                other_list.append(number)
    return result


new_other_list = list(set(other_list))
print(new_other_list)
my_list = my_list + new_other_list

print(my_filter(lambda number: number % 2 == 0), my_filter(lambda number: number % 2 != 0),
      my_filter(lambda number: number > 4), sep='\n')
# -------------------------------------------------------------------------------------------------------------------
# сортировка по функции
cities = [('Москва ', 1000), ('Лондон', 5000), ('Париж', 10000)]


def by_count(city):
    return cities[1]


print(sorted(cities, key=lambda city: cities[1]))
# -------------------------------------------------------------------------------------------------------------------
# фильтрация

def is_even(number):
    return number % 2 == 0


print(f'Специально для Андрея {sorted(list(set(filter(lambda number: number % 2 == 0, my_list))))} - нужная '
      f'последовательность')
# -------------------------------------------------------------------------------------------------------------------
# фильтрация
import random
my_list = []
for i in range(1, 20):
    numbers = random.randint(1, 20)
    my_list.append(numbers)
print(sorted(set(my_list)))

my_list = sorted(set(map(lambda number: number ** 2, my_list)))
print(list(map(lambda number: str(number), my_list)))
# -------------------------------------------------------------------------------------------------------------------

# Импорт модулей и библиотек
import math
import random as rd
from random import randint, random

print(math.pi)

print(math.cos(90))

print(rd.randint(1, 10))

print(randint)
print(random)
# -------------------------------------------------------------------------------------------------------------------

import math

r = 4

# Найти длину окружномти
print(round(2 * r * math.pi))

# Найти площадь окружности
print(r ** 2 * math.pi)
print(math.pow(r, 2) * math.pi)

# по координатам двух точек найти расстояние меж ними

x1 = 100
y1 = 200
x2 = 50
y2 = 150

print(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

# Найти факториал

print(math.factorial(9))
# -------------------------------------------------------------------------------------------------------------------
# Создание папок

import os
import sys

name = sys.platform

for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
    os.mkdir(new_path)

# -------------------------------------------------------------------------------------------------------------------

# Консольные команды
import os
import sys


def ping():
    print('pong')


def hello(per_name):
    print('Hello', per_name)


def get_info():
    print(os.listdir(path))


param = sys.argv[1]

if param == 'ping':
    ping()
elif param == 'list':
    get_info()
elif param == 'name':
    name = sys.argv[2]
    hello(name)
# -------------------------------------------------------------------------------------------------------------------

# работа с открытием и чтением файлов

f = open('first.txt', 'w')

f.write('Хай\n')
f.write('мир\n')

f.writelines(['hello\n', 'Python\n'])

f = open('first.txt', 'r')

# print(f.read())

for line in f:
    print(line.replace('\n', ''))

# print(f.readlines())
f.close()

with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))
print('end')
# -------------------------------------------------------------------------------------------------------------------

# работа с байтами, запись, кодирование и декодирование
s = 'string'

sb = b'byte'

print(type(b), b, sep='\n')

print(sb[2])
print(sb[2:4])

for item in sb:
    print(item)

s = 'hello world мир'

sb = s.encode('utf-8')

sb = sb.decode('utf-8')

print(sb)
# -------------------------------------------------------------------------------------------------------------------

with open('bytes.txt', 'wb') as f:
    f.write(b'Hello World')

with open('bytes.txt', 'r', encoding='ascii') as f:
    print(f.read())

with open('bytes.txt', 'wb') as f:
    my_str = 'Привет мир'
    f.write(my_str.encode('utf-8'))

with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

with open('bytes.txt', 'wb') as f:
    my_str = 'Привет мир'
    f.write(my_str.encode('utf-8'))

with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    s = result.decode('utf-8')
    print(s)
# -------------------------------------------------------------------------------------------------------------------

import pickle

person = {'name': 'Vlad', 'Phones': [123, 456]}
# пишем словарь через пикли
with open('person.dat', 'wb') as f:
    pickle.dump(person, f)
print('Объект записан')

# читаем словарь через пикли
with open('person.dat', 'rb') as f:
    pickle.load(f)
print(person)
# -------------------------------------------------------------------------------------------------------------------

# пишем и читаем через json
import json

person = {'name': 'Vlad', 'age': '23', 'Phones': [123, 456]}, {'name': 'Leo', 'age': '24'}

a = json.dumps(person)

print(person)

json.loads(a)

print(a)

with open('person.jon', 'w') as f:
    a = json.dump(person, f)

with open('person.jon', 'r') as f:
    a = json.load(f)
print(a)

# -------------------------------------------------------------------------------------------------------------------

# Тернарный оператор
is_has_name = True

name = "Max" if is_has_name else 'Empty'

print(name)

# -------------------------------------------------------------------------------------------------------------------
# Обычный оператор
word = "слово"

result = []

for i in range(len(word)):
    if i % 2 != 0:
        letter = word[i].lower()
    else:
        letter = word[i].upper()
    result.append(letter)

result = ''.join(result)

print(result)

# Тернальный оператор
result = []

for i in range(len(word)):
    letter = word[i].lower() if i % 2 != 0 else word[i].upper()
    result.append(letter)

result = ''.join(result)  # Перевод списка в строку
print(result)
# -------------------------------------------------------------------------------------------------------------------

# Generator of list
import random

my_list = []

for i in range(1, 10):
    numbers = random.randint(-30, 10)
    my_list.append(numbers)
print(my_list)

result = []

# realise through cycle FOR
for i in my_list:
    if i > 0:
        result.append(i)
print(result)

# create through lambda function
result = filter(lambda number: number > 0, my_list)
print(list(result))

# create though generator

result = [number for number in my_list if number > 0]
print(result)
# -------------------------------------------------------------------------------------------------------------------
# genegator of dict
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

result = {}
# though cycle FOR
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val
print(result)
# through generator of dict
result = {pair[0]: pair[1] for pair in pairs}
print(result)
# -------------------------------------------------------------------------------------------------------------------
# make a list from 1 to 100 random numbers
import random

numbers = [random.randint(1, 100) for number in range(10)]
print(numbers)

# Создать список квадратных чисел
numbers = [1, 2, 3, -4]

numbers = [number ** 2 for number in numbers if number > 0]
print(numbers)

# Создать список имен на букву А

names = ['Max', 'Alan', 'Kate', 'Bob', 'Andrey', 'John', 'Anna']

names = [name for name in names if name[0] == 'A']
names = [name for name in names if name.startswith('A')]  # Альтернативаная запись
print(names)
# -------------------------------------------------------------------------------------------------------------------

s = 'asd'
i = {'a': 'asd'}
# через IF
if len(s) != 0:
    print('строка не пустая')
else:
    print('Строка пустая')
# тернальный
a = "string is not empty" if s else 'string is empty'
print(a)

# удобный способ, можно использовать логические выражения and и or
if s and i:
    print('строка не пустая')
else:
    print('Строка пустая')
# -------------------------------------------------------------------------------------------------------------------
# использование and
import math
import random

numbers = [random.randint(-5, 5) for number in range(10)]
print(numbers)

result = []
# обычный способ
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        if sqrt < 2:
            result.append(number)
print(result)

# Ленивый способ

result = []

for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)
# Генератор
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]

print(result)


# -------------------------------------------------------------------------------------------------------------------
#  использование or

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
# -------------------------------------------------------------------------------------------------------------------
# изменение значения в списке путем передачи оного списка параметром в функцию
numbers = [1, 2, 3]


def change_number(input_list):
    input_list[1] = 200


change_number(numbers)

print(numbers)

a = [1, 2, 3]
# срез
b = a[:]
b[1] = 100
print(a)
print(b)

# методом copy
b = a.copy()
b[1] = 100

print(a)

# Метод глубокого копирования
import copy

c = [1, 2, [3, 4]]
b = copy.deepcopy(c)
b[2][1] = 100

print(c, b)
# -------------------------------------------------------------------------------------------------------------------
# Обработка исключений
try:
    a = int(input())
    a = 100 // a
except ZeroDivisionError:
    print('деление на 0')
except Exception as e:
    print('Введены буквы вместо чисел')
    print('Информация об ошибке', e)
else:
    print('Ошибки не произошло, число -', a)
    raise Exception('что-то пошло не так')  # создание исключения
finally:
    print('все хорошо, всегда выполняюсь')
# -------------------------------------------------------------------------------------------------------------------
