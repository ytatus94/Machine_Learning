from scipy.stats import norm
from numpy import linspace
from pylab import plot, show, hist, figure, title

# 依照 normal distribution 產生 150 個數據點
# mean=0, standard deviation=1
sample = norm.rvs(loc=0, scale=1, size=150)

# fitting
param = norm.fit(sample)
# mu = param[0], sigma = param[1]

x = linspace(-5, 5, 100) # -5 到 5 產生 100 個點，包含 -5 和 5
# fitted distribution
pdf_fitted = norm.pdf(x, loc=param[0], scale=param[1])
# original distribution
pdf = norm.pdf(x)

title('Normal distribution')
plot(x, pdf_fitted, 'r-', x, pdf, 'b-')
# hist(sample, normed=1, alpha=.3)
hist(sample, density=1, alpha=.3)

show()