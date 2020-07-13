# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:19:26 2019

@author: Anirban
"""

#a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
#a =[-2, -3, 4, -1, -2, 1, 5, -3]
a = [1,-1,-2]

current_max_sum = 0
max_sum_tillnow = -1000000000
start_index = 0
end_index = 0

for i in range(len(a)):
    current_max_sum += a[i]
    
    if current_max_sum>max_sum_tillnow:
        max_sum_tillnow = current_max_sum
        end_index = i
    
    if current_max_sum<0:
        start_index= i+1
        current_max_sum=0
        
        
