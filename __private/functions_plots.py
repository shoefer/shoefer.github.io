import numpy as np
import matplotlib.pylab as plt

t = 10000*np.array([40, 50, 60, 80, 100])
x = 0.00013*t + 70

plt.plot(t, x, lw=5.0, color="b", alpha=0.5)
plt.scatter(t, x, s=100, color="b", alpha=0.8)
plt.xlabel("annual revenue")
plt.ylabel("stock price")

plt.figure()
x2 = [ 23, 134, 686, 240, 35]
plt.plot(t, x2, lw=5.0, color="b", alpha=0.5)
plt.scatter(t, x2, s=100, color="b", alpha=0.8)
plt.xlabel("annual revenue")
plt.ylabel("stock price")

plt.show()