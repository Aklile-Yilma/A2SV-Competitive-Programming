class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UnionFind(len(equations)*2)
        letter_map = {}
        idx = 0
        
        for eq in equations:
            letter1 = eq[0]
            symbol = eq[1:3]
            letter2 = eq[3]
            
            if letter1 not in letter_map:
                letter_map[letter1] = idx
                idx += 1
            if letter2 not in letter_map:
                letter_map[letter2] = idx
                idx += 1
            if symbol == "==":
                uf.union(letter_map[letter1], letter_map[letter2])
              
        for eq in equations:
            letter1 = eq[0]
            symbol = eq[1:3]
            letter2 = eq[3]
            
            if symbol == "!=" and uf.connected(letter_map[letter1], letter_map[letter2]):
                return False
            
        return True
                
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
