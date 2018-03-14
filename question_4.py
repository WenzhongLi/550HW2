#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import matplotlib.pyplot as plt
import numpy as np


def graph():
    fin = open('sum1','r')
    y1 = []
    for line in fin:
        y1.append(float(line))
    fin.close()

    fin = open('sum2','r')
    y2 = []
    for line in fin:
        y2.append(float(line))
    fin.close()
    x = range(21)
    plt.ylim(0, 700000000)  #
    #pl.ylim(-1, 110)
    plt.plot(x, y1, marker='o', mec='r', mfc='w',label='c1')
    plt.plot(x, y2, marker='*', ms=10, label="c2")
    plt.legend()  #
    # plt.xticks(x, names)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel("iteration")  # X
    plt.ylabel("cost")  # Y
    plt.title("question4-kmeans")  # title

    plt.show()

if __name__ == "__main__":
    graph()