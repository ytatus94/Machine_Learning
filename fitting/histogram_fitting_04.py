from pylab import *
from numpy import loadtxt
from scipy.optimize import leastsq

fit_func = lambda p, x: p[0] * exp(-0.5*((x - p[1])/p[2])**2) + p[3]
err_func = lambda p, x, y: (y - fit_func(p, x))

filename = 'gaussdata.csv'
data = loadtxt(filename, skiprows=1, delimiter=',')
xdata = data[:, 0]
ydata = data[:, 1]
# xdata = np.linspace(0, 10, 101)
# ydata = np.random.normal(5, 0.8, len(xdata))
# print(xdata)
# print(ydata)

init = [1.0, 0.5, 0.5, 0.5]

out = leastsq(err_func, init, args=(xdata, ydata))
c = out[0]

print('A exp[-0.5((x-mu)/sigma)^2] + k')
print('Parent Coefficients:')
print('1.000, 0.200, 0.300, 0.625')
print('Fit Coefficients:')
print(c[0], c[1], abs(c[2]), c[3])

plot(xdata, fit_func(c, xdata), label='fit func')
plot(xdata, ydata, label='data')

title(r'$A = %.3f\ \mu = %.3f\ \sigma = %.3f\ k = %.3f $' % (c[0], c[1], abs(c[2]), c[3]))

show()