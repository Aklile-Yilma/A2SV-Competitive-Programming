class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        res_graph = defaultdict(set)
        
        for u, v in restrictions:
            res_graph[u].add(v)
            res_graph[v].add(u)
            
        uf = UnionFind(n, res_graph)
        ans = []
        
        for u, v in requests:
            can = True
            #check if u is connected to any of restrictions of v
            res_u = uf.group_res[uf.find(u)]
            res_v = uf.group_res[uf.find(v)]
            
            # print(u, v, res_u, res_v)
            for r1 in res_u:
                if uf.connected(v, r1):
                    can = False
                    break
                    
            for r2 in res_v:
                if uf.connected(u, r2):
                    can = False
                    break
                        
            if can:
                uf.union(u, v)
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
    
class UnionFind:
    def __init__(self, n, res_graph):
        self.par = {}
        self.rank = {}
        self.group_res = defaultdict(set)

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
            self.group_res[i] = res_graph[i]

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
            # print(n1, n2, p1, p2, "hree")
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            # print(p1, p2, self.group_res[p1], self.group_res[p2])
            self.group_res[p1].update(self.group_res[p2])
            # print(self.group_res[p2])
        elif self.rank[p1] < self.rank[p2]:       
            # print(n1, n2, p1, p2,  self.group_res[p1], self.group_res[p2])
            self.par[p1] = p2
            self.group_res[p2].update(self.group_res[p1])
        else:
            # print(n1, n2, p1, p2,  self.group_res[p1], self.group_res[p2])
            self.par[p1] = p2
            self.group_res[p2].update(self.group_res[p1])
            # print(self.group_res[p2])
            self.rank[p2] += 1
        return True

    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)