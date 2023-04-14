class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        row_len, col_len = len(grid2), len(grid2[0])
        directions = [1, 0, -1, 0, 1]
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        count = 0
        
        def dfs(row, col, isSubIsland):
            
            grid2[row][col] = 0
            
            if grid1[row][col] == 0:
                isSubIsland = False
                
            for idx in range(len(directions)-1):
                new_row = row + directions[idx]
                new_col = col + directions[idx+1]
                if inbound(new_row, new_col) and grid2[new_row][new_col] == 1:
                    isSubIsland = dfs(new_row, new_col, isSubIsland)
                     
            return isSubIsland
        
        
        for row in range(row_len):
            for col in range(col_len):
                if grid2[row][col] == 1:
                    if dfs(row, col, True):
                        count += 1
                        
        return count
                        
                    
                    
        