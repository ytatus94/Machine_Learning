from scipy.stats import norm, rayleigh
from numpy import linspace
from pylab import plot, show, hist, figure, title

# 依照 rayleigh 分布產生數據
y = rayleigh.rvs(loc=5, scale=2, size=150)
# fitting
param = rayleigh.fit(y)
# 畫圖
x = linspace(5, 13, 100)
# fitted distribution
pdf_fitted = rayleigh.pdf(x, loc=param[0], scale=param[1])
# original distribution
pdf = rayleigh.pdf(x, loc=5, scale=2)

title('Rayleigh distribution')
plot(x, pdf_fitted, 'r-', x, pdf, 'b-')
# hist(y, normed=1, alpha=.3)
hist(y, density=1, alpha=.3)
show()