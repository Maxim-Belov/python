import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dir(dir_name: str=None):
    if not dir_name:
        print('Please, enter directory name to create')
        return
    try:
        os.mkdir(dir_name)
        print(f'The {dir_name} directory has been successfully created')
    except FileExistsError:
        print(f'The {dir_name} directory already exists')


def remove_dir(dir_name: str=None):
    if not dir_name:
        print('Please, enter directory name to delete')
        return
    try:
        os.rmdir(dir_name)
        print(f'The {dir_name} directory has been successfully deleted')
    except FileNotFoundError:
        print(f'Failed to delete the directory to {dir_name} since there is not directory named '
              f'{dir_name} in {os.getcwdb()}')


# for i in range(1, 10):
#     dir_name = f'dir_{i}'
#     make_dir(dir_name)
#     remove_dir(dir_name)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_current_dir():
    current_dir = os.getcwd()
    print('The list of files in current directory: {}'.format(', '.join(os.listdir(current_dir))))


# list_current_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_current_file():
    current_file = os.path.basename(__file__)

    shutil.copy(current_file, f'{current_file}'.replace('.py', '_copy.py'))


# copy_current_file()
