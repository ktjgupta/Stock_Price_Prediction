# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:23:38 2019

@author: ktjgu
"""

def solution(A):
    # write your code in Python 3.6
    return recursearr(A, 0)

def recursearr(A, i):
    if i == len(A):
        return 0
    
    minval = 1000000000
    minindex = 0
    ogi = i
    while i < len(A):
        if A[i] < minval:
            minval = A[i]
            minindex = i
        i += 1
    if (ogi == minindex):
        return recursearr(A, minindex + 1)
    return (1 + recursearr(A, minindex + 1))

A = [1, 2, 4, 5, 3]
print(solution(A))