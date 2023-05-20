class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        for u, v in pairs:
            uf.union(u, v)
            
        collections = [[] for _ in range(n)]
        
        #collect the connected components
        for node in uf.par:
            parent = uf.find(node)
            collections[parent].append(node)
            
        #sort the indices
        for idx in range(len(collections)):
            collections[idx] = sorted(collections[idx])
            
        #collect the letters by the indices
        #sort the letters by the indices            
        letters = [sorted(collections[i], key=lambda x: s[x]) for i in range(len(collections))] 
                
        ans = [None] * n
        for idx in range(len(collections)):
            for j in range(len(collections[idx])):
                i = collections[idx][j]
                ans[i] = s[letters[idx][j]]
        
        return ''.join(ans)

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0

    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)