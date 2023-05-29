class Solution:
    def __init__(self):
        self.memo = {}
        
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(row, col):
            
            if (row, col) == (m-1, n-1):
                return 1
            
            if row >= m or col >= n:
                return 0
            
            if (row, col) not in self.memo:
                self.memo[(row, col)] = dfs(row+1, col) + dfs(row, col+1)
                
            return self.memo[(row, col)]
        
        return dfs(0, 0)