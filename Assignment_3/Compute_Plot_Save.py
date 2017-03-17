from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import csv
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
    print(X)
    Y = np.array(y)
    print(Y)
    # X, Y = np.meshgrid(X, Y)
    print(X)
    print(Y)
    Z = np.array(z)
    print(Z)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()

def csv_exporter(data):
    with open("data_out.csv", "w+", newline='\n') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def main():
    num_vertices = 2000
    X_v = []
    Y_e = []
    Z_t = []
    try:
        for i in range(2, num_vertices, 50):
            for j in range(2, i*(i-1)+1, 1000):
                X_v.append(i)
                Y_e.append(j)
                t = get_compute_time(i, gen_test_case(i, j))
                Z_t.append(t)
                os.system('cls')
                print("V{} E{} T{}".format(i, j, t))
        generate_plot(X_v, Y_e, Z_t)
    except:
        generate_plot(X_v[:-1], Y_e[:-1], Z_t)

    csv_exporter(list(zip(X_v, Y_e, Z_t)))

if __name__ == '__main__':
    main()
