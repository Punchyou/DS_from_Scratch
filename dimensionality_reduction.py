# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:40:18 2019

@author: maria_p
"""
from matrices import shape
from vectors import scalar_mulltiply
from statistics2 import mean, standard_deviation
from matrices import get_column
from vectors import dot, vector_sum, vector_substract
from working_wiith_data import make_matrix
import matplotlib.pyplot as plt
import numpy as np
import random
from gradient_descent import maximize_batch
from functools import partial

'''Principal component anaysis'''
A = [[random.randrange(70) for _ in range(2)] for __ in range(200)]

def make_scatterplot(A, xlab, ylab, title):
    for i, _ in enumerate(A):
        plt.scatter(A[i][0], A[i][1], marker = '.', color= 'purple')
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.title(title)
    return plt.show()

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


make_scatterplot(de_mean_matrix(A), "", "", "De-meaning")

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

'''The First prinsipal component is the direction tht maximizes
the directional_varince function.'''

def first_principal_component(X):
    guess = [1 for _ in X[0]]
    unscaled_maximizer = maximize_batch(
            partial(directional_variance, X),
            partial(directional_variance_gradient, X),
            guess)
    return direction(unscaled_maximizer)


''' Project the data on the first principal component to find the
values of that component.'''

def project(v, w):
    '''return the projection of v onto the directon w'''
    projection_length = dot(v, w)
    return scalar_mulltiply(projection_length, w)

''' If we want to find further components, remove the projections from the data'''
def remove_projection_from_vector(v, w):
    '''projects v onto w and subtracts the results from v'''
    return vector_substract(v, project(v, w))

def remove_projection(v, w):
    '''for each row of X projects the row of onto w,
    and subtracts the result from the row'''
    return [remove_projection_from_vector(x_i, w) for x_i in X]
 
'''On a higher dimention data set, we can iteratively find
as many components as we want'''

def principal_component_analysis(X, num_components):
    components = []
    for _ in range(num_components):
        component = first_principal_component(X)
        components.append(component)
        X = remove_projection(X, component)
    return component

'''We can then transform out data into the lower-imentional space
spanned by the components.'''
def transform_vector(v, components):
    return [dot(v, x) for w in components]

def transform(C, components);:
    return [transform_vector(x_i, components) for x_ in X]