class Buffer:
    def __init__(self):
        self.posledov=[]
    def add(self, *a):
        self.posledov.extend(a)
        while len(self.posledov)-5>=0:
            print(sum(self.posledov[0:5]))
            self.posledov=self.posledov[5:]
    def get_current_part(self):
        return self.posledov

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
