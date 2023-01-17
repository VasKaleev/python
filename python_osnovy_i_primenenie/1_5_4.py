aa=[]
while True:
    try:
        line = input()
    except:
        break
    a=line.rfind("yz")
    b=line.find("ab")
    c="no" in line
    if a!=-1 or b!=-1 or c!=False:
        aa.append(line)
print(*aa)

"""  
result = []
while True:
    try:
        line = input()
    except:
        break
    if line.startswith('ab') or line.endswith('yz') or 'no' in line:
        result.append(line)
print(*result, sep='\n')
"""