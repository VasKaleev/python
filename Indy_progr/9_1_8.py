""" from string import punctuation
def longest_word_in_file(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        a = file.read().split()
        b = []
        len_max = 0
        for i in a:
            if len_max < len(i.strip((punctuation))):
               len_max = len(i.strip((punctuation))) 
               c = i.strip((punctuation))
        print(c) 
longest_word_in_file("1.txt") """
""" from string import punctuation
def longest_word_in_file(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as f:
        a = f.read().split()
        return max([i.strip((punctuation)) for i in f.read().split()][::-1], key = len)
longest_word_in_file("1.txt") """
from string import punctuation
def longest_word_in_file(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        a = file.read().split()
        b = []
        for i in a:
            b.append(i.strip((punctuation)))
        print(b) 
        print(max([i for i in b][::-1], key = len))
        print(punctuation) 
longest_word_in_file("1.txt")



    