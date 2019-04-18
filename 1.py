import matplotlib.pyplot as plt
import numpy as np

X = np.load('daneX.npy')
Y = np.load('daneY.npy')
Z = np.histogram2d(X,Y, bins=100, range=None, normed=None, weights=None)
plt.pcolormesh(Z[0], cmap='magma')
plt.colorbar()
plt.show()
