import numpy as np

population = np.random.randn(30)
print("Population", population)

sample = np.random.choice(population, 20)
print("\nSample", sample)

# variance
result_population = np.var(population)
result_sample = np.var(sample)
print("Result for population:", result_population)
print("Result for sample:", result_sample)
