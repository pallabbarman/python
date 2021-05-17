import statistics as st

import scipy.stats as ss

dataset = [1, 2, 3, 6, 9, 8, 6, 5, 6, 4, 6]
mode1 = st.mode(dataset)
print("Mode using Statistics:", mode1)

mode2 = ss.mode(dataset)
print("Mode using Scipy:", mode2)
