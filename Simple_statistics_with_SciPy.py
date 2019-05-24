'''
Scipy 是基於 Numpy 的，而且是使用 Numpy arrays 和 data types 來運算
Scipy 把 Numpy package 中所有的函數和一些 sub-packages 中的函數都 import 進去了
Scipy 可以用 info 函數來查詢 Scipy 中的函數，scipy.info(scipy.stats)  
'''
import scipy as sp
import numpy as np

import matplotlib as mpl
from matplotlib import pyplot as plt

#
# 1. Descriptive statistics
#

# 依照 Gaussian 分佈產生 100 個隨機數
s = sp.randn(100) # 等同於 np.random.rand()
print(s)
print(len(s))
# statistics
print('Mean: {0:8.6f}'.format(s.mean())) # 也可以用 sp.mean(s) 的方式
print('Mean: {0:8.6f}'.format(sp.mean(s)))

print('Min: {0:8.6f}'.format(s.min()))
print('Max: {0:8.6f}'.format(s.max()))

'''
計算 variance 時分母室使用母體的數目 N 
scipy.var(s, ddof=1) 用 ddof 參數使分母變成樣本數目 N - ddof
預設 ddof=0
'''
print('Variance: {0:8.6f}'.format(s.var())) # 也可以用 sp.var(s) 的方式
print('Variance: {0:8.6f}'.format(sp.var(s)))

print('Variance with N in denominator = {0:8.6f}'.format(sp.var(s)))
print('Variance with N - 1 in demoninator = {0:8.6f}'.format(sp.var(s, ddof=1)))

print('Std. deviation: {0:8.6f}'.format(s.std())) # 也可以用 sp.std(s) 的方式
print('Std. deviation: {0:8.6f}'.format(sp.std(s)))

print('Median: {0:8.6f}'.format(sp.median(s)))

# scipy.stat 的 describe() 可以列出統計值
from scipy import stats

n, min_max, mean, var, skew, kurt = stats.describe(s)
print('Number of elements: {0:d}'.format(n))
print('Minimum: {0:8.6f}, Maximum: {1:8.6f}'.format(min_max[0], min_max[1]))
print('Mean: {0:8.6f}'.format(mean))
print('Variance: {0:8.6f}'.format(var)) # 這裡是用 N-1 當分母來算出來的值
print('Skew: {0:8.6f}'.format(skew))
print('Kurtosis: {0:8.6f}'.format(kurt))

#
# 2. Probability distributions
#

'''
機率分佈函數放在 scipy.stats 裡面
scipy 有 81 個連續和 10 個不連續的機率分佈函數
也有許多統計函數
函數的參數寫在 docstring 裡面方便查詢
例如: 可以用 help(stats.poisson) 或用 scipy.info(stats.poisson) 來查詢
在 iPython 中可以用 stats.poisson? 來查詢
'''
# 產生一個 mean=3.5, std=2.0 的 Gaussian 分佈物件
n = stats.norm(loc=3.5, scale=2.0) # 先定義物件
print(n.rvs()) # 再依照剛才定義的高斯分佈產生隨機變數
print(stats.norm.rvs(loc=3.5, scale=2.0)) # 直接產生高斯分佈的隨機變數

'''
2.1 PDF & PMF

pdf: probability density function, 連續
pmf: probability mass function, 不連續
例如 norm, chi2, t, uniform 是連續的機率分佈函數
binom, poisson 是不連續的機率分佈函數
'''
# PDf of Gaussian of mean=0.0 and std. deviation=1.0 at 0.
print(stats.norm.pdf(0, loc=0.0, scale=1.0)) # 計算 x=0 時 N(0, 1) 是多少
# 也可以傳入 list 來計算
print(stats.norm.pdf([-0.1, 0.0, 0.1], loc=0.0, scale=1.0))

