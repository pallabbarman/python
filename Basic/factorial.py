import math


def fact(n):
    initial = 1
    for i in range(1, n+1):
        initial *= i
    return initial


result = fact(5)
print(result)

# using built in function


n = 5
print(math.factorial(n))
