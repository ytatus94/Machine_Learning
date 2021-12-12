import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# Generate normaly distribution random sample
mu_true = 0
sigma_true = 0.1
s = np.random.normal(mu_true, sigma_true, 2000)

# Fit normal distribution to the data and calculate PDF
mu, sigma = stats.norm.fit(s)
points = np.linspace(stats.norm.ppf(0.01, loc=mu, scale=sigma),
                     stats.norm.ppf(0.9999, loc=mu, scale=sigma), 100)
# ppf() 是 cdf() 的反函數
# cdf() 是給定 x 求在 x 處的累計機率
# ppf() 是給定累計機率，求對應的 x 數值
pdf = stats.norm.pdf(points, loc=mu, scale=sigma)

# Display fitted PDF and the data histogram
plt.hist(s, 30, density=True)
plt.plot(points, pdf, color="r")
plt.show()

import seaborn as sns
ax = sns.distplot(s)