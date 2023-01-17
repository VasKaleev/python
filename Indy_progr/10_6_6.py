def find_keys (**kwargs):
    a = []
    for key, value in kwargs.items():    
        if isinstance(value, list):
            a.append(key)
        elif isinstance(value, tuple):
            a.append(key)
    return (sorted(a, key=str.lower))       
    #return s
#print(kwargs) # {'t': [4, 5], 'W': [5, 3], 'A': (3, 2), 'a': {2, 3}, 'b': [4]}

print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
#print(find_keys('am', 'world', 'hello', 'is'))
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