import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

x = [50, 100, 150, 250, 350, 500, 750, 1000]
y = [3, 4, 5, 6]
z = [[0.021, 0.024, 0.027, 0.029],
     [0.047, 0.055, 0.062, 0.065],
     [0.084, 0.087, 0.102, 0.103],
     [0.148, 0.164, 0.178, 0.190],
     [0.230, 0.251, 0.264, 0.277],
     [0.327, 0.368, 0.406, 0.422],
     [0.538, 0.573, 0.637, 0.690],
     [0.733, 0.809, 0.848, 0.894]]

X = np.asarray(x)
Y = np.asarray(y)
X, Y = np.meshgrid(X, Y)
Z = np.asarray(z)
Z = Z.transpose()

surf = ax.plot_surface(X, Y, Z, cmap=cm.cool, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
