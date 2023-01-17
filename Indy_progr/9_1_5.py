#file_name = input()
import locale
import sys

#locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
#print(locale.getlocale())
def file_read(file_name):
    file = open(file_name, 'r',encoding = 'utf-8')
    print(file.read())
file_read("1.txt")



