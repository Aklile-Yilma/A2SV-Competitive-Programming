class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        uf = UnionFind(n)
        size = len(queries)
        answer = [False] * size
        queries_with_index = [[] for _ in range(size)]
        
        for i in range(size):
            queries_with_index[i] = queries[i]
            queries_with_index[i].append(i)
            
        # Sort all edges in increasing order of their edge weights.
        edgeList.sort(key=lambda x: x[2])
        # Sort all queries in increasing order of the limit of edge allowed.
        queries_with_index.sort(key=lambda x: x[2])
        
        edges_index = 0
        
        #Iterate on each query one by one
        
        for [p, q, limit, query_original_index] in queries_with_index:
            # join 
            while edges_index < len(edgeList) and edgeList[edges_index][2] < limit:
                node1 = edgeList[edges_index][0]
                node2 = edgeList[edges_index][1]
                uf.union(node1, node2)
                edges_index += 1
                
            #if both nodes belong to the same component, it means we can reach them
            answer[query_original_index] = uf.connected(p, q)
                
        return answer
        
        
class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.rank = {}

        for i in range(n):
            self.root[i] = i
            self.rank[i] = 0

    # Find parent of n, with path compression.
    def find(self, n):
        p = self.root[n]
        while p != self.root[p]:
            self.root[p] = self.root[self.root[p]]
            p = self.root[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        root1, root2 = self.find(n1), self.find(n2)
        if root1 == root2:
            return False

        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        else:
            self.root[root1] = root2
            self.rank[root2] += 1
        return True

    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)