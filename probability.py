# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:47:42 2019

@author: maria_p
"""
"""Conditionl Probabilities."""

"""A family with two unknown children."""
from random import choice, seed
from math import sqrt, exp, pi, erf
from matplotlib import pyplot as plt

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
print("P(both | older): ", both_girls / older_girl)
print("P(both | either: ", both_girls / either_girl)

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
plt.show()

"""The norms cdfs"""
def normal_cdf(x, mu=0, sigma=1):
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2 #using the erf, error function

plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label = 'mu=0, sigma=1') #standart norma distribution
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label = 'mu=0, sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label = 'mu=0, sigma=0.5')
plt.plot(xs, [normal_cdf(x, mu = -1) for x in xs], '-.', label = 'mu=-1, sigma=1')
plt.legend(loc = 4) #bottom right
plt.title("Various Normal cdfs")
plt.show()
