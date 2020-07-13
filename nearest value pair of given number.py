# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 01:18:28 2019

@author: Anirban
"""

# Program_to_find_the_nearest_value_pair_among_the_two_sorted_arrays

ar1 = [1, 4, 5, 7]
ar2 = [10, 20, 30, 40]

x = 32 #Given value for which value pair is being calculated

l=0
r=len(ar2) - 1

diff= 9999

while(l<len(ar1) - 1 and r>0):
    
    diff_x = ar1[l]+ar1[r]-x
    if(abs(diff_x) < abs(diff)):
        diff = diff_x
    else:
        break
    
    r -= 1    
    if(r>=0 and abs(ar1[l]+ar2[r]-x)> abs(diff)):
        r += 1
        
    l += 1
    if(l<=len(ar1) - 1 and abs(ar1[l]+ar1[r]-x)>abs(diff)):
        l -= 1          

        

print(ar1[l])
print(ar2[r])
