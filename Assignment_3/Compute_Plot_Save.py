from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import time
import os

from Bellman_Ford import BellmanFord as bf
from Random_Graph_Generator import RandomGraphGenerator as rgg

def gen_test_case(v, e):
    g = rgg(v, e)
    # start = time.clock()
    # print(start)
    g.generate_edge_list()
    # end = time.clock()
    # print(end)
    # runtime = end - start
    # print(runtime)
    return g.get_edge_list()

def get_compute_time(v, graph):
    algo = bf(1, v, eTuple=graph)
    start = time.clock()
    # print(start)
    algo.process()
    end = time.clock()
    # print(end)
    runtime = end - start
    # print(runtime)
    return runtime

def generate_plot(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X = np.array(x)
    Y = np.array(y)
    X, Y = np.meshgrid(X, Y)
    Z = np.array(z)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()

def main():
    num_vertices = 200
    X_v = []
    Y_e = []
    Z_t = []
    for i in range(2, num_vertices):
        for j in range(2, i*(i-1)+1):
            X_v.append(i)
            Y_e.append(j)
            t = get_compute_time(i, gen_test_case(i, j))
            Z_t.append(t)
            os.system('cls')
            print("V{} E{} T{}".format(i, j, t))
    generate_plot(X_v, Y_e, Z_t)


if __name__ == '__main__':
    main()
    # print(get_compute_time(50, gen_test_case(50, 2450)))
    # print(get_compute_time(100, gen_test_case(100, 9900)))
    # print(get_compute_time(200, gen_test_case(200, 39800)))
