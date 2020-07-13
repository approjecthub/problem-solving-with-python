# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:23:42 2019

@author: Anirban
"""


matrix = [[6, 7, 8, 9],
			  [4, 6, 7, 8],
			  [1, 4, 6, 7],
			  [0, 1, 4, 6],
			  [2, 0, 1, 4],
             [3,2,0,1]
			 ]

n1 = len(matrix)
n2 = len(matrix[0])

ans=True

for i in range(n1-1):
    for j in range(n2-1):
        if matrix[i][j] != matrix[i+1][j+1]:
            ans=False
            
print(ans)        