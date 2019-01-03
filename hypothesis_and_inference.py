# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:55:12 2019

@author: maria_p
"""

"""Test if a coin is fair."""

import math
from probability import normal_cdf, inverse_normal_cdf
def normal_approximation_to_binomial(n, p):
    """finds mu and sigma to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

#the normal cdf is the probability the vriable is below  threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

#it's between if it's less than hi, but not less than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

#it's outside if it's not between
def norml_probability_outside(lo, hi, mu=1, sigma=0):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

"""find an interval centered at mean and containg 60% of probability"""
def normal_upper_bound(probability, mu=0, sigma=1):
    """returns z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu=0, sigma=1)

def normal_lower_bound(probability, mu=0, sigma=1):
    """returns z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu=0, sigma=1)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specific probability"""
    tail_probability = (1 - probability) / 2
    
    #upper bound should have tail probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    
    #lower bound should have tail probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    
    return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

print(mu_0, sigma_0)
print(normal_two_sided_bounds(0.95, mu_0, sigma_0))    