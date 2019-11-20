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
