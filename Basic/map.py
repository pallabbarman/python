def multiplication(num):
    return num * 5


result = []
number = [1, 9, 7, 5, 4, 3]

for i in number:
    result.append(multiplication(i))
print(result)

# using map


def mul(element):
    return element * 5


value = [5, 4, 8, 2, 9, 3]
store = list(map(mul, value))
print(store)
