class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        for node in graph:
            if len(graph[node]) == n:
                return node
        