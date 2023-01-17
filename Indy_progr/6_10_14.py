a = set(input().lower())
c = 0
for i in a:
    if 97 <= ord(i) <= 122:
        c+=1
print("YES" if c == 26 else "NO")