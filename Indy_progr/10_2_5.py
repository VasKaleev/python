def gen_squares(N): 
   for i in range(1,N+1): 
       yield i ** 2     

for i in gen_squares(3):     
   print(i)
   
