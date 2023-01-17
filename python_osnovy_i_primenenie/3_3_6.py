import requests, re
a=input()
b=input()
#regex = (r'<a.+?href="([^"]+).+?a>')
#regex = r'https.+?html'
regex = r'https.*html'
resa = requests.get(a)
s=str(resa.text)
l = re.findall(regex, s)
x="No"
l1=[]
for i in l:
    if b in re.findall(regex, requests.get(i).text):
       x='Yes'
print(x) 

""" import requests
import re
a, b = input(), input()
pattern = r'https.+?html'
result = 'No'
for url in re.findall(pattern, requests.get(a).text):
    if b in re.findall(pattern, requests.get(url).text):
        result = 'Yes'
        break
print(result) """
    