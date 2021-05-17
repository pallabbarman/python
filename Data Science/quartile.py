import numpy as np

dataset = [1, 2, 6, 4, 5, 8, 6, 7, 9]
Q1 = np.percentile(dataset, 25)
print('Q1:', Q1)
Q2 = np.percentile(dataset, 50)
print('Q1:', Q2)
Q3 = np.percentile(dataset, 75)
print('Q1:', Q3)

IQR = Q3-Q1
print('IQR:', IQR)
