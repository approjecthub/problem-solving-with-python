# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:30:49 2019

@author: Anirban
"""
a = 'abc'
def char_frequency_substring(word = a):
    vowel_count=0
    char_count = [0]*len(word)
    n = len(word)
    for i in range(n):       
        if(i==0):
            char_count[i] = n
        else:
            char_count[i] = (n-i)+char_count[i-1]-i
            
    for i in range(n):
        if word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u':
            vowel_count += char_count[i]
    
    return [char_count , vowel_count]