
# 0, 1, 1, 2, 3, 5, 8, 13

def fib(n):
    if n<1:
        print('Please, Enter 1 or Greater NUmber!')
    else:
        a = 0
        b = 1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a+b
                a = b
                b = c
                print(c)

fib(10)