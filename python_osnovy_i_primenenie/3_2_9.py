import re,sys
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"z.{3}z", line, flags=0):
        print(line, end='\n')