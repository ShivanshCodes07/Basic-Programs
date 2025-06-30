import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate random data from a normal distribution
mu, sigma = 0, 1  # Mean = 0, Standard deviation = 1
data = np.random.normal(mu, sigma, 1000)

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='b', label="Histogram")

# Plot the actual Gaussian curve
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2, label="Gaussian Curve")

plt.title("Gaussian (Normal) Distribution")
plt.xlabel("X values")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
