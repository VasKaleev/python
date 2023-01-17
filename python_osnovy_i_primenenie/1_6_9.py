import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(Loggable, list):
    def append(self, arg):
        super(LoggableList, self).append(arg)
        self.log(arg)

a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)