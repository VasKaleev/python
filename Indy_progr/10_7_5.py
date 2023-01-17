s = input().lower().split()
a = []
for i in s:
    if len(i) >= 5:
        if i[-5:] == 'ought':
            a.append('a')
            print(i)
        else:
            a.append('')    
print(any(a))
