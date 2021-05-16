import numpy as np

m1 = ([1, 2, 3],
      [4, 5, 6],
      [7, 8, 9])

m2 = ([3, 2, 1],
      [6, 5, 4],
      [9, 8, 7])

result = np.add(m1, m2)
result1 = np.subtract(m1, m2)
result2 = np.dot(m1, m2)  # multiply
result3 = np.multiply(m1, m2)  # index multiplication
print("Add: \n", result)
print("Sub: \n", result1)
print("Mul: \n", result2)
print("\n", result3)
