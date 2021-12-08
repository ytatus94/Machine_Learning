from scipy.integrate import quad

import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

# Normal distribution
x_min = 0.0
x_max = 16.0

mean = 8.0
std = 3.0

x = np.linspace(x_min, x_max, 100)
y = scipy.stats.norm.pdf(x, mean, std)

plt.plot(x, y, color="black")

# Integration between x1 and x2

def normal_distribution_function(x):
	value = scipy.stats.norm.pdf(x, mean, std)
	return value

x1 = mean + std
x2 = mean + 2.0 * std

res, err = quad(normal_distribution_function, x1, x2)

print("Normal distribution (mean, std):", mean, std)
print("Integration between {} and {} --->".format(x1, x2), res)

# Plot integration surface

ptx = np.linspace(x1, x2, 10)
pty = scipy.stats.norm.pdf(ptx, mean, std)

plt.fill_between(ptx, pty, color="#0b559f", alpha=1.0)

plt.grid()

plt.xlim(x_min, x_max)
plt.ylim(0, 0.25)

plt.title("How to integrate a normal distribution in python?", fontsize=10)

plt.xlabel("x")
plt.ylabel("Normal Distribution")

plt.savefig("integrate_normal_distribution.png")
plt.show()