# PMF of binomial distribution with p=0.5, trials n=10
tries = range(11) # 0 to 10
print(stats.binom.pmf(tries, 10, 0.5)) # 第一個參數就是 N 次試驗中幾次成功
# 畫圖
import matplotlib.pyplot as plt
def binom_pmf(n=4, p=0.5):
    # There are n+1 possible number of 'successes': 0 to n.
    x = range(n + 1)
    y = stats.binom.pmf(x, n, p)
    plt.plot(x, y, 'o', color='black')

    # Format x-axis and y-axis
    plt.axis([-(max(x) - min(x)) * 0.05, max(x) * 1.05, -0.01, max(y) * 1.10])
    plt.xticks(x)
    plt.title('Binomial distribution PMF for tries = {0} & p = {1}'.format(n, p))
    plt.xlabel('Variate')
    plt.ylabel('Probability')

    # plt.draw() # 只畫圖，畫完就把圖關掉，視窗會消失
    plt.show() # 畫完圖後視窗還在，要自己關掉

binom_pmf(10, 0.5)

'''
2.2 CDF

CDF: Cumulative density function
變量 x 小於等於某個給定值的機率
'''
print(stats.norm.cdf(0.0, loc=0.0, scale=1.0)) # 變量 x 小於等於 0 的機率
# 畫圖
def norm_cdf(mean=0.0, std=1.0):
    # 50 numbers between -3 \sigma and 3 \sigma
    x = sp.linspace(-3 * std, 3 * std, 50)
    # CDF at these values
    y = stats.norm.cdf(x, loc=mean, scale=std)

    plt.plot(x, y, color='black')
    plt.xlabel('Variate')
    plt.ylabel('Cumulative Probability')
    plt.title('CDF for Gaussian of mean = {0} & std. deviation = {1}'.format(mean, std))

    # plt.draw()
    plt.show()

norm_cdf(0.0, 1.0)

'''
2.3 PPF

PPF: Percent point function (inverse cumulative function)
PPF 就是 inverse cumulative function
如果說 y = f(x) 是 CDF，給定 x 求出 y
那 PPF 就是給 y 反推求出 x
'''
print(stats.norm.ppf(0.5, loc=0.0, scale=1.0))
# 畫圖
def norm_ppf(mean=0.0, std=1.0):
    # 100 numbers between 0 and 1.0 i.e., probabilities
    x = sp.linspace(0, 1.0, 100) # x 是 CDF 的值，因為是機率所以介於 0 ~ 1 之間
    # PPF at these values
    y = stats.norm.ppf(x, loc=mean, scale=std)

    plt.plot(x, y, color='black')
    plt.xlabel('Cumulative Probability')
    plt.ylabel('Variate')
    plt.title('PPF for Gaussian of mean = {0} & std. deviation = {1}'.format(mean, std))

    # plt.draw()
    plt.show()

norm_ppf(0.0, 1.0)

'''
2.4 SF
SF: Survival function
變量 x 比給定值大的機率
SF = 1 - CDF
'''
print(stats.norm.sf(0.0, loc=0.0, scale=1.0))
# 畫圖
def norm_sf(mean=0.5, std=1.0):
    # 50 numbers between -3\sigma and 3\sigma
    x = sp.linspace(-3 * std, 3 * std, 50)
    # SF at these values
    y = stats.norm.sf(x, loc=mean, scale=std)

    plt.plot(x, y, color='black')
    plt.xlabel('Variate')
    plt.ylabel('Probability')
    plt.title('SF for Gaussian of mean = {0} & std. deviation = {1}'.format(mean, std))

    # plt.draw()
    plt.show()

norm_sf(0.0, 1.0)

'''
2.5 ISF
ISF: Inverse survival function
給定 survival function 的值來逆推回 variate 的值
'''
print(stats.norm.isf(0.5, loc=0.0, scale=1.0))
# 畫圖
def norm_isf(mean=0.0, std=1.0):
    # 100 numbers between 0 and 1.0
    x = sp.linspace(0, 1.0, 100) # x 是 SF 的值，因為是機率所以介於 0 ~ 1 之間
    # ISF at these values
    y = stats.norm.isf(x, loc=mean, scale=std)

    plt.plot(x, y, color='black')
    plt.xlabel('Probability')
    plt.ylabel('Variate')
    plt.title('ISF for Gaussian of mean = {0} & std. deviation = {1}'.format(mean, std))

    # plt.draw()
    plt.show()

norm_isf(0.0, 1.0)

