class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
            graph[v].append(u)
            indegree[u] += 1
            
        q = deque()
        #append independent
        for node in range(n):
            if indegree[node] <= 1:
                q.append(node)
        
        last_level = list(q)
        
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        q.append(child)
            if q:          
                last_level = list(q)
                  
        return last_level
        
        
        
            