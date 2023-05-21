class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        uf = UnionFind()
        
        for l1, l2 in zip(s1, s2):
            uf.union(l1, l2)
        
        # assign the smallest letter in connected letters which is the root 
        ans = list(baseStr)
        for idx in range(len(baseStr)):
            letter = baseStr[idx]
            par = uf.find(letter)
            ans[idx] = par
            
        return ''.join(ans)
                            
class UnionFind:
    def __init__(self):
        self.root = {}
        
        for idx in range(ord('a'), ord('z')+1):
            self.root[chr(idx)] = chr(idx)
            
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
        
        if root1 == root2:
            return

        if root1 <= root2:
            self.root[root2] = root1
        else:
            self.root[root1] = root2

    def connected(self, x, y):
        return self.find(x) == self.find(y)