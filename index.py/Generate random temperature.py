import numpy as np
import matplotlib.pyplot as plt

# Generate random temperature data
temperatures = np.random.normal(loc=30, scale=5, size=100)

# Plot Histogram
plt.hist(temperatures, bins=10)

plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

plt.show()