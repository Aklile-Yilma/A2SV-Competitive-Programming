class Solution:
    def build(self, n):
        self.n = 0
        self.root = [node for node in range(n)]
        self.size = [1 for _ in range(n)]
        
    def find(self, x):
        #hold x
        hold = x
        while self.root[x] != x:
            x = self.root[x]
            
        #path compression
        #x is now the root, i didn't reach the root
        while x != self.root[hold]:
            temp = self.root[hold]
            #change root of node
            self.root[hold] = x
            hold = temp
            
        return x
            
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        size1 = self.size[root1]
        size2 = self.size[root2]
        
        if size1 <= size2:
            self.root[root2] = root1
            self.size[root1] += root2
        else:
            self.root[root1] = root2
            self.size[root2] += root1
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.build(len(edges))
        
        for u, v in edges:
            u = u-1
            v = v-1
            if self.connected(u, v):
                return [u+1, v+1]
            
            self.union(u, v)
        