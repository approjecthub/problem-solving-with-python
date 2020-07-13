# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:39:37 2019

@author: Anirban
"""

ar = [12,16,22,30,35,39,42,45,48,50,53,55,56] #input array

X=35 #the element in the array for which k closest element has to be found
k=4

sub = []
for i in range(len(ar)):
    if(abs(X-ar[i])!=0):
        sub.append(X-ar[i])
    
for i in range(len(sub)):
    for j in range(len(sub)-i-1):
        if(abs(sub[j])>abs(sub[j+1])):
            sub[j],sub[j+1] = sub[j+1], sub[j]

for i in range(k):
    print(X-sub[i])