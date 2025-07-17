#Recursion is a function that calls itself. It has a limit which is 1000.
def recursion():
     print('Hello Kajol')
     recursion()                          #function er moddhe function k call korte hobe


recursion()    



def factorial(n):
    # Base case: Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5)) # Output: 120 (5 * 4 * 3 * 2 * 1)