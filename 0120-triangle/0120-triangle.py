class Solution:        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        #top-down
        @lru_cache(None)
        def dfs(curr_row, curr_col):
            
            if curr_row == len(triangle):
                return 0 
            
            return triangle[curr_row][curr_col] + min(dfs(curr_row + 1, curr_col), dfs(curr_row+1, curr_col + 1))
                       
        return dfs(0, 0)
                