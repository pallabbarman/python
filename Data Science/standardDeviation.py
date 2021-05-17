import numpy as np

population = np.random.randn(30)
print("Population", population)

sample = np.random.choice(population, 15)
print("\nSample", sample)

result_population = np.std(population)
result_sample = np.std(sample)
print("\nStandard deviation for population:", result_population)
print("\nStandard deviation for sample:", result_sample)
