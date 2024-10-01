# -----------------------------------------------------------------------------
# Author: Pedram Keyani
# Email: pedram@openai.com
# Date: 2024-10-01
#
# Description: 
# The microbits python file documentation notes that the micro python implentation
# of files is very limited. In order to append, you must first read the contents,
# add your new content to that list and then overwrite the file. The helper functions
# file_exists, list_files, read_file and append_file can just be cut/paste into other
# projects
# -----------------------------------------------------------------------------
from microbit import *
from os import *

def file_exists(file_name) -> bool:
    files = listdir()
    for file in files:
        if file == file_name:
            return True
    return False


def list_files():
    files = listdir()
    print(files)

def read_file(file_name) -> str:
    with open(file_name, 'r') as file:
        lines = file.read()
        return lines

def append_file(file_name, new_line):
    if file_exists(file_name) == False:
        open(file_name, 'w')
    lines = ''
    with open(file_name, 'r') as file:
        lines = file.read()
   
    with open(file_name, 'w') as file:
        lines = lines + '\n' + new_line
        file.write(lines)

# Testing the functions above

list_files()

file_name =  'test.txt'

print(file_exists(file_name))

append_file(file_name, 'a')
append_file(file_name, 'b')
append_file(file_name, 'c')

print(file_exists(file_name))

lines = read_file(file_name)
print(lines)

append_file(file_name, 'd')
lines = read_file(file_name)
print(lines)

append_file(file_name, 'e')
lines = read_file(file_name)
print(lines)

list_files()
