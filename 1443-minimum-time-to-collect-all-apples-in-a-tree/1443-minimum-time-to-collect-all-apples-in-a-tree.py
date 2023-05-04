class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            count = 0
            subtree_count = 0
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue                    
                subtree_count = dfs(neighbor)
                if subtree_count or hasApple[neighbor]:
                    count += 2 + subtree_count

            return count
        
        return dfs(0)
        