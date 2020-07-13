# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:00:06 2019

@author: Anirban
"""

### https://www.geeksforgeeks.org/maximum-path-sum-matrix/

##Assuming all are non negative numbers

grid = [[1,4,8,6,2,2,1,7],
        [4,7,3,1,4,5,5,1],
        [8,8,2,1,1,8,0,1],
        [8,9,2,9,8,0,8,9],
        [5,7,5,7,1,8,5,5],
        [7,0,9,4,5,6,5,6],
        [4,9,9,7,9,1,9,0]]

'''
def minPathSum(self, grid: List[List[int]]) -> int:  ## my solution ## didn't work
    cost = grid[-1][-1]
    
    i=len(grid)-1; j=len(grid[0])-1
    while( i>=0 and j>=0):
        if (i>=1 and j>=1) and grid[i-1][j]<grid[i][j-1]:
            i -= 1
            
        elif (i>=1 and j>=1) and grid[i-1][j]>grid[i][j-1]:
            j -= 1
        
        elif i==0 and j!=0:
            j -= 1
            
        else:
            i -= 1
            
        if i<0 or j<0:
            break
        
        print(grid[i][j])    
        cost += grid[i][j]
                                    
    return cost
    '''
    
def minPathSum( grid): ## dp sloution
    # dp
    # reason: sub-problem yealds best solution for larger problem
    # [i][j] : minimal sums to destination
    # [i][j] = min ([i+1][j] if possible, [i, j+1] if possible) + cost[i][j]
    
    # recursive way
    # Time  O(M*N) Space: O(M*N) 

    ## iterative way
    # i: M-1 -> 0, j: N-1 -> 0
    
    M, N = len(grid), len(grid[0])
    
    for i in range(M-1, -1, -1):
        for j in range(N-1, -1, -1):
            if i < M-1 and j < N-1:
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
            elif i == M-1 and j < N-1:
                grid[i][j] += grid[i][j+1]
            elif i < M-1 and j == N-1:
                grid[i][j] += grid[i+1][j]
    
    return grid[0][0]