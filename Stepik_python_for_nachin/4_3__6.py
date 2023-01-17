import click
one = [1,3,5,7,8,10,12]
two = [4,6,9,11]
three = [2]
month = int(input("Введите номер месяца:"))
if month in one:
    print(31)
elif month in two:
    print(30)
elif month in three:
    print(28)   


click.pause('Чтобы продолжить, нажмите Enter.') 
click.pause("--------------------------------")