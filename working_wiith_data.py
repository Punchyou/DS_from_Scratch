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
import matplotlib.pyplot as plt

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