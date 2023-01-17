# put your python code here
from sys import stdin
import re
for line in stdin:
    a=re.sub(r'(\w)\1{1,}',r"\1",line, flags=0)  
    print(a, end='')