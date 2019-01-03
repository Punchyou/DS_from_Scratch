# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:23:00 2019

@author: maria_p
"""
"""Estimating the gradient"""
from functools import partial
from vectors import distance
import matplotlib.pyplot as plt
import random

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
            for i, _ in enumerate(v)]


"""Using the gradient"""
"""Pick a strting point nd thet tke tiny steps in the opposite direction
untill the gradient is very small"""
def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

#pick a random starting point
v = [random.randint(-10, 10) for i in range(3)]

tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v) #compute the gradient at v
    next_v = step(v, gradient, -0.01) #take a negtive gradient step
    if distance(next_v, v) < tolerance: #stop if you are converging
        break
    v = next_v #continue if you're not

"""Choosing the right step_size"""
"""Some step sizes can result invalid inputs for functions.
 avoid this, we create a safe apply function."""
 
def safe(f):
    """return new function that's the sme as f,
    except htat it outputs infinity whenever
    f produces an error"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return flot('inf')
    return safe_f