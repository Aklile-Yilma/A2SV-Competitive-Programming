class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        colors_map = defaultdict(bool)
        visited = set()
        graph = defaultdict(list)
        
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            colors_map[u], colors_map[v] = None, None
            
        
        def dfs(parent, curr_node, curr_color):
            
            if curr_node in visited:
                if colors_map[curr_node] != curr_color:
                    return False
                return True
            
            visited.add(curr_node)
            colors_map[curr_node] = curr_color
            for neighbor in graph[curr_node]:
                if neighbor != parent:
                    possible = dfs(curr_node, neighbor, not curr_color)
                    if not possible:
                        return False
                    
            return True
        
        for node in graph:
            if node not in visited:
                possible = dfs(None, node, True)    
                if not possible:
                    return False
                
        return True
        
            