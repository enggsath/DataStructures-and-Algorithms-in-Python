#Fibonacci sequence using recursion

def fibonacci(n):
    if(n<=1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)

#without iteration
'''
def fibonacci(n):
    fib=[0,1]
    for i in range(2,n+1):
        fib.append(fib[i-2]+fib[i-1])
    return fib[n]
'''
for i in range(0,20):
    print(f'fibonacci {i+1} term value:{fibonacci(i)}')
    


