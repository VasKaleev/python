#print(42/(4+2*(-2)))
#print(7/3)
#print(2018**18)
#print(2018**2018)
a, b = map(int, input().split())
for x in '+', '-', '*', '/', '**':
    print(eval('a' + x + 'b'))
