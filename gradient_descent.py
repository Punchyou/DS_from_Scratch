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

"""Putting it all together"""
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """use gradient descent to find theta that minimizes trget function"""
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0 #initial value of theta
    target_fn = safe_f(target_fn) #safe version of target_fn
    value = target_fn(theta) #value we're minimizing
    
    while True:
        gradient = grdient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size
                            for step_size in step_sizes)]
        
    #choose the one that minimizes the error function
    next_theta = min(next_thetas, key=target_fn)
    next_value = target_fn(next_theta)
    
    # stop if we re converging
    if abs(value - next_value) < tolerance:
        return theta
    else:
        theta, value = next_theta, next_value
        
"""Maximizing a function"""
def negate(f):
    """return a func that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    """the same when f returns a list of munbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)
