number = [1, 5, 6, 7, 4, 6, 9, 8, 1, 2, 3, 4, 8, 7]

result = list(filter((lambda n: n % 2), number))
print('Odd numbers are: ', result)
