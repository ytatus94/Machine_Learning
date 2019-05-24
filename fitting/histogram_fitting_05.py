import matplotlib.pyplot as plt
import scipy
import scipy.stats # import scipy 時不會包含 stats，所以還要自己 import 進來

size = 20000
x = scipy.arange(size)
# 用 beta distribution 產生 y 值
y = scipy.int_(scipy.round_(scipy.stats.beta.rvs(6, 2, size=size) * 47))
# creating the histogram
h = plt.hist(y, bins=range(48))

dist_names = ['alpha', 'beta', 'arcsine', 'weibull_min', 'weibull_max', 'rayleigh']

for dist_name in dist_names:
    dist = getattr(scipy.stats, dist_name) # 傳回 scipy.stats.dist_name 的屬性 dist_name 必須要是 string
    param = dist.fit(y)
    print(param)
    pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1]) * size # pdf 畫的是 normalized 的，所以要乘上 size 變成原本的大小
    plt.plot(pdf_fitted, label=dist_name)
    plt.xlim(0, 47)

plt.legend(loc='upper left')
plt.show()