# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:47:42 2019

@author: maria_p
"""
"""Conditionl Probabilities."""

"""A family with two unknown children."""
from random import choice, seed, random
from math import sqrt, exp, pi, erf
from matplotlib import pyplot as plt
from collections import Counter

def random_kid():
    return choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

seed(5) # seed() returns a different sequence of values

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1
#print("P(both | older): ", both_girls / older_girl)
#print("P(both | either: ", both_girls / either_girl)

"""The density function"""
def uniform_pdf(x):
    return 1 if x >= 0 and x <1 else 0

"""The cumulative distribution function"""
def uniform_cfd(x):
    """returns the probbility that a uniform random vroable
    is <= x"""
    if x<0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

"""The normal pdfs"""
def normal_pdf(x, mu = 0, sigma = 1):
    sqrt_two_pi = sqrt(2 * pi)
    return (exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label = 'mu=0, sigma=1') #standart norma distribution
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label = 'mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label = 'mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu = -1) for x in xs], '-.', label = 'mu=-1, sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
#plt.show()

"""The norms cdfs"""
def normal_cdf(x, mu=0, sigma=1):
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2 #using the erf, error function

plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label = 'mu=0, sigma=1') #standart norma distribution
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label = 'mu=0, sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label = 'mu=0, sigma=0.5')
plt.plot(xs, [normal_cdf(x, mu = -1) for x in xs], '-.', label = 'mu=-1, sigma=1')
plt.legend(loc = 4) #bottom right
plt.title("Various Normal cdfs")
#plt.show()

"""Invert normal_cdf to find the values corresponding to specific probabiity.
This function repeatedly bisects intervals until it narrows in on a Z
tht's close enough to the desired probability."""
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search."""
    
    #if not standard, compute standard nd rescale
    if mu !=0 or sigma !=1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10.0 #normal_cdf(-10) is close to 0
    hi_z = 10.0 #norml_cfd(10) is close to 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 #the midpoint
        mid_p = normal_cdf(mid_z) #and the cdf's value there
        if mid_p < p:
            #midpoint still too low, search above it
            low_z = mid_z
        elif mid_p > p:
            #midpoint still to high
            hi_z = mid_z
        else:
            break
    return mid_z
"""The central limit theorem - For large n sampe of samples, the distribution
of means for the samples of samples is approximatelly normal."""
"""A Bernouli variable is the sum of n independent bernouli random variables,
each of which equals 1 with probability p and 0 with probability 1 - p."""
def bernouli_trial(p):
    return 1 if random() < p else 0

def binomial(n, p):
    return sum(bernouli_trial(p) for _ in range(n))

"""Ploting the binomial and normal distributions."""
def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    
    #use a bar chrt to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
             [v / num_points for v in histogram.values()],
             0.8,
             color='0.75')
    
    mu = p * n
    sigma = sqrt(n * p * ( 1 - p))
    
    #use a line to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
        for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    #plt.show()

#make_hist(0.75, 100, 10000)