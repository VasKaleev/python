#days = (i for i in range(1, 78))
d = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
days = ((i, d[i % len(d)]) for i in range(77))
for i in enumerate(days,0):
    for j in d:
        print((next(days)))
