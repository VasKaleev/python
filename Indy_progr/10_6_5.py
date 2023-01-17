def count_strings(*args):
    s = 0
    sum_string = ''
    for i in args:
        if isinstance(i, str):
            s += 1
            sum_string = sum_string + i
    return s
print(count_strings(1, 2, 'hello', True, 't'))
print(count_strings('am', 'world', 'hello', 'is'))
#count_strings()  
#count_strings(True, False)  

""" args = ['am', 'world', 'hello', 'is']
s = 0
sum_string = ''
for i in args:
        if isinstance(i, str):
            s += 1
            sum_string = sum_string + i
print(s,sum_string) """