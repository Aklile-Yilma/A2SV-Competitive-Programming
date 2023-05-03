class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row_len, col_len = len(grid), len(grid[0])
        inbound = lambda row, col : 0 <= row < row_len and 0 <= col < col_len
        directions = [1, 0, -1, 0, 1]
        fresh_count = 0
        min_time = -1
        q = deque()
        
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    fresh_count += 1
                    
        if fresh_count:
            while q:
                size = len(q)
                for _ in range(size):
                    row, col = q.popleft()

                    for idx in range(len(directions)-1):
                        new_row = row + directions[idx]
                        new_col = col + directions[idx+1]
                        if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            fresh_count -= 1
                            q.append((new_row, new_col))

                min_time += 1
            
            return min_time if fresh_count == 0 else -1
        return 0
                        
            

                        
                
                    
                    
        
        
        
        