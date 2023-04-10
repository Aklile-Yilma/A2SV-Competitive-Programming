class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        network_rank = defaultdict(int)
        edgeset = set()
        max_rank = 0        
        
        for u, v in roads:
            network_rank[u] += 1
            network_rank[v] += 1
            edgeset.add((u, v))
            
        for u in range(n):
            for v in range(u+1, n):
                
                curr_rank = network_rank[u] + network_rank[v]
                if (u,v) in edgeset or (v,u) in edgeset:
                    curr_rank -= 1    
                max_rank = max(max_rank, curr_rank)
                
        return max_rank