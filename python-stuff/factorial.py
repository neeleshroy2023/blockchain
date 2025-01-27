def factorial(n):
    if n == 0:
        return 0
    fact = 1
    while(n > 1):
        fact = fact * n
        n -= 1
    return fact
    
print(factorial(5))