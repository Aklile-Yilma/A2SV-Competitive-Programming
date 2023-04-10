class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        directions = [1, 0, -1, 0, 1]
        visited = set()
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        count = 0
        
        
        def dfs(row, col):
            
            visited.add((row, col))
            for idx in range(len(directions)-1):
                new_row, new_col = row + directions[idx], col + directions[idx+1]
                if (new_row, new_col) not in visited and inbound(new_row, new_col) and grid[new_row][new_col] != "0":
                    dfs(new_row, new_col)

            return
        
        for row in range(row_len):
            for col in range(col_len):
                if (row,col) not in visited and grid[row][col] != "0":
                    dfs(row, col)
                    count += 1
                    
        return count
        
        
        