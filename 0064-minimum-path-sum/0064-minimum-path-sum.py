class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row_len, col_len = len(grid), len(grid[0])
        
        dp = [[float('inf')] * col_len for _ in range(row_len)]
        dp[-1][-1] = grid[-1][-1]
        
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len 
        
        for row in range(row_len-1, -1, -1):
            for col in range(col_len-1, -1, -1):
            
                if [row, col] == [row_len-1, col_len-1]:
                    continue
                    
                down = dp[row+1][col] if inbound(row+1,col) else float('inf')
                right = dp[row][col+1] if inbound(row,col+1) else float('inf')
                
                dp[row][col] = min(down, right) + grid[row][col]   
                
        
        return dp[0][0]