import numpy as np

mu = 10; sigma = 2.5; # mean = 10, deviation = 2.5
L = 100000 # length of the random vector

# Random samples generated using numpy.random.normal()
samples_normal = np.random.normal(loc=mu, scale=sigma, size=(L, 1))
# generate normally distributted samples

# For plotting
import matplotlib.pyplot as plt
#%matplotlib inline
plt.style.use("ggplot")

fig, ax0 = plt.subplots(ncols=1, nrows=1) # creating plot axes
(values, bins, _) = ax0.hist(samples_normal, bins=100, density=True, label="Histogram of samples") # compute and plot histogram, return the computed values and bins

from scipy import stats
bin_centers = 0.5 * (bins[1:] + bins[: -1])
pdf = stats.norm.pdf(x=bin_centers, loc=mu, scale=sigma) # compute probability density function
ax0.plot(bin_centers, pdf, label="PDF", color="black") # plot PDF
ax0.legend() # legend entries
ax0.set_title("PDF of samples from numpy.random.normal()")

# Use Box-Muller transformation
# Generate a pair of normally distributed random numbers (Z1, Z2)
# by transforming a pair of uniformly distributed independent random samples (U1, U2)
# a = sqrt(-2 ln U1), b = 2 pi U2
# Z1 = a sin(b), Z2 = a cos(b)

# Samples generated using Box-Muller transformation
from numpy.random import uniform
U1 = np.random.uniform(low=0, high=1, size=(L, 1)) # uniformaly distributed random numbers U(0, 1)
U2 = np.random.uniform(low=0, high=1, size=(L, 1)) # uniformaly distributed random numbers U(0, 1)

a = np.sqrt(-2 * np.log(U1))
b = 2 * np.pi * U2

Z = a * np.cos(b) # Standard normal distributed numbers
samples_box_muller = Z * sigma + mu # Normal distribution with mean and sigma

# Plotting
fig, ax1 = plt.subplots(ncols=1, nrows=1) # creating plot axes
(values, bins, _) = ax1.hist(samples_box_muller, bins=100, density=True, label="Histogram of samples") # Plot histogram
bin_centers = 0.5 * (bins[1:] + bins[:-1])
pdf = stats.norm.pdf(x=bin_centers, loc=mu, scale=sigma) # compute probability density function
ax1.plot(bin_centers, pdf, label="PDF", color="black") # plot PDF
ax1.legend() # legend entries
ax1.set_title("Box-Muller transformation")

plt.show()