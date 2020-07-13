# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:03:12 2020

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



'''
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
'''

visit = [0,0,0,0,0,0,0,0,0]

g_list ={}
g_list[0] = [1,3,4]
g_list[1] = [2,4]
g_list[2] = [5]
g_list[3] = [4,6]
g_list[4] = [5,7]
g_list[5] = []
g_list[6] = [4,7]
g_list[7] = [5,8]
g_list[8] = []

class queue:
    def __init__(self):
        ## an infinite size queue
        self.q = []
        
    def enqueue(self, data):
        self.q.append(data)
        
    def dequeue(self):
        if len(self.q)>0:
            data = self.q[0]
            self.q.remove(data)
            return data
        else:
            return False
        
    def size(self):
        return len(self.q)
        
def bfs_matrix(v):
    global g_matrix
    global visit
    
    q = queue()
    q.enqueue(v)
    visit[v] = 1
    
    while q.size()>0:
        data = q.dequeue()
        
        print(data, end=' ')
        
        for i in range(len(g_matrix[data])):
            if g_matrix[data][i]==1 and visit[i]==0:
                q.enqueue(i)
                visit[i]=1
                
        
#bfs_matrix(0)

def bfs_list(v):
    global g_list
    global visit
    
    q = queue()
    q.enqueue(v)
    visit[v] = 1
    
    while q.size()>0:
        data = q.dequeue()
        
        print(data, end=' ')
        
        for i in range(len(g_list[data])):
            if visit[g_list[data][i]]==0:
                q.enqueue(g_list[data][i])
                visit[g_list[data][i]]=1
                

bfs_list(0)