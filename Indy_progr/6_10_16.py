str = input()[1:-1]
d = set() 
for i in str:
    if i.isalpha():
        d.add(i)
print(len(d))