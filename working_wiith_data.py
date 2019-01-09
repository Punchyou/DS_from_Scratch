# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:35:19 2019

@author: maria_p
"""
"""Exloring one-dimensional data"""
import math
from collections import Counter
import random
from probability import inverse_normal_cdf
from statistics2 import correlation, covariance
import matplotlib.pyplot as plt
from matrices import shape, get_column, make_matrix

"""Group the data into descrete buckets and count how many fall into each bucket."""
def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of buvket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

random.seed(0)

#uniform between -100 and 100
uniform = [200 * random.random() - 100 for _ in range(10000)]

#normal distribution with mean 0, standard deviation 57
normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]


plot_histogram(uniform, 10, 'Uniform Histogram')
plot_histogram(normal, 10, 'Normal Histogram')

"""Two-Domentional data"""
def random_normal():
    '''returns a random draw from a stndard normal distribution'''
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() /2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]
data = [xs, ys1]
plot_histogram(ys1, 10, 'ys1')
plot_histogram(ys2, 10, 'ys2')


plt.scatter(xs, ys1, marker='.', color= 'black', label='ys1')
plt.scatter(xs, ys2, marker='.', color= 'gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys1, ys2')
plt.legend(loc=9)
plt.title('Very Different Joint Distributions')
plt.show()

"""Many dimensions"""
def correlaion_matrix(data):
    """retuns the num_columns x num_columns matrix whose (i, j)th
    entry is the correlation between columns i and j of the data"""
    _, num_columns = shape(data)
    
    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))
    return make_matrix(num_columns, num_columns, matrix_entry)