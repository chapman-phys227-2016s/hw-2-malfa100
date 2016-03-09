"""
File: midpoint_vec.py
Copyright (c) 2016 Andrew Malfavon
Excerise 5.22
License: MIT
Compares the runtimes of python sum, python for loop summation
and numpy vectorized sum on the midpoint integral formula.
"""

import numpy as np
import timeit

#midpoint rule for approximating an integral using a for loop
def midpointint(f, a, b, n):
    h = (b - a) / float(n)
    sum_function = 0
    for i in range(n):
        sum_function += h * f(a - (h / 2) + (i * h))
    return sum_function


#compute the sum with the built in sum function
def midpoint_sum_func(f, a, b, n):
    h = (b - a) / float(n)
    arr = []
    for i in range(n):
        arr.append(h * f(a - (h / 2) + (i * h)))
    return sum(arr)


#compute the sum by the sum function in the numpy package
def midpoint_npsum(f, a, b, n):
    h = (b - a) / float(n)
    arr = []
    for i in range(n):
        arr.append(h * f(a - (h / 2) + (i * h)))
    return np.sum(arr)

#function for testing
def func(x):
    return x

#test that each approximates the integral correctly
def test_func():
    assert round(midpointint(func, 0 , 10, 1000)) == 50.0
    assert round(midpoint_sum_func(func, 0, 10, 1000)) == 50.0
    assert round(midpoint_npsum(func, 0, 10, 1000)) == 50.0

#additional test
def test_func2():
    assert round(midpointint(np.sin, 0 , np.pi, 1000)) == 2.0
    assert round(midpoint_sum_func(np.sin, 0, np.pi, 1000)) == 2.0
    assert round(midpoint_npsum(np.sin, 0, np.pi, 1000)) == 2.0