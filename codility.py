# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:11:49 2019

@author: Anirban
"""


def solution1(S):
    if(len(S)<3):
        return len(S)
    ss = [S[i:j] for i in range(len(S)) for j in range(i+1, len(S)+1)]
    max_len = 2
    for s in ss:
        temp_len = 2
        for i in range(len(s)-2):
            if(s[i]!=s[i+1] or (s[i]==s[i+1] and s[i+1]!=s[i+2])):
                temp_len += 1
            else:
                break
            
        if temp_len>max_len:
            max_len = temp_len
            
    return max_len

    
    