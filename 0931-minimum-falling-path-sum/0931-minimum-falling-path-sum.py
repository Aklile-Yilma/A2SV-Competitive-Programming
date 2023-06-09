class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        inbound = lambda row, col: 0 <= row < n and 0 <= col < n
        
        dp = [[float('inf')] * n for _ in range(n)]
    
        #dp base case as last row
        for col in range(n):
            dp[-1][col] = matrix[-1][col]
            
        for row in range(n-1, -1, -1):
            for col in range(n):
                leftD = dp[row + 1][col - 1] if inbound(row + 1, col - 1) else float('inf')
                down = dp[row + 1][col] if inbound(row + 1, col) else float('inf')
                rightD = dp[row + 1][col + 1] if inbound(row + 1, col + 1) else float('inf')
                
                dp[row][col] = min(dp[row][col], matrix[row][col] + min(leftD, down, rightD))
        
        return min(dp[0])
    
# class Solution:
#     def __init__(self):
#         self.memo = {}
        
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
#         n = len(matrix)
#         inbound = lambda row, col: 0 <= row < n and 0 <= col < n
        
#         def dp(row, col):
            
#             #basecase
#             if row == n - 1:
#                 return matrix[row][col]
        
#             if (row, col) not in self.memo:
#                 leftD = dp(row + 1, col - 1) if inbound(row + 1, col - 1) else float('inf')
#                 down = dp(row + 1, col) if inbound(row + 1, col) else float('inf')
#                 rightD = dp(row + 1, col + 1) if inbound(row + 1, col + 1) else float('inf')
                
#                 self.memo[(row, col)] =  matrix[row][col] + min(leftD, down, rightD)
                
#             return self.memo[(row, col)]
        
#         ans = float('inf')
#         for col in range(n):
#             ans = min(ans, dp(0, col))
            
#         return ans
        