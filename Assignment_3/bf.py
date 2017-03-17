import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

x = [50, 100, 150, 250, 350, 500, 750, 1000]
y = [3, 4, 5, 6]
z = [[0.014, 0.013, 0.017, 0.021],
     [0.026, 0.032, 0.037, 0.044],
     [0.040, 0.053, 0.060, 0.066],
     [0.072, 0.090, 0.103, 0.116],
     [0.108, 0.128, 0.152, 0.171],
     [0.155, 0.177, 0.214, 0.249],
     [0.229, 0.286, 0.334, 0.402],
     [0.309, 0.383, 0.433, 0.518]]

X = np.asarray(x)
Y = np.asarray(y)
X, Y = np.meshgrid(X, Y)
Z = np.asarray(z)
Z = Z.transpose()

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
