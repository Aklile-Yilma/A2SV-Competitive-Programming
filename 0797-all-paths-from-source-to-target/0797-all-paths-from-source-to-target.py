class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        paths = []
        
        def backtrack(node, curr_path):
            
            if node == len(graph)-1:
                paths.append(curr_path.copy())
            
            for idx in range(len(graph[node])):
                next_node = graph[node][idx]
                curr_path.append(next_node)
                backtrack(next_node, curr_path)
                curr_path.pop()
            return
        
        backtrack(0, [0])
        
        return paths