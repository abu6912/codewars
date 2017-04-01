prod = 800

from math import sqrt, floor

def fib(n):
    return int(floor(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))

def productFib(prod):
    fib_list = 0
    num = 1
    while fib(num) * fib(num+1) <= prod:
        fib_list = (fib(num) * fib(num+1))
        num += 1
    if fib_list == prod:
        return [fib(num-1), fib(num), True]
    else:
        return [fib(num), fib(num+1), False]
    
    
if __name__ == '__main__':
    print(productFib(prod))

for num in range(50, 81):
    print(fib(num-2), ' + ', fib(num-1), ' = ', fib(num) == fib(num-1)+fib(num-2))
    
190392490709135  +  308061521170129  =  False
498454011879265
498454011879264
print(190392490709135  +  308061521170129  )