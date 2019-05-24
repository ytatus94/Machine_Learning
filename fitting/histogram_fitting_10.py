import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

arr = np.random.randn(1000)

plt.figure(1)
result = plt.hist(arr) # result 包含了 entities, bins, patches
plt.xlim(min(arr), max(arr))

mean = np.mean(arr)
variance = np.var(arr)
sigma = np.sqrt(variance)

x = np.linspace(min(arr), max(arr), 100)
dx = result[1][1] - result[1][0] # result[1] 就是 bins
scale = len(arr) * dx # arr 的元素數目是固定的，當填入 histogram 時 dx 越大 bar 就越高
plt.plot(x, mlab.normpdf(x, mean, sigma) * scale) # 乘以 scale 相當於乘以面積

plt.show()