'''
2.6 Random variates
可以用 rvs 依照某個分部來產生隨機變數
'''
# 100 random values from a normal distribution with mu = 0.0, sigma=1.0
print(stats.norm.rvs(loc=0.0, scale=1.0, size=100))
# 100 random values from a Poisson distribution with mu = 1.0
print(stats.poisson.rvs(1.0, size=100))
# 畫圖
# 每兩秒為一個時間間隔，產生 100 個依照 Poisson 分部的隨機數，mu = 1.69
# 也畫出 Poisson 分部的 Probability Mass Function (PMF), mu = 1.69
# Poisson 分布是不連續的，點跟點之間的線只是用平滑曲線連接起來
# Poisson distribution
# P(k events in interval) = \frac{\lambda^{k}e^{-\lambda}}{k!}
# 在固定時間間隔內發生了 k 次，\lambda 是在時間間隔內發生的平均次數，又可以叫做 event rate
import scipy as sp
from scipy import stats
from scipy import interpolate
from matplotlib import pyplot as plt

def simulate_poisson():
    # Mean is 1.69
    mu = 1.69
    sigma = sp.sqrt(mu) # Poisson 的標準差 \sigma_{k} = \sqrt(\lambda)
    mu_plus_sigma = mu + sigma

    # Draw random samples from the Poisson distribution, to simulate
    # the observed events per 2 second interval
    counts = stats.poisson.rvs(mu, size=100)

    # Bins for the histogram: only the last bin is closed on both
    # sides. We need one more bin than the maximum value of count, so
    # that the maximum values goes in its own bin instead of getting
    # added to the previous bin.
    # [0, 1), [1, 2), ...[max(counts), max(counts)+1]
    bins = range(0, max(counts) + 2)

    # Plot histogram
    plt.hist(counts, bins=bins, align='left', histtype='step', color='black')

    # Create Poisson distribution for given mu.
    x = range(0, 10)
    prob = stats.poisson.pmf(x, mu) * 100 # 產生 x 所對應的 Poisson 分佈的值
                                          # 因為產生了 100 個 Poisson 分佈的數值，所以這邊也要乘上 100
    # Plot the PMF
    plt.plot(x, prob, 'o', color='black')

    # Draw a smooth curve through the PMF
    l = sp.linspace(0, 11, 100) # x 值
    s = interpolate.spline(x, prob, l) # 用內插法來找出 y 值
    plt.plot(l, s, color='black')

    plt.xlabel('Number of counts per 2 seconds')
    plt.ylabel('Number of occurrences (Poisson)')

    # Interpolated probability at x = \mu + \sigma; for marking \sigma in the graph.
    xx = sp.searchsorted(l, mu_plus_sigma) - 1 # 找出 mu_plus_sigma 在 l 中會位在第幾個元素
    v = ((s[xx + 1] - s[xx]) / (l[xx + 1] - l[xx])) * (mu_plus_sigma - l[xx])
    v += s[xx]

    ax = plt.gca() # gca: get current axes
    # Reset axis range and ticks.
    ax.axis([-0.5, 10, 0, 40])
    ax.set_xticks(range(1, 10), minor=True)
    ax.set_yticks(range(0, 41, 8))
    ax.set_yticks(range(4, 41, 8), minor=True)

    # Draw arrow and then place an opaque box with \mu in it.
    # 在 (mu, 29) (mu, 13) 兩個座標畫一個箭頭
    ax.annotate('', xy=(mu, 29), xycoords='data', xytext=(mu, 13),
                textcoords='data', arrowprops=dict(arrowstyle='->',
                                                   connectionstyle='arc3'))
    bbox_props = dict(boxstyle='round', fc='w', ec='w')
    ax.text(mu, 21, r'$\mu$', va='center', ha='center',
            size=15, bbox=bbox_props)

    # Draw arrow and then place an opaque box with \sigma in it.
    ax.annotate('', xy=(mu, v), xytext=(mu_plus_sigma, v),
                arrowprops=dict(arrowstyle='<->', connectionstyle='arc3'))
    bbox_props = dict(boxstyle='round', fc='w', ec='w')
    ax.text(mu + (sigma / 2.0), v, r'$\sigma$', va='center', ha='center',
                  size=15, bbox=bbox_props)

    # Refresh plot and asve figure
    # plt.draw()
    # plt.savefig('simulate_poisson.png')
    plt.show()

simulate_poisson()