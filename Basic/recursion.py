'''
import sys

print("Limit", sys.getrecursionlimit())
sys.setrecursionlimit(1500)

count = 0


def function():
    global count
    count += 1
    print("Count", count)
    function()


function()
'''


def func(x):
    if x == 0:
        return 1
    return x * func(x-1)


result = func(6)
print("Result:", result)
