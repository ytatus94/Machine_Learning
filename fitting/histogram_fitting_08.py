import numpy as np
from matplotlib import pyplot as plt

N = 1000
data = np.random.rand(N) # 0~1 之間產生 N 個隨機數

avg = np.mean(data)
var = np.var(data)

pdf_x = np.linspace(np.min(data), np.max(data), 1000)
pdf_y = 1.0 / np.sqrt(2 * np.pi * var) * np.exp(-0.5 * (pdf_x - avg)**2 / var) # 用 x 值帶入 gaussian function 求 y，所以這不算 fitting

plt.figure()
# plt.hist(data, 30, normed=True)
plt.hist(data, 30, density=True)
plt.plot(pdf_x, pdf_y, 'k--')
plt.legend(('Fit', 'Data'), 'best')
plt.show()
