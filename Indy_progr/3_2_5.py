a = int(input())
b = int(input())
minimum = maximum = 0
minimum = a if a < b else b
maximum = a if a > b else b
print(minimum,maximum)