import numpy as np
import matplotlib.pylab as plt

t = 10000*np.array([40, 50, 60, 80, 100])
f = lambda t: 0.00013*t + 70
x = f(t)

plt.plot(t, x, lw=5.0, color="b", alpha=0.5)
plt.scatter(t, x, s=100, color="b", alpha=0.8)
plt.xlabel("annual revenue")
plt.ylabel("stock price")
xlim, ylim = plt.xlim(), plt.ylim()

# fit polynomial of high deg to data
t_evil = np.hstack([t, 10000*np.array([45, 55, 70, 90])])
x_evil = np.hstack([x, [ f(t_evil[len(t)+i]) + [1,-1][i % 2] * 5 for i in range(4) ]])
p = np.polyfit(t_evil, x_evil, x_evil.shape[0])
x5 = np.poly1d(p)
T = np.arange(40, 101, 0.1)*10000

plt.figure()
plt.plot(T, x5(T), lw=5.0, color="r", alpha=0.5)
plt.plot(t, x, lw=2.0, ls="--", color="b", alpha=0.5)
plt.scatter(t, x, s=100, color="b", alpha=0.8)
plt.xlabel("annual revenue")
plt.ylabel("stock price")
plt.xlim(xlim)
plt.ylim(ylim)

# fit polynomial of high deg to data
x_evil2 = np.hstack([x, [ f(t_evil[len(t)+i]) + [1,-1][(i+1) % 2] * 5 for i in range(4) ]])
p2 = np.polyfit(t_evil, x_evil2, x_evil.shape[0])
x52 = np.poly1d(p2)

# plt.figure()
# x2 = [ 23, 134, 686, 240, 35]
# plt.plot(t, x2, lw=5.0, color="b", alpha=0.5)
# plt.scatter(t, x2, s=100, color="b", alpha=0.8)
# plt.xlabel("annual revenue")
# plt.ylabel("stock price")

#############

n = 10

Xrot = np.zeros( (n+1, 2) )
Xrot[1,:] = [0.909, 1.0]
for i in range(2, n+1):
  Xrot[i,:] = Xrot[1,:] + np.random.randn(2)*0.1
Xrot = np.clip(Xrot, 0, 1)

Yrot = np.zeros( (n+1, 2) )
Yrot[1,:] = [0.109, 0.1]
for i in range(2, n+1):
  Yrot[i,:] = Yrot[1,:] + np.random.randn(2)*0.1
Yrot = np.clip(Yrot, 0, 1)

t = [0.,1.]
x = [1.,0.1 ]

plt.figure()

plt.plot(T, x52(T), lw=5.0, color="g", alpha=0.5)
plt.plot(T, x5(T), lw=2.0, ls="--", color="r", alpha=0.5)
plt.plot(t, x, lw=2.0, ls="--", color="b", alpha=0.5)
plt.scatter(t, x, s=100, color="b", alpha=0.8)
plt.xlabel("annual revenue")
plt.ylabel("stock price")
plt.xlim(xlim)
plt.ylim(ylim)

############################
# noisy sample
x_rand = x + np.random.randn(x.shape[0])*10
print x_rand

# fit polynomial of high deg to noisy data
t_evil = np.hstack([t, 10000*np.array([45, 55, 70, 90])])
x_evil = np.hstack([x, [ f(t_evil[len(t)+i]) + [1,-1][i % 2] * 5 for i in range(4) ]])
p = np.polyfit(t, x_rand, x_rand.shape[0])
xr = np.poly1d(p)
T = np.arange(40, 101, 0.1)*10000

plt.figure()
plt.plot(T, xr(T), lw=5.0, color="r", alpha=0.5)
plt.plot(t, x, lw=5.0, ls="--", color="b", alpha=0.5)
plt.scatter(t, x_rand, s=100, color="b", alpha=0.8)
plt.xlabel("annual revenue")
plt.ylabel("stock price")
plt.xlim(xlim)
plt.ylim(ylim)

#plt.figure()
#x2 = [ 23, 134, 686, 240, 35]
#plt.plot(t, x2, lw=5.0, color="b", alpha=0.5)
#plt.scatter(t, x2, s=100, color="b", alpha=0.8)
#plt.xlabel("annual revenue")
#plt.ylabel("stock price")

plt.show()
