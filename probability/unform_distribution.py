import numpy as np
import matplotlib.pyplot as plt

# continues uniform from 0 to 1

samples = np.random.uniform(0,1,10000)

plt.hist(samples, bins=50, density=True, alpha=0.6, color='skyblue')
plt.title("Continues Uniform Distribution (0 to 1)")
plt.xlabel("value")
plt.ylabel("probability density")
plt.grid(True)
plt.show()