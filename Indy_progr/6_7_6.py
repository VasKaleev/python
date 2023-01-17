""" s1 = list(input())
s2 = list(input())
if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")   """  

s1 = input()
s2 = input()
d1 = {}
d2 = {}
for i in s1:
    d1[i] = d1.get(i, 0) + 1 
for i in s2:
    d2[i] = d2.get(i, 0) + 1  
if d1 == d2:
    print("YES")
else:
    print("NO")

