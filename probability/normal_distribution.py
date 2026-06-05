import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# general value 

x = np.linspace(-4,4,10000)
mean = 0
std_dev = 1

# get the probability density 

y = norm.pdf (x, loc=mean,scale=std_dev)

# plot 

plt.plot(x, y)
plt.title("standard normal distribution(mu = 0, sigma = 1)")
plt.xlabel("x")
plt.ylabel(" probability density")
plt.grid(True)
plt.show()