class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        indegree = [0] * n
        order = []
        ancestors = [set() for _ in range(n)]
        
        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1
            
        q = deque()
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
                
        while q:
            node = q.popleft()
            order.append(node)
            
            for child in graph[node]:
                indegree[child] -= 1
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)            
                if indegree[child] == 0:
                    q.append(child)
                    
        return [sorted(ancestors[idx]) for idx in range(n)]
        
        
        
        