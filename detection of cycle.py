# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:41:11 2019

Detection of cycle in undirected graph
            @author: Anirban
"""
parent = []
        
def union(i,j):
    parent[i] = j
    
def find(i):
    while(parent[i]>=0):
        i = parent[i]
    
    return i

vertex = 3
edges = []

graph = [[0,1,1],
         [1,0,1],
         [1,1,0]]

def edge_list():
    
    for i in range(vertex):
        parent.append(-1)
        for j in range(i):
            if(i!=j and graph[i][j]!=0):
                edges.append([i,j])
                
def detectcycle(cycle_flag=0):    
    for e in edges:
        e1 = find(e[0])
        e2 = find(e[1])
        
        if(e1==e2 and e1!=-1):
            cycle_flag = 1
            
        union(e1,e2)
        
    return cycle_flag
        
            