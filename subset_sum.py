# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:03:45 2020

@author: Anirban
"""

## https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

#arr = [3, 34, 4, 12, 5, 2]
#sum_e = 14


def ps(sum_o,n):
    global arr
    global sum_e
    if sum_e==sum_o:
        return True
    elif n<0 :
        return False
    else:
        return (ps(arr[n]+sum_o, n-1) or ps(sum_o, n-1))
    
import math

arr = [3, 1, 5, 9, 12]

if math.ceil(sum(arr)/2)!=math.floor(sum(arr)/2):
    print(False)
else:
    sum_e = sum(arr)//2
    print(ps(0, len(arr)-1))
    
#print(ps(0, len(arr)-1))