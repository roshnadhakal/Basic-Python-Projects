#Recursive Method (the sum of the two preceding ones)
def fibonacci(n):
    if n <= 1:
        return [0] # first fibonacci nsequence starts with zero
    elif n == 2:
        return [0, 1] #return the first two Fibonacci numbers
    else:
        # get the Fibonacci sequence up to n-1
        fib = fibonacci(n-1)
        # Append the next Fibonacci number by summing the last two numbers in the sequence
        fib.append(fib[-1] + fib[-2])
        return fib
    
print(fibonacci(10)) 
    