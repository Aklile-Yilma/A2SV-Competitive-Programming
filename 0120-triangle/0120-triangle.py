class Solution:        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        
        dp = []
        curr_col = 1
        for _ in range(row):
            dp.append([float('inf')] * curr_col)
            curr_col += 1
            
        dp[0][0] = triangle[0][0] 
        
        # push dp
        for r in range(row-1):
            for c in range(len(triangle[r])):
                dp[r+1][c] = min(dp[r+1][c], dp[r][c] + triangle[r+1][c])
                dp[r+1][c+1] = min(dp[r+1][c+1], dp[r][c] + triangle[r+1][c+1])
                
        return min(dp[-1])
    
# class Solution:        
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         #top-down
#         @lru_cache(None)
#         def dfs(curr_row, curr_col):
            
#             if curr_row == len(triangle):
#                 return 0 
            
#             return triangle[curr_row][curr_col] + min(dfs(curr_row + 1, curr_col), dfs(curr_row+1, curr_col + 1))
                       
#         return dfs(0, 0)
                