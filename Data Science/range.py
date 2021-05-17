import numpy as np

n = np.random.randint(5, 30, 20)
print(n)

result = np.max(n) - np.min(n)
print("Result is:", result)
