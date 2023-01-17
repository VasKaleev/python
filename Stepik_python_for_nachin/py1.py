""" n=int(input())
max1=0
max2=0
for i in range(1,n+1):
    num=int(input())
    if num>max1:
        max2=max1
        max1=num
    elif num>max2:
        max2=num    
print(max1)
print(max2) """

n=int(input())
a = []  #Сождаем список введенных значений a
for i in range(1,n+1):
    num=int(input())
    a.append(num) #добавляем в список a
#print(a)
a = sorted(a) #сортируем список a
print(max(a)) #находим макксимальное значение в списке a
a.remove(max(a)) #удаляем это максимальное значение из списка a
print(max(a)) #находим максимальное в оставшемся списке

""" n = int(input())
if n >= 2:
    print(n, 'Первое число')
#s = int()

for i in range(1, n+1):
    k = int(max(input()))
print(k, '1-е Наибольшее число из последовательности')
print() """

# print(max(s))
#print(i, '2 -е Наибольшее число из последовательности')
