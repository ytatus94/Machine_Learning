import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.mlab as mlab
from scipy import stats

arr = np.random.randn(100)

plt.figure(1)
# plt.hist(arr, normed=True)
plt.hist(arr, density=True)
plt.xlim((min(arr), max(arr)))

mean = np.mean(arr)
variance = np.var(arr)
sigma = np.sqrt(variance)

x = np.linspace(min(arr), max(arr), 100)

# plt.plot(x, mlab.normpdf(x, mean, sigma))
plt.plot(x, stats.norm.pdf(x, mean, sigma))
plt.show()
