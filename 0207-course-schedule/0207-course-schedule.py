class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
    
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque()
        visited = set()
        order = []
        # find source node
        for node in range(len(indegree)):
            if indegree[node] == 0:
                q.append(node)
                visited.add(node)
                
        while q:
            node = q.popleft()
            order.append(node)
            
            for child in graph[node]:
                if child not in visited:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        q.append(child)
                        visited.add(child)
                        
        if len(visited) < numCourses:
            return False
                        
        return True