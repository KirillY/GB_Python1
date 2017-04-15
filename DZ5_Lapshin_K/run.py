import libs.myfirstlib as mylib
import os

print(mylib.do_something())
print(os.name)
print('os.getcwd() = ', os.getcwd())

dir_path = os.path.join(os.getcwd(), 'NewDir')
try:
    os.mkdir(dir_path)
except FileExistsError:
    print('Такая директория уже существует')
