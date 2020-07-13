# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:35:48 2019

@author: Anirban
"""

def gcd(a=1,b=1):
    r=0
    if(a>b):
        a,b = b,a
    while(True):
        r = b%a
        b = a
        
        if r==0:
            break
        a = r
        
    return a

a=[2,3,6]

a1 = a[0]

for i in range(1,len(a)):
    a1 = gcd(a1,a[i])
    

