# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, shutil


def create_dir_1_8(n=1, m=8):
    '''
    creates empty dir_n...dir_m in the current directory
    have no return
    '''
    count = 0
    for i in range(n, m + 1):  # iterating over the arguments
        dirpath = os.path.join(os.getcwd(), 'dir_' + str(i))  # creating path for each dir
        # print(dirpath)
        try:
            os.mkdir(dirpath)  # trying to create a dir
            count += 1  # if success, increase count for print statement
        except FileExistsError:
            print('dir_{} already exists'.format(i))
    print('{} dirs were successfully created \n'.format(count))


def remove_dir_1_8(n=1, m=8, dir_name='dir'):
    '''
    remove empty 'dir_name'+'_'+n...'dir_name'+'_'+m from the current directory
    have no return
    '''
    count = 0
    for i in range(n, m + 1):  # iterating over the arguments
        dirpath = os.path.join(os.getcwd(), dir_name + '_' + str(i))  # creating path for each dir
        print(dirpath)
        try:
            os.rmdir(dirpath)  # trying to remove a dir
            count += 1
        except FileNotFoundError:  # if dir is not found
            print("{}_{} doesn't exist or is not empty".format(dir_name, i))
    print('{} empty dirs were successfully removed \n'.format(count))


def create_dir(dir_path):
    try:
        dir_path = os.path.join(os.getcwd(), dir_path)
        os.mkdir(dir_path)
        print("Directory '{}' was successfully created in the current working dir".format(dir_path))
    except FileExistsError:
        print("Directory '{}' already exists in the current working dir".format(dir_path))


def remove_dir(dir_path):
    try:
        os.remove(dir_path)
        print("Directory '{}' was successfully removed from the current working dir".format(dir_path))
    except FileNotFoundError:
        print("Directory '{}' doesn't exist".format(dir_path))


def change_dir(dir_path):
    try:
        os.path.join(os.getcwd(), dir_path)
        os.chdir(dir_path)
        print('{}>'.format(os.getcwd()))
    except FileNotFoundError:
        print("Directory '{}' doesn't exist".format(dir_path))

# change_dir('C:\\Users\\Cactus\\OneDrive\\Edu\\GeekBrains\\Python 1\\')


# Задача-2:
# Напишите скрипт отображающий папки текущей директории

def get_current_subdirectories(): # if default parameter is dir_name = os.getcwd(), it doesn't redefines later TODO: check in import
    '''
    print subdirectories in current working dir_name
    :dir_name: full source path
    :return: None
    '''
    L = []
    dir_name = os.getcwd()
    for name in os.listdir(dir_name):  # iterate over files and dirs in the given directory
        if os.path.isdir(
                os.path.join(dir_name, name)):  # concatenate dir_name path and entities in it, if result is dir
            L.append(name)  # append entity to the list
    print('Current subdirectories are:')
    [print(elt) for elt in L]
    print('\n')

# get_current_subdirectories()

# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт


def copy_current_file(file_name=None, dir_name=os.getcwd()):
    '''
    copy current file in the given directory (current dir by default)
    'copy_' is added at the beginning to created copy
    :dir_name: full destination path for copy_file.ext
    :return: None
    '''
    current_file_path = os.path.abspath(__file__)  # get absolute path=Full_Path
    get_basename = os.path.basename(
        current_file_path)  # extract basename=File_name from current path alt: get_basename = os.path.basename(sys.argv[0])
    if file_name is None:
        file_name = 'copy_' + get_basename
    try:  # copy file from current_file_path to dir_name/copy_filename.ext
        shutil.copyfile(current_file_path, os.path.join(dir_name, file_name))
        print('File copy was successfully created at {}'.format(dir_name))
    except IOError:
        print('{} is not writable'.format(dir_name))


if __name__ == "__main__":  # check if file is used in import
    create_dir_1_8()
    input('Enter any raw_command to proceed \n')
    remove_dir_1_8()
    input('Enter any raw_command to proceed \n')
    get_current_subdirectories()
    input('Enter any raw_command to proceed \n')
    copy_current_file(file_name='easy.py',
                      dir_name='C:\\Users\\Cactus\\OneDrive\\Edu\\GeekBrains\\Python 1\\DZ5_Lapshin_K\\NewDir')
