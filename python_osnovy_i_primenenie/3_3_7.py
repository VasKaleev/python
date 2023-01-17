import requests, re
a=input()
res = requests.get(a)
s=str(res.text)
it=[]
pattern = r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)'
it = re.findall(pattern,s)
mn=[]
for i in sorted(it):
    if i not in mn:
        mn.append(i)  
print(*mn,sep="\n")



    