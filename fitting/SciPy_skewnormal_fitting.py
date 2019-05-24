# https://stackoverflow.com/questions/50140371/scipy-skewnormal-fitting

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# choose some parameters
a, loc, scale = 5.3, -0.1, 2.2

# draw a sample
data = stats.skewnorm(a, loc, scale).rvs(1000) # 產生 1000 個 skew normal 的隨機數

# estimate parameters from sample
ae, loce, scalee = stats.skewnorm.fit(data)
print(ae, loce, scalee)

# plot the pdf
plt.figure()
plt.hist(data, bins=100, density=True, alpha=0.6, color='g')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = stats.skewnorm.pdf(x, ae, loce, scalee)
plt.plot(x, y, 'k', linewidth=2)
plt.show()
