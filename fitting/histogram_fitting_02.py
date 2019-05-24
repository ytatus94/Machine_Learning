# 1. import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 2. Define the fit function
def fit_func(x, A, beta, B, mu, sigma):
	return (A * np.exp(-x / beta) + B * np.exp(-1. * (x - mu)**2 / (2 * sigma**2)))

# 3. Get the data for fitting
# 用來 fitting 的數據可以是從實驗得到的，或是模擬產生的
# 這邊用模擬產生數據

# background
data = np.random.exponential(scale=2.0, size=100000)
# signal

data2 = np.random.normal(loc=3.0, scale=0.3, size=15000) # mu=3.0 sigma=0.3
bins = np.linspace(0, 6, 61) # 0 ~ 6 之間產生 61 個點，包含 0 與 6

# 得到 signal 和 background 的 histogram
# data_entries 是每個 bin 的高度 (就是 y)
# bins 是每個 bin 的數值 (就是 x)
data_entries_1, bins_1 = np.histogram(data, bins=bins)
data_entries_2, bins_2 = np.histogram(data2, bins=bins)

# 把 signal 和 background 的 histogram 加起來
data_entries = data_entries_1 + data_entries_2

# 計算 bin 的中心值, fitting 時的 x 值用這個帶入
bins_centers = np.array([0.5 * (bins[i] + bins[i + 1]) for i in range(len(bins) - 1)])

# 4. Fit the function to the histogram
# fitting function 用名字傳入
# 把要 fit 的 x, y 值都傳入
# 初始的參數值也可以傳入
# fitting 後傳回參數列表 (popt) 和 covariance matrix (pcov)
# covariance matrix 對角線元素表示 fitted 參數的 variance
popt, pcov = curve_fit(fit_func, xdata=bins_centers, ydata=data_entries, p0=[20000, 2.0, 2000, 3.0, 0.3])

print(popt)
print(pcov)

# 5. 把 fitting 的結果和 histogram 疊圖
xspace = np.linspace(0, 6, 100000) # 產生很多點, 畫圖時比較 smooth

# 畫圖
plt.bar(bins_centers, data_entries, width=bins[1] - bins[0], color='navy', label=r'Histogram entries')
plt.plot(xspace, fit_func(xspace, *popt), color='darkorange', linewidth=2.5, label=r'Fitted function')

plt.xlim(0, 6)
plt.xlabel(r'x axis')
plt.ylabel(r'Number of entries')
plt.title(r'Exponential decay with gaussian peak')
plt.legend(loc='best')
plt.show()
plt.clf()