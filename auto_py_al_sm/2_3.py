""" i=1 # задаём начальное значение i 
while i<=100: # проверка. пока значение i меньше или равно 100   
    print('i =', i)  
    i=i+1 # стандартный счётчик увеличивающий значение i """

a=0
for i in '3232453232455456': # делаем цикл по строке (а не числу!)
    if i == '3':
        print(i)
        a=a+1 # увеличиваем счетчик троек
        print('Число троек в строке =' ,a) 





