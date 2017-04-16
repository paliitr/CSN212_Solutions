from Point import Point as P
from Random_Case_Generator import RandomCaseGenerator as RCG

from Gift_Wrapping import GiftWrapping as GW
from Graham_Scan import GrahamScan as GS
from Quick_Hull import QuickHull as QH

import numpy as np
import time
import matplotlib.pyplot as plt
import csv

numpts = [100, 1000, 2000, 5000, 10000]
x_range = [-1000, 1000]
y_range  = [-1000, 1000]

def pt_to_arr(pts):
    for i in range(len(pts)):
        pts[i] = [pts[i].x, pts[i].y]
    return pts

def write_to_csv(pts, algo=None):
    if algo == None:
        pts = pt_to_arr(pts)
        filename = "data/points.csv"
    if algo == "gw":
        filename = "giftwrap.csv"
    if algo == "gs":
        filename = "grahamscan.csv"
    if algo == "qh":
        filename = "quickhull.csv"
    if algo == "time":
        filename = "data/time.csv"

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(pts)

def main():
    ts_gw = []
    ts_gs = []
    ts_qh = []

    for numpt in numpts:
        print("Running for {} points".format(numpt))
        rcg = RCG(numpt, x_range, y_range)
        pts = rcg.generate()
        print("Points generated")
        gw = GW(pts)
        gs = GS(pts)
        qh = QH(pts)

        t0 = time.time()
        print("GW started at {}".format(t0))
        gw.run()
        t1 = time.time()
        print("GS started at {}".format(t1))
        gs.run()
        t2 = time.time()
        print("QH started at {}".format(t2))
        qh.run()
        t3 = time.time()
        print("All finished at {}".format(t3))

        ts_gw.append(t1 - t0)
        ts_gs.append(t2 - t1)
        ts_qh.append(t3 - t2)

        time_arr = [ts_gw, ts_gs, ts_qh]

    print("Saving Data")
    write_to_csv(pts)
    write_to_csv(time_arr, algo="time")
    print("Written to csv")

    l_gw = plt.plot(numpts, ts_gw, label="Gift Wrap")
    l_gs = plt.plot(numpts, ts_gs, label="Graham Scan")
    l_qh = plt.plot(numpts, ts_qh, label="Quick Hull")

    plt.ylabel("Runtime in seconds")
    plt.xlabel("Number of points")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
    plt.axis([0, 11000, 0, 1])
    plt.savefig('chart.png')
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
