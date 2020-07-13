# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 01:53:27 2020

@author: Anirban
"""

## https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/

arr = [5, 3, 7, 10]

def best_result(i,n):
    global arr
    if i>n:
        return arr[i]
    elif i+1==n:
        return max(arr[i], arr[i+1])
    else:
        return max(arr[i]+min(best_result(i+1,n-1), best_result(i+2,n)) , 
                   arr[n]+min(best_result(i,n-2), best_result(i+1,n-1)))
    
print(best_result(0,len(arr)-1))