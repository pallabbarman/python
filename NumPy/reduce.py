import functools


def add(num1, num2):
    return num1+num2


list1 = [2, 1, 5, 6, 8, 7, 3, 9, 4, 5]

result = functools.reduce(add, list1)
print(result)
