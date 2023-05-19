class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n+1)
        
        for cityA, cityB, dist in roads:
            uf.union(cityA, cityB)
        
        min_score = float('inf')
        for cityA, cityB, dist in roads:
            if uf.connected(1, cityB):
                min_score = min(min_score, dist)
                
        return min_score
        
        
        
class UnionFind:
    def __init__(self, n):
        self.n = 0
        self.root = [node for node in range(n)]
        self.size = [1 for _ in range(n)]


    def find(self, x):
        # hold x
        hold = x
        while self.root[x] != x:
            x = self.root[x]

        # path compression
        # x is now the root, i didn't reach the root
        while x != self.root[hold]:
            temp = self.root[hold]
            # change root of node
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
 

