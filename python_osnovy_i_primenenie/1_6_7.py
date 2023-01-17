d={}

def foo(s1, s2):
  global d
  a=[]
  if not d.get(s2):
    d[s2]=[]
  if s1==s2:
    return "Yes"
  a+=d[s2]
  while a!=[]:
    if a[0]!=s1:
      a+=d[a[0]]
      del a[0]
    else:
      return "Yes"
  return "No"

n=int(input())
for i in range(n):
  a=input().split()
  if len(a)>2:
      x=a[2:]
      d[a[0]]=x
  else:
    d[a[0]]=[]

n=int(input())
for i in range(n):
  s1, s2 = input().split()
  print(foo(s1, s2))