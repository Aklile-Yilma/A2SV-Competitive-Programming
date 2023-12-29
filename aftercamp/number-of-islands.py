class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row_len, col_len = len(grid), len(grid[0])
        count = 0
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        directions = [[1, 0] , [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            
            q = deque()
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                for d in directions:
                    nr = row + d[0]
                    nc = col + d[1]
                    
                    if inbound(nr, nc) and grid[nr][nc] != "0":
                        grid[nr][nc] = '0'
                        q.append((nr, nc))
         
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] != "0":
                    grid[r][c] = '0'
                    bfs(r, c)
                    count += 1
        print(grid)           
        return count
                        
                        
            