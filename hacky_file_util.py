# Imports go at the top
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


list_files()


def read_file() -> str:
    with open('test.txt', 'r') as file:
        lines = file.read()
        return lines

def append_file(new_line):
    if file_exists('test.txt') == False:
        open('test.txt', 'w')
    lines = ''
    with open('test.txt', 'r') as file:
        lines = file.read()
   
    with open('test.txt', 'w') as file:
        lines = lines + '\n' + new_line
        file.write(lines)

print(file_exists('test.txt'))

append_file('a')
append_file('b')
append_file('c')

print(file_exists('test.txt'))

lines = read_file()
print(lines)

append_file('d')
lines = read_file()
print(lines)

append_file('e')
lines = read_file()
print(lines)

list_files()
