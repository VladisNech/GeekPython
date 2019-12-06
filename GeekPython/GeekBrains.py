# Урок 8
"""""
Задание №1

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


# вызов других функций
if __name__ == '__main__':
    create_file('test.dat', 'some text')
    create_folder('new_folder')
    get_list()
    get_list(True)
    delete_all('new_folder')
    copy_file('new_folder', 'new_f')
