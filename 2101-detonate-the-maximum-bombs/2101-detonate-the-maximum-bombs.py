class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for bomb1 in range(len(bombs)):
            x1, y1, r1 = bombs[bomb1]
            graph[bomb1] = graph.get(bomb1, [])
            for bomb2 in range(bomb1+1, len(bombs)):
                x2, y2, r2 = bombs[bomb2]
                #find eucledean distance
                distance = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
                
                if distance <= r1:
                    graph[bomb1].append(bomb2)
                
                if distance <= r2:
                    graph[bomb2].append(bomb1)
              

        def dfs(node):
            
            curr_count = 1
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    curr_count += dfs(neighbor)
                    
            return curr_count
        
        max_bombs = 1
        for node in graph:
            visited = set()
            curr_count = dfs(node)
            max_bombs = max(max_bombs, curr_count)
            
                
        return max_bombs