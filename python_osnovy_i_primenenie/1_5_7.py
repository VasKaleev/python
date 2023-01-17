s=input()
count=0
for i in range(len(s)):
    if s[i]=='f':
        count+=1
        if count==2:
            print(i)
if count==1:
    print("-1")
elif count==0:
    print("-2")