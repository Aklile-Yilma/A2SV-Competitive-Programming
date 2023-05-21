class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UnionFind(len(equations)*2)        
        for eq in equations:
            letter1 = eq[0]
            symbol = eq[1:3]
            letter2 = eq[3]
            
            if symbol == "==":
                uf.union(letter1, letter2)
              
        for eq in equations:
            letter1 = eq[0]
            symbol = eq[1:3]
            letter2 = eq[3]
            if symbol == "!=" and uf.connected(letter1, letter2):
                return False
            
        return True
                
class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.size = {}
        
        for idx in range(ord('a'), ord('z')+1):
            self.root[chr(idx)] = chr(idx)
            self.size[chr(idx)] = 1
            
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
