s=input()
a=[]
for i in range(len(s)):
    if s[i]=="h":
        a.append(i)
print(s[:min(a)]+s[max(a)+1:])