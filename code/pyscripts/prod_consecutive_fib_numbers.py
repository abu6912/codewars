prod = 800

def fib():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def SubFib(num):
    count = 0
    for fib_num in  fib():
        if num == count:
            return fib_num
            break
        count += 1

def productFib(prod):
    fib_list = 0
    num = 1
    while SubFib(num) * SubFib(num+1) <= prod:
        fib_list = (SubFib(num) * SubFib(num+1))
        num += 1
    if fib_list == prod:
        return [SubFib(num-1), SubFib(num), True]
    else:
        return [SubFib(num), SubFib(num+1), False]

if __name__ == '__main__':
    print productFib(prod)


