class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        #top-down
        row = 100
        dp = []
        curr_col = 1
        for _ in range(row):
            dp.append([0] * curr_col)
            curr_col += 1
            
        dp[0][0] = poured
        
        #push-dp
        for r in range(row-1):
            for c in range(len(dp[r])):
                curr = 0
                if dp[r][c] > 1:
                    curr = dp[r][c] - 1
                    dp[r][c] -= curr
                    
                if curr > 0:
                    dp[r+1][c] += (curr / 2)
                    dp[r+1][c+1] += (curr / 2)
                     
        return dp[query_row][query_glass]
                
        
            
        