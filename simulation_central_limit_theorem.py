import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 1000  # Sample size
samples = 100000  # Number of samples

# Draw samples from a uniform distribution
sample_means = [np.mean(np.random.uniform(0, 1, n)) for _ in range(samples)]

# Plot the histogram of the sample means
plt.hist(sample_means, bins=1000, density=True)
plt.title("Distribution of Sample Means (n=100) - Central Limit Theorem")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()
