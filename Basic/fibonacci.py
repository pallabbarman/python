def fibonacci(n):
    a = 0
    b = 1
    for i in range(2, n):
        c = a+b
        a = b
        b = c
        print(c)


fibonacci(10)
