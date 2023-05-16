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
        visited = set()
        heights = {}
        #append independent
        for node in range(n):
            if indegree[node] <= 1:
                q.append((node, -1))
                visited.add(node)
                heights[node] = -1
        
        min_height = -1
        while q:
            node, height = q.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                if child not in visited and indegree[child] <= 1:
                    q.append((child, height-1))
                    heights[child] = height-1
                    min_height = min(min_height, height-1)
                    visited.add(child)
                    
        answer = []
        for node in heights:
            if heights[node] == min_height:
                answer.append(node)
                  
        return answer
        
        
        
            