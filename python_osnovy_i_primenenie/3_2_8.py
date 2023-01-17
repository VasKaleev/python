""" import re,sys
str = sys.stdin.read()
s=re.findall(r"cat.*cat", str)
print(*s,sep="\n") """

import re,sys
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\b(cat)+\b", line, flags=0):
        print(line, end='\n')
