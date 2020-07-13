# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 08:17:12 2019

@author: Anirban
"""

### Count the pairs of vowels in the given string
def count_vowelPair():
    #s = list('abaebio')
    s=list('aeiou')
    ans = 0
    for i in range(1, len(s)):
        if (s[i-1]=='a' or s[i-1]=='e' or s[i-1]=='i' or s[i-1]=='o' or s[i-1]=='u') and \
        (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
                ans += 1
                
    return ans