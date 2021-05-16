import statistics as st

import numpy as np

dataset1 = [1, 2, 3, 5, 7, 8, 9, 5, 3]

# mean
mean1 = np.mean(dataset1)
print("Mean using Numpy:", mean1)

mean2 = st.mean(dataset1)
print("Mean using statistics:", mean2)

# median
median1 = np.median(dataset1)
print("Median using Numpy:", median1)

median2 = st.median(dataset1)
print("Median using statistics:", median2)
