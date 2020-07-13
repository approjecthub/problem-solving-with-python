# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:42:32 2020

@author: Anirban
"""

g_matrix = [[0,1,1,1,1,0,0,0],
     [1,0,0,0,0,1,0,0],
     [1,0,0,0,0,1,0,0],
     [1,0,0,0,0,0,1,0],
     [1,0,0,0,0,0,1,0],
     [0,1,1,0,0,0,0,1],
     [0,0,0,1,1,0,0,1],
     [0,0,0,0,0,1,1,0]]

visit = [0,0,0,0,0,0,0,0]

g_list = {}
g_list[0] = [1,2,3,4]
g_list[1] = [0,5]
g_list[2] = [0,5]
g_list[3] = [0,6]
g_list[4] = [0,6]
g_list[5] = [1,2,7]
g_list[6] = [3,4,7]
g_list[7] = [5,6]

def dfs_matrix(v):
    
    global g_matrix
    global visit
    print(v, end=' ')
    visit[v] = 1
    for i in range(len(g_matrix[v])):
        if g_matrix[v][i] == 1 and visit[i]==0:
            #print('i : ',i)
            dfs_matrix(i)
            
            
#dfs_matrix(0)
            
def dfs_list(v):
    global g_list
    global visit
    
    print(v, end= ' ')
    visit[v] = 1
    for i in range(len(g_list[v])):
        if visit[g_list[v][i]]==0:
            #print('i : ',i)
            dfs_list(g_list[v][i])    
    
    
dfs_list(0)
            
        