class minheap():
    def __init__(self):
        self.heap = []
        self.pos = {}
    def push(self, x):#x[0] = key, x[1]= value
        if x[1] in self.pos:
            return False
        n = len(self.heap)
        self.pos[x[1]] = n
        self.heap.append(x)
        i = n
        temp = n
        while i>0:
            if i%2!=0:
                i = (i-1)//2
            else:
                i = (i-2)//2
            if self.heap[i][0]>=self.heap[temp][0]:
                self.pos[self.heap[i][1]] = temp
                self.pos[self.heap[temp][1]] = i
                self.heap[i], self.heap[temp] =  self.heap[temp],self.heap[i]
                temp = i
        
    def pop(self):
        n = len(self.heap)
        if n==0:
            return
        x = self.heap[0]
        self.heap[0] = self.heap[n-1]
        self.pos[self.heap[n-1][1]] = 0
        del self.pos[x[1]]
        self.heap.pop()
        self.heapify()
        return x
    
    def size(self):
        return len(self.heap)
    
    def top(self):
        if len(self.heap)==0:
            return 
        return self.heap[0]
    
    def update(self,x):
        if x[1] not in self.pos:
            return
        self.heap[self.pos[x[1]]]= x
        self.decreasekey(self.pos[x[1]])
        
    def decreasekey(self, pos):
       
        print(pos)
        i = pos
        temp = pos
        while i>0:
            if i%2!=0:
                i = (i-1)//2
            else:
                i = (i-2)//2
            if self.heap[i][0]>=self.heap[temp][0]:
                self.pos[self.heap[i][1]] = temp
                self.pos[self.heap[temp][1]] = i
                self.heap[i], self.heap[temp] =  self.heap[temp],self.heap[i]
                temp = i
    
    def heapify(self):
        i = 0
        n = len(self.heap)
        while (2*i+1)<n:
            if (2*i + 2)<n and self.heap[2*i+2][0]<self.heap[2*i+1][0]:
                if self.heap[i][0]>=self.heap[2*i+2][0]:
                    self.pos[self.heap[2*i+2][1]] = i
                    self.pos[self.heap[i][1]] = 2*i+2
                    self.heap[2*i+2],self.heap[i] = self.heap[i],self.heap[2*i+2]
                i = 2*i+2
                    
            else:
                if self.heap[i][0]>=self.heap[2*i+1][0]:
                    self.pos[self.heap[2*i+1][1]] = i
                    self.pos[self.heap[i][1]] = 2*i+1
                    self.heap[2*i+1],self.heap[i] = self.heap[i],self.heap[2*i+1]
                    
                i = 2*i+1
