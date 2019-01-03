# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:23:00 2019

@author: maria_p
"""
"""Estimating the gradient"""
from functools import partial
import matplotlib.pyplot as plt

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h #as h approaches zero

def square(x):
    return x * x

def derivative(x):
    return 2 * x

derivative_estimate = partial(difference_quotient, square, h=0.00001)

#plot to show they 're basically the same

x = range(-10, 10)
plt.title("Actual Derivtives vs. Estimates")
plt.plot(x, list(map(derivative, x)), 'rx', label='Actual')
plt.plot(x, list(map(derivative_estimate, x)), 'b+', label='Estimate')
plt.legend(loc=9)
plt.show()

def partial_derivative_quotent(f, v, i, h):
    """compute the ith partial difference quotent of f at v"""
    w = [v_j + (h if j == i else 0)
    for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimte_gradient(f, v, h=0.00001):
    return [partial_derivative_quotent(f, v, i, h)
            for i, _ in enumerte(v)]