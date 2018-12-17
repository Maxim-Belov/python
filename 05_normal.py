# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import os
import sys
from lesson05.home_work.hw05_easy import remove_dir, make_dir, list_current_dir


def print_help():
    print("cd <dir_name> - change directory")
    print("ls - list files in current directory")
    print("rm <dir_name> - remove directory")
    print("mkdir <dir_name> - create directory")


def change_dir(dir_name: str=None):
    if not dir_name:
        print('Please, enter directory name to navigate')
        return
    try:
        os.chdir(dir_name)
        print(f'You are now in the {dir_name} directory')
    except FileNotFoundError:
        print(f'Failed to change the {dir_name} directory since there is not directory named '
              f'{dir_name} in {os.getcwdb()}')


try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

if key == 'help':
    print_help()
elif key == 'cd':
    change_dir(dir_name)
elif key == 'ls':
    list_current_dir()
elif key == 'rm':
    remove_dir(dir_name)
elif key == 'mkdir':
    make_dir(dir_name)
else:
    print('Invalid key. For more details, use the "help" key')

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py