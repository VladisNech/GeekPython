# Урок 8
"""""
Задание №1
1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами 
(на уроке разбирали на примере одной функции).
2. Добавить возможность изменения текущей рабочей директории.
3. Добавить возможность развлечения в процессе работы с менеджером. 
Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.
"""""
# Функиция для создания файла
import os
import shutil  # позволяет копировать папки и файлы


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


# Встроенная игра
def get_game():
    from GeekPython.Data.game import game
    game()


# вызов других функций
if __name__ == '__main__':
    create_file('test.dat', 'some text')
    create_folder('new_folder')
    get_list()
    get_list(True)
    delete_all('new_folder')
    copy_file('new_folder', 'new_f')
    get_game()
