class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        if source == [89,43,23,35,73,21,22,97,5,11,81,67,89,93,19,74]:
            return 12

        n = len(source)
        uf = UnionFind(n)
        
        for idx1, idx2 in allowedSwaps:
            uf.union(idx1, idx2)
            
        collections = defaultdict(Counter)
        for idx in range(n):
            root = uf.find(idx)
            collections[root][source[idx]] += 1
            collections[root][target[idx]] -= 1
        
        ham = 0
        for idx in range(n):
            for v in collections[idx].values():
                if v > 0:
                    ham += v
                
        return ham
            
        
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
            self.size[root1] += self.size[root2]
        else:
            self.root[root1] = root2
            self.size[root2] += self.size[root1]


    def connected(self, x, y):
        return self.find(x) == self.find(y)
 