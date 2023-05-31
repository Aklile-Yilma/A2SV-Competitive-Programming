class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        inbound = lambda row, col: 0 <= row < m and 0 <= col < n
        
        def answer(row, col):
            if inbound(row, col):
                return dp[row][col]
            return 0
        
        #reverse row wise
        for c in range(n-1, -1, -1):
            for r in range(m-1, -1, -1):
                if (r, c) == (m-1, n-1):
                    continue
                dp[r][c] = answer(r, c+1) + answer(r+1, c)
                
        return dp[0][0]
        
        
#top down
# class Solution:
#     def __init__(self):
#         self.memo = {}
        
#     def uniquePaths(self, m: int, n: int) -> int:
        
#         def dfs(row, col):
            
#             if (row, col) == (m-1, n-1):
#                 return 1
            
#             if row >= m or col >= n:
#                 return 0
            
#             if (row, col) not in self.memo:
#                 self.memo[(row, col)] = dfs(row+1, col) + dfs(row, col+1)
                
#             return self.memo[(row, col)]
        
#         return dfs(0, 0)