# Урок 5
"""""
Задание №1

"""""

import os
import sys

path = os.getcwd()


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

