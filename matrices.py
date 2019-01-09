# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:36:33 2018

@author: maria_p
"""

def shape(A):
    """Shape of matrix A."""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_column(A, i):
    return A[i]

def get_row(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """returns  num_rows x num_cols matrix
    whose (i, j)th entry is entry_dn(i, j)"""
    return [[entry_fn(i, j) # given i, create a list
             for j in range(num_cols)] #[entry_fn(i, 0)...]
             for i in range(num_rows)] # create one for each i
    
# Make a marix
def is_diagonal(i, j):
    """1's on the diagonal, 0's everything else."""
    return 1 if i == j else 0

if __name__ == "__main__":
    identiry_matrix = make_matrix(5, 5, is_diagonal)
    print(identiry_matrix)