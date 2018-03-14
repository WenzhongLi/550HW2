#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import numpy as np
import scipy.linalg as linalg


def page_rank():
    fin = open("graph.txt",'r')
    r = np.zeros(shape = (100,))
    for i in range(100):
        r[i] = 0.01

    tele = np.zeros(shape=(100,))
    for i in range(100):
        tele[i] = 0.002
    # print(r)

    matrix = np.zeros(shape = (100, 100))
    for line in fin:
        data = line.rstrip().split('\t')
        matrix[int(data[1])-1, int(data[0])-1] = 1.0

    # matrix[0, 0] = 1
    # matrix[1, 0] = 1
    # r_next = matrix.dot(r)
    # r_next = r_next*0.1
    # print(r_next)

    for i in range(100):
        count = float(0)
        for j in range(100):
            count += matrix[j, i]
        for j in range(100):
            if matrix[j, i] != 0:
                matrix[j, i] = 1.0/count

    print(matrix)

    for i in range(40):
        # p = matrix.dot(r)
        # print(p)
        r = 0.8 * matrix.dot(r) + tele
        print(r)

    sum = 0
    for i in r:
        sum += i
    print(sum)

    print(r.argsort()[:3])





if __name__ == "__main__":
    page_rank()