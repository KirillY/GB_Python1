# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку cd
# 2. Просмотреть содержимое текущей папки ls
# 3. Удалить папку del
# 4. Создать папку mkdir
# При выборе пунктов: 1, 3,4, программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"

# Для решения данной задачи используйте алоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py

import NewDir.easy as easy, os, shlex
from inspect import signature

while True:
    raw_command = input(os.getcwd() + '>')  # getting user input
    raw_command = raw_command.replace("\\",
                                      "\\\\")  # '\' -> '\\' shlex parser will treat backslashes as backslash, not as control char
    args = shlex.split(raw_command, posix=True)  # splitting str by spaces preserving quotes
    command = args[0]  # first elt is command (cd, del...)
    # print(args)
    d = {  # making command dir
        'cd': easy.change_dir,
        'ls': easy.get_current_subdirectories,
        'del': easy.remove_dir,
        'mkdir': easy.create_dir,
        'help': easy.help_menu
    }

    if raw_command == 'q':
        break
    else:
        try:
            func_name = d[command]  # remember function name
            args_len = len(
                signature(func_name).parameters)  # remember number of given function parameters for the exception
            # print("'{}'".format(args[1:])) # checking other arguments
            func_name(*args[1:])  # function execution, [1:] returns None if more than
        except KeyError:  # if unknown key was entered
            print('Unknown command')
        except TypeError:  # if more arguments were given then required
            print("Function '{}' takes {} positional argument, {} were given".format(func_name.__name__, args_len,
                                                                                          len(args[1:])))
