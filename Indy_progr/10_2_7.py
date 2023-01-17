""" def my_range_gen(*args)->int:
    for i in range(*args):
        yield i
          
for i in my_range_gen(8, 5, -1):     
   print(i)  """

from typing import Generator


def my_range_gen(*args) -> Generator[int, None, None]:
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        inc = args[2]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        inc = 1
    elif len(args) == 1:
        start = 0
        stop = args[0]
        inc = 1
    while (inc > 0 and start < stop) or (inc < 0 and start > stop):
        yield start
        start += inc


for i in my_range_gen(4, 8):
    print(i)

""" def my_range_gen(start: int, stop: int, inc: int = 1)->int:
    while (inc > 0 and start < stop) or (inc < 0 and start > stop):
        yield start
        start += inc

for i in my_range_gen(8,5,-1):     
   print(i) """
