x = list(input('Введите имя: '))
print(x)
spis = ['a','A','а','А']
#if 'a' in x or 'A' in x or 'а' in x or 'А' in x: # здесь буквы не повторяются, а написаны на En/Rus
for i in x:
        if i in spis:
            print('В имени есть буква "А".') 
            break
        else: print('В имени нет буквы "А".')
