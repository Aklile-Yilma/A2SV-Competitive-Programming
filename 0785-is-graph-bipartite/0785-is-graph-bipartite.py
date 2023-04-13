class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = [None] * len(graph)
        
        def dfs(curr_node, curr_color):
            #basecase
            #if curr_node is visited
            if colors[curr_node] != None:
                if colors[curr_node] != curr_color:
                    return False                
                return True
            
            colors[curr_node] = curr_color            
            for neighbor in graph[curr_node]:
                if not dfs(neighbor, not curr_color):
                    return False
                
            return True
            
        
        for node in range(len(graph)):
            #if not visited
            if colors[node] == None:
                if not dfs(node, True):
                    return False
                
        return True