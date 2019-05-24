from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# 產生隨機的事件
# np.random.rand() 產生 0~1 之間的隨機數
# np.random.normal(mu, sigma, N)
y = 50 * np.random.rand() * np.random.normal(10, 10, 100) + 20

# plot normed histogram
# plt.hist(y, normed=True) # normed 是舊的方式，新的要改用 density
plt.hist(y, density=True)

# 找 xticks 最大跟最小值, 這樣才知道分布的範圍
xt = plt.xticks()[0]
xmin, xmax = min(xt), max(xt)
lnspc = np.linspace(xmin, xmax, len(y)) # np.linspace(起點, 終點, 包含起點到終點共幾個點)

# normal distribution
m, s = stats.norm.fit(y) # mean, std
pdf_g = stats.norm.pdf(lnspc, m, s) # 用 fit 到的參數求出的函數值，lnspc 就是 x 的值組成的 list
plt.plot(lnspc, pdf_g, label='Norm') # 畫出 fit 到的曲線

# gamma distribution
ag, bg, cg = stats.gamma.fit(y)
pdf_gamma = stats.gamma.pdf(lnspc, ag, bg, cg)
plt.plot(lnspc, pdf_gamma, label='Gamma')

# beta distribution
ab, bb, cb, db = stats.beta.fit(y)
pdf_beta = stats.beta.pdf(lnspc, ab, bb, cb, db)
plt.plot(lnspc, pdf_beta, label='Beta')

plt.legend()
plt.show()