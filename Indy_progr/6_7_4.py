s = input()
d = {}
for i in s.lower():
    if i.isalpha():
        d[i] = d.get(i, 0) + 1   
print(d)
