__author__ = 'sweety'

import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("../data/web_traffic.tsv", delimiter='\t')
print data[:10]
print data.shape
x = data[:, 0]
y = data[:, 1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 50, full = True)
print fp1
print(residuals)

def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


f1 = sp.poly1d(fp1)
print error(f1, x, y)

fx = sp.linspace(0, x[-1], 1000)

print fx
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(['d=%i'% f1.order], loc='upper left')
plt.scatter(x, y)
plt.title('web traffic over the last month')
plt.xlabel('Time')
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid(0)
plt.show()

