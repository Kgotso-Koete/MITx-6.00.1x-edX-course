# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:24:54 2016

@author: Kgotso Koete
"""

def general_poly(L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def x_function(x):
        result = []
        count = len(L)-1
        for e in range(len(L)):
            result.append(L[e]*x**count)
            count -= 1
        return sum(result)
    return x_function