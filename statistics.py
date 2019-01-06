# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:16:17 2018

@author: maria_p
"""

#Describing  single set of data

from collections import Counter
from matplotlib import pyplot as plt
from vectors import sum_of_squares, dot
from math import sqrt

num_friends = [100, 49, 41, 40, 25, 25, 100, 100,
               #...and lots more
               ]
friends_counts = Counter(num_friends)

xs = range(101)
ys = [friends_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()


#  Central Tendencies
def mean(x):
    """Average."""
    return sum(x)/len(x)

print(mean(num_friends))

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        #if odd number of elements, return the middle value
        return sorted_v[midpoint]
    else:
        #if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi])/2

print(median(num_friends))


#Quantile, represents the values less than which a certain
#persentage of the data lies.
def quantile(x, p):
    """returns the pth-percentile values in x."""
    p_index = int(p * len(x))
    return sorted(x)[p_index]
print(quantile(num_friends, 0.1))

# Mode, the most common values
def mode(x):
    """returns a list, might be more tha one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]


#Dispersion, how spread out the data is.
#A measure of dispersion is the variance.
def de_mean(x):
    """translate x by substracting its mean."""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements."""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return sqrt(variance(x))

print(standard_deviation(num_friends))
    
#Another method
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

print(interquartile_range(num_friends))

#Correlation
daily_mins = [50, 23, 24, 22, 27, 29, 70, 65] #the mins that a user
#spends on a social media site
def covariance(x, y):
    """how two variables vary in tandem from their means"""
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

print(covariance(num_friends, daily_mins))

#Its difficult to say what counts as a "large" covariance.
#That's why we use correlation

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x /stdev_y
    else:
        return 0
print("Correlation num_friends, daily_mins: ", correlation(num_friends, daily_mins))

plt.scatter(num_friends, daily_mins)
plt.show()