import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import interpolate

A = np.load('inter1D.npz')
x = A['x']
y = A['y']
f = interpolate.interp1d(x, y, kind='cubic')
c = np.linspace(-1,1,100)
b = np.linspace(-1,1,12)
ynew=f(c)
plt.plot(b, np.interp(b,x,y), '--o')
plt.plot(x,y, 'o', c, ynew, '-')
plt.show()
