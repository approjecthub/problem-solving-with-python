# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:48:51 2020

@author: Anirban
"""

ans = []

def all_factor(n):
    global ans
    
    for i in range(2, n//2):
        if(n%i == 0):
            ans.append(i)
            all_factor(n//i)
            
    return ans
            

def prime_factor(n):
    ansp = []
    i=2
    while(i<=n//2):
        
        if(n%i == 0):
            ansp.append(i)
            n = n//i
            i = 2
            continue
            
        i +=1
        
    ansp.append(n)
            
    return ansp

def digit_sum(n):
    q = n
    r = 0
    s = 0
    while(q!=0):
        r = q %10
        q = q//10
        s += r
        
    return s
                  

def smith(n):
    p = prime_factor(n)
    if len(p)==1:
        return False
    fs = 0
    ns = digit_sum(n)
    for i in range(len(p)):
        fs += digit_sum(p[i])
        
    if fs== ns:
        return True
    else:
        return False
   
def sphenic(n):
    p = prime_factor(n)
    if len(p)!=3:
        return False
    p = set(p)
    if len(p)==3:
        return True
    else:
        return False
        
            