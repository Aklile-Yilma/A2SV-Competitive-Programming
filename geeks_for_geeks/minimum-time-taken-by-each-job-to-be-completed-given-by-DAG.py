from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        
        for u, v in edges:
            graph[u-1].append(v-1)
            indegree[v-1] += 1
            
        q = deque()
        
        for node in range(n):
            if indegree[node] == 0:
                q.append((node, 1))
        
        time = [-1 for _ in range(n)]
        
        while q:
            node, curr_time = q.popleft()
            time[node] = curr_time
            
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append((child, curr_time + 1))
                    
        return " ".join(str(t) for t in time)
        
        
