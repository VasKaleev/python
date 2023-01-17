nums = sorted([int(i) for i in  input().split(',')], reverse=True)
m = nums
#print(m)
a,b,c = nums[:3]
print(a*b*c)