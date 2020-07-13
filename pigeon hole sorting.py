# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:48:34 2019

@author: Anirban
"""

a = [80,3,2,7,4,6,8]

def pigeonhole_sorting(a):
    minm = min(a)
    maxm = max(a)
    
    size = maxm - minm +1
    
    hole = [0]*size
    
    for i in a:
        hole[i - minm] += 1
        
    print(minm)
    print(hole)
        
    i=0
    for c in range(size):
        while( hole[c]>0):
            a[i]= c+ minm
            hole[c] -= 1
            i += 1
        
    return a
