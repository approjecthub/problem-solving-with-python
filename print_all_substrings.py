# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 02:46:06 2019

@author: Anirban
"""

inp_str = 'xyyx'

def print_substring(word = inp_str):
    substrings = []
    vowel_count = 0
    l = 0
    all_ss = ['']*((len(word)*(len(word)+1))//2)
    for i in range(len(word)):
        substrings.append('')
        for j in range(i, len(word)):
            for k in range(i,j+1):
                if(word[k]=='a' or word[k]=='e' or word[k]=='i' or word[k]=='o' or word[k]=='u'):
                    vowel_count += 1
                substrings[i]+= word[k]
                all_ss[l] += word[k]
                #print(word[k], end='')
            l+=1
            #print()
            
    return [substrings,all_ss, vowel_count]
	
print(print_substring(inp_str))
        