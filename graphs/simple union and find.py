n = 3
parent = [-1] * n

def find(i):
    if parent[i]==-1:
        return i
    else:
        return find(parent[i])
        
def union(i,j):
    parent[j] = i
    
edges = [[0,1],[1,2],[0,2]]

for e in edges:
    x = find(e[0])
    y = find(e[1])
    
    if(x==y):
        print('cycle')
    else:
        union(e[0],e[1])
    
