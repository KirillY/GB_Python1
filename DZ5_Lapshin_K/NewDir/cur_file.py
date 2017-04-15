import os, sys

print(os.path.abspath(__file__))
print(sys.argv[0])

import shutil, sys, os

# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.split(os.path.abspath(__file__))) # return ('C:\\Users\\Cactus\\OneDrive\\Edu\\GeekBrains\\Python 1\\DZ5_Lapshin_K\\NewDir', 'cur_file.py')

print('sys.argv = ', sys.argv)
# Список путей для поиска модулей
print('sys.path = ', sys.path)
# Полный путь к интерпретатору
print('sys.executable = ', sys.executable)
# Словарь имён загруженных модулей
print('sys.modules = ', sys.modules)
# Информация об операционной системе
print('sys.platform = ', sys.platform)



# my_file = sys.argv[0]
# my_file_copy = my_file + '.copy'
# try:
#     shutil.copy(my_file, my_file_copy)
# except FileExistsError:
#     print('Не удалось создать копию файла.')
# print(my_file, my_file_copy)