class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
            
        q = deque()
        #append independent nodes
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        answer = []
        ancestors = [set() for _ in range(numCourses)]
        
        while q:
            node = q.popleft()
            
            for child in graph[node]:
                indegree[child] -= 1
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)
                
                if indegree[child] == 0:
                    q.append(child)
           
        answer = [False for _ in range(len(queries))]
        
        for idx in range(len(queries)):
            parent, child = queries[idx]
            if parent in ancestors[child]:
                answer[idx] = True
                
        return answer