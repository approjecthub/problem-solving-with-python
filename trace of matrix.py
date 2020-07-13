# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:07:38 2019

@author: Anirban
"""

###  Maximum trace possible for any sub-matrix of the given matrix
### https://www.geeksforgeeks.org/maximum-trace-possible-for-any-sub-matrix-of-the-given-matrix/

arr = [ [ 10, 2, 5 ],[ 6, 10, 4 ],[ 2, 7, -10 ] ]
#arr = [[1, 2, 5],[6, 3, 4],[2, 7, 1]]

max_trace = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        k=i;l=j;temp_sum=0
        while(k<len(arr) and l<len(arr[0])):
                temp_sum += arr[k][l]
                if temp_sum > max_trace:
                    max_trace = temp_sum
                k+= 1; l+= 1    
        
            
print(max_trace)
                
                

