def find(parent, i):
    if parent[i] != -1:
        parent[i] = find(parent, parent[i])
        return parent[i]
    return i
    
def union(parent, rank, x,y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot]<rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot]>rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
        
n = 3
parent = [-1]*n
rank = [0]*n
edges = [[0,1],[1,2],[0,2]]
for e in edges:
 
    x = find(parent,e[0])
    y = find(parent,e[1])
    
 
    if(x==y):
        
        print('cycle')
    else:
        union(parent, rank,x,y)
