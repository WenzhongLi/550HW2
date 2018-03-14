#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import scipy.linalg as linalg
import numpy as np


def question_b():
    matrix_m = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
    eigenvalues, eigenvectors = linalg.eigh(matrix_m.transpose().dot(matrix_m))
    print(eigenvalues)
    print(eigenvectors)


def question_a():
    # matrix_m = [[1, 2], [2, 1], [3, 4], [4, 3]]
    # U,sig,Vh = linalg.svd(matrix_m, full_matrices = False)
    # print(U)
    # print(sig)
    # print(Vh)

    # A = np.array([[1, 2, 3], [4, 5, 6]])
    matrix_m = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
    print(matrix_m[1])
    # A = np.array([[1, 2, 3, 4], [2, 1, 4, 3]])
    print(matrix_m)
    # array([[1, 2, 3],
    #        [4, 5, 6]])
    M, N = matrix_m.shape
    U, s, Vh = linalg.svd(matrix_m)
    Sig = linalg.diagsvd(s, M, N)[0:2, 0:2]
    # U, Vh = U, Vh
    U = U[0:4, 0:2]
    print(U)
    # array([[-0.3863177, -0.92236578],
    #        [-0.92236578, 0.3863177]])
    print(Sig)
    # Sig = np.array([[7.61577311, 0], [0, 1.41421356]])
    # array([[9.508032, 0., 0.],
    #        [0., 0.77286964, 0.]])

    print(Vh)
    # Vh = np.array([[-0.27854301, -0.27854301, -0.64993368, -0.64993368],
    #       [0.5, -0.5, 0.5, -0.5]])
    # array([[-0.42866713, -0.56630692, -0.7039467],
    #        [0.80596391, 0.11238241, -0.58119908],
    #        [0.40824829, -0.81649658, 0.40824829]])
    print(U.dot(Sig.dot(Vh)))  # check computation
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])


if __name__ == "__main__":
    question_a()
    question_b()