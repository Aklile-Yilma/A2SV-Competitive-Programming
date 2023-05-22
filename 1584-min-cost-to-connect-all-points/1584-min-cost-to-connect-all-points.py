class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
   
        #Kruskal’s algorithm for MST 
        n = len(points)
        edges = []
        for idx in range(n):
            u = points[idx]
            for idx2 in range(idx+1, n):
                v = points[idx2]
                edges.append((tuple(u), tuple(v)))
                
        #Sort all the edges in non-decreasing order of their weight.
        sorted_edges = sorted(edges, key=lambda edge: abs(edge[0][0] - edge[1][0]) + abs(edge[0][1] - edge[1][1]))
        
        # Pick the smallest edge. Check if it forms a cycle with the spanning-tree formed so far. If the cycle is not formed, include this edge. Else, discard it.
        total = 0
        uf = UnionFind(points)
        for edge in sorted_edges:
            u = edge[0]
            v = edge[1]
            if not uf.connected(u, v):
                uf.union(u, v)
                total += abs(u[0] - v[0]) + abs(u[1] - v[1])
                
        return total
        
class UnionFind:
    def __init__(self, points):
        self.root = defaultdict(list)
        self.size = defaultdict(int)
        
        for point in points:
            point = tuple(point)
            self.root[point] = point
            self.size[point] = 1

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
