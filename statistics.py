# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:16:17 2018

@author: maria_p
"""

#Describing  single set of data

from collections import Counter
from matplotlib import pyplot as plt

num_friends = [100, 49, 41, 40, 25, 25, 100,
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
