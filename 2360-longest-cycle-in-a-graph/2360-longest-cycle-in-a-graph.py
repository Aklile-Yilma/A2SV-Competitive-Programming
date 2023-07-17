class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        N = len(edges)            
        indegree = [0] * N
        
        for node in range(N):
            if edges[node] != -1:
                indegree[edges[node]] += 1     
        
        q = deque()
        visited = set()
        for node in range(N):
            if indegree[node] == 0:
                q.append(node)
                visited.add(node)
                
        while q:
            node = q.popleft()
            
            child = edges[node]
            if child != -1:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
                    visited.add(child)
            
        #check unvisited nodes for longest cycle
        ans = -1
        for node in range(N):
            #count cycle 

            if node not in visited:
                count = 1
                neighbor = edges[node]
                visited.add(node)
                
                while node != neighbor:
                    count += 1
                    visited.add(neighbor)
                    neighbor = edges[neighbor]
                    
                #update answer
                ans = max(ans, count)
            
        return ans
    