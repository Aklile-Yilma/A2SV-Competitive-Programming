class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row_len, col_len = len(grid), len(grid[0])
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        
        isvisited = set()
        found = False
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1:
                    start = (r, c)
                    found = True
                    break
            if found:
                break
                
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        q.append(start)
        total = 0
        visited = set()
        
        while q:
            r, c = q.popleft()
            
            if (r, c) in visited:
                continue
                
            visited.add((r, c))
            
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                
                if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] != 0:
                    q.append((nr, nc))
                    
                if not inbound(nr, nc) or grid[nr][nc] == 0:
                    total += 1
                    
        return total