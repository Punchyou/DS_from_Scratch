# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:40:18 2019

@author: maria_p
"""
from matrices import shape
from statistics2 import mean, standard_deviation
from matrices import get_column
from vectors import dot, vector_sum
from working_wiith_data import make_matrix
import numpy as np

'''Principal component anaysis'''
A = [[1, 2, 3], [2, 5, 8], [7, 9, 1]]

def scale(data_matrix):
    '''returns the meas and standard deviation of each column'''
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix, j)) for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix, j))
    for j in range(num_cols)]
    return means, stdevs
    
def de_mean_matrix(A):
    '''returns the result of subtracting from every value in A the mean
    value of its column, The resulting matrix has mean 0 in every column'''
    nr, nc = shape(A)
    column_means, _ = scale(A)
    return make_matrix(nr, nc, lambda i, j: A[i][j] - column_means[j])

def direction(w):
    mag = np.linalg.norm(w)
    return [w_i / mag for w_i in w]

def directional_variance_i(x_i, w):
    '''the variance of the data in the direction determined by w'''
    return dot(x_i, direction(w)) ** 2

def directional_variance(X, w):
    '''the variamce of the data in the direction determined by w'''
    return sum(directional_variance_i(x_i, w)
               for x_i in X)

'''maximize the variance'''
def directional_variance_gradient_i(x_i, w):
    '''the contribution of row x_i to the grdient of the direction-w variance'''
    projection_length = dot(x_i, direction(w))
    return [2 * projection_length * x_ij for x_ij in x_i]

def directional_variance_gradient(X, w):
    return vector_sum(directional_variance_gradient_i(x_i, w) for x_i in X)