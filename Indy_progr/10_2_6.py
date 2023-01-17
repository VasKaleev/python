def gen_fibonacci_numbers(n):
    a, b = 1, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(list(gen_fibonacci_numbers(10)))  
   
