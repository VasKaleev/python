s = input().lower().split()
a = []
for i in s:
    if 'a' in i:
        a.append('a')
    else:
        a.append('')    
print(all(a))
