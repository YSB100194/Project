# Recursion --A recursive algorithm calls itself repeatedly in order to solve the problem until a certain condition 
# is fulfilled
a=int(input("Enter the number for Factorial :"))
def factorial(n):  
    # test for a base case       
    if  n == 0:  
        return 1  
    else:  
        return n*factorial(n-1)    # Do the calculation and a recursive call 
   

 
print(factorial(a))
