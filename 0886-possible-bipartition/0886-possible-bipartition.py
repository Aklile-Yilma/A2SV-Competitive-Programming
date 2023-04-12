class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        group1 = set()
        group2 = set()
        visited = set()
        graph = defaultdict(list)
        
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)            
        
        def dfs(curr_node, curr_color):
            
            if curr_node in visited:
                if (curr_color and curr_node not in group1) or (not curr_color and curr_node not in group2):
                    return False
                
                return True
            
            visited.add(curr_node)
            if curr_color: 
                group1.add(curr_node)
            else:
                group2.add(curr_node)
                
            for neighbor in graph[curr_node]:
                possible = dfs(neighbor, not curr_color)
                if not possible:
                    return False
                    
            return True
        
        for node in graph:
            if node not in visited:
                possible = dfs(node, True)    
                if not possible:
                    return False
                
        return True
        
            