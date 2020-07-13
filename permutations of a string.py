# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:12:52 2019

@author: Anirban
"""

a = 'abc'
   
def permute(word = list(a),l=0,r=len(a)):
    if l==r-1:
        print(''.join(word))
        
    else:
        for i in range(l, r):
            word[l], word[i] = word[i], word[l]
            permute(word, l+1, r)
            word[l], word[i] = word[i], word[l]
            
    
    
