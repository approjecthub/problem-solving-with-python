# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:28:36 2019

@author: Anirban
"""

##  Count the number of primes in the prefix sum array of the given array

import math

arr = [1, 5, 2, 3, 7, 9]

def isprime(value):
    if(value<2):
        return False
    
    for i in range(2, math.ceil(math.sqrt(value))):
        
        if(value%i==0):
            return False
    
    return True
        

def prefix_sum(a = arr):
    sum = 0
    prime_count = 0
    
    for i in range(len(a)):
        sum += a[i]
        a[i] = sum
        if(isprime(a[i])==1):
            prime_count += 1
        
    return prime_count