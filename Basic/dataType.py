# Numeric
x, y, z = 5, 5.5, 3+7J
result = type(x)  # int
result1 = type(y)  # float
result2 = type(z)  # complex
result3 = type(x > y)  # bool
print(result, result1, result2, result3)

# Sequence
a = "Tom Hanks"  # string
b = {1, 2, 3, 4, 5}  # set
c = (1, 2, 3, 4, 5)  # tuple
d = [1, 2, 3, 4, 5]  # list
result4 = type(a)
result5 = type(b)
result6 = type(c)
result7 = type(d)
print(result4, result5, result6, result7)
