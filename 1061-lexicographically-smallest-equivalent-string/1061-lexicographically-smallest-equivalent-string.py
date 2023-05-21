class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        uf = UnionFind()
        
        for l1, l2 in zip(s1, s2):
            uf.union(l1, l2)
        
        collections = defaultdict(set)
        for letter in uf.root:
            par = uf.find(letter)
            collections[par].add(letter)
        
        # assign the smallest letter in connected letters
        ans = list(baseStr)
        for idx in range(len(baseStr)):
            curr_letter = baseStr[idx]
            for key, values in collections.items():
                if curr_letter in values:
                    for v in values:
                        if v < ans[idx]:
                            ans[idx] = v
                            
        return ''.join(ans)
                            
class UnionFind:
    def __init__(self):
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