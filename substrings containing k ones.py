# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 07:43:53 2019

@author: Anirban
"""

### Count of substrings of a binary string containing K ones

def solution2():        ## O(N^2) solution
    s = list('10010')
    k=1
    
    ans = 0
    for i in range(len(s)):
        ones=0
        
        for j in range(i, len(s)):
            if s[j]=='1':
                ones += 1
                
            if(ones == k):
                ans += 1
            if(ones >k):
                break
    return ans