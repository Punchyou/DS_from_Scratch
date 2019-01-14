# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from functools import partial, reduce
import math

vectors = [[1, 3, 5], [3,5,9], [2,4,8]]
v = [3,4,7]
w = [2, 7, 9]
''' Adding vectors. '''
def vector_add(v, w):
	return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_substract(v, w):
    """substracts cooresponding elements."""
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    #sum all cooresponding elements
	result = vectors[0]
	for vector in vectors[1:]:
		result = vector_add(result, vector)
	return result

#we prctically reduce the list of vectors, so
def vector_sum(vectors):
	return partial(reduce, vector_add)

print(vector_sum(vectors))



'''Multiplying vectors.'''

#multiply   vector by a scalar
def scalar_mulltiply(c, v):
    """c is  number, v is a vector"""
    return [c*v_i for v_i in v]
    
def vector_mean(v, w):
    """compute the vector whose ith element
    is the men of the ith elements of the input vectors."""
    n = len(vectors)
    return scalar_mulltiply(1/n, vector_sum(vectors))

# the sum of vectors' coorespondingwise products - The dot product
''' The dot product measures the length of the vector you'd get
    if you projected v onto w.'''
def dot(v, w):
    """v_1*w_1 + v_2*w_2 + ... + v_n*w_n"""
    return sum(v_i*w_i for v_i, w_i in zip(v, w))

print(dot(v,w))

# sum of squeares
def sum_of_squares(v):
    return dot(v, v)
print(sum_of_squares(v))
 
def squared_distance(v, w):
    """(v_i, w_i)**2 + ... + (v_n - w_n)**2"""
    return sum_of_squares(vector_substract(v, w))

def distance(w, v):
    return math.sqrt(squared_distance(v, w))

