class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
            
        q = deque()
        visited = set()
        order = []
        # get most independent node
        for node in graph:
            if indegree[node] == 1:
                q.append(node)
                visited.add(node)
                break
                
        while q:
            node = q.popleft()
            order.append(node)
            
            for child in graph[node]:
                if child not in visited:
                    visited.add(node)
                    indegree[child] -= 1
                    if indegree[child] <= 1:
                        q.append(child)
                        
        return order
                    