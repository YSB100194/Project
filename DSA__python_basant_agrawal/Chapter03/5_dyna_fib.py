#dynamic fibonacci 
'''re-use of the already computed values
This is called the memoization technique, wherein 
there is no recomputation of overlapping calls to functions when breaking a problem down into 
its sub-problems.'''
def dyna_fib(n): 
    if n == 0: 
        return 0 
    if n == 1: 
        return 1   
    if lookup[n] is not None: 
        return lookup[n] 

    lookup[n] = dyna_fib(n-1) + dyna_fib(n-2) 
    return lookup[n] 

 
lookup = [None]*(1000) 

a=int(input("Enter number for Fibonacci series :")) # Take input from User
for i in range(a):  
    print(dyna_fib(i)) 
