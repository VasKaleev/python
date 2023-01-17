n = int(input())
c = []
a = n
while a <= n**2:
    if a % 2 != 0:
       c.append(a)
    a += 1
print(tuple(c))
