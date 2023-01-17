import datetime
a=input().split(" ")
b=int(input())
c = datetime.datetime(int(a[0]),int(a[1]),int(a[2]))+ datetime.timedelta(days=b)
#print(c)
print(c.year, c.month, c.day)
