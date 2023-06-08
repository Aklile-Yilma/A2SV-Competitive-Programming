class Solution:
    def __init__(self):
        self.memo = {}
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row_len, col_len = len(grid), len(grid[0])
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        
        #top-down
        def dfs(row, col):
            
            if [row, col] == [row_len-1, col_len-1]:
                return grid[row][col]
            
            if (row, col) not in self.memo:
                down = dfs(row+1, col) if inbound(row+1, col) else float('inf')
                right = dfs(row, col+1) if inbound(row, col+1) else float('inf')
                
                self.memo[(row, col)] = min(down, right) + grid[row][col]
                
            return self.memo[(row, col)]
    
        return dfs(0, 0)