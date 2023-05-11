class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # None(0) -> white(unvisited), -1 -> visited(grey), 1 -> (Black)visited and added to stack
        
        def dfs(sv,visited):
            if visited[sv]==-1:# this course had not been added into the res, but visited again; there is a cycle!
                return False
            if visited[sv]==1:# this course had been successfully added into the res
                return True
            visited[sv]=-1 # set the current course as currently being visited
            for u in adj[sv]:
                if not dfs(u,visited):
                    return False # if there is a cycle detected at any point, terminate!
            res.append(sv) # no cycle found, dfs finished, good to add the course into the res
            visited[sv]=1  # this course finished
            return True
        
        adj=[[] for i in range(numCourses)]
        res=[]
        for u,v in prerequisites:
            adj[v].append(u)
        visited=[0]*numCourses
        for i in range(numCourses):
            if not dfs(i,visited):
                # if False, there must be a cycle; terminate by returning an empty list
                return []
        return res[::-1]
        
# BFS
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         graph = defaultdict(list)
#         indegree = [0] * numCourses
    
#         for u, v in prerequisites:
#             graph[v].append(u)
#             indegree[u] += 1
        
#         q = deque()
#         visited = set()
#         order = []
#         # find source node
#         for node in range(len(indegree)):
#             if indegree[node] == 0:
#                 q.append(node)
#                 visited.add(node)
                
#         while q:
#             node = q.popleft()
#             order.append(node)
            
#             for child in graph[node]:
#                 if child not in visited:
#                     indegree[child] -= 1
#                     if indegree[child] == 0:
#                         q.append(child)
#                         visited.add(child)
                        
#         if len(visited) < numCourses:
#             return []
                        
#         return order
                    
        
        
                
        
            
        