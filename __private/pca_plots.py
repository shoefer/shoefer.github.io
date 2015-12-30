"""
PCA Tutorial
"""
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

n = 50
theta = np.linspace(-2 * np.pi, 2 * np.pi, n)
X = np.zeros( (n, 3) ) 
X[:,0] = theta #np.linspace(-2, 2, 100)
X[:,1] = 3*np.sin(theta)
X[:,2] = 0.

Rx = lambda th: np.array([
 [1, 0, 0], [0, cos(th), -sin(th)], [0, sin(th), cos(th)]
])
Ry = lambda th: np.array([
 [0, 1, 0], [cos(th), 0, -sin(th)], [sin(th), 0, cos(th)]
])

Xrot = X.dot(Rx(pi/2.).T).dot(Rx(pi/8).T)

# original
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(X[:,0],X[:,1],X[:,2], marker='o', s=20, c="blue", alpha=0.6)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(Xrot[:,0],Xrot[:,1],Xrot[:,2], marker='o', s=20, c="blue", alpha=0.6)

# compute PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca.fit(Xrot)

# plane
normal = pca.components_[-1]
d = -np.array([0,0,0]).dot(normal)
# create x,y
# xx, yy = np.meshgrid(theta, theta)
xx, yy = np.meshgrid(linspace(theta[0],theta[-1],5), linspace(theta[0]/2,theta[-1]/2,5))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# plot the surface
#plt3d = plt.figure().gca(projection='3d')
ax.plot_surface(xx, yy, z, alpha=0.3)

ax.set_xlim3d([theta[0],theta[-1]])
ax.set_ylim3d([theta[0],theta[-1]])#([-1,1])
ax.set_zlim3d([theta[0],theta[-1]])#([-1,1])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

# for ii in xrange(0,45,1):
# 	ax.view_init(elev=10., azim=ii)
# 	plt.savefig("movie%d.png" % ii)

#http://stackoverflow.com/questions/3688870/create-animated-gif-from-a-set-of-jpeg-images