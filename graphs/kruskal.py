edges = [[0, 1, 4],[0, 7, 8],[1, 2, 8],[1, 7, 11],[2, 3, 7],[2, 5, 4],[2, 7, 7],[2, 8, 2],[3, 4, 9],[3, 5, 14],[4, 5, 10],[5, 6, 2],[6, 7, 1],[6, 8, 6]]#[v1,v2,w]
n = 9
parent = [-1]*n
rank = [0]*n

edges.sort(key=lambda x:x[2])

def find(parent, node):
    
    if parent[node] !=-1:
        parent[node] = find(parent, parent[node])
        return parent[node]

    return node

def union(i,j, parent, rank):
    rooti = find(parent, i)
    rootj = find(parent, j)

    if rank[rooti]>rank[rootj]:
        parent[rootj] = rooti

    elif rank[rootj]>rank[rooti]:
        parent[rooti] = rootj

    else:
        parent[rooti] = rootj
        rank[rootj] += 1
ec = 0
cost = 0
mst = []
for e in edges:
    if ec==n-1:
        break

    root1 = find(parent,e[0])
    root2 = find(parent,e[1])

    if root1!=root2:
        
        mst.append([e[0], e[1]])
        union(e[0],e[1],parent,rank)
        cost += e[2]
        ec += 1

print(cost)
print(mst)
    

