s, a, b = (input() for _ in range(3))
coun=0
while coun<=1000:
    if a in s:
        s=s.replace(a,b)
        coun+=1
    else:
        print(coun)
        exit()
else:
    print('Impossible')
