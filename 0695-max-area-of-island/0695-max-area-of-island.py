class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row_len, col_len = len(grid), len(grid[0])
        directions = [1, 0, -1, 0, 1]
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        max_area = 0
        
        def dfs(row, col):

            depth = 1
            grid[row][col] = 0
            for idx in range(len(directions)-1):
                new_row, new_col = row + directions[idx], col + directions[idx+1]
                if inbound(new_row, new_col) and grid[new_row][new_col] != 0:
                    depth += dfs(new_row, new_col)

            return depth
        
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] != 0:
                    max_area = max(max_area, dfs(row, col))
                    
        return max_area