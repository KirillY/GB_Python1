### module for hw05 ###

import os, shutil, sys


def create_dir(dir_path):
    try:
        dir_path = os.path.join(os.getcwd(), dir_path)
        os.mkdir(dir_path)
        print("Directory '{}' was successfully created in the current working dir".format(dir_path))
    except FileExistsError:
        print("Directory '{}' already exists in the current working dir".format(dir_path))


# from inspect import signature
# len(signature(create_dir).parameters)

def remove_dir(dir_path):
    try:
        dir_path = os.path.join(os.getcwd(), dir_path)
        os.rmdir(dir_path)
        print("Directory '{}' was successfully removed from the current working dir".format(dir_path))
    except FileNotFoundError:
        print("Directory '{}' doesn't exist".format(dir_path))


def change_dir(dir_path):
    '''
    changing current working dir to dir_path
    '''
    # dir_path = dir_path[1]
    try:
        dir_path = os.path.join(os.getcwd(), dir_path)  # join dir_path to cwd, in case dir_path is not full path
        os.chdir(dir_path)  # goto dir_path
        # print('{}>'.format(os.getcwd()))
    except FileNotFoundError:
        print("Directory '{}' doesn't exist".format(dir_path))

# if default parameter is dir_name = os.getcwd(), it doesn't redefines later TODO: check in import
# in import default parameter dir_name = os.getcwd() works fine, 'ls' shows new directory after each 'cd' command
# looks like in import it creates new scope each time
def get_current_subdirectories(dir_name = os.getcwd()):
    '''
    print subdirectories in current working dir_name
    :dir_name: full source path
    :return: None
    '''
    L = []
    dir_name = os.getcwd()
    for name in os.listdir(dir_name):  # iterate over files and dirs in the given directory
        if os.path.isdir(
                os.path.join(dir_name, name)):  # concatenate dir_name path and entities in it, then if result is dir
            L.append(name)  # append entity to the list
    print('Current sub folders:')
    [print(elt) for elt in L]


def help_menu():
    print('''help
cd <path> or <folder> - change directory
ls - current directory content
del <path> or <folder>- delete empty directory
mkdir <path> or <folder> - create directory
q - quit''')
