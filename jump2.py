# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:18:28 2019

@author: ktjgu
"""

def solution(A):
    # write your code in Python 3.6
    big_len = 0
    for word in A:
        curr_word = set(word)
        if len(curr_word) != len(word):
            continue
        for addword in A:
            new_word = set(addword)
            if len(new_word) != len(addword):
                continue
            combined = curr_word.union(new_word)
            if (len(combined) < (len(curr_word) + len(new_word))):
                continue
            curr_word = combined
        big_len = len(curr_word)
        break
    
    return big_len

def solutionB(A):
    # write your code in Python 3.6
    big_len = 0
    for word in A:
        curr_word = set(word)
        if len(curr_word) == len(word):
            break
        
    print(curr_word)
    for addword in A:
        new_word = set(addword)
        if len(new_word) != len(addword):
            continue
        combined = curr_word.union(new_word)
        print (combined)
        if (len(combined) < (len(curr_word) + len(new_word))):
            continue
        curr_word = combined
    big_len = len(curr_word)
    return big_len

A = ['eva', 'jqw', 'tyn', 'jan']
print(solutionB(A))