x = {1, 2, 3, 4, 5}
x.add(6)  # add single item
x.update([7, 8, 9])  # add multiple item
x.remove(9)
x.discard(10)  # if item found then remove otherwise stay remain
print(x)

a = [1, 2, 3, 4, 5, 6, 1, 3, 6, 8]
result = set(a)
print(result)
