class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        uf = UnionFind(stones)
        n = len(stones)
        for i in range(n):
            row1, col1 = stones[i]
            for j in range(i+1, n):
                row2, col2 = stones[j]
                if row1 == row2 or col1 == col2:
                    uf.union((row1, col1), (row2, col2))
                    
        max_stones = 0
        for r in uf.root:
            parent = uf.root[r]
            if r == parent:
                max_stones += uf.size[parent] - 1

        return max_stones
        
        
        
class UnionFind:
    def __init__(self, stones):
        self.root = {(row, col): (row, col) for row, col in stones}
        self.size = {(row, col): 1 for row, col in stones}

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
        
        if root1 == root2:
            return

        if size1 <= size2:
            self.root[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.root[root1] = root2
            self.size[root2] += self.size[root1]

    def connected(self, x, y):
        return self.find(x) == self.find(y)
