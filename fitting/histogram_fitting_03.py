import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# 產生數據
y = np.random.normal(1.35, 1.43, 1000) # mu=1.35, sigma=1.43, N=1000

# fit data
(mu, sigma) = norm.fit(y)

# histogram
# n, bins, patches = plt.hist(y, 60, normed=True, facecolor='green', alpha=0.75) # normed 過時了, 要用 density
n, bins, patches = plt.hist(y, 60, density=True, facecolor='green', alpha=0.75)
# n 是 histogram 每個 bin 的高度
# bins 是每個 bin 的值

# 用 fit 到的參數來畫出理論的曲線
pdf_fitted = norm.pdf(bins, mu, sigma)
plt.plot(bins, pdf_fitted, 'r--', linewidth=2)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
plt.grid(True)

plt.show()