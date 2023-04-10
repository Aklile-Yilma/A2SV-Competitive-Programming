class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row_len, col_len = len(grid), len(grid[0])
        directions = [1, 0, -1, 0, 1]
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        max_area = 0
        count = 1
        
        def dfs(row, col):
            nonlocal count 
            
            grid[row][col] = 0
            for idx in range(len(directions)-1):
                new_row, new_col = row + directions[idx], col + directions[idx+1]
                if inbound(new_row, new_col) and grid[new_row][new_col] != 0:
                    count += 1
                    dfs(new_row, new_col)

            return 
        
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] != 0:
                    dfs(row, col)
                    max_area = max(max_area, count)
                count = 1
                    
        return max_area