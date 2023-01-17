s=input()
a=[]
for i in s:
    if i.isdigit():
        a.append(i)
print(*a,sep="")