def fib(n):
  if n <= 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)


a=int(input("Enter number for Fibonacci series :")) # Take input from User
for i in range(a):
  print(fib(i)) 


'''Other Techniques'''

#1. Using a For Loop -- loop method is the simplest to code but becomes slow for significant inputs
a, b = 0, 1

n = 10

for i in range(n):

   print(a)

   a, b = b, a + b

#2. Fibonacci Series Using a While Loop
a, b = 0, 1  

n = 10

while b < n:

    print(b)

    a, b = b, a+b

#3. Backtracking Fibonacci Generation
def fib(n, a=0, b=1):

    if n == 0: 

        return a

    return fib(n-1, b, a+b)

print(fib(5))

#4. Using Recursion --Same as solution -- elegant code but has redundant function calls.
def fib(n):

   if n <= 1:

       return n

   else:

       return fib(n-1) + fib(n-2)

print(fib(7))

#5. Using Dynamic Programming --Dynamic programming improves recursion by storing results.
memo = {0:0, 1:1} 

def fib_dynamic(n):

    if n in memo:

        return memo[n]

    memo[n] = fib_dynamic(n-1) + fib_dynamic(n-2)   

    return memo[n]

print(fib_dynamic(6))

#6. Using Caching --Caching further boosts efficiency by reusing prior computation.
from functools import lru_cache

@lru_cache(maxsize=1000)

def fib(n):

    if n == 0:

        return 0  

    elif n == 1:

        return 1

    else:

        return fib(n-1) + fib(n-2)

print(fib(5))