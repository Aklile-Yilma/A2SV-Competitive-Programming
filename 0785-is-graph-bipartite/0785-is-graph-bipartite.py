class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group1 = set()
        group2 = set()
        visited = set()
        
        def dfs(curr_node, curr_color):
            #basecase
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
                if not dfs(neighbor, not curr_color):
                    return False
                
            return True
            
        
        for node in range(len(graph)):
            if node not in visited:
                if not dfs(node, True):
                    return False
                
        return True