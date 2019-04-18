import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

X = np.load('daneX.npy')
Y = np.load('daneY.npy')
Z = np.histogram2d(X,Y, bins=100)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(0,100,1)

A,B = np.meshgrid(x,y)

ax.plot_surface(A, B, Z[0], cmap='jet')

plt.show()
