year = int(input())
for i in range(year, 9999):
    if len(set(str(i + 1)))==4:
        print(i+1)
        break

