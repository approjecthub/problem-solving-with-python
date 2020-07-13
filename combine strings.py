# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:36:30 2019

@author: Anirban
"""

'''
We are given 3 strings: str1, str2, and str3. Str3 is said to be a shuffle of 
str1 and str2 if it can be formed by interleaving the characters of str1 and str2 
in a way that maintains the left to right ordering of the characters from each string. 
For example, given str1=”abc” and str2=”def”, str3=”dabecf” is a valid shuffle since
 it preserves the character ordering of the two strings. So, given these 3 strings 
 write a function that detects whether str3 is a valid shuffle of str1 and str2.
'''


def combine_check(str1, str2, str3):
    str1, str2, str3 = list(str1), list(str2), list(str3)
    l1, l2, l3 = len(str1), len(str2), len(str3)
    if(l3!=(l1+l2)):
        return False
    i, j = 0,0
    for s in str3:
        if(i!=l1 and s==str1[i]):
            i+=1
        elif(j!=l2 and s==str2[j]):
            j+=1
        else:
            return False
            
    return True

def driver():
    str1 = 'abc'
    str2 = 'def'
    #str3 = 'dacebf'
    str3 = 'dabecf'
    print(combine_check(str1, str2, str3))
            