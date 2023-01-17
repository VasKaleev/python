s = input()
a=[]
b= ('a', 'e', 'i', 'o', 'u', 'y')
for i in s: 
    if i.lower() in b:
        a.append(i.upper())
    else:
        a.append(i.lower())    
print(*a,sep="") 

#s.translate({ord('a'):'A', ord('e'):'E', ord('i'):'I'})
"""
s.translate({ord('a'): ord('A'), ord('e'): ord('E')})
s.translate({ord('o'): ord('O'), ord('u'): ord('U'), ord('y'):ord('Y')})
print(s)
"""
""" s = input()
a=[]
for i in s: 
    if i.lower()=="a":
        i=i.replace("a","A")
        a.append(i)
    elif i.lower()=="e":
        i=i.replace("e","E")
        a.append(i)
    elif i.lower()=="i":
        i=i.replace("i","I")
        a.append(i)   
    elif i.lower()=="o":
        i=i.replace("o","O")
        a.append(i)
    elif i.lower()=="u":
        i=i.replace("u","U")
        a.append(i)
    elif i.lower()=="y":
        i=i.replace("y","Y")
        a.append(i)
    else:
        a.append(i.lower())   
print(*a,sep="")  